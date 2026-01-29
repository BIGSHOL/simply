"""
테스트 API 테스트

Phase 1, T1.3: 테스트 목록 API
Phase 2, T2.3: AI 결과 생성 API
"""
import pytest
import os
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.core.database import Base, get_db
from app.models import Test, Question, Choice


# 테스트용 SQLite (동기, 파일 기반)
TEST_DB_FILE = "./test_api.db"
TEST_DATABASE_URL = f"sqlite:///{TEST_DB_FILE}"


@pytest.fixture(scope="module")
def test_engine():
    """테스트 엔진 (모듈 단위)"""
    # 기존 파일 삭제
    if os.path.exists(TEST_DB_FILE):
        try:
            os.remove(TEST_DB_FILE)
        except PermissionError:
            pass

    eng = create_engine(
        TEST_DATABASE_URL,
        connect_args={"check_same_thread": False},
    )
    yield eng
    eng.dispose()

    # 테스트 후 파일 정리
    if os.path.exists(TEST_DB_FILE):
        try:
            os.remove(TEST_DB_FILE)
        except PermissionError:
            pass


@pytest.fixture(scope="function")
def setup_db(test_engine):
    """테스트 DB 설정"""
    Base.metadata.create_all(bind=test_engine)
    yield test_engine
    Base.metadata.drop_all(bind=test_engine)


@pytest.fixture
def db_session(setup_db):
    """테스트용 DB 세션"""
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=setup_db)
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()


def _get_override_db(engine):
    """테스트용 DB 세션 오버라이드 팩토리"""
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    def override_get_db():
        session = TestingSessionLocal()
        try:
            yield session
        finally:
            session.close()

    return override_get_db


@pytest.fixture
def seed_tests(db_session):
    """테스트 데이터 시드"""
    test1 = Test(
        title="MBTI로 알아보는 나의 연애 스타일",
        description="당신의 연애 성향을 분석합니다",
        category="love",
        play_count=100,
    )
    test2 = Test(
        title="직장에서 나는 어떤 유형?",
        description="직장 내 성격을 알아보세요",
        category="career",
        play_count=50,
    )
    db_session.add_all([test1, test2])
    db_session.commit()
    db_session.refresh(test1)
    db_session.refresh(test2)

    # test1에 질문과 선택지 추가
    q1 = Question(test_id=test1.id, order_num=1, content="질문 1")
    q2 = Question(test_id=test1.id, order_num=2, content="질문 2")
    db_session.add_all([q1, q2])
    db_session.commit()
    db_session.refresh(q1)
    db_session.refresh(q2)

    choices = []
    for q in [q1, q2]:
        for i in range(1, 5):
            choice = Choice(question_id=q.id, order_num=i, content=f"선택지 {i}")
            db_session.add(choice)
            choices.append(choice)
    db_session.commit()

    # 선택지 refresh
    for choice in choices:
        db_session.refresh(choice)

    return {
        "test1": test1,
        "test2": test2,
        "q1": q1,
        "q2": q2,
        "choices": choices,
    }


@pytest.fixture
def client(setup_db):
    """테스트 클라이언트"""
    app.dependency_overrides[get_db] = _get_override_db(setup_db)
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()


def test_get_tests_returns_list(client, seed_tests):
    """GET /api/v1/tests - 테스트 목록 조회"""
    response = client.get("/api/v1/tests")

    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert len(data["data"]) == 2
    # play_count 내림차순 정렬 확인
    assert data["data"][0]["play_count"] >= data["data"][1]["play_count"]


def test_get_tests_filter_by_category(client, seed_tests):
    """GET /api/v1/tests?category=love - 카테고리 필터링"""
    response = client.get("/api/v1/tests?category=love")

    assert response.status_code == 200
    data = response.json()
    assert len(data["data"]) == 1
    assert data["data"][0]["category"] == "love"


def test_get_test_detail(client, seed_tests):
    """GET /api/v1/tests/{id} - 테스트 상세 조회"""
    test_id = str(seed_tests["test1"].id)

    response = client.get(f"/api/v1/tests/{test_id}")

    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert data["data"]["id"] == test_id
    assert "questions" in data["data"]
    assert len(data["data"]["questions"]) == 2


def test_get_test_detail_not_found(client):
    """GET /api/v1/tests/{invalid_id} - 존재하지 않는 테스트"""
    response = client.get("/api/v1/tests/00000000-0000-0000-0000-000000000000")

    assert response.status_code == 404
    data = response.json()
    assert "detail" in data
    assert data["detail"]["code"] == "TEST_NOT_FOUND"


def test_submit_test_generates_ai_result(client, seed_tests):
    """POST /api/v1/tests/{id}/submit - 테스트 제출 및 AI 결과 생성"""
    test_id = str(seed_tests["test1"].id)
    q1 = seed_tests["q1"]
    q2 = seed_tests["q2"]
    choices = seed_tests["choices"]

    # q1의 첫 번째 선택지, q2의 두 번째 선택지 선택
    q1_choice = next(c for c in choices if c.question_id == q1.id and c.order_num == 1)
    q2_choice = next(c for c in choices if c.question_id == q2.id and c.order_num == 2)

    response = client.post(
        f"/api/v1/tests/{test_id}/submit",
        json={
            "answers": [
                {"question_id": str(q1.id), "choice_id": str(q1_choice.id)},
                {"question_id": str(q2.id), "choice_id": str(q2_choice.id)},
            ]
        },
    )

    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert "result_type" in data["data"]
    assert "result_title" in data["data"]
    assert "result_content" in data["data"]
    assert "share_code" in data["data"]
    assert data["meta"]["cached"] is False


def test_submit_test_invalid_answers(client, seed_tests):
    """POST /api/v1/tests/{id}/submit - 잘못된 답변"""
    test_id = str(seed_tests["test1"].id)
    q1 = seed_tests["q1"]

    # 하나의 질문만 답변 (불완전)
    response = client.post(
        f"/api/v1/tests/{test_id}/submit",
        json={
            "answers": [
                {"question_id": str(q1.id), "choice_id": str(seed_tests["choices"][0].id)},
            ]
        },
    )

    assert response.status_code == 400
    data = response.json()
    assert data["detail"]["code"] == "INVALID_ANSWERS"


def test_submit_test_uses_cache(client, seed_tests):
    """POST /api/v1/tests/{id}/submit - 동일 답변은 캐시 사용"""
    test_id = str(seed_tests["test1"].id)
    q1 = seed_tests["q1"]
    q2 = seed_tests["q2"]
    choices = seed_tests["choices"]

    q1_choice = next(c for c in choices if c.question_id == q1.id and c.order_num == 1)
    q2_choice = next(c for c in choices if c.question_id == q2.id and c.order_num == 2)

    payload = {
        "answers": [
            {"question_id": str(q1.id), "choice_id": str(q1_choice.id)},
            {"question_id": str(q2.id), "choice_id": str(q2_choice.id)},
        ]
    }

    # 첫 번째 제출
    response1 = client.post(f"/api/v1/tests/{test_id}/submit", json=payload)
    assert response1.status_code == 200
    assert response1.json()["meta"]["cached"] is False
    result_id_1 = response1.json()["data"]["id"]

    # 두 번째 제출 (동일 답변)
    response2 = client.post(f"/api/v1/tests/{test_id}/submit", json=payload)
    assert response2.status_code == 200
    assert response2.json()["meta"]["cached"] is True
    result_id_2 = response2.json()["data"]["id"]

    # 동일한 결과 반환 확인
    assert result_id_1 == result_id_2

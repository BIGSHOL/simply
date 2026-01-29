"""
결과 API 테스트

Phase 3, T3.1: 결과 조회 API
"""
import pytest
import os
from datetime import datetime, timedelta
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.core.database import Base, get_db
from app.models import Test, Question, Choice, Result


# 테스트용 SQLite (동기, 파일 기반)
TEST_DB_FILE = "./test_results_api.db"
TEST_DATABASE_URL = f"sqlite:///{TEST_DB_FILE}"


@pytest.fixture(scope="module")
def test_engine():
    """테스트 엔진 (모듈 단위)"""
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
def seed_result(db_session):
    """테스트 데이터 시드"""
    # 테스트 생성
    test = Test(
        title="테스트 제목",
        description="테스트 설명",
        category="personality",
        play_count=100,
    )
    db_session.add(test)
    db_session.commit()
    db_session.refresh(test)

    # 결과 생성
    result = Result(
        test_id=test.id,
        answers_hash="test_hash_123",
        result_type="분석가형",
        result_title="당신은 분석가형입니다!",
        result_content="상세한 결과 내용입니다.",
    )
    db_session.add(result)
    db_session.commit()
    db_session.refresh(result)

    return {"test": test, "result": result}


@pytest.fixture
def seed_expired_result(db_session):
    """만료된 결과 시드"""
    test = Test(
        title="만료 테스트",
        description="만료 테스트 설명",
        category="fun",
    )
    db_session.add(test)
    db_session.commit()
    db_session.refresh(test)

    result = Result(
        test_id=test.id,
        answers_hash="expired_hash",
        result_type="만료형",
        result_title="만료된 결과",
        result_content="만료된 결과 내용",
        expires_at=datetime.utcnow() - timedelta(days=1),  # 어제 만료
    )
    db_session.add(result)
    db_session.commit()
    db_session.refresh(result)

    return {"test": test, "result": result}


@pytest.fixture
def client(setup_db):
    """테스트 클라이언트"""
    app.dependency_overrides[get_db] = _get_override_db(setup_db)
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()


def test_get_result_by_id(client, seed_result):
    """GET /api/v1/results/{id} - 결과 조회"""
    result_id = str(seed_result["result"].id)

    response = client.get(f"/api/v1/results/{result_id}")

    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert data["data"]["id"] == result_id
    assert data["data"]["result_title"] == "당신은 분석가형입니다!"
    assert data["data"]["result_content"] == "상세한 결과 내용입니다."


def test_get_result_by_share_code(client, seed_result):
    """GET /api/v1/results/{share_code} - 공유 코드로 결과 조회"""
    share_code = seed_result["result"].share_code

    response = client.get(f"/api/v1/results/{share_code}")

    assert response.status_code == 200
    data = response.json()
    assert data["data"]["share_code"] == share_code


def test_get_result_not_found(client):
    """GET /api/v1/results/{invalid_id} - 존재하지 않는 결과"""
    response = client.get("/api/v1/results/00000000-0000-0000-0000-000000000000")

    assert response.status_code == 404
    data = response.json()
    assert data["detail"]["code"] == "RESULT_NOT_FOUND"


def test_get_result_expired(client, seed_expired_result):
    """GET /api/v1/results/{expired_id} - 만료된 결과"""
    result_id = str(seed_expired_result["result"].id)

    response = client.get(f"/api/v1/results/{result_id}")

    assert response.status_code == 410
    data = response.json()
    assert data["detail"]["code"] == "RESULT_EXPIRED"


def test_view_count_increments(client, seed_result, db_session):
    """결과 조회 시 조회수 증가 확인"""
    result_id = str(seed_result["result"].id)
    initial_count = seed_result["result"].view_count

    # 첫 번째 조회
    client.get(f"/api/v1/results/{result_id}")

    # 두 번째 조회
    client.get(f"/api/v1/results/{result_id}")

    # DB에서 직접 확인
    db_session.refresh(seed_result["result"])
    assert seed_result["result"].view_count == initial_count + 2

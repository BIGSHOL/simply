"""
pytest 공통 fixture

Phase 1, T1.1: 데이터베이스 스키마 & 시드 데이터
"""
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.database import Base
# 모델 import (테이블 생성에 필요)
from app.models import Test, Question, Choice, Result  # noqa: F401


# 테스트용 SQLite (동기, 인메모리)
TEST_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def db_session():
    """테스트용 DB 세션"""
    # 테이블 생성
    Base.metadata.create_all(bind=engine)

    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()
        # 테이블 삭제
        Base.metadata.drop_all(bind=engine)


@pytest.fixture
def test_fixture(db_session):
    """테스트 fixture"""
    from app.models.test import Test

    test = Test(
        title="테스트 제목",
        description="테스트 설명",
        category="personality",
    )
    db_session.add(test)
    db_session.commit()
    db_session.refresh(test)
    return test


@pytest.fixture
def question_fixture(db_session, test_fixture):
    """질문 fixture"""
    from app.models.test import Question

    question = Question(
        test_id=test_fixture.id,
        order_num=1,
        content="질문 내용",
    )
    db_session.add(question)
    db_session.commit()
    db_session.refresh(question)
    return question


@pytest.fixture
def choice_fixture(db_session, question_fixture):
    """선택지 fixture"""
    from app.models.test import Choice

    choice = Choice(
        question_id=question_fixture.id,
        order_num=1,
        content="선택지 내용",
    )
    db_session.add(choice)
    db_session.commit()
    db_session.refresh(choice)
    return choice


@pytest.fixture
def result_fixture(db_session, test_fixture):
    """결과 fixture"""
    from app.models.result import Result

    result = Result(
        test_id=test_fixture.id,
        answers_hash="test_hash",
        result_type="결과 타입",
        result_title="결과 제목",
        result_content="결과 내용",
    )
    db_session.add(result)
    db_session.commit()
    db_session.refresh(result)
    return result


@pytest.fixture
def test_with_questions(db_session):
    """질문이 포함된 테스트 fixture"""
    from app.models.test import Test, Question, Choice

    test = Test(
        title="질문 포함 테스트",
        description="설명",
        category="love",
    )
    db_session.add(test)
    db_session.commit()
    db_session.refresh(test)

    for i in range(1, 4):
        question = Question(
            test_id=test.id,
            order_num=i,
            content=f"질문 {i}",
        )
        db_session.add(question)
        db_session.commit()
        db_session.refresh(question)

        for j in range(1, 5):
            choice = Choice(
                question_id=question.id,
                order_num=j,
                content=f"선택지 {j}",
            )
            db_session.add(choice)

    db_session.commit()
    db_session.refresh(test)
    return test


@pytest.fixture
def question_with_choices(db_session, test_fixture):
    """선택지가 포함된 질문 fixture"""
    from app.models.test import Question, Choice

    question = Question(
        test_id=test_fixture.id,
        order_num=1,
        content="선택지 포함 질문",
    )
    db_session.add(question)
    db_session.commit()
    db_session.refresh(question)

    for i in range(1, 5):
        choice = Choice(
            question_id=question.id,
            order_num=i,
            content=f"선택지 {i}",
        )
        db_session.add(choice)

    db_session.commit()
    db_session.refresh(question)
    return question

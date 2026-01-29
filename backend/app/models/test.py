"""
테스트 관련 모델

Phase 1, T1.1: 데이터베이스 스키마 & 시드 데이터
"""
import uuid
import enum
from datetime import datetime
from sqlalchemy import String, Text, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base
from app.models.types import UUID


class TestCategory(enum.Enum):
    """테스트 카테고리"""
    PERSONALITY = "personality"
    LOVE = "love"
    CAREER = "career"
    FUN = "fun"


class Test(Base):
    """심리테스트 모델"""
    __tablename__ = "tests"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(),
        primary_key=True,
        default=uuid.uuid4,
    )
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    thumbnail_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
    category: Mapped[str] = mapped_column(String(20), nullable=False)
    play_count: Mapped[int] = mapped_column(Integer, default=0)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )

    # 관계
    questions: Mapped[list["Question"]] = relationship(
        "Question",
        back_populates="test",
        cascade="all, delete-orphan",
        order_by="Question.order_num",
    )
    results: Mapped[list["Result"]] = relationship(
        "Result",
        back_populates="test",
        cascade="all, delete-orphan",
    )
    result_types: Mapped[list["ResultType"]] = relationship(
        "ResultType",
        back_populates="test",
        cascade="all, delete-orphan",
        order_by="ResultType.min_score.desc()",
    )

    @property
    def question_count(self) -> int:
        return len(self.questions)


class Question(Base):
    """질문 모델"""
    __tablename__ = "questions"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(),
        primary_key=True,
        default=uuid.uuid4,
    )
    test_id: Mapped[uuid.UUID] = mapped_column(
        UUID(),
        ForeignKey("tests.id", ondelete="CASCADE"),
        nullable=False,
    )
    order_num: Mapped[int] = mapped_column(Integer, nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    image_url: Mapped[str | None] = mapped_column(String(500), nullable=True)

    # 관계
    test: Mapped["Test"] = relationship("Test", back_populates="questions")
    choices: Mapped[list["Choice"]] = relationship(
        "Choice",
        back_populates="question",
        cascade="all, delete-orphan",
        order_by="Choice.order_num",
    )


class Choice(Base):
    """선택지 모델"""
    __tablename__ = "choices"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(),
        primary_key=True,
        default=uuid.uuid4,
    )
    question_id: Mapped[uuid.UUID] = mapped_column(
        UUID(),
        ForeignKey("questions.id", ondelete="CASCADE"),
        nullable=False,
    )
    order_num: Mapped[int] = mapped_column(Integer, nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    score: Mapped[int] = mapped_column(Integer, default=0)  # 점수

    # 관계
    question: Mapped["Question"] = relationship("Question", back_populates="choices")


class ResultType(Base):
    """결과 유형 모델 (미리 정의된 결과)"""
    __tablename__ = "result_types"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(),
        primary_key=True,
        default=uuid.uuid4,
    )
    test_id: Mapped[uuid.UUID] = mapped_column(
        UUID(),
        ForeignKey("tests.id", ondelete="CASCADE"),
        nullable=False,
    )
    min_score: Mapped[int] = mapped_column(Integer, nullable=False)  # 최소 점수
    max_score: Mapped[int] = mapped_column(Integer, nullable=False)  # 최대 점수
    result_type: Mapped[str] = mapped_column(String(100), nullable=False)
    result_title: Mapped[str] = mapped_column(String(200), nullable=False)
    result_content: Mapped[str] = mapped_column(Text, nullable=False)
    result_image_url: Mapped[str | None] = mapped_column(String(500), nullable=True)

    # 관계
    test: Mapped["Test"] = relationship("Test", back_populates="result_types")


# Result 모델에서 순환 참조 방지
from app.models.result import Result  # noqa: E402, F401

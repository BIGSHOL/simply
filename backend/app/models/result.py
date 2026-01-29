"""
결과 관련 모델

Phase 1, T1.1: 데이터베이스 스키마 & 시드 데이터
"""
import uuid
import secrets
from datetime import datetime, timedelta
from sqlalchemy import String, Text, Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base
from app.models.types import UUID


def generate_share_code() -> str:
    """8자리 공유 코드 생성"""
    return secrets.token_urlsafe(6)[:8]


def default_expires_at() -> datetime:
    """30일 후 만료"""
    return datetime.utcnow() + timedelta(days=30)


class Result(Base):
    """테스트 결과 모델"""
    __tablename__ = "results"

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
    answers_hash: Mapped[str] = mapped_column(String(64), nullable=False, index=True)
    result_type: Mapped[str] = mapped_column(String(100), nullable=False)
    result_title: Mapped[str] = mapped_column(String(200), nullable=False)
    result_content: Mapped[str] = mapped_column(Text, nullable=False)
    result_image_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
    share_code: Mapped[str] = mapped_column(
        String(8),
        unique=True,
        default=generate_share_code,
        index=True,
    )
    view_count: Mapped[int] = mapped_column(Integer, default=0)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    expires_at: Mapped[datetime] = mapped_column(DateTime, default=default_expires_at)

    # 관계
    test: Mapped["Test"] = relationship("Test", back_populates="results")

    @property
    def is_expired(self) -> bool:
        return datetime.utcnow() > self.expires_at


# 순환 참조 방지
from app.models.test import Test  # noqa: E402, F401

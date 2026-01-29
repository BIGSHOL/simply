"""
커스텀 SQLAlchemy 타입

Phase 1, T1.1: 데이터베이스 스키마 & 시드 데이터
"""
import uuid
from typing import Any
from sqlalchemy import String, TypeDecorator


class UUID(TypeDecorator):
    """플랫폼 독립적 UUID 타입 (PostgreSQL, SQLite 호환)"""
    impl = String(32)
    cache_ok = True

    def process_bind_param(self, value: Any, dialect: Any) -> str | None:
        if value is None:
            return None
        if isinstance(value, uuid.UUID):
            return value.hex
        return str(uuid.UUID(value)).replace("-", "")

    def process_result_value(self, value: Any, dialect: Any) -> uuid.UUID | None:
        if value is None:
            return None
        if isinstance(value, uuid.UUID):
            return value
        return uuid.UUID(value)

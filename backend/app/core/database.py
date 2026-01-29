"""
데이터베이스 연결 설정

Phase 1, T1.1: 데이터베이스 스키마 & 시드 데이터
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Session
from app.core.config import settings


class Base(DeclarativeBase):
    pass


# 데이터베이스 URL 처리
database_url = settings.database_url

# PostgreSQL asyncpg를 sync로 변환
if "+asyncpg" in database_url:
    database_url = database_url.replace("+asyncpg", "")

# SQLite 설정
connect_args = {}
if database_url.startswith("sqlite"):
    connect_args = {"check_same_thread": False}

engine = create_engine(
    database_url,
    echo=settings.debug,
    connect_args=connect_args,
)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)


def get_db() -> Session:
    """DB 세션 생성"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

"""
FastAPI 메인 애플리케이션

Phase 1, T1.3: 테스트 목록 API
"""
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import api_router
from app.core.config import settings
from app.core.database import engine, Base
from app.models import *  # noqa: F401,F403 - 모델 등록용

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 시작: DB 테이블 자동 생성
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="Simly API",
    description="AI 심리테스트 플랫폼 API",
    version="0.1.0",
    lifespan=lifespan,
)

# CORS 설정 - 환경변수에서 쉼표 구분으로 여러 origin 지원
cors_origins = [origin.strip() for origin in settings.cors_origins.split(",")]

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API 라우터 등록
app.include_router(api_router)


@app.get("/")
async def root():
    return {"message": "Welcome to Simly API"}


@app.get("/health")
async def health():
    return {"status": "healthy"}

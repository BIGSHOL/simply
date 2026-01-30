"""
API v1 라우터

Phase 1, T1.3: 테스트 목록 API
Phase 3, T3.1: 결과 조회 API
"""
from fastapi import APIRouter
from app.api.v1.tests import router as tests_router
from app.api.v1.results import router as results_router
from app.api.v1.admin import router as admin_router

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(tests_router)
api_router.include_router(results_router)
api_router.include_router(admin_router)

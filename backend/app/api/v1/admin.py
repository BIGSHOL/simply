"""
관리자 API 라우터

실제 통계 조회용 (비공개)
"""
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.config import settings
from app.services import test_service

router = APIRouter(prefix="/admin", tags=["admin"])


@router.get("/stats")
def get_real_stats(
    key: str = Query(..., description="관리자 키"),
    db: Session = Depends(get_db),
):
    """실제 통계 조회 (관리자 전용)"""
    if key != settings.secret_key:
        raise HTTPException(status_code=403, detail="Forbidden")

    stats = test_service.get_real_stats(db)
    return {"data": stats}

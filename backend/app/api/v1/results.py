"""
결과 API 라우터

Phase 3, T3.1: 결과 조회 API
"""
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.result import ResultApiResponse, ResultResponse
from app.services import result_service

router = APIRouter(prefix="/results", tags=["results"])


@router.get("/{result_id}", response_model=ResultApiResponse)
def get_result(
    result_id: str,
    db: Session = Depends(get_db),
) -> ResultApiResponse:
    """
    결과 조회 (ID 또는 공유 코드)

    - UUID 형식이면 ID로 조회
    - 8자리 문자열이면 공유 코드로 조회
    """
    result = None

    # UUID 형식인지 확인
    try:
        uuid_id = UUID(result_id)
        result = result_service.get_result_by_id(db, uuid_id)
    except ValueError:
        # 공유 코드로 조회
        if len(result_id) == 8:
            result = result_service.get_result_by_share_code(db, result_id)

    if not result:
        raise HTTPException(
            status_code=404,
            detail={
                "code": "RESULT_NOT_FOUND",
                "message": "결과를 찾을 수 없습니다",
            },
        )

    # 만료 확인
    if result.is_expired:
        raise HTTPException(
            status_code=410,
            detail={
                "code": "RESULT_EXPIRED",
                "message": "결과가 만료되었습니다",
            },
        )

    # 조회수 증가
    result_service.increment_view_count(db, result.id)

    return ResultApiResponse(data=ResultResponse.model_validate(result))

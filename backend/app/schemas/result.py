"""
결과 API 스키마

Phase 3, T3.1: 결과 조회 API
"""
from pydantic import BaseModel
from typing import Optional
from uuid import UUID


class ResultResponse(BaseModel):
    """결과 응답"""
    id: UUID
    test_id: UUID
    result_type: str
    result_title: str
    result_content: str
    result_image_url: Optional[str] = None
    share_code: str
    view_count: int = 0

    model_config = {"from_attributes": True}


class ResultApiResponse(BaseModel):
    """결과 API 응답"""
    data: ResultResponse

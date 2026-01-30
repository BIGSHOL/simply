"""
테스트 API 스키마

Phase 1, T1.3: 테스트 목록 API
"""
from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID


class ChoiceResponse(BaseModel):
    """선택지 응답"""
    id: UUID
    order_num: int
    content: str

    model_config = {"from_attributes": True}


class QuestionResponse(BaseModel):
    """질문 응답"""
    id: UUID
    order_num: int
    content: str
    image_url: Optional[str] = None
    choices: list[ChoiceResponse] = []

    model_config = {"from_attributes": True}


class TestSummaryResponse(BaseModel):
    """테스트 요약 응답 (목록용)"""
    id: UUID
    title: str
    description: str
    thumbnail_url: Optional[str] = None
    category: str
    question_count: int
    play_count: int
    like_count: int = 0

    model_config = {"from_attributes": True}


class TestDetailResponse(BaseModel):
    """테스트 상세 응답"""
    id: UUID
    title: str
    description: str
    thumbnail_url: Optional[str] = None
    category: str
    question_count: int
    play_count: int
    like_count: int = 0
    questions: list[QuestionResponse] = []

    model_config = {"from_attributes": True}


class TestListResponse(BaseModel):
    """테스트 목록 API 응답"""
    data: list[TestSummaryResponse]


class TestDetailApiResponse(BaseModel):
    """테스트 상세 API 응답"""
    data: TestDetailResponse


# Submit 관련 스키마
class AnswerRequest(BaseModel):
    """단일 답변 요청"""
    question_id: UUID
    choice_id: UUID


class SubmitTestRequest(BaseModel):
    """테스트 제출 요청"""
    answers: list[AnswerRequest]


class ResultResponse(BaseModel):
    """결과 응답"""
    id: UUID
    test_id: UUID
    result_type: str
    result_title: str
    result_content: str
    result_image_url: Optional[str] = None
    share_code: str

    model_config = {"from_attributes": True}


class SubmitTestResponse(BaseModel):
    """테스트 제출 응답"""
    data: ResultResponse
    meta: Optional[dict] = None

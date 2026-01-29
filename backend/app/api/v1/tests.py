"""
테스트 API 라우터

Phase 1, T1.3: 테스트 목록 API
Phase 2, T2.3: 점수 기반 결과 생성
"""
from uuid import UUID
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.test import (
    TestListResponse,
    TestDetailApiResponse,
    TestSummaryResponse,
    TestDetailResponse,
    SubmitTestRequest,
    SubmitTestResponse,
    ResultResponse,
)
from app.services import test_service, result_service, score_service

router = APIRouter(prefix="/tests", tags=["tests"])


@router.get("", response_model=TestListResponse)
def get_tests(
    category: Optional[str] = Query(None, description="카테고리 필터 (personality, love, career, fun)"),
    db: Session = Depends(get_db),
) -> TestListResponse:
    """테스트 목록 조회"""
    tests = test_service.get_tests(db, category=category)

    return TestListResponse(
        data=[
            TestSummaryResponse(
                id=test.id,
                title=test.title,
                description=test.description,
                thumbnail_url=test.thumbnail_url,
                category=test.category,
                question_count=test.question_count,
                play_count=test.play_count,
            )
            for test in tests
        ]
    )


@router.get("/{test_id}", response_model=TestDetailApiResponse)
def get_test_detail(
    test_id: UUID,
    db: Session = Depends(get_db),
) -> TestDetailApiResponse:
    """테스트 상세 조회"""
    test = test_service.get_test_by_id(db, test_id)

    if not test:
        raise HTTPException(
            status_code=404,
            detail={
                "code": "TEST_NOT_FOUND",
                "message": "테스트를 찾을 수 없습니다",
            },
        )

    return TestDetailApiResponse(data=TestDetailResponse.model_validate(test))


@router.post("/{test_id}/submit", response_model=SubmitTestResponse)
def submit_test(
    test_id: UUID,
    request: SubmitTestRequest,
    db: Session = Depends(get_db),
) -> SubmitTestResponse:
    """테스트 제출 및 점수 기반 결과 생성"""
    # 테스트 조회
    test = test_service.get_test_by_id(db, test_id)
    if not test:
        raise HTTPException(
            status_code=404,
            detail={
                "code": "TEST_NOT_FOUND",
                "message": "테스트를 찾을 수 없습니다",
            },
        )

    # 답변 검증
    question_ids = {str(q.id) for q in test.questions}
    answer_question_ids = {str(a.question_id) for a in request.answers}

    if question_ids != answer_question_ids:
        raise HTTPException(
            status_code=400,
            detail={
                "code": "INVALID_ANSWERS",
                "message": "모든 질문에 답변해야 합니다",
            },
        )

    # 선택지 검증
    choice_map = {}
    for q in test.questions:
        for c in q.choices:
            choice_map[str(c.id)] = {"question_id": str(q.id), "content": c.content}

    for answer in request.answers:
        choice_id = str(answer.choice_id)
        if choice_id not in choice_map:
            raise HTTPException(
                status_code=400,
                detail={
                    "code": "INVALID_CHOICE",
                    "message": "유효하지 않은 선택지입니다",
                },
            )
        if choice_map[choice_id]["question_id"] != str(answer.question_id):
            raise HTTPException(
                status_code=400,
                detail={
                    "code": "INVALID_CHOICE",
                    "message": "선택지가 질문과 일치하지 않습니다",
                },
            )

    # 캐시 확인
    answers_dict = [
        {"question_id": a.question_id, "choice_id": a.choice_id}
        for a in request.answers
    ]
    answers_hash = result_service.generate_answers_hash(test_id, answers_dict)
    cached_result = result_service.find_cached_result(db, test_id, answers_hash)

    if cached_result:
        return SubmitTestResponse(
            data=ResultResponse.model_validate(cached_result),
            meta={"cached": True},
        )

    # 점수 계산 및 결과 유형 조회
    total_score = score_service.calculate_score(db, test_id, answers_dict)
    result_type = score_service.get_result_type_by_score(db, test_id, total_score)

    if result_type:
        result_data = {
            "result_type": result_type.result_type,
            "result_title": result_type.result_title,
            "result_content": result_type.result_content,
        }
    else:
        result_data = score_service.get_default_result(test.title)

    # 결과 저장
    result = result_service.create_result(
        db=db,
        test_id=test_id,
        answers_hash=answers_hash,
        result_type=result_data["result_type"],
        result_title=result_data["result_title"],
        result_content=result_data["result_content"],
    )

    # 참여 수 증가
    test_service.increment_play_count(db, test_id)

    return SubmitTestResponse(
        data=ResultResponse.model_validate(result),
        meta={"cached": False, "score": total_score},
    )

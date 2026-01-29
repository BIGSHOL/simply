"""
결과 서비스 - 결과 저장 및 캐싱

Phase 2, T2.3: AI 결과 생성 API
"""
import hashlib
import json
from uuid import UUID
from typing import Optional
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.result import Result


def generate_answers_hash(test_id: UUID, answers: list[dict]) -> str:
    """
    답변 조합의 고유 해시 생성

    동일한 테스트에서 동일한 답변 조합은 같은 해시를 생성
    """
    # 답변을 정렬하여 순서에 상관없이 동일한 해시 생성
    sorted_answers = sorted(
        [{"q": str(a["question_id"]), "c": str(a["choice_id"])} for a in answers],
        key=lambda x: x["q"]
    )
    payload = json.dumps({
        "test_id": str(test_id),
        "answers": sorted_answers
    }, sort_keys=True)

    return hashlib.sha256(payload.encode()).hexdigest()


def find_cached_result(db: Session, test_id: UUID, answers_hash: str) -> Optional[Result]:
    """
    캐시된 결과 조회

    동일한 답변 조합이 있으면 기존 결과 반환 (AI 호출 절약)
    """
    query = (
        select(Result)
        .where(Result.test_id == test_id)
        .where(Result.answers_hash == answers_hash)
    )
    result = db.execute(query)
    return result.scalar_one_or_none()


def create_result(
    db: Session,
    test_id: UUID,
    answers_hash: str,
    result_type: str,
    result_title: str,
    result_content: str,
    result_image_url: Optional[str] = None,
) -> Result:
    """새 결과 생성"""
    result = Result(
        test_id=test_id,
        answers_hash=answers_hash,
        result_type=result_type,
        result_title=result_title,
        result_content=result_content,
        result_image_url=result_image_url,
    )
    db.add(result)
    db.commit()
    db.refresh(result)
    return result


def get_result_by_id(db: Session, result_id: UUID) -> Optional[Result]:
    """결과 조회"""
    query = select(Result).where(Result.id == result_id)
    result = db.execute(query)
    return result.scalar_one_or_none()


def get_result_by_share_code(db: Session, share_code: str) -> Optional[Result]:
    """공유 코드로 결과 조회"""
    query = select(Result).where(Result.share_code == share_code)
    result = db.execute(query)
    return result.scalar_one_or_none()


def increment_view_count(db: Session, result_id: UUID) -> None:
    """조회수 증가"""
    result = get_result_by_id(db, result_id)
    if result:
        result.view_count += 1
        db.commit()

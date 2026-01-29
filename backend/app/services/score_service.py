"""
점수 기반 결과 서비스

선택지 점수를 합산하여 미리 정의된 결과 유형 반환
"""
from uuid import UUID
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.test import Test, Choice, ResultType


def calculate_score(db: Session, test_id: UUID, answers: list[dict]) -> int:
    """
    선택된 답변들의 점수 합산

    Args:
        db: DB 세션
        test_id: 테스트 ID
        answers: [{"question_id": ..., "choice_id": ...}, ...]

    Returns:
        총점
    """
    choice_ids = [a["choice_id"] for a in answers]

    query = select(Choice).where(Choice.id.in_(choice_ids))
    result = db.execute(query)
    choices = result.scalars().all()

    return sum(c.score for c in choices)


def get_result_type_by_score(db: Session, test_id: UUID, score: int) -> ResultType | None:
    """
    점수에 해당하는 결과 유형 조회

    Args:
        db: DB 세션
        test_id: 테스트 ID
        score: 총점

    Returns:
        ResultType 또는 None
    """
    query = (
        select(ResultType)
        .where(ResultType.test_id == test_id)
        .where(ResultType.min_score <= score)
        .where(ResultType.max_score >= score)
    )
    result = db.execute(query)
    return result.scalar_one_or_none()


def get_default_result(test_title: str) -> dict:
    """기본 결과 (결과 유형이 없을 때)"""
    return {
        "result_type": "분석 완료",
        "result_title": "당신의 결과가 나왔어요!",
        "result_content": f"""### 분석 결과

{test_title} 테스트를 완료했습니다!

결과 유형이 아직 설정되지 않았습니다.
관리자에게 문의해주세요.""",
    }

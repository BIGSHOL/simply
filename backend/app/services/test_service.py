"""
테스트 서비스

Phase 1, T1.3: 테스트 목록 API
"""
from uuid import UUID
from typing import Optional
from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload
from app.models.test import Test, Question


def get_tests(
    db: Session,
    category: Optional[str] = None,
) -> list[Test]:
    """테스트 목록 조회"""
    query = select(Test).where(Test.is_active == True).order_by(Test.play_count.desc())

    if category:
        query = query.where(Test.category == category)

    result = db.execute(query)
    return list(result.scalars().all())


def get_test_by_id(db: Session, test_id: UUID) -> Optional[Test]:
    """테스트 상세 조회 (질문, 선택지 포함)"""
    query = (
        select(Test)
        .options(
            selectinload(Test.questions).selectinload(Question.choices)
        )
        .where(Test.id == test_id)
        .where(Test.is_active == True)
    )

    result = db.execute(query)
    return result.scalar_one_or_none()


def increment_play_count(db: Session, test_id: UUID) -> None:
    """참여 수 증가 (표시용 + 실제)"""
    query = select(Test).where(Test.id == test_id)
    result = db.execute(query)
    test = result.scalar_one_or_none()
    if test:
        test.play_count += 1
        test.real_play_count += 1
        db.commit()


def increment_like_count(db: Session, test_id: UUID) -> None:
    """좋아요 수 증가 (표시용 + 실제)"""
    query = select(Test).where(Test.id == test_id)
    result = db.execute(query)
    test = result.scalar_one_or_none()
    if test:
        test.like_count += 1
        test.real_like_count += 1
        db.commit()


def get_real_stats(db: Session) -> list[dict]:
    """관리자용: 실제 통계 조회"""
    query = select(Test).where(Test.is_active == True).order_by(Test.real_play_count.desc())
    result = db.execute(query)
    tests = list(result.scalars().all())
    return [
        {
            "id": str(t.id),
            "title": t.title,
            "category": t.category,
            "play_count_display": t.play_count,
            "real_play_count": t.real_play_count,
            "like_count_display": t.like_count,
            "real_like_count": t.real_like_count,
        }
        for t in tests
    ]

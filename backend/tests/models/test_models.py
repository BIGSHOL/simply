"""
모델 테스트 (RED 상태 → GREEN으로 전환 예정)

Phase 1, T1.1: 데이터베이스 스키마 & 시드 데이터
TDD: 테스트 먼저 작성
"""
import pytest
from datetime import datetime
from uuid import UUID


class TestTestModel:
    """Test 모델 테스트"""

    def test_create_test_with_required_fields(self, db_session):
        """필수 필드로 테스트 생성"""
        from app.models.test import Test

        test = Test(
            title="MBTI로 알아보는 나의 연애 스타일",
            description="당신의 연애 성향을 분석합니다",
            category="love",
        )
        db_session.add(test)
        db_session.commit()
        db_session.refresh(test)

        assert test.id is not None
        assert isinstance(test.id, UUID)
        assert test.title == "MBTI로 알아보는 나의 연애 스타일"
        assert test.category == "love"
        assert test.play_count == 0
        assert test.is_active is True
        assert test.created_at is not None

    def test_test_category_enum_values(self):
        """카테고리 enum 값 검증"""
        from app.models.test import TestCategory

        assert TestCategory.PERSONALITY.value == "personality"
        assert TestCategory.LOVE.value == "love"
        assert TestCategory.CAREER.value == "career"
        assert TestCategory.FUN.value == "fun"

    def test_test_with_thumbnail(self, db_session):
        """썸네일이 있는 테스트 생성"""
        from app.models.test import Test

        test = Test(
            title="테스트",
            description="설명",
            category="personality",
            thumbnail_url="/images/test.jpg",
        )
        db_session.add(test)
        db_session.commit()

        assert test.thumbnail_url == "/images/test.jpg"


class TestQuestionModel:
    """Question 모델 테스트"""

    def test_create_question_with_test(self, db_session, test_fixture):
        """테스트에 질문 추가"""
        from app.models.test import Question

        question = Question(
            test_id=test_fixture.id,
            order_num=1,
            content="연인과 데이트할 때 선호하는 방식은?",
        )
        db_session.add(question)
        db_session.commit()
        db_session.refresh(question)

        assert question.id is not None
        assert question.test_id == test_fixture.id
        assert question.order_num == 1
        assert question.image_url is None

    def test_question_with_image(self, db_session, test_fixture):
        """이미지가 있는 질문"""
        from app.models.test import Question

        question = Question(
            test_id=test_fixture.id,
            order_num=1,
            content="질문 내용",
            image_url="/images/q1.jpg",
        )
        db_session.add(question)
        db_session.commit()

        assert question.image_url == "/images/q1.jpg"


class TestChoiceModel:
    """Choice 모델 테스트"""

    def test_create_choice_with_question(self, db_session, question_fixture):
        """질문에 선택지 추가"""
        from app.models.test import Choice

        choice = Choice(
            question_id=question_fixture.id,
            order_num=1,
            content="집에서 영화 보기",
        )
        db_session.add(choice)
        db_session.commit()
        db_session.refresh(choice)

        assert choice.id is not None
        assert choice.question_id == question_fixture.id
        assert choice.order_num == 1

    def test_multiple_choices_per_question(self, db_session, question_fixture):
        """한 질문에 여러 선택지"""
        from app.models.test import Choice

        choices = [
            Choice(question_id=question_fixture.id, order_num=i, content=f"선택지 {i}")
            for i in range(1, 5)
        ]
        db_session.add_all(choices)
        db_session.commit()

        assert len(choices) == 4


class TestResultModel:
    """Result 모델 테스트"""

    def test_create_result(self, db_session, test_fixture):
        """결과 생성"""
        from app.models.result import Result

        result = Result(
            test_id=test_fixture.id,
            answers_hash="abc123hash",
            result_type="ENFP형 연애 스타일",
            result_title="열정적인 로맨티스트",
            result_content="당신은 열정적인 로맨티스트입니다...",
        )
        db_session.add(result)
        db_session.commit()
        db_session.refresh(result)

        assert result.id is not None
        assert result.share_code is not None  # 자동 생성
        assert len(result.share_code) == 8
        assert result.view_count == 0
        assert result.expires_at is not None  # 30일 후

    def test_result_with_image(self, db_session, test_fixture):
        """이미지가 있는 결과"""
        from app.models.result import Result

        result = Result(
            test_id=test_fixture.id,
            answers_hash="hash123",
            result_type="타입",
            result_title="제목",
            result_content="내용",
            result_image_url="/images/result.jpg",
        )
        db_session.add(result)
        db_session.commit()

        assert result.result_image_url == "/images/result.jpg"

    def test_find_result_by_share_code(self, db_session, result_fixture):
        """share_code로 결과 조회"""
        from app.models.result import Result

        found = db_session.query(Result).filter_by(share_code=result_fixture.share_code).first()
        assert found is not None
        assert found.id == result_fixture.id

    def test_result_cache_by_answers_hash(self, db_session, test_fixture):
        """동일 답변은 캐시된 결과 반환"""
        from app.models.result import Result

        # 첫 번째 결과
        result1 = Result(
            test_id=test_fixture.id,
            answers_hash="same_hash",
            result_type="타입",
            result_title="제목",
            result_content="내용",
        )
        db_session.add(result1)
        db_session.commit()

        # 같은 hash로 조회
        cached = db_session.query(Result).filter_by(
            test_id=test_fixture.id,
            answers_hash="same_hash"
        ).first()

        assert cached is not None
        assert cached.id == result1.id


class TestRelationships:
    """모델 관계 테스트"""

    def test_test_has_questions(self, db_session, test_with_questions):
        """테스트 -> 질문 관계"""
        assert len(test_with_questions.questions) > 0
        assert test_with_questions.questions[0].test_id == test_with_questions.id

    def test_question_has_choices(self, db_session, question_with_choices):
        """질문 -> 선택지 관계"""
        assert len(question_with_choices.choices) > 0
        assert question_with_choices.choices[0].question_id == question_with_choices.id

    def test_cascade_delete_test(self, db_session, test_with_questions):
        """테스트 삭제 시 질문도 삭제"""
        from app.models.test import Test, Question

        test_id = test_with_questions.id
        db_session.delete(test_with_questions)
        db_session.commit()

        assert db_session.query(Test).get(test_id) is None
        assert db_session.query(Question).filter_by(test_id=test_id).count() == 0

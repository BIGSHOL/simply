"""
연애 유형 테스트 서비스 단위 테스트

Phase 1, T1-LOVE.1: RED 단계
"""
import pytest
from app.services.love_test_service import (
    calculate_dimension_scores,
    classify_love_type,
    QUESTION_DIMENSION_MAP,
    DIMENSIONS,
)


class TestDimensionScoreCalculation:
    """차원별 점수 계산 테스트"""

    def test_all_a_answers(self):
        """모든 답변이 A일 때 점수 계산"""
        answers = [{"question_id": i, "choice": "A"} for i in range(1, 21)]
        scores = calculate_dimension_scores(answers)

        # 적극성: Q1,4,8,12,17 -> 모두 A = 10점 -> 100%
        assert scores["proactivity"] == 100
        # 감정표현: Q2,5,9,14 -> 모두 A = 8점 -> 100%
        assert scores["expression"] == 100
        # 독립성: Q3,20은 B가 점수, Q7,16은 A가 점수 -> A선택시 4점 -> 50%
        assert scores["independence"] == 50
        # 헌신도: Q10,13,18 -> 모두 A = 6점 -> 100%
        assert scores["commitment"] == 100
        # 로맨스: Q6,11,15,19 -> 모두 A = 8점 -> 100%
        assert scores["romance"] == 100

    def test_all_b_answers(self):
        """모든 답변이 B일 때 점수 계산"""
        answers = [{"question_id": i, "choice": "B"} for i in range(1, 21)]
        scores = calculate_dimension_scores(answers)

        assert scores["proactivity"] == 0
        assert scores["expression"] == 0
        # 독립성: Q3,20은 B가 점수 -> 4점 -> 50%
        assert scores["independence"] == 50
        assert scores["commitment"] == 0
        assert scores["romance"] == 0

    def test_mixed_answers(self):
        """혼합 답변 점수 계산"""
        # 적극성 HIGH (Q1,4,8,12,17 중 4개 A): 8/10 = 80
        # 감정표현 HIGH (Q2,5,9,14 중 4개 A): 8/8 = 100
        # 독립성 LOW (Q3,7,16,20 모두 A): 4/8 = 50
        # 헌신도 MID (Q10,13,18 중 2개 A): 4/6 = 67
        # 로맨스 HIGH (Q6,11,15,19 중 3개 A): 6/8 = 75
        answers = [
            {"question_id": 1, "choice": "A"},   # 적극성
            {"question_id": 2, "choice": "A"},   # 감정표현
            {"question_id": 3, "choice": "A"},   # 독립성 (역코딩, 0점)
            {"question_id": 4, "choice": "A"},   # 적극성
            {"question_id": 5, "choice": "A"},   # 감정표현
            {"question_id": 6, "choice": "A"},   # 로맨스
            {"question_id": 7, "choice": "A"},   # 독립성
            {"question_id": 8, "choice": "A"},   # 적극성
            {"question_id": 9, "choice": "A"},   # 감정표현
            {"question_id": 10, "choice": "A"},  # 헌신도
            {"question_id": 11, "choice": "A"},  # 로맨스
            {"question_id": 12, "choice": "A"},  # 적극성
            {"question_id": 13, "choice": "A"},  # 헌신도
            {"question_id": 14, "choice": "A"},  # 감정표현
            {"question_id": 15, "choice": "A"},  # 로맨스
            {"question_id": 16, "choice": "A"},  # 독립성
            {"question_id": 17, "choice": "B"},  # 적극성 (0점)
            {"question_id": 18, "choice": "B"},  # 헌신도 (0점)
            {"question_id": 19, "choice": "B"},  # 로맨스 (0점)
            {"question_id": 20, "choice": "A"},  # 독립성 (역코딩, 0점)
        ]
        scores = calculate_dimension_scores(answers)

        assert scores["proactivity"] == 80
        assert scores["expression"] == 100
        assert scores["independence"] == 50
        assert scores["commitment"] == 67
        assert scores["romance"] == 75


class TestLoveTypeClassification:
    """연애 유형 분류 테스트"""

    def test_straight_shooter(self):
        """직진 러버 유형 분류"""
        # 적극성 HIGH + 감정표현 HIGH + 독립성 LOW
        scores = {
            "proactivity": 100,
            "expression": 100,
            "independence": 25,
            "commitment": 67,
            "romance": 50,
        }
        result = classify_love_type(scores)
        assert result == "straight_shooter"

    def test_romance_express(self):
        """로맨틱 폭주기관차 유형 분류"""
        # 적극성 HIGH + 감정표현 HIGH + 로맨스 HIGH
        scores = {
            "proactivity": 100,
            "expression": 100,
            "independence": 25,
            "commitment": 100,
            "romance": 100,
        }
        result = classify_love_type(scores)
        assert result == "romance_express"

    def test_slow_burner(self):
        """슬로우 버너 유형 분류"""
        # 적극성 LOW + 독립성 MID 이상
        scores = {
            "proactivity": 10,
            "expression": 25,
            "independence": 75,
            "commitment": 33,
            "romance": 25,
        }
        result = classify_love_type(scores)
        assert result == "slow_burner"

    def test_free_spirit(self):
        """자유영혼 연인 유형 분류"""
        # 독립성 HIGH + 헌신도 LOW
        scores = {
            "proactivity": 50,
            "expression": 50,
            "independence": 100,
            "commitment": 17,
            "romance": 50,
        }
        result = classify_love_type(scores)
        assert result == "free_spirit"

    def test_emotional_dreamer(self):
        """감성 몽글러 유형 분류"""
        # 로맨스 HIGH + 적극성 LOW
        scores = {
            "proactivity": 30,
            "expression": 63,
            "independence": 50,
            "commitment": 50,
            "romance": 100,
        }
        result = classify_love_type(scores)
        assert result == "emotional_dreamer"

    def test_tsundere_expert(self):
        """츤데레 마스터 유형 분류"""
        # 감정표현 LOW + 적극성 MID
        scores = {
            "proactivity": 60,
            "expression": 20,
            "independence": 50,
            "commitment": 50,
            "romance": 50,
        }
        result = classify_love_type(scores)
        assert result == "tsundere_expert"

    def test_devoted_partner(self):
        """헌신형 파트너 유형 분류"""
        # 독립성 LOW + 헌신도 HIGH
        scores = {
            "proactivity": 50,
            "expression": 50,
            "independence": 20,
            "commitment": 100,
            "romance": 50,
        }
        result = classify_love_type(scores)
        assert result == "devoted_partner"

    def test_push_pull_master(self):
        """밀당 장인 유형 분류"""
        # 적극성 MID + 감정표현 LOW
        scores = {
            "proactivity": 60,
            "expression": 40,
            "independence": 50,
            "commitment": 50,
            "romance": 50,
        }
        result = classify_love_type(scores)
        assert result == "push_pull_master"

    def test_practical_lover(self):
        """현실주의 연인 유형 분류"""
        # 헌신도 HIGH + 로맨스 LOW
        scores = {
            "proactivity": 40,
            "expression": 30,
            "independence": 70,
            "commitment": 100,
            "romance": 20,
        }
        result = classify_love_type(scores)
        assert result == "practical_lover"

    def test_default_type(self):
        """기본 유형 (중립적 점수)"""
        # 모든 점수가 중간값
        scores = {
            "proactivity": 50,
            "expression": 50,
            "independence": 50,
            "commitment": 50,
            "romance": 50,
        }
        result = classify_love_type(scores)
        # 기본값은 steady_lover
        assert result == "steady_lover"


class TestQuestionDimensionMapping:
    """문항-차원 매핑 테스트"""

    def test_mapping_completeness(self):
        """20개 문항 모두 매핑되어 있는지 확인"""
        assert len(QUESTION_DIMENSION_MAP) == 20
        for i in range(1, 21):
            assert i in QUESTION_DIMENSION_MAP

    def test_dimension_question_counts(self):
        """각 차원별 문항 수 확인"""
        dimension_counts = {dim: 0 for dim in DIMENSIONS}
        for dimension, _ in QUESTION_DIMENSION_MAP.values():
            dimension_counts[dimension] += 1

        assert dimension_counts["proactivity"] == 5   # 적극성 5문항
        assert dimension_counts["expression"] == 4    # 감정표현 4문항
        assert dimension_counts["independence"] == 4  # 독립성 4문항
        assert dimension_counts["commitment"] == 3    # 헌신도 3문항
        assert dimension_counts["romance"] == 4       # 로맨스 4문항

    def test_score_values(self):
        """점수값이 올바른지 확인 (0 또는 2)"""
        for dimension, scores in QUESTION_DIMENSION_MAP.values():
            assert scores["A"] in [0, 2]
            assert scores["B"] in [0, 2]
            # 각 문항은 A 또는 B 중 하나만 점수를 가져야 함
            assert scores["A"] + scores["B"] == 2

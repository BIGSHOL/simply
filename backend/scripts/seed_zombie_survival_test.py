"""
좀비 아포칼립스 생존 유형 시드 스크립트
10문항, 8개 결과 유형
실행: python -m scripts.seed_zombie_survival_test
"""
import os
import sys
import uuid

# Windows 콘솔 UTF-8 출력 설정
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

# 프로젝트 루트 경로 추가
BACKEND_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BACKEND_DIR)

from app.core.database import Base, SessionLocal, engine
from app.models import Test, Question, Choice, ResultType


def seed_zombie_survival_test():
    """좀비 아포칼립스 생존 유형 시드 데이터 생성"""
    db = SessionLocal()

    try:
        # 기존 테스트 확인
        existing = db.query(Test).filter(Test.title.contains("좀비")).first()
        if existing:
            print("⚠️  좀비 아포칼립스 테스트가 이미 존재합니다. 시드 스킵.")
            return

        # 테스트 ID 생성
        test_id = uuid.uuid4()

        # 테스트 생성
        test = Test(
            id=test_id,
            title="좀비 아포칼립스 생존 유형",
            description="극한 상황에서의 당신의 생존 전략은? 의사결정, 생존전략, 사회성 3가지 축으로 당신의 서바이벌 페르소나를 찾아보세요!",
            category="fun",
            thumbnail_url="/images/tests/zombie-survival.png",
            play_count=38920,
            like_count=3210,
        )
        db.add(test)

        # 10개 문항 (A=0점, B=3점)
        questions_data = [
            {
                "order_num": 1,
                "content": "좀비 발생 첫날, 당신의 첫 반응은?",
                "choices": [
                    {"order_num": 1, "content": "뉴스와 SNS를 확인하며 상황을 분석한다", "score": 0},
                    {"order_num": 2, "content": "일단 집에 있는 식량과 무기부터 챙긴다", "score": 3},
                ],
            },
            {
                "order_num": 2,
                "content": "좀비 무리를 마주쳤을 때 당신의 선택은?",
                "choices": [
                    {"order_num": 1, "content": "숨을 죽이고 조용히 우회한다", "score": 0},
                    {"order_num": 2, "content": "무기를 들고 길을 뚫고 나간다", "score": 3},
                ],
            },
            {
                "order_num": 3,
                "content": "생존자 그룹을 발견했다. 당신의 선택은?",
                "choices": [
                    {"order_num": 1, "content": "혼자가 안전하다. 조용히 떠난다", "score": 0},
                    {"order_num": 2, "content": "합류를 제안하거나 도움을 요청한다", "score": 3},
                ],
            },
            {
                "order_num": 4,
                "content": "은신처를 선택해야 한다. 어디로 갈까?",
                "choices": [
                    {"order_num": 1, "content": "지도를 보며 탈출로가 많은 2층 건물을 선택한다", "score": 0},
                    {"order_num": 2, "content": "뭔가 느낌이 좋은 저 창고로 간다", "score": 3},
                ],
            },
            {
                "order_num": 5,
                "content": "좀비가 문을 두드리기 시작했다. 어떻게 할까?",
                "choices": [
                    {"order_num": 1, "content": "뒷문으로 조용히 빠져나간다", "score": 0},
                    {"order_num": 2, "content": "문 열리기 전에 무기 들고 대기한다", "score": 3},
                ],
            },
            {
                "order_num": 6,
                "content": "부상당한 생존자를 발견했다. 어떻게 할까?",
                "choices": [
                    {"order_num": 1, "content": "안됐지만 내 생존이 우선이다. 지나간다", "score": 0},
                    {"order_num": 2, "content": "응급처치를 해주거나 안전한 곳으로 데려간다", "score": 3},
                ],
            },
            {
                "order_num": 7,
                "content": "물자가 있는 마트에 좀비가 있다. 어떻게 할까?",
                "choices": [
                    {"order_num": 1, "content": "좀비가 없는 편의점을 찾아 멀리 돌아간다", "score": 0},
                    {"order_num": 2, "content": "마트에 진입해서 좀비를 처리하고 물자를 확보한다", "score": 3},
                ],
            },
            {
                "order_num": 8,
                "content": "무전으로 구조 요청이 들려온다. 하지만 위치가 애매하다.",
                "choices": [
                    {"order_num": 1, "content": "무전 내용을 분석하고 지도로 정확한 위치를 계산한다", "score": 0},
                    {"order_num": 2, "content": "대충 저쪽 방향인 것 같다. 일단 가본다", "score": 3},
                ],
            },
            {
                "order_num": 9,
                "content": "생존자 그룹에서 리더를 뽑는다. 당신의 선택은?",
                "choices": [
                    {"order_num": 1, "content": "리더는 다른 사람이 하고, 나는 자유롭게 행동한다", "score": 0},
                    {"order_num": 2, "content": "리더가 되거나 적극적으로 그룹 활동에 참여한다", "score": 3},
                ],
            },
            {
                "order_num": 10,
                "content": "좀비 소굴을 발견했다. 어떻게 대응할까?",
                "choices": [
                    {"order_num": 1, "content": "표시해두고 절대 가지 않을 루트로 지정한다", "score": 0},
                    {"order_num": 2, "content": "좀비들을 유인해서 한꺼번에 제거할 방법을 생각한다", "score": 3},
                ],
            },
        ]

        # 문항 및 선택지 추가
        for q_data in questions_data:
            question_id = uuid.uuid4()
            question = Question(
                id=question_id,
                test_id=test_id,
                content=q_data["content"],
                order_num=q_data["order_num"],
            )
            db.add(question)

            for c_data in q_data["choices"]:
                choice = Choice(
                    id=uuid.uuid4(),
                    question_id=question_id,
                    content=c_data["content"],
                    score=c_data["score"],
                    order_num=c_data["order_num"],
                )
                db.add(choice)

        # 8개 결과 유형 (점수 범위: 0-30점, 8개 구간)
        result_types_data = [
            {
                "result_type": "냉철한 생존주의자",
                "result_title": "감정은 사치, 생존만이 진리. 혼자서도 끝까지 살아남는다",
                "result_content": """## 좀비 세계에서의 역할
당신은 좀비 아포칼립스에서 **혼자서도 무섭게 잘 살아남는 독립 생존 전문가**입니다. 다른 사람들이 패닉에 빠져 있을 때, 당신은 이미 물자를 계산하고 안전한 은신처를 확보했을 거예요.

## 생존 성향 분석
- **의사결정**: 감정보다 데이터. 모든 것을 계산하고 판단합니다.
- **생존전략**: 정면승부는 비효율적. 안전하게 이동하고 불필요한 전투는 회피합니다.
- **사회성**: 팀플보다 솔플이 편해요. 혼자서 생존하는 것이 더 효율적입니다.

## 생존 강점
1. 냉정한 상황 판단으로 최적의 선택
2. 효율적 자원 관리
3. 독립적 생존 능력
4. 위험 회피 전문가

## 생존 약점
1. 타인과의 협력 부족
2. 감정적 유대감 결여
3. 과도한 신중함으로 기회 놓칠 수 있음""",
                "min_score": 0,
                "max_score": 3,
            },
            {
                "result_type": "전술 참모형",
                "result_title": "팀의 두뇌, 완벽한 작전으로 모두를 살린다",
                "result_content": """## 좀비 세계에서의 역할
당신은 생존자 그룹의 **두뇌이자 전략 담당 참모**입니다. 완벽한 작전을 짜는 게 당신의 특기! 리더가 "가자!"라고 하면 "잠깐, 지도 보고 최적 루트 계산부터 해요"라고 말리는 타입이죠.

## 생존 성향 분석
- **의사결정**: 데이터 기반 전략 수립. 모든 변수를 고려합니다.
- **생존전략**: 정면 충돌은 최후의 수단. Plan A, B, C까지 준비합니다.
- **사회성**: 팀플레이가 생존 확률을 높인다는 것을 아는 협력주의자.

## 생존 강점
1. 완벽한 전략 기획
2. 팀 생존율 극대화
3. 리스크 관리 능력
4. 냉정한 조율자

## 생존 약점
1. 과도한 계획 집착
2. 행동력 부족
3. 리더십 발휘 어려움""",
                "min_score": 4,
                "max_score": 7,
            },
            {
                "result_type": "게릴라 파이터",
                "result_title": "혼자서 좀비 소탕, 조용하지만 치명적인 원맨아미",
                "result_content": """## 좀비 세계에서의 역할
당신은 **혼자서 좀비를 사냥하는 고독한 전사**입니다. 다른 사람들이 숨어 있을 때, 당신은 이미 무기를 들고 좀비를 제거하러 나섰을 거예요. 약점을 정확히 파악하고 효율적으로 처치하는 게 당신의 스타일.

## 생존 성향 분석
- **의사결정**: 전투 시뮬레이션을 머릿속으로 돌려요.
- **생존전략**: 도망치는 건 비효율적. 위협은 직접 제거합니다.
- **사회성**: 혼자가 편해요. 전투 효율을 최우선으로.

## 생존 강점
1. 전투 효율성
2. 냉정한 판단력
3. 자립적 생존
4. 전술적 사고

## 생존 약점
1. 고립 위험
2. 과신
3. 팀워크 부재""",
                "min_score": 8,
                "max_score": 11,
            },
            {
                "result_type": "전투 마스터",
                "result_title": "팀의 검과 방패, 전장에서 빛나는 전술 리더",
                "result_content": """## 좀비 세계에서의 역할
당신은 생존자 그룹의 **전투 리더이자 최강 전력**입니다. "내가 선두에서 좀비 막을 테니까 다들 내 뒤에서 안전하게 이동해!"라고 외치는 든든한 존재죠.

## 생존 성향 분석
- **의사결정**: 전투 경험과 데이터를 바탕으로 최적의 전술 선택.
- **생존전략**: 공격이 최선의 방어. 위협을 제거해야 팀이 안전합니다.
- **사회성**: 동료와 함께 싸우는 게 더 강하다는 것을 알아요.

## 생존 강점
1. 뛰어난 전투 능력
2. 전술적 리더십
3. 희생 정신
4. 냉정한 전장 판단

## 생존 약점
1. 과도한 책임감
2. 전투 의존
3. 번아웃 위험""",
                "min_score": 12,
                "max_score": 15,
            },
            {
                "result_type": "야생 생존왕",
                "result_title": "본능으로 위험을 피하고, 자연 속에서 홀로 살아남는다",
                "result_content": """## 좀비 세계에서의 역할
당신은 **도시를 벗어나 야생에서 홀로 생존하는 자연주의자**입니다. 본능적으로 환경을 읽어내는 능력이 탁월해요. 산 속에 은신처를 만들고 덫을 놓는 타입.

## 생존 성향 분석
- **의사결정**: 머리보다 몸이 먼저 반응. 위험 감지 즉시 회피.
- **생존전략**: 싸우는 것보다 숨는 게 낫죠.
- **사회성**: 혼자가 편하고, 다른 사람과 있으면 오히려 불안해요.

## 생존 강점
1. 뛰어난 위험 감지
2. 자연 친화력
3. 은신 기술
4. 자립적 생존

## 생존 약점
1. 사회성 부족
2. 자원 제한
3. 고립감""",
                "min_score": 16,
                "max_score": 19,
            },
            {
                "result_type": "파티 수호자",
                "result_title": "동료의 안전이 최우선, 든든한 방패막이",
                "result_content": """## 좀비 세계에서의 역할
당신은 생존자 그룹의 **수호천사이자 든든한 방패**입니다. "다들 내 뒤로! 내가 막을게!"라고 외치며 동료들을 지키는 게 당신의 본능이에요.

## 생존 성향 분석
- **의사결정**: "위험한 느낌이 들어"라는 직감을 믿고 즉시 대피.
- **생존전략**: 싸우기보다 팀원들을 안전하게 지키는 게 우선.
- **사회성**: 혼자보다 함께가 강하다는 것을 알아요.

## 생존 강점
1. 뛰어난 위험 감지
2. 희생 정신
3. 신뢰의 중심
4. 방어 전문가

## 생존 약점
1. 과도한 희생
2. 공격력 부족
3. 감정적 부담""",
                "min_score": 20,
                "max_score": 23,
            },
            {
                "result_type": "무법자 서바이버",
                "result_title": "본능대로 움직이고, 누구도 날 막을 수 없다",
                "result_content": """## 좀비 세계에서의 역할
당신은 **규칙 따위 신경 안 쓰는 자유로운 아웃사이더**입니다. "좀비 한 마리 나타났네? 일단 두들겨 패고 보자"는 식으로 본능대로 움직이는 타입!

## 생존 성향 분석
- **의사결정**: 생각보다 행동이 빨라요. "일단 해보고 안 되면 다른 거 하지 뭐"
- **생존전략**: 피하는 것보다 정면돌파가 짜릿하죠.
- **사회성**: 혼자가 편해요. 다른 사람 눈치 보는 건 답답합니다.

## 생존 강점
1. 뛰어난 순발력
2. 강력한 전투력
3. 자유로운 행동
4. 두려움 없음

## 생존 약점
1. 무모함
2. 계획 부재
3. 고립""",
                "min_score": 24,
                "max_score": 27,
            },
            {
                "result_type": "카리스마 리더",
                "result_title": "본능적 결단력으로 팀을 이끄는 타고난 지도자",
                "result_content": """## 좀비 세계에서의 역할
당신은 생존자 그룹의 **절대적 리더이자 희망의 상징**입니다. "믿고 따라와, 내가 책임진다!"라는 한마디로 사람들을 하나로 모으는 카리스마를 가졌어요.

## 생존 성향 분석
- **의사결정**: "이거다!"싶으면 즉시 결정하고 추진. 직감을 믿어요.
- **생존전략**: 공격이 최선의 방어. 위협은 정면으로 돌파.
- **사회성**: 함께 있을 때 더 강해져요. 팀을 이끌고 모두를 살리는 게 목표.

## 생존 강점
1. 강력한 리더십
2. 빠른 결단력
3. 희생 정신
4. 전투력과 전략의 조화

## 생존 약점
1. 과도한 책임감
2. 직관 의존
3. 번아웃""",
                "min_score": 28,
                "max_score": 30,
            },
        ]

        # 결과 유형 추가
        for rt_data in result_types_data:
            result_type = ResultType(
                id=uuid.uuid4(),
                test_id=test_id,
                result_type=rt_data["result_type"],
                result_title=rt_data["result_title"],
                result_content=rt_data["result_content"],
                min_score=rt_data["min_score"],
                max_score=rt_data["max_score"],
            )
            db.add(result_type)

        # 커밋
        db.commit()
        print("✅ 좀비 아포칼립스 생존 유형 시드 데이터 생성 완료!")
        print(f"   - 테스트 ID: {test_id}")
        print(f"   - 문항 수: 10개")
        print(f"   - 결과 유형: 8개")

    except Exception as e:
        db.rollback()
        print(f"❌ 좀비 아포칼립스 테스트 시드 실패: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    # 테이블 생성 확인
    Base.metadata.create_all(bind=engine)
    seed_zombie_survival_test()

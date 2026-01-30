"""
퇴사 후 나에게 맞는 부캐는? 시드 스크립트
10문항, 8개 결과 유형
실행: python -m scripts.seed_side_hustle_test
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


def seed_side_hustle_test():
    """퇴사 후 나에게 맞는 부캐는? 시드 데이터 생성"""
    db = SessionLocal()

    try:
        # 기존 테스트 확인
        existing = db.query(Test).filter(Test.title.contains("부캐")).first()
        if existing:
            print("⚠️  부캐 테스트가 이미 존재합니다. 시드 스킵.")
            return

        # 테스트 ID 생성
        test_id = uuid.uuid4()

        # 테스트 생성
        test = Test(
            id=test_id,
            title="퇴사 후 나에게 맞는 부캐는? 🚀",
            description="회사 그만두고 뭐 할까? Social/Solo, Creative/Consistent, Meaning/Money 3가지 축으로 당신에게 딱 맞는 부캐를 찾아보세요!",
            category="career",
            thumbnail_url="/images/tests/side-hustle.png",
            play_count=43210,
            like_count=3670,
        )
        db.add(test)

        # 10개 문항 (A=0점, B=3점)
        questions_data = [
            {
                "order_num": 1,
                "content": "퇴사 후 가장 이상적인 하루는?",
                "choices": [
                    {"order_num": 1, "content": "혼자 카페에서 조용히 노트북 작업", "score": 0},
                    {"order_num": 2, "content": "코워킹 스페이스에서 사람들과 네트워킹", "score": 3},
                ],
            },
            {
                "order_num": 2,
                "content": "부업/창업 아이템을 정할 때",
                "choices": [
                    {"order_num": 1, "content": "이미 검증된 수익 모델 선택", "score": 0},
                    {"order_num": 2, "content": "아무도 안 해본 새로운 시도", "score": 3},
                ],
            },
            {
                "order_num": 3,
                "content": "프로젝트 진행 방식은?",
                "choices": [
                    {"order_num": 1, "content": "혼자 집중해서 완성도 높이기", "score": 0},
                    {"order_num": 2, "content": "팀원들과 브레인스토밍하며 진행", "score": 3},
                ],
            },
            {
                "order_num": 4,
                "content": "퇴사 후 첫 달 목표는?",
                "choices": [
                    {"order_num": 1, "content": "최소 생활비 벌기", "score": 0},
                    {"order_num": 2, "content": "내가 하고 싶던 일 도전하기", "score": 3},
                ],
            },
            {
                "order_num": 5,
                "content": "업무 루틴은?",
                "choices": [
                    {"order_num": 1, "content": "매일 정해진 시간에 같은 작업", "score": 0},
                    {"order_num": 2, "content": "그때그때 영감에 따라 유연하게", "score": 3},
                ],
            },
            {
                "order_num": 6,
                "content": "수익이 불안정하다면?",
                "choices": [
                    {"order_num": 1, "content": "당장 안정적인 수입원 확보", "score": 0},
                    {"order_num": 2, "content": "의미 있는 일이면 조금 더 버팀", "score": 3},
                ],
            },
            {
                "order_num": 7,
                "content": "에너지 충전 방법은?",
                "choices": [
                    {"order_num": 1, "content": "혼자만의 시간으로 재충전", "score": 0},
                    {"order_num": 2, "content": "사람들 만나서 수다 떨며 충전", "score": 3},
                ],
            },
            {
                "order_num": 8,
                "content": "일하는 방식 선호도는?",
                "choices": [
                    {"order_num": 1, "content": "매뉴얼과 체크리스트로 체계적으로", "score": 0},
                    {"order_num": 2, "content": "즉흥적이고 실험적으로", "score": 3},
                ],
            },
            {
                "order_num": 9,
                "content": "성공의 기준은?",
                "choices": [
                    {"order_num": 1, "content": "통장 잔고가 늘어나는 것", "score": 0},
                    {"order_num": 2, "content": "내 일이 누군가에게 영향을 주는 것", "score": 3},
                ],
            },
            {
                "order_num": 10,
                "content": "새로운 프로젝트 제안이 들어온다면?",
                "choices": [
                    {"order_num": 1, "content": "수익성과 효율성 먼저 계산", "score": 0},
                    {"order_num": 2, "content": "재미있고 의미 있으면 일단 도전", "score": 3},
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
                "result_type": "수익형 전문가",
                "result_title": "혼자 꾸준히 돈 벌기",
                "result_content": """## 퇴사 후 당신의 모습
퇴사 3개월 차, 당신은 카페에서 노트북을 펴고 전문 프리랜서로 일하고 있습니다. 온라인 강의 제작, IT 외주, 번역, 세무/법무 컨설팅... 당신의 전문성을 활용한 고단가 프로젝트로 회사 다닐 때보다 더 많이 벌고 있죠.

## 성향 분석
- **독립성**: 상사 눈치 안 보고 내 속도로 일하는 것을 최고로 칩니다
- **체계성**: 검증된 방법을 선호합니다
- **수익 지향**: 시간 대비 수입을 정확히 계산합니다

## 강점
전문성을 돈으로 전환하는 능력 탁월, 혼자서도 안정적으로 수익 창출 가능

## 추천 부캐
IT 프리랜서, 전문 컨설턴트, 온라인 강사, 전문 번역가""",
                "min_score": 0,
                "max_score": 3,
            },
            {
                "result_type": "장인 크래프터",
                "result_title": "완벽한 작품을 만드는 사람",
                "result_content": """## 퇴사 후 당신의 모습
퇴사 후 당신은 작은 공방을 차렸습니다. 핸드메이드 가죽 제품, 도자기, 수제 비누, 목공예... 매일 아침 작업실에 들어서면 행복합니다. 대량 생산은 관심 없고, 하나하나 정성 들여 만든 작품에 당신의 이름을 새깁니다.

## 성향 분석
- **독립성**: 타인의 간섭 없이 내 작품 세계에 몰입
- **체계성**: 정해진 공정과 기법을 따르며 완벽 추구
- **의미 지향**: 돈보다 '내가 만든 것'에 대한 자부심

## 강점
장인 정신으로 고품질 제품 생산, 브랜드 충성도 높은 팬층

## 추천 부캐
핸드메이드 공예가, 수제 제과/제빵, 맞춤 의류 제작, 주얼리 디자이너""",
                "min_score": 4,
                "max_score": 7,
            },
            {
                "result_type": "디지털 노마드",
                "result_title": "세계 어디서든 창작하며 벌기",
                "result_content": """## 퇴사 후 당신의 모습
발리의 코워킹 스페이스에서 노트북을 열고, 오전엔 클라이언트 프로젝트, 오후엔 서핑. 당신의 수익원은 다양합니다. 디지털 디자인 판매, 블로그 수익, 유튜브 광고, 온라인 코칭...

## 성향 분석
- **독립성**: 조직의 틀에서 벗어나 내 방식대로
- **창의성**: 새로운 수익 모델을 끊임없이 실험
- **수익 지향**: 돈은 자유를 위한 수단

## 강점
시간과 장소의 완전한 자유, 다양한 수익원 실험 가능

## 추천 부캐
웹/앱 개발자, 그래픽/UI 디자이너, 블로거/브이로거, 온라인 마케터""",
                "min_score": 8,
                "max_score": 11,
            },
            {
                "result_type": "프리랜서 크리에이터",
                "result_title": "내 작품으로 세상에 메시지 전달",
                "result_content": """## 퇴사 후 당신의 모습
당신은 작가입니다. 소설, 웹툰, 일러스트, 음악... 회사 다닐 때 퇴근 후에만 할 수 있었던 창작을 이제 하루 종일 합니다. 수익? 솔직히 회사 다닐 때보다 적습니다. 하지만 '내 작품'을 세상에 내놓는 그 순간의 희열은 월급으로 살 수 없죠.

## 성향 분석
- **독립성**: 혼자만의 시간과 공간에서 몰입할 때 최고
- **창의성**: 새로운 표현, 새로운 메시지 끊임없이 탐구
- **의미 지향**: 돈보다 작품의 메시지와 가치

## 강점
순수 창작에 집중 가능, 독창적 세계관 구축

## 추천 부캐
작가, 웹툰 작가, 일러스트레이터, 인디 음악가, 독립 영화 감독""",
                "min_score": 12,
                "max_score": 15,
            },
            {
                "result_type": "N잡러 프로",
                "result_title": "다양한 부업으로 수익 다각화",
                "result_content": """## 퇴사 후 당신의 모습
월요일엔 카페 알바, 화요일엔 온라인 과외, 수요일엔 행사 MC, 목요일엔 대리운전... "너 직업이 뭐야?"라는 질문에 한 마디로 답하기 어렵습니다. 하지만 당신은 이 다양한 일들이 좋습니다.

## 성향 분석
- **사회성**: 사람들과 함께 일할 때 에너지
- **체계성**: 검증된 부업들을 조합
- **수익 지향**: 시간 활용을 최적화해 여러 곳에서 수익

## 강점
수익원 다각화로 안정성 확보, 다양한 인맥과 경험

## 추천 부캐
다양한 알바 조합, 배달 라이더+온라인 판매, 플랫폼 긱워커""",
                "min_score": 16,
                "max_score": 19,
            },
            {
                "result_type": "커뮤니티 빌더",
                "result_title": "사람들과 함께 의미있는 공간 만들기",
                "result_content": """## 퇴사 후 당신의 모습
당신은 작은 책방 겸 카페를 열었습니다. 수익은 프랜차이즈보다 적지만, 단골손님들과 나누는 대화가 당신을 행복하게 합니다. 매주 북클럽 모임, 작가와의 만남, 동네 주민들을 위한 강연...

## 성향 분석
- **사회성**: 사람들과 교류하며 의미 있는 관계
- **체계성**: 검증된 비즈니스 모델 선호
- **의미 지향**: 수익보다 '우리 동네에 이런 공간이 있어서 좋다'

## 강점
사람들과 깊은 유대 형성, 지역 커뮤니티의 중심 역할

## 추천 부캐
독립 책방 운영, 동네 카페 사장, 공유 오피스, 공방 겸 커뮤니티 공간""",
                "min_score": 20,
                "max_score": 23,
            },
            {
                "result_type": "콘텐츠 크리에이터",
                "result_title": "구독자와 소통하며 수익 창출",
                "result_content": """## 퇴사 후 당신의 모습
"오늘 영상 뭐 찍지?" 매일 아침 이 고민으로 시작합니다. 유튜브 구독자 10만, 인스타 팔로워 5만... 댓글로 소통하고, 라이브 방송에서 팬들과 수다 떨고, 협찬 제안 메일을 확인하는 것이 당신의 일상입니다.

## 성향 분석
- **사회성**: 사람들의 반응과 피드백에서 에너지
- **창의성**: 새로운 포맷, 새로운 트렌드 빠르게 캐치
- **수익 지향**: 조회수, 구독자 = 돈

## 강점
높은 수익 가능성, 구독자와 직접 소통, 퍼스널 브랜드 구축

## 추천 부캐
유튜버, 인스타그램 인플루언서, 틱톡 크리에이터, 팟캐스트 호스트""",
                "min_score": 24,
                "max_score": 27,
            },
            {
                "result_type": "소셜 임팩터",
                "result_title": "창의적 방식으로 사회 변화 만들기",
                "result_content": """## 퇴사 후 당신의 모습
당신은 소셜 벤처를 창업했습니다. 친환경 제품 판매, 취약계층 일자리 창출, 교육 격차 해소... 수익도 중요하지만 "우리가 세상에 어떤 변화를 만들고 있는가?"가 더 중요합니다.

## 성향 분석
- **사회성**: 사람들과 협력해 더 큰 변화
- **창의성**: 새로운 방식으로 사회 문제 해결
- **의미 지향**: 돈은 미션을 실행하기 위한 수단

## 강점
일의 의미와 보람 극대화, 사회적 지지와 응원

## 추천 부캐
소셜 벤처 창업, 비영리 단체 운영, 공정무역 사업, 친환경 브랜드""",
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
        print("✅ 퇴사 후 나에게 맞는 부캐 시드 데이터 생성 완료!")
        print(f"   - 테스트 ID: {test_id}")
        print(f"   - 문항 수: 10개")
        print(f"   - 결과 유형: 8개")

    except Exception as e:
        db.rollback()
        print(f"❌ 부캐 테스트 시드 실패: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    # 테이블 생성 확인
    Base.metadata.create_all(bind=engine)
    seed_side_hustle_test()

"""
무인도 생존 유형 시드 스크립트

10문항, 8개 결과 유형
실행: python -m scripts.seed_island_survival_test
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


def seed_island_survival_test():
    """무인도 생존 유형 시드 데이터 생성"""
    db = SessionLocal()

    try:
        # 기존 테스트 확인
        existing = db.query(Test).filter(Test.title.contains("무인도")).first()
        if existing:
            print("⚠️  무인도 생존 유형 테스트가 이미 존재합니다. 시드 스킵.")
            return

        # 테스트 ID 생성
        test_id = uuid.uuid4()

        # 테스트 생성
        test = Test(
            id=test_id,
            title="무인도 생존 유형 🏝️",
            description="무인도에 표류하면 당신의 역할은? 10개 질문으로 알아보는 나의 생존 유형",
            category="fun",
            thumbnail_url="/images/tests/island-survival.png",
            play_count=22340,
            like_count=1870,
        )
        db.add(test)

        # 문항 데이터 (A=0, B=3)
        questions_data = [
            {
                "content": "무인도에 표류했다! 가장 먼저 하는 행동은?",
                "order_num": 1,
                "choices": [
                    {"content": "일단 주변을 둘러보며 상황을 파악한다", "score": 0, "order_num": 1},
                    {"content": "바로 은신처를 만들기 시작한다", "score": 3, "order_num": 2},
                ],
            },
            {
                "content": "해변에서 다른 표류자들을 발견! 어떻게 하겠어?",
                "order_num": 2,
                "choices": [
                    {"content": "일단 멀리서 지켜보며 상황을 살핀다", "score": 0, "order_num": 1},
                    {"content": "바로 다가가서 인사하고 팀을 만든다", "score": 3, "order_num": 2},
                ],
            },
            {
                "content": "밤이 됐는데 이상한 소리가 들린다! 당신의 반응은?",
                "order_num": 3,
                "choices": [
                    {"content": "소리의 방향과 패턴을 분석해서 원인을 추론한다", "score": 0, "order_num": 1},
                    {"content": "직감을 믿고 일단 안전해 보이는 방향으로 이동한다", "score": 3, "order_num": 2},
                ],
            },
            {
                "content": "식량이 떨어졌다! 어떻게 구할래?",
                "order_num": 4,
                "choices": [
                    {"content": "먹을 수 있는 식물 도감을 떠올리며 안전한 것만 채집한다", "score": 0, "order_num": 1},
                    {"content": "직접 바다에 뛰어들어 물고기를 잡는다", "score": 3, "order_num": 2},
                ],
            },
            {
                "content": "표류자 그룹에서 의견 충돌이 생겼다! 당신은?",
                "order_num": 5,
                "choices": [
                    {"content": "내 할 일에 집중한다, 알아서 해결되겠지", "score": 0, "order_num": 1},
                    {"content": "중간에 나서서 서로 이야기를 들어보자고 한다", "score": 3, "order_num": 2},
                ],
            },
            {
                "content": "갑자기 폭풍이 몰려온다! 어떻게 대처할래?",
                "order_num": 6,
                "choices": [
                    {"content": "바람 방향, 구름 형태를 분석해서 최적의 대피 장소를 계산한다", "score": 0, "order_num": 1},
                    {"content": "느낌적으로 안전해 보이는 동굴 쪽으로 바로 뛴다", "score": 3, "order_num": 2},
                ],
            },
            {
                "content": "뗏목을 만들어 탈출할 기회! 당신의 역할은?",
                "order_num": 7,
                "choices": [
                    {"content": "설계도를 그리고 구조적으로 튼튼한 뗏목을 계획한다", "score": 0, "order_num": 1},
                    {"content": "나무를 베고 밧줄을 엮으며 바로 제작에 돌입한다", "score": 3, "order_num": 2},
                ],
            },
            {
                "content": "무인도에서 가장 하고 싶은 일은?",
                "order_num": 8,
                "choices": [
                    {"content": "혼자 섬을 탐험하며 비밀 장소를 찾는 것", "score": 0, "order_num": 1},
                    {"content": "모닥불 앞에 다 같이 모여 이야기하는 것", "score": 3, "order_num": 2},
                ],
            },
            {
                "content": "정체불명의 열매를 발견했다! 먹을까 말까?",
                "order_num": 9,
                "choices": [
                    {"content": "색깔, 냄새, 벌레의 흔적 등을 꼼꼼히 확인한 뒤 판단한다", "score": 0, "order_num": 1},
                    {"content": "직감적으로 괜찮아 보이면 조금만 맛본다", "score": 3, "order_num": 2},
                ],
            },
            {
                "content": "구조 헬기가 보인다! 그런데 신호를 보낼 도구가 없다면?",
                "order_num": 10,
                "choices": [
                    {"content": "혼자서라도 어떻게든 연기를 피워 신호를 만든다", "score": 0, "order_num": 1},
                    {"content": "모두를 불러 모아 함께 소리치고 옷을 흔들며 신호를 보낸다", "score": 3, "order_num": 2},
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

        # 8개 ResultType
        result_types = [
            {
                "result_type": "섬의 전략가",
                "result_title": "생존 확률? 이미 엑셀로 계산 끝났는데요",
                "result_content": """무인도에 도착하자마자 지형을 분석하고, 자원을 파악하고, 생존 계획표를 머릿속에 짜는 타입이에요. 혼자서도 차분하게 상황을 정리하고 최적의 생존 루트를 설계합니다. 다른 사람들이 멘붕에 빠져 있을 때 당신은 이미 3일치 계획을 세워놨죠. "걱정 마, 다 계산했어"가 당신의 생존 모토! 냉철한 분석력으로 무인도에서도 체계적인 생활을 만들어가는 당신, 혼자서도 오래 살아남을 수 있는 진정한 서바이벌 전략가입니다.

**생존 스타일:**
- 도착하자마자 섬 전체 지도를 머릿속에 그림
- 식량, 물, 은신처 우선순위를 논리적으로 정함
- 체크리스트 만들어서 하나씩 실행하는 계획형""",
                "min_score": 0,
                "max_score": 3,
            },
            {
                "result_type": "표류한 맥가이버",
                "result_title": "코코넛 하나로 정수기를 만들어버리는 천재",
                "result_content": """당신은 무인도의 발명왕입니다. 남들이 "이걸 어떻게 해?"라고 할 때, 당신은 이미 나뭇가지와 야자수 잎으로 뭔가를 만들고 있어요. 신중하게 관찰하다가 번뜩이는 영감이 떠오르면 바로 뚝딱뚝딱 제작에 돌입합니다. 혼자만의 시간에 아이디어가 더 잘 나오는 타입이라, 한쪽 구석에서 조용히 작업하다 보면 어느새 물 정화 장치가 완성돼 있죠. 무인도 특허왕은 바로 당신! 주변 사람들이 "이걸 어떻게 만들었어?!"라며 놀라는 그 순간이 당신의 하이라이트입니다.

**생존 스타일:**
- 떠내려온 잔해물을 모아 DIY 도구 제작
- "이거랑 이거 합치면..." 창의적 조합의 달인
- 조용히 혼자 작업하다 대작을 완성하는 타입""",
                "min_score": 4,
                "max_score": 7,
            },
            {
                "result_type": "섬의 대통령",
                "result_title": "표류 3일 만에 자치정부 세운 사람",
                "result_content": """카리스마와 논리로 무장한 당신은 무인도의 타고난 리더입니다. 표류한 사람들 사이에서 자연스럽게 중심에 서게 되고, 역할 분배부터 규칙 제정까지 착착 진행합니다. "자, 다들 모여봐. 일단 역할을 나누자"가 당신의 첫마디. 감정보다 이성적 판단을 우선시하면서도 모든 사람의 의견을 경청하는 리더십이 있어요. 무인도에서 문명을 재건할 사람이 있다면, 그건 바로 당신입니다. 대통령 선거가 열린다면 압도적 1위 당선 확실!

**생존 스타일:**
- 가장 먼저 사람들을 모아 회의를 시작함
- 효율적인 역할 분배와 규칙 시스템 구축
- 매일 아침 조회(?)를 열어 현황을 공유하는 스타일""",
                "min_score": 8,
                "max_score": 11,
            },
            {
                "result_type": "난파선의 힐러",
                "result_title": "몸도 마음도 치료해주는 섬의 백의천사",
                "result_content": """무인도에서 가장 필요한 사람이 바로 당신입니다. 다친 사람을 돌보고, 약초를 찾아 민간요법을 시도하고, 지친 사람들의 멘탈까지 케어하는 만능 힐러예요. "괜찮아, 다 잘 될 거야"라는 당신의 한마디가 무인도에서 가장 큰 위로가 됩니다. 직감적으로 누가 아픈지, 누가 힘든지를 감지하고 먼저 다가가는 따뜻한 마음의 소유자. 당신이 없으면 무인도 생존 멤버들의 사기가 바닥을 칠 거예요. 진짜 생존은 체력보다 멘탈이니까요!

**생존 스타일:**
- 섬에서 약초와 치료용 식물을 본능적으로 찾아냄
- 다친 동료를 세심하게 돌보는 간호 담당
- 밤에 모닥불 앞에서 모두의 고민을 들어주는 상담사""",
                "min_score": 12,
                "max_score": 15,
            },
            {
                "result_type": "고독한 사냥꾼",
                "result_title": "말보다 행동, 혼자서 식량 문제 해결 완료",
                "result_content": """무인도에 도착하자마자 회의? 토론? 그런 거 없습니다. 당신은 이미 창을 만들어 사냥에 나섰어요. 혼자서 움직이는 게 가장 효율적이라는 걸 아는 실전형 생존자입니다. 물고기를 잡고, 함정을 설치하고, 먹을 수 있는 열매와 못 먹는 열매를 냉철하게 구분합니다. 과묵하지만 행동으로 모든 걸 증명하는 타입이라, 다른 사람들은 당신이 가져온 식량을 보며 존경의 눈빛을 보냅니다. 무인도의 실질적 식량 공급원은 바로 당신!

**생존 스타일:**
- 동이 트자마자 사냥 & 채집 출발
- 효율적인 함정과 낚시 도구를 직접 제작
- 불필요한 대화 없이 묵묵히 결과로 보여주는 타입""",
                "min_score": 16,
                "max_score": 19,
            },
            {
                "result_type": "야생의 탐험가",
                "result_title": "무인도가 놀이터, 탐험이 곧 생존인 모험가",
                "result_content": """무인도에 표류했는데... 오히려 좋아? 당신에게 무인도는 거대한 모험의 무대입니다. 호기심이 폭발해서 섬 구석구석을 탐험하고, 동굴을 발견하고, 숨겨진 수원지를 찾아냅니다. 다른 사람들이 해변에서 구조 신호를 보낼 때, 당신은 이미 섬 반대편 정글을 탐사하고 있죠. 직감과 행동력이 만나면 어떤 미지의 환경도 정복할 수 있습니다. 무인도 전체 지리를 꿰뚫는 사람은 당신뿐이에요!

**생존 스타일:**
- 도착 첫날부터 섬 탐험을 시작하는 모험가
- 직감으로 안전한 장소와 위험한 장소를 감별
- 남들이 모르는 비밀 루트와 자원 포인트를 발견""",
                "min_score": 20,
                "max_score": 23,
            },
            {
                "result_type": "해변의 외교관",
                "result_title": "표류자들 사이 갈등? 내가 다 해결해줄게",
                "result_content": """무인도 생존에서 가장 어려운 건 뭐다? 바로 사람 관계입니다. 극한 상황에서 사람들 사이에 갈등이 터지면 당신이 나설 차례! 적극적으로 사람들 사이를 오가며 중재하고, 논리적인 설득으로 합의점을 찾아냅니다. "자, 자, 일단 서로 이야기를 들어보자"가 당신의 시그니처 멘트. 행동력과 사교성, 이성적 판단력이 조합된 당신은 무인도 커뮤니티의 윤활유 같은 존재예요. 당신 덕분에 팀이 분열되지 않고 함께 생존할 수 있습니다!

**생존 스타일:**
- 갈등이 생기면 즉시 중재에 나서는 액션형
- 양쪽 의견을 논리적으로 정리해 합의점 도출
- 모두가 만족하는 win-win 솔루션을 찾아내는 협상가""",
                "min_score": 24,
                "max_score": 27,
            },
            {
                "result_type": "낙원의 요리사",
                "result_title": "무인도에서도 맛있는 건 포기 못 해, 오늘 메뉴는 코코넛 스프",
                "result_content": """생존도 중요하지만, 잘 먹는 게 진짜 생존 아닌가요? 당신은 무인도에서도 요리 본능이 깨어나는 타입입니다. 직감적으로 먹을 수 있는 재료를 찾아내고, 행동력으로 즉시 조리에 돌입하며, 팀원들과 함께 나눠 먹는 것에 행복을 느낍니다. 모닥불에 구운 생선을 야자수 잎 접시에 담아내면 무인도가 갑자기 레스토랑으로 변신! 당신의 요리를 먹는 순간, 모두가 "여기가 무인도 맞아?"라고 물을 거예요. 맛있는 음식은 최고의 생존 동력입니다!

**생존 스타일:**
- 식재료를 직감적으로 찾아내는 미식 본능
- 한정된 재료로 최고의 맛을 끌어내는 서바이벌 쿡
- 함께 먹는 시간을 통해 팀워크를 강화하는 파티 플래너""",
                "min_score": 28,
                "max_score": 30,
            },
        ]

        # 결과 유형 추가
        for rt_data in result_types:
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
        print("✅ 무인도 생존 유형 테스트 시드 데이터 생성 완료!")
        print(f"   - 테스트 ID: {test_id}")
        print(f"   - 문항 수: 10개")
        print(f"   - 결과 유형: 8개")

    except Exception as e:
        db.rollback()
        print(f"❌ 무인도 생존 유형 테스트 시드 실패: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    # 테이블 생성 확인
    Base.metadata.create_all(bind=engine)
    seed_island_survival_test()

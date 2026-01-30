"""
이별 후 나의 회복 유형은? 시드 스크립트
10문항, 8개 결과 유형
실행: python -m scripts.seed_breakup_recovery_test
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


def seed_breakup_recovery_test():
    """이별 후 나의 회복 유형은? 시드 데이터 생성"""
    db = SessionLocal()

    try:
        # 기존 테스트 확인
        existing = db.query(Test).filter(Test.title.contains("이별")).first()
        if existing:
            print("⚠️  이별 회복 테스트가 이미 존재합니다. 시드 스킵.")
            return

        # 테스트 ID 생성
        test_id = uuid.uuid4()

        # 테스트 생성
        test = Test(
            id=test_id,
            title="이별 후 나의 회복 유형은? 💔",
            description="이별의 아픔을 어떻게 극복하나요? 감정처리, 사회적지지, 자기돌봄 3가지 차원으로 당신만의 회복 방식을 찾아보세요. 공감과 위로가 가득한 결과가 기다려요!",
            category="love",
            thumbnail_url="/images/tests/breakup-recovery.png",
            play_count=29450,
            like_count=2360,
        )
        db.add(test)

        # 10개 문항 (A=0점, B=3점)
        questions_data = [
            {
                "order_num": 1,
                "content": "이별 직후, 가장 먼저 하고 싶은 건?",
                "choices": [
                    {"order_num": 1, "content": "혼자만의 시간이 필요해. 일단 방문 닫고 혼자 있고 싶어.", "score": 0},
                    {"order_num": 2, "content": "친구들한테 연락해야겠어. 혼자 있으면 미칠 것 같아.", "score": 3},
                ],
            },
            {
                "order_num": 2,
                "content": "이별 후 밤에 잠이 안 올 때 나는?",
                "choices": [
                    {"order_num": 1, "content": "조용히 눈물 흘리며 그 사람 생각에 잠겨.", "score": 0},
                    {"order_num": 2, "content": "일기에 감정을 쏟아내거나, 슬픈 노래 크게 틀어놓고 울어.", "score": 3},
                ],
            },
            {
                "order_num": 3,
                "content": "친구들이 \"괜찮아?\"라고 물어보면?",
                "choices": [
                    {"order_num": 1, "content": "\"응, 괜찮아\" 하고 넘어가. 내 감정은 나만 알면 돼.", "score": 0},
                    {"order_num": 2, "content": "\"사실 너무 힘들어...\" 하며 솔직하게 털어놓아.", "score": 3},
                ],
            },
            {
                "order_num": 4,
                "content": "이별 후 주말, 나의 모습은?",
                "choices": [
                    {"order_num": 1, "content": "집에서 쉬면서 감정을 느끼고 받아들이는 시간.", "score": 0},
                    {"order_num": 2, "content": "운동하러 가거나 새로운 활동을 시작해. 가만히 있을 수 없어!", "score": 3},
                ],
            },
            {
                "order_num": 5,
                "content": "SNS에서 그 사람 사진을 보게 됐을 때?",
                "choices": [
                    {"order_num": 1, "content": "조용히 마음 아파하고, 혼자 슬퍼해.", "score": 0},
                    {"order_num": 2, "content": "친구들한테 톡 보내. \"SNS에서 봤는데 너무 화나...\"", "score": 3},
                ],
            },
            {
                "order_num": 6,
                "content": "이별 후 가장 위로가 되는 건?",
                "choices": [
                    {"order_num": 1, "content": "혼자만의 공간에서 조용히 생각 정리하는 시간.", "score": 0},
                    {"order_num": 2, "content": "친구들, 가족들과 함께 있어주는 시간.", "score": 3},
                ],
            },
            {
                "order_num": 7,
                "content": "이별의 슬픔을 극복하기 위해 나는?",
                "choices": [
                    {"order_num": 1, "content": "감정을 충분히 느끼고, 시간이 해결해주길 기다려.", "score": 0},
                    {"order_num": 2, "content": "운동, 공부, 새로운 취미 등 뭔가를 시작해서 딴 생각을 해.", "score": 3},
                ],
            },
            {
                "order_num": 8,
                "content": "친구가 \"우리 만나자\"라고 하면?",
                "choices": [
                    {"order_num": 1, "content": "\"미안, 나 혼자 있고 싶어\" 하고 정중히 거절.", "score": 0},
                    {"order_num": 2, "content": "\"그래, 나가자!\" 혼자 있는 것보다 누군가와 함께 있는 게 좋아.", "score": 3},
                ],
            },
            {
                "order_num": 9,
                "content": "이별 후 감정 기복이 심할 때 나는?",
                "choices": [
                    {"order_num": 1, "content": "혼자 조용히 감정을 삭이며 시간을 보내.", "score": 0},
                    {"order_num": 2, "content": "일기 쓰기, 운동, 친구에게 전화 등으로 감정을 표출해.", "score": 3},
                ],
            },
            {
                "order_num": 10,
                "content": "이별 후 1주일, 나의 목표는?",
                "choices": [
                    {"order_num": 1, "content": "일단 감정을 있는 그대로 받아들이고, 천천히 회복하기.", "score": 0},
                    {"order_num": 2, "content": "새로운 루틴 만들기, 운동 시작하기 등 변화 만들기.", "score": 3},
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
                "result_type": "혼자만의 치유 시간",
                "result_title": "나만의 템포로, 조용히 아물어가는 중",
                "result_content": """이별 후 당신은 일단 사람들로부터 한 발짝 물러나요. SNS도 잠시 멀리하고, 친구들 만남도 정중히 거절하며 나만의 공간에 머물러요. 혼자 산책하거나, 좋아하는 음악을 들으며, 책을 읽으며 시간을 보냅니다.

당신은 감정을 내면에서 천천히 소화하는 타입이에요. 급하게 잊으려 하지 않고, 슬픔과 상실감을 있는 그대로 느끼면서 자연스럽게 회복해요.

**강점**: 깊이 있는 자기 성찰, 진정한 치유, 내적 강인함
**약점**: 고립의 위험, 회복 속도, 반추 경향

💙 혼자서 조용히 회복하는 당신의 모습, 정말 용감해요. 지금 느끼는 모든 감정은 당신을 더 단단하게 만들어줄 거예요.""",
                "min_score": 0,
                "max_score": 3,
            },
            {
                "result_type": "천천히 나를 찾아가는 중",
                "result_title": "혼자서도 잘해, 조금씩 새로운 나로 성장 중",
                "result_content": """이별 후 당신은 잠시 멈칫하지만, 곧 "이제 뭐 할까?" 하며 새로운 계획을 세워요. 혼자 할 수 있는 취미를 찾아보거나, 미뤄왔던 자기계발을 시작하죠. 헬스장 등록하기, 온라인 강의 듣기, 새로운 언어 배우기...

당신은 감정을 내면에서 소화하면서도, 동시에 적극적으로 자신을 개선하려는 타입이에요. "슬프긴 한데... 그래도 나는 계속 성장해야지"라는 마인드로 이별을 업그레이드 기회로 삼아요.

**강점**: 생산적인 회복, 자립심, 목표 지향적
**약점**: 감정 회피, 완벽주의, 소진 위험

🌟 이별 후에도 멈추지 않고 계속 앞으로 나아가는 당신, 정말 멋져요!""",
                "min_score": 4,
                "max_score": 7,
            },
            {
                "result_type": "함께하며 마음 돌보기",
                "result_title": "사람들 곁에서 조용히 위로받는 중",
                "result_content": """이별 후 당신은 혼자 있고 싶지 않지만, 그렇다고 이별 얘기를 꺼내고 싶지도 않아요. 친구들과 만나 아무 말 없이 영화를 보거나, 카페에 앉아 있기만 해도 위로가 돼요.

당신은 감정을 혼자 곱씹으면서도, 동시에 사람들의 온기가 필요한 타입이에요. 깊은 대화보다는 함께 있는 것 자체로 위로받고, 일상적인 상호작용 속에서 서서히 회복해요.

**강점**: 균형 잡힌 회복, 깊은 유대감, 건강한 의존
**약점**: 소통 부족, 수동적 회복, 감정 억제

💚 당신은 혼자가 아니에요. 지금 당신 곁에 있는 사람들이 당신의 가장 큰 힘이에요.""",
                "min_score": 8,
                "max_score": 11,
            },
            {
                "result_type": "친구들과 새로운 시작",
                "result_title": "함께 움직이며 조용히 털어내는 중",
                "result_content": """이별 후 당신은 친구들에게 먼저 연락해요. "우리 뭐 할까?"라며 새로운 계획을 제안하고, 함께 운동하거나 여행을 가죠. 이별 얘기를 길게 늘어놓진 않지만, "헤어졌어. 근데 우리 이거 해보자!"라며 자연스럽게 새로운 활동을 시작해요.

당신은 감정을 혼자 소화하면서도, 친구들과 함께 움직이며 회복하는 타입이에요. 슬픔을 말로 풀기보단 활동으로 풀고, 친구들과 새로운 경험을 쌓으며 이별의 공백을 채워가죠.

**강점**: 활기찬 회복, 새로운 추억, 사회적 자본
**약점**: 감정 지연, 피로 누적, 의존성

🌈 친구들과 함께 새로운 시작을 만들어가는 당신, 정말 밝은 에너지를 갖고 있어요!""",
                "min_score": 12,
                "max_score": 15,
            },
            {
                "result_type": "감정 표출형 회복",
                "result_title": "울 땐 실컷 울고, 혼자서 털어내는 중",
                "result_content": """이별 후 당신은 일단 방문을 닫고 실컷 울어요. 슬픈 노래를 크게 틀어놓고 눈물을 쏟아내거나, 베개에 소리를 지르기도 하죠. 감정을 억누르지 않고 있는 그대로 표출하는 게 당신의 방식이에요.

당신은 감정을 밖으로 꺼내놓아야 직성이 풀리는 타입이에요. 혼자 있지만 조용하지 않죠. 울고, 화내고, 슬퍼하고... 감정의 롤러코스터를 충분히 타고 나면 자연스럽게 회복돼요.

**강점**: 빠른 정화, 솔직함, 감정 인식
**약점**: 감정 과다, 충동성, 고립

💜 울고 싶을 땐 마음껏 우는 당신, 정말 용감해요. 감정을 억누르지 않고 있는 그대로 느끼는 건 정말 중요한 거예요.""",
                "min_score": 16,
                "max_score": 19,
            },
            {
                "result_type": "일기와 운동의 힘",
                "result_title": "감정은 쏟아내고, 몸은 움직이며 극복 중",
                "result_content": """이별 후 당신은 밤에는 일기를 쓰고, 낮에는 운동을 해요. 감정을 글로 쏟아내고, 몸을 움직이며 스트레스를 날려버리죠. 헬스장에서 땀을 흘리거나, 한강을 뛰며 "나 이제 괜찮아!"라고 외치기도 해요.

당신은 감정을 밖으로 꺼내놓으면서도, 동시에 적극적으로 움직이는 타입이에요. "슬프긴 한데, 가만히 있을 순 없어!"라는 마인드로 감정 표출과 자기 개선을 동시에 해나가죠.

**강점**: 이중 발산, 빠른 회복, 자기 효능감
**약점**: 과도한 몰입, 감정 회피, 고립

💪 감정도 쏟아내고, 몸도 움직이는 당신, 정말 에너지가 넘쳐요!""",
                "min_score": 20,
                "max_score": 23,
            },
            {
                "result_type": "친구들에게 털어놓기",
                "result_title": "친구들과 실컷 떠들고 울며 회복 중",
                "result_content": """이별 후 당신은 바로 친구들에게 전화해요. "나 이별했어, 만나자"라며 친구들을 소집하고, 치맥 먹으며 밤새 이별 얘기를 쏟아내죠. 울기도 하고, 웃기도 하고, 화내기도 하면서 친구들과 감정을 나눠요.

당신은 감정을 혼자 삭이지 못하고, 반드시 누군가와 나눠야 하는 타입이에요. 친구들에게 이별 스토리를 A부터 Z까지 다 털어놓고, 공감받으며 회복해요.

**강점**: 빠른 위로, 감정 정리, 깊은 우정
**약점**: 과도한 공유, 타인 의존, 감정 소비

💛 친구들에게 마음을 활짝 열고 도움을 받는 당신, 정말 용감해요!""",
                "min_score": 24,
                "max_score": 27,
            },
            {
                "result_type": "적극적 재기 모드",
                "result_title": "세상 밖으로 나가서 새롭게 시작!",
                "result_content": """이별 후 당신은 "이제 내 인생 살아야지!"라며 적극적으로 움직여요. 친구들에게 이별 소식을 알리고, "우리 뭔가 새로운 거 해보자!"라며 계획을 세워요. 함께 여행을 가거나, 새로운 취미를 시작하거나, SNS에 활기찬 모습을 올리죠.

당신은 이별을 새로운 시작의 신호탄으로 여기는 타입이에요. 슬퍼하긴 하지만, 그 감정을 친구들과 나누며 빠르게 털어내고, 곧바로 새로운 활동에 뛰어들어요.

**강점**: 빠른 전환, 네트워크 확장, 긍정적 에너지
**약점**: 감정 회피, 충동적 결정, 번아웃

🌟 이별 후에도 멈추지 않고 세상 밖으로 나가는 당신, 정말 대단해요!""",
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
        print("✅ 이별 후 나의 회복 유형 시드 데이터 생성 완료!")
        print(f"   - 테스트 ID: {test_id}")
        print(f"   - 문항 수: 10개")
        print(f"   - 결과 유형: 8개")

    except Exception as e:
        db.rollback()
        print(f"❌ 이별 회복 테스트 시드 실패: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    # 테이블 생성 확인
    Base.metadata.create_all(bind=engine)
    seed_breakup_recovery_test()

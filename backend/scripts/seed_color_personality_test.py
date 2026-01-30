"""
나를 색깔로 표현하면? 시드 스크립트

10문항, 10개 결과 유형
실행: python -m scripts.seed_color_personality_test
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


def seed_color_personality_test():
    """나를 색깔로 표현하면? 시드 데이터 생성"""
    db = SessionLocal()

    try:
        # 기존 테스트 확인
        existing = db.query(Test).filter(Test.title.contains("색깔로 표현")).first()
        if existing:
            print("⚠️  색깔 성격 테스트가 이미 존재합니다. 시드 스킵.")
            return

        # 테스트 ID 생성
        test_id = uuid.uuid4()

        # 테스트 생성
        test = Test(
            id=test_id,
            title="나를 색깔로 표현하면? 🎨",
            description="10개 질문으로 찾는 나만의 색깔. 당신의 컬러를 찾아보세요!",
            category="personality",
            thumbnail_url="/images/tests/color-personality.png",
            play_count=41230,
            like_count=3340,
        )
        db.add(test)

        # 문항 데이터
        questions_data = [
            {
                "content": "주말 아침, 눈을 떴을 때 가장 먼저 하고 싶은 건?",
                "order_num": 1,
                "choices": [
                    {"content": "친구들한테 연락해서 오늘 뭐 할지 계획 세우기", "score": 0, "order_num": 1},
                    {"content": "이불 속에서 음악 틀어놓고 느긋하게 나만의 시간 보내기", "score": 3, "order_num": 2},
                ],
            },
            {
                "content": "친구가 갑자기 울기 시작했을 때 나는?",
                "order_num": 2,
                "choices": [
                    {"content": "같이 울거나 꼭 안아주면서 감정을 함께 나눈다", "score": 0, "order_num": 1},
                    {"content": "일단 진정시키고 무슨 일인지 차분하게 물어본다", "score": 3, "order_num": 2},
                ],
            },
            {
                "content": "새로운 모임에 갔을 때 나의 모습은?",
                "order_num": 3,
                "choices": [
                    {"content": "먼저 말 걸면서 자연스럽게 분위기에 섞인다", "score": 0, "order_num": 1},
                    {"content": "조용히 관찰하다가 맞는 사람이 있으면 천천히 다가간다", "score": 3, "order_num": 2},
                ],
            },
            {
                "content": "여행 계획을 세울 때 나의 스타일은?",
                "order_num": 4,
                "choices": [
                    {"content": "그때그때 끌리는 대로, 감성 따라 자유롭게", "score": 0, "order_num": 1},
                    {"content": "동선, 맛집, 시간표까지 꼼꼼하게 계획", "score": 3, "order_num": 2},
                ],
            },
            {
                "content": "스트레스를 받았을 때 푸는 방법은?",
                "order_num": 5,
                "choices": [
                    {"content": "신나는 음악 틀고 밖에 나가서 움직이기", "score": 0, "order_num": 1},
                    {"content": "조용한 카페에서 혼자 생각 정리하기", "score": 3, "order_num": 2},
                ],
            },
            {
                "content": "내가 더 끌리는 칭찬은?",
                "order_num": 6,
                "choices": [
                    {"content": "너 진짜 분위기 좋다, 같이 있으면 재밌어", "score": 0, "order_num": 1},
                    {"content": "너 진짜 깊이 있다, 생각이 남다르네", "score": 3, "order_num": 2},
                ],
            },
            {
                "content": "영화를 고를 때 더 끌리는 장르는?",
                "order_num": 7,
                "choices": [
                    {"content": "눈물 펑펑 감동 로맨스, 감성 다큐", "score": 0, "order_num": 1},
                    {"content": "반전 스릴러, 논리적인 추리물", "score": 3, "order_num": 2},
                ],
            },
            {
                "content": "중요한 결정을 내릴 때 나는?",
                "order_num": 8,
                "choices": [
                    {"content": "직감을 믿고 빠르게 결정! 일단 해보자", "score": 0, "order_num": 1},
                    {"content": "충분히 고민하고 여러 가능성을 따져본 후 결정", "score": 3, "order_num": 2},
                ],
            },
            {
                "content": "나를 더 설레게 하는 데이트는?",
                "order_num": 9,
                "choices": [
                    {"content": "핫플 탐방, 사람 많은 축제나 야시장", "score": 0, "order_num": 1},
                    {"content": "한적한 산책길, 조용한 전시회", "score": 3, "order_num": 2},
                ],
            },
            {
                "content": "인스타 피드를 꾸밀 때 나의 스타일은?",
                "order_num": 10,
                "choices": [
                    {"content": "느낌 있는 감성 사진, 분위기 중시", "score": 0, "order_num": 1},
                    {"content": "깔끔한 구도와 통일감 있는 톤 정리", "score": 3, "order_num": 2},
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

        # 10개 ResultType (점수 범위별 색깔 유형)
        result_types = [
            {
                "result_type": "빨강",
                "result_title": "열정 스파크",
                "result_content": "당신은 어디에 있든 가장 뜨거운 에너지를 내뿜는 사람이에요. 하고 싶은 일이 생기면 망설이지 않고 바로 행동에 옮기는 추진력이 있죠. 사람들 사이에서 자연스럽게 중심이 되고, 당신의 열정은 주변 사람들에게도 불꽃처럼 번져요. 때로는 너무 뜨겁게 달려서 지칠 수 있지만, 그 불타는 에너지가 바로 당신만의 매력이에요.",
                "min_score": 0,
                "max_score": 3,
            },
            {
                "result_type": "주황",
                "result_title": "무드 메이커",
                "result_content": "당신은 따뜻한 햇살 같은 존재예요. 어떤 자리에서든 분위기를 밝게 만드는 특별한 능력이 있죠. 유쾌한 에너지와 넉넉한 마음으로 사람들을 편안하게 해주고, 당신 옆에 있으면 누구나 자연스럽게 미소를 짓게 돼요. 낙천적인 성격으로 힘든 상황에서도 긍정의 기운을 잃지 않는 당신은, 모두에게 사랑받는 에너지 비타민이에요.",
                "min_score": 4,
                "max_score": 7,
            },
            {
                "result_type": "노랑",
                "result_title": "아이디어 스파클러",
                "result_content": "당신의 머릿속은 늘 반짝이는 아이디어로 가득 차 있어요. 호기심이 끝없고, 새로운 것에 대한 탐구 욕구가 누구보다 강하죠. 톡톡 튀는 발상으로 주변 사람들을 놀라게 하고, 밝고 경쾌한 에너지로 분위기를 환하게 만들어요. 한 가지에 오래 집중하는 건 조금 어렵지만, 그 자유로운 사고방식이야말로 당신을 특별하게 만드는 빛이에요.",
                "min_score": 8,
                "max_score": 11,
            },
            {
                "result_type": "초록",
                "result_title": "힐링 가디언",
                "result_content": "당신은 숲속의 나무처럼 조용하지만 든든한 존재예요. 주변 사람들의 이야기를 진심으로 들어주고, 조용히 곁을 지켜주는 따뜻한 마음의 소유자죠. 갈등 상황에서도 차분하게 균형을 잡아주고, 누구와든 편안한 관계를 만들어가요. 화려하진 않지만, 당신 곁에 있으면 어느새 마음이 치유되는 걸 느낄 수 있어요.",
                "min_score": 12,
                "max_score": 15,
            },
            {
                "result_type": "하늘",
                "result_title": "맑은 공기 같은 존재",
                "result_content": "당신은 맑은 하늘처럼 투명하고 순수한 매력을 가진 사람이에요. 거짓이나 꾸밈 없이 솔직한 모습이 오히려 사람들의 마음을 끌어당기죠. 복잡한 것보다 깔끔하고 단순한 것을 좋아하고, 자유로운 영혼으로 어디에도 얽매이지 않아요. 당신의 청량한 에너지는 만나는 사람마다 상쾌한 기분을 선물해요.",
                "min_score": 16,
                "max_score": 19,
            },
            {
                "result_type": "파랑",
                "result_title": "깊은 바다 사색가",
                "result_content": "당신은 깊은 바다처럼 넓고 풍부한 내면 세계를 품고 있는 사람이에요. 겉으로는 차분하고 조용하지만, 속에는 깊은 생각과 풍부한 감수성이 가득하죠. 혼자만의 시간에 에너지를 충전하고, 그 시간 속에서 남들이 보지 못하는 통찰을 얻어요. 진정한 깊이를 아는 당신은 알면 알수록 빠져드는 매력의 소유자예요.",
                "min_score": 20,
                "max_score": 23,
            },
            {
                "result_type": "보라",
                "result_title": "미스터리 드리머",
                "result_content": "당신은 보라색처럼 신비롭고 독특한 아우라를 가진 사람이에요. 남들과 다른 독창적인 시선으로 세상을 바라보고, 예술적 감수성이 깊어서 아름다운 것에 마음을 빼앗기죠. 때로는 현실과 꿈의 경계를 자유롭게 넘나들며, 그 몽환적인 분위기가 주변 사람들을 매료시켜요. 당신만의 세계관은 그 누구도 따라할 수 없는 유일무이한 매력이에요.",
                "min_score": 24,
                "max_score": 27,
            },
            {
                "result_type": "핑크",
                "result_title": "사랑의 아이콘",
                "result_content": "당신은 핑크색처럼 달콤하고 사랑스러운 감성의 소유자예요. 사람에 대한 애정이 깊고, 소중한 사람들을 세심하게 챙기는 마음이 있죠. 예쁜 것, 귀여운 것, 로맨틱한 것에 자연스럽게 끌리고, 당신의 따뜻한 관심은 주변을 핑크빛으로 물들여요. 감정에 솔직하고 공감 능력이 뛰어나서, 사람들은 당신 곁에서 사랑받는 느낌을 받아요.",
                "min_score": 28,
                "max_score": 29,
            },
            {
                "result_type": "하양",
                "result_title": "퓨어 소울",
                "result_content": "당신은 하얀색처럼 깨끗하고 순수한 에너지를 가진 사람이에요. 편견 없이 세상을 바라보고, 누구에게나 공정하고 진실한 태도를 유지하죠. 복잡한 것보다 깔끔하고 정돈된 환경을 좋아하고, 내면의 평화를 중요하게 여겨요. 당신의 담백하고 진솔한 매력은 오래 곁에 두고 싶은 편안함을 줘요. 화려하지 않아도 빛나는, 그게 바로 당신이에요.",
                "min_score": 30,
                "max_score": 30,
            },
            {
                "result_type": "검정",
                "result_title": "카리스마 오라",
                "result_content": "당신은 검정색처럼 강렬하고 묵직한 존재감을 가진 사람이에요. 말을 많이 하지 않아도 그 자리에 있는 것만으로 분위기가 달라지죠. 자신만의 확고한 기준과 철학이 있고, 쉽게 흔들리지 않는 단단한 내면의 소유자예요. 겉으로는 차가워 보일 수 있지만, 가까운 사람에게는 누구보다 깊은 신뢰를 주는 당신. 알면 알수록 빠져드는 반전 매력의 소유자예요.",
                "min_score": 31,
                "max_score": 999,
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
        print("✅ 색깔 성격 테스트 시드 데이터 생성 완료!")
        print(f"   - 테스트 ID: {test_id}")
        print(f"   - 문항 수: 10개")
        print(f"   - 결과 유형: 10개")

    except Exception as e:
        db.rollback()
        print(f"❌ 색깔 성격 테스트 시드 실패: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    # 테이블 생성 확인
    Base.metadata.create_all(bind=engine)
    seed_color_personality_test()

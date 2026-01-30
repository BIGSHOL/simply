"""
전생에 나의 러브스토리는? 시드 스크립트

10문항, 8개 결과 유형
실행: python -m scripts.seed_past_life_love_test
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


def seed_past_life_love_test():
    """전생에 나의 러브스토리는? 시드 데이터 생성"""
    db = SessionLocal()

    try:
        # 기존 테스트 확인
        existing = db.query(Test).filter(Test.title.contains("전생")).first()
        if existing:
            print("⚠️  전생 러브스토리 테스트가 이미 존재합니다. 시드 스킵.")
            return

        # 테스트 ID 생성
        test_id = uuid.uuid4()

        # 테스트 생성
        test = Test(
            id=test_id,
            title="전생에 나의 러브스토리는? 🏰",
            description="조선시대 세자빈? 로마 검투사의 연인? 전생 러브스토리를 찾아보세요",
            category="love",
            thumbnail_url="/images/tests/past-life-love.png",
            play_count=54320,
            like_count=4560,
        )
        db.add(test)

        # 문항 데이터 (A=0, B=3)
        questions_data = [
            {
                "content": "좋아하는 사람이 생겼을 때, 당신의 첫 반응은?",
                "order_num": 1,
                "choices": [
                    {"content": "티 안 내고 조용히 상대 주변을 맴돌면서 은근히 챙겨줌", "score": 0, "order_num": 1},
                    {"content": "좋아하는 마음을 어떻게든 전달하고 싶어서 표현 방법을 고민함", "score": 3, "order_num": 2},
                ],
            },
            {
                "content": "연인과 의견이 다를 때, 당신의 스타일은?",
                "order_num": 2,
                "choices": [
                    {"content": "상대의 의견을 먼저 듣고, 될 수 있으면 맞춰주려 함", "score": 0, "order_num": 1},
                    {"content": "내 생각을 확실히 말하고, 더 나은 방향을 제안함", "score": 3, "order_num": 2},
                ],
            },
            {
                "content": "전생에서 연인과 보낼 하룻밤, 어떤 장면이 더 끌려?",
                "order_num": 3,
                "choices": [
                    {"content": "벽난로 앞에서 조용히 손잡고 이야기하며 보내는 밤", "score": 0, "order_num": 1},
                    {"content": "폭풍우 치는 성 안에서 운명적 만남을 갖는 극적인 밤", "score": 3, "order_num": 2},
                ],
            },
            {
                "content": "기념일에 연인에게 마음을 전한다면?",
                "order_num": 4,
                "choices": [
                    {"content": "직접 요리를 해주거나, 상대가 갖고 싶어하던 걸 몰래 준비함", "score": 0, "order_num": 1},
                    {"content": "진심을 담은 편지를 쓰거나, 직접 고른 노래를 불러줌", "score": 3, "order_num": 2},
                ],
            },
            {
                "content": "데이트 계획은 누가 세우는 게 좋아?",
                "order_num": 5,
                "choices": [
                    {"content": "상대가 정해주면 나는 거기에 맞춰서 즐기는 편", "score": 0, "order_num": 1},
                    {"content": "내가 코스를 짜고 에스코트하는 게 더 설렘", "score": 3, "order_num": 2},
                ],
            },
            {
                "content": "전생 러브스토리에서 당신이 끌리는 전개는?",
                "order_num": 6,
                "choices": [
                    {"content": "오랜 시간 신뢰를 쌓아가며 자연스럽게 시작되는 사랑", "score": 0, "order_num": 1},
                    {"content": "모든 걸 걸고 장애물을 뚫고 이뤄내는 금지된 사랑", "score": 3, "order_num": 2},
                ],
            },
            {
                "content": "연인이 힘들어하고 있을 때, 당신의 반응은?",
                "order_num": 7,
                "choices": [
                    {"content": "말없이 따뜻한 음료를 건네고, 옆에 조용히 앉아줌", "score": 0, "order_num": 1},
                    {"content": "\"괜찮아? 나한테 다 말해도 돼\"라며 감정을 함께 나눔", "score": 3, "order_num": 2},
                ],
            },
            {
                "content": "연인과의 여행에서 당신의 역할은?",
                "order_num": 8,
                "choices": [
                    {"content": "상대가 가고 싶은 곳에 따라가며, 함께하는 것 자체가 좋음", "score": 0, "order_num": 1},
                    {"content": "숙소부터 일정까지 내가 주도해서 완벽한 여행을 만들고 싶음", "score": 3, "order_num": 2},
                ],
            },
            {
                "content": "사랑에 대한 당신의 가치관과 가까운 것은?",
                "order_num": 9,
                "choices": [
                    {"content": "사랑은 서로를 편안하게 만들어주는 따뜻한 안식처", "score": 0, "order_num": 1},
                    {"content": "사랑은 심장이 터질 것 같은, 온몸이 뜨거워지는 경험", "score": 3, "order_num": 2},
                ],
            },
            {
                "content": "전생에서 연인에게 남기는 마지막 한마디는?",
                "order_num": 10,
                "choices": [
                    {"content": "(아무 말 없이 손을 꼭 잡아준다)", "score": 0, "order_num": 1},
                    {"content": "\"다음 생에서도 꼭 다시 만나자, 사랑해\"", "score": 3, "order_num": 2},
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
                "result_type": "조선시대 내조의 여왕/왕",
                "result_title": "말 한마디 없어도 눈빛만으로 통하는, 묵직한 사랑의 주인공",
                "result_content": """전생의 당신은 조선시대 양반가의 현숙한 배우자였어요. 화려한 말이나 과한 스킨십보다, 상대의 뒤에서 묵묵히 지지해주는 사랑을 했죠. 시어른 눈치 보면서도 은밀히 도시락에 하트 모양 반찬을 넣어주는 센스! 말은 적지만 행동 하나하나에 깊은 사랑이 담겨 있어서, 함께하는 시간이 길어질수록 더 빛나는 타입이었어요.

**전생 연애 스타일:**
- 손편지 대신 정성스러운 행동으로 마음 전달
- 상대가 힘들 때 묵묵히 옆자리를 지키는 타입
- 은근한 눈빛 교환으로 모든 대화 완료

**강점:** 꾸준하고 변함없는 사랑으로 상대에게 절대 안정감을 줌

**성장 포인트:** 가끔은 마음을 말로 표현해보세요. 당신의 한마디가 상대에게는 천 마디 행동보다 큰 선물이 될 수 있어요""",
                "min_score": 0,
                "max_score": 3,
            },
            {
                "result_type": "로마의 검투사 연인",
                "result_title": "사랑을 위해서라면 콜로세움도 뛰어드는, 행동파 열정러버",
                "result_content": """전생의 당신은 로마 콜로세움의 검투사 또는 그 검투사를 사랑한 사람이었어요. 말보다 행동이 앞서고, 사랑하는 사람을 위해서라면 목숨까지 걸 수 있는 열정의 소유자! 직접적인 감정 표현은 서툴지만, 위험한 순간에 몸을 던져 상대를 지키는 극적인 사랑을 했죠.

**전생 연애 스타일:**
- 고백은 못 해도 위기 상황에서 먼저 뛰쳐나감
- 한번 사랑하면 끝까지, 뒤돌아보지 않는 일편단심
- 행동으로 증명하는 뜨거운 사랑

**강점:** 사랑하는 사람을 지키려는 강렬한 보호 본능

**성장 포인트:** 모든 걸 혼자 감당하려 하지 마세요. 사랑은 함께 싸우는 거예요""",
                "min_score": 4,
                "max_score": 7,
            },
            {
                "result_type": "빅토리아 시대 귀족",
                "result_title": "우아한 리드와 절제된 매너, 품격 있는 사랑의 대가",
                "result_content": """전생의 당신은 빅토리아 시대 영국 귀족이었어요. 무도회장에서 우아하게 손을 내밀며 \"이 춤 허락해 주시겠습니까?\"로 시작하는 품격 있는 로맨스의 주인공! 감정을 과하게 드러내지 않지만 절제된 매너 속에 깊은 배려가 숨어 있죠.

**전생 연애 스타일:**
- 데이트 코스는 내가 완벽하게 플래닝
- 절제된 표현 속에 계산된 디테일 배려
- 상대를 존중하는 세련된 매너

**강점:** 격식과 배려를 갖춘 리더십으로 상대를 편안하게 이끔

**성장 포인트:** 완벽한 매너 뒤에 날것의 감정을 숨기지 마세요""",
                "min_score": 8,
                "max_score": 11,
            },
            {
                "result_type": "해적선의 캡틴 러버",
                "result_title": "거친 바다 위에서도 사랑은 포기 못 해, 모험형 열정 러버",
                "result_content": """전생의 당신은 카리브해를 누비던 해적선의 캡틴이거나, 그 캡틴과 함께 모험을 떠난 사람이었어요. 자유롭고 대담하며, 사랑도 모험처럼 스릴 있게 즐기는 타입! \"지루한 사랑은 사랑이 아니다\"가 인생 모토이고, 상대를 위해 보물섬까지 찾아 나서는 행동력의 소유자.

**전생 연애 스타일:**
- \"따라와, 재밌는 데 데려다줄게\" 한마디로 시작되는 데이트
- 예측불가한 서프라이즈와 이벤트의 달인
- 거칠지만 한없이 따뜻한 보호 본능

**강점:** 함께하면 지루할 틈이 없는 압도적 에너지

**성장 포인트:** 가끔은 닻을 내리고 잔잔한 항구에서 쉬어가세요""",
                "min_score": 12,
                "max_score": 15,
            },
            {
                "result_type": "헤이안 시대 궁정 시인",
                "result_title": "달빛 아래 시 한 편으로 마음을 전하는, 감성 충만 로맨티스트",
                "result_content": """전생의 당신은 헤이안 시대 궁정에서 시를 짓던 감성파였어요. 벚꽃 흩날리는 정원에서 부채 뒤로 살짝 미소 짓고, 마음을 담은 와카(시) 한 수로 고백하는 스타일! 감정 표현이 풍부하지만 은은하고 섬세해서, 상대를 강하게 이끌기보다는 분위기와 감성으로 자연스럽게 마음을 사로잡죠.

**전생 연애 스타일:**
- 감성적인 메시지와 편지로 마음 표현
- 상대의 감정에 공감하고 위로하는 따뜻한 사람
- 무드 있는 데이트 분위기를 자연스럽게 연출

**강점:** 섬세한 감성으로 상대의 마음을 깊이 터치하는 능력

**성장 포인트:** 감성에만 머무르지 말고, 때로는 현실적인 행동으로도 마음을 보여주세요""",
                "min_score": 16,
                "max_score": 19,
            },
            {
                "result_type": "이집트 파라오의 연인",
                "result_title": "피라미드도 세울 만큼 뜨겁고 드라마틱한 사랑의 화신",
                "result_content": """전생의 당신은 고대 이집트에서 파라오의 사랑을 받던 존재, 혹은 사랑을 위해 피라미드를 세운 파라오 그 자체였어요. 감정 표현이 화끈하고, 사랑하면 온 세상에 공표하고 싶을 만큼 열정적! \"너를 위해 별이라도 따다 줄게\"가 과장이 아닌 진심인 타입이죠.

**전생 연애 스타일:**
- 사랑 고백은 화끈하고 드라마틱하게
- 감정을 숨기지 않는 솔직하고 뜨거운 표현
- 연인을 세상의 중심에 놓는 헌신적 애정

**강점:** 압도적인 사랑 표현으로 상대를 세상에서 가장 특별한 사람으로 느끼게 함

**성장 포인트:** 뜨거운 사랑도 좋지만, 상대의 온도에 맞춰주는 것도 사랑이에요""",
                "min_score": 20,
                "max_score": 23,
            },
            {
                "result_type": "르네상스 예술가의 뮤즈",
                "result_title": "사랑을 예술로 승화시키는, 감각적이고 주도적인 로맨티스트",
                "result_content": """전생의 당신은 피렌체의 예술가에게 영감을 준 뮤즈이거나, 사랑을 작품으로 남긴 예술가였어요. 감정 표현도 풍부하고, 관계를 세련되게 리드하는 능력까지 겸비한 완벽한 로맨티스트! 상대에게 직접 노래를 불러주거나, 손으로 그린 초상화를 선물하는 스타일이죠.

**전생 연애 스타일:**
- 상대를 위한 특별한 이벤트와 선물을 직접 기획
- 감정을 창의적이고 세련된 방식으로 표현
- 관계의 분위기와 방향을 자연스럽게 이끌어감

**강점:** 감각적인 표현력으로 일상도 특별한 추억으로 만드는 능력

**성장 포인트:** 아름답게 꾸미는 것도 좋지만, 때로는 꾸미지 않은 날것의 감정도 나눠보세요""",
                "min_score": 24,
                "max_score": 27,
            },
            {
                "result_type": "그리스 신화 운명의 연인",
                "result_title": "신들도 질투할 만큼 완전체 사랑, 모든 차원에서 올인하는 운명의 러버",
                "result_content": """전생의 당신은 그리스 신화에 등장할 법한 운명적 사랑의 주인공이었어요. 감정 표현도 화끈하고, 관계를 당당하게 리드하며, 사랑의 열정은 올림포스 산을 녹일 정도! \"운명이라 느끼면 그게 운명이야\"가 좌우명이고, 사랑 앞에서는 신도 막을 수 없는 타입이죠.

**전생 연애 스타일:**
- 운명적 만남을 믿고 직감적으로 사랑에 뛰어듦
- 감정도, 행동도, 열정도 풀가동하는 올인형 사랑
- 상대를 위해 세상과도 맞서는 드라마틱한 결단력

**강점:** 모든 면에서 진심을 다하는 완전체 사랑으로 상대를 압도적으로 감동시킴

**성장 포인트:** 올인하는 것도 멋지지만, 사랑의 불꽃이 당신 자신을 태우지 않도록 조심하세요""",
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
        print("✅ 전생 러브스토리 테스트 시드 데이터 생성 완료!")
        print(f"   - 테스트 ID: {test_id}")
        print(f"   - 문항 수: 10개")
        print(f"   - 결과 유형: 8개")

    except Exception as e:
        db.rollback()
        print(f"❌ 전생 러브스토리 테스트 시드 실패: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    # 테이블 생성 확인
    Base.metadata.create_all(bind=engine)
    seed_past_life_love_test()

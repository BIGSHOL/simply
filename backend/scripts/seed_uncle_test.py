"""
아재력 테스트 시드 스크립트

15문항, 20개 결과 유형
점수 범위: 15-60점

실행: python scripts/seed_uncle_test.py
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


def seed_uncle_test():
    """아재력 테스트 시드 데이터 생성"""
    db = SessionLocal()

    try:
        # 기존 테스트 확인
        existing = db.query(Test).filter(Test.title.contains("아재력")).first()
        if existing:
            print("⚠️  아재력 테스트가 이미 존재합니다. 시드 스킵.")
            return

        # 테스트 ID 생성
        test_id = uuid.uuid4()

        # 테스트 생성
        test = Test(
            id=test_id,
            title="아재 아니라고요? (확인 좀 해볼게요 ㅎㅎ)",
            description="요즘 애들 뭐 좋아하는지 모른다고요? 괜찮아요, 저도 몰라요~ 15개 질문으로 당신의 숨겨진 아재력을 측정해드립니다! 날씨가 좋으니까... 날'아'가고 싶'씨'? ㅋㅋ",
            category="fun",
            thumbnail_url="/images/tests/uncle-power.png",
            play_count=0,
        )
        db.add(test)

        # 문항 데이터
        questions_data = [
            {
                "content": '친구가 "오늘 날씨 좋다"라고 하자 당신의 반응은?',
                "order_num": 1,
                "choices": [
                    {"content": '"인정ㅇㅈ 날씨 미쳤다 진짜"', "score": 1, "order_num": 1},
                    {"content": '"날씨 좋으니까 기분도 좋네"', "score": 2, "order_num": 2},
                    {"content": "\"날씨가 좋아서 '날'이 '씨'원하네\"", "score": 3, "order_num": 3},
                    {"content": "\"날씨가 좋으니까... 날'아'가고 싶'씨'? ㅎㅎ\"", "score": 4, "order_num": 4},
                ],
            },
            {
                "content": "회식 자리에서 당신의 모습은?",
                "order_num": 2,
                "choices": [
                    {"content": "핸드폰 보면서 언제 끝나나 카운트", "score": 1, "order_num": 1},
                    {"content": "적당히 분위기 맞춰주고 조용히 있음", "score": 2, "order_num": 2},
                    {"content": '"자 자 우리 한 잔씩 들고~" 분위기 주도', "score": 3, "order_num": 3},
                    {"content": '"내가 말이야~ 너희 나이 때..." 장문의 스피치 시작', "score": 4, "order_num": 4},
                ],
            },
            {
                "content": "SNS에 올릴 사진을 찍을 때 당신은?",
                "order_num": 3,
                "choices": [
                    {"content": "0.5 각도에 필터 5개 돌리고 보정까지", "score": 1, "order_num": 1},
                    {"content": "기본 카메라로 찍고 밝기만 조정", "score": 2, "order_num": 2},
                    {"content": '후면 카메라로 찍고 "이게 자연스럽지"', "score": 3, "order_num": 3},
                    {"content": '엄지척 포즈 + "인생샷 인증ㅋㅋ" 텍스트', "score": 4, "order_num": 4},
                ],
            },
            {
                "content": "노래방 가서 첫 곡으로 부를 노래는?",
                "order_num": 4,
                "choices": [
                    {"content": "지금 멜론 TOP10에 있는 노래", "score": 1, "order_num": 1},
                    {"content": "2-3년 전 나왔던 띵곡", "score": 2, "order_num": 2},
                    {"content": "5년 전 나왔지만 명곡인 노래", "score": 3, "order_num": 3},
                    {"content": '"이 노래 모르면 간첩이야" + 10년 전 발라드', "score": 4, "order_num": 4},
                ],
            },
            {
                "content": '후배가 "요즘 ~~이 대세예요"라고 하면?',
                "order_num": 5,
                "choices": [
                    {"content": '"오 진짜? 나도 그거 알지 ㅇㅇ"', "score": 1, "order_num": 1},
                    {"content": '"아 그렇구나~ 요즘 그게 유행이야?"', "score": 2, "order_num": 2},
                    {"content": '"그게 뭔데? 근데 요즘 애들은 그런 거 좋아해?"', "score": 3, "order_num": 3},
                    {"content": '"요즘 애들은... 우리 때는 이게 대세였는데ㅋㅋ"', "score": 4, "order_num": 4},
                ],
            },
            {
                "content": "이모티콘을 고를 때 당신의 기준은?",
                "order_num": 6,
                "choices": [
                    {"content": "요즘 유행하는 밈 이모티콘", "score": 1, "order_num": 1},
                    {"content": "귀엽고 쓸만한 캐릭터 이모티콘", "score": 2, "order_num": 2},
                    {"content": "기본 이모티콘으로 충분", "score": 3, "order_num": 3},
                    {"content": '움직이는 이모티콘 + "ㅋㅋㅋㅋㅋㅋ" 텍스트', "score": 4, "order_num": 4},
                ],
            },
            {
                "content": "옷 쇼핑할 때 당신의 스타일은?",
                "order_num": 7,
                "choices": [
                    {"content": "인스타 감성 맞춘 트렌디한 스타일", "score": 1, "order_num": 1},
                    {"content": "무난하고 깔끔한 베이직 아이템", "score": 2, "order_num": 2},
                    {"content": "편하고 활동성 좋은 스타일", "score": 3, "order_num": 3},
                    {"content": '등산복 + "이게 제일 편해" + 주머니 많은 조끼', "score": 4, "order_num": 4},
                ],
            },
            {
                "content": "주말에 주로 하는 취미는?",
                "order_num": 8,
                "choices": [
                    {"content": "숏폼 보기 + 침대에서 폰 만지작", "score": 1, "order_num": 1},
                    {"content": "카페 가서 친구들이랑 수다", "score": 2, "order_num": 2},
                    {"content": "운동이나 산책하면서 건강 관리", "score": 3, "order_num": 3},
                    {"content": '등산 or 낚시 + "자연이 최고야"', "score": 4, "order_num": 4},
                ],
            },
            {
                "content": '"ㅇㅈ", "ㄹㅇ", "ㅇㅋ" 같은 줄임말을 보면?',
                "order_num": 9,
                "choices": [
                    {"content": "당연히 알지, 나도 매일 씀", "score": 1, "order_num": 1},
                    {"content": "알긴 아는데 잘 안 쓰게 됨", "score": 2, "order_num": 2},
                    {"content": "이게 무슨 뜻이지? 요즘엔 이런 것도 있어?", "score": 3, "order_num": 3},
                    {"content": '"제대로 말 좀 해라 알아듣게" + 진심으로 불편함', "score": 4, "order_num": 4},
                ],
            },
            {
                "content": "카톡으로 대화할 때 당신의 스타일은?",
                "order_num": 10,
                "choices": [
                    {"content": "ㅋㅋ / ㅇㅇ / ㄱㄱ 초고속 짧은 답장", "score": 1, "order_num": 1},
                    {"content": "이모티콘 + 적당한 텍스트", "score": 2, "order_num": 2},
                    {"content": "문장으로 정확하게 표현", "score": 3, "order_num": 3},
                    {"content": '"안녕하세요^^ 오늘 날씨가 참 좋네요ㅎㅎ 밥은 드셨나요?"', "score": 4, "order_num": 4},
                ],
            },
            {
                "content": '"이거 레알 핵인싸템 아니냐"는 말을 들으면?',
                "order_num": 11,
                "choices": [
                    {"content": '"ㅇㅈ 인정ㅋㅋ"', "score": 1, "order_num": 1},
                    {"content": '"아 그렇구나~" (대충 이해는 함)', "score": 2, "order_num": 2},
                    {"content": '"레알이 뭐고 핵인싸템이 뭐야?"', "score": 3, "order_num": 3},
                    {"content": '"제대로 된 한국말 좀 쓰자" + 진심으로 답답함', "score": 4, "order_num": 4},
                ],
            },
            {
                "content": "영상 콘텐츠 볼 때 당신의 습관은?",
                "order_num": 12,
                "choices": [
                    {"content": "숏폼만 봄, 1분 넘어가면 스킵", "score": 1, "order_num": 1},
                    {"content": "유튜브 쇼츠/릴스 위주, 가끔 긴 영상", "score": 2, "order_num": 2},
                    {"content": "10-20분 영상이 적당함", "score": 3, "order_num": 3},
                    {"content": "TV 켜고 1시간짜리 다큐 정주행", "score": 4, "order_num": 4},
                ],
            },
            {
                "content": "단톡방에 아재개그가 올라오면?",
                "order_num": 13,
                "choices": [
                    {"content": '읽씹 or "..." + 무표정 이모티콘', "score": 1, "order_num": 1},
                    {"content": '"ㅋ" 하나 정도는 쳐줌 (예의상)', "score": 2, "order_num": 2},
                    {"content": '"ㅋㅋㅋ 이건 좀 웃기네요"', "score": 3, "order_num": 3},
                    {"content": '"ㅋㅋㅋㅋㅋㅋ 이거 나도 알려드릴까요?" + 추가 아재개그', "score": 4, "order_num": 4},
                ],
            },
            {
                "content": '누가 "요즘 대세는 ~~야"라고 하면?',
                "order_num": 14,
                "choices": [
                    {"content": "바로 검색해보고 공부함", "score": 1, "order_num": 1},
                    {"content": '"아 그래? 나중에 찾아봐야지"', "score": 2, "order_num": 2},
                    {"content": '"그런 게 유행이야? 잘 모르겠네"', "score": 3, "order_num": 3},
                    {"content": '"대세는 변해도 진리는 변하지 않아" + 철학 모드', "score": 4, "order_num": 4},
                ],
            },
            {
                "content": "식당에서 사장님과 당신의 관계는?",
                "order_num": 15,
                "choices": [
                    {"content": "주문만 하고 폰 봄, 대화 없음", "score": 1, "order_num": 1},
                    {"content": '"잘 먹겠습니다" 인사 정도', "score": 2, "order_num": 2},
                    {"content": '"맛있어요~" 정도의 짧은 대화', "score": 3, "order_num": 3},
                    {"content": '사장님과 10분 수다 + "사장님 여기 자주 올게요^^"', "score": 4, "order_num": 4},
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

        # 결과 유형 데이터 (20개)
        result_types_data = [
            {
                "type": "MZ 순혈",
                "title": "아재와는 1도 상관없는 당신",
                "content": "당신은 아재력이라고는 찾아볼 수 없는 순수 MZ세대입니다. 숏폼 콘텐츠가 체질이고, 아재개그는 물리적으로 불가능합니다. 친구들이 '너는 진짜 MZ다'라고 하면 그게 칭찬인 줄 아는 유형. 아재력 0%를 유지하는 것도 재능입니다.",
                "min_score": 15,
                "max_score": 17,
            },
            {
                "type": "Z세대 수호자",
                "title": "아재력 감지 레이더 가동 중",
                "content": "아재력의 징조가 조금이라도 보이면 즉시 차단하는 당신. 주변에 아재개그 하는 사람이 있으면 '아재 냄새 난다'며 즉시 경고하는 타입입니다. MZ 문화의 수호자로서 트렌드에 누구보다 민감합니다.",
                "min_score": 18,
                "max_score": 19,
            },
            {
                "type": "밈 마스터",
                "title": "숏폼만이 내 언어",
                "content": "당신의 언어는 숏폼과 밈입니다. 말을 할 때도 밈으로 대화하고, 카톡도 밈 이미지로만 소통합니다. 3분 이상 영상은 2배속이 기본이고, 아재개그는 당신의 알고리즘에 없습니다.",
                "min_score": 20,
                "max_score": 21,
            },
            {
                "type": "틱톡 네이티브",
                "title": "15초가 내 인생",
                "content": "15초 안에 모든 것을 표현할 수 있는 당신. 틱톡, 릴스, 쇼츠가 당신의 주요 정보 소스이며, 긴 설명은 이해가 안 갑니다. 아재들이 '요즘 애들은 집중력이 없다'고 하면 '아니 15초로 충분한데요?'라고 당당히 말하는 타입.",
                "min_score": 22,
                "max_score": 24,
            },
            {
                "type": "MZ 표준형",
                "title": "딱 요즘 세대스러운 당신",
                "content": "당신은 MZ세대의 표준 모델입니다. 트렌드도 적당히 따라가고, 밈도 적당히 이해하고, 아재개그에는 적당히 무반응. 너무 앞서가지도, 뒤처지지도 않는 완벽한 균형감각을 가졌습니다.",
                "min_score": 25,
                "max_score": 27,
            },
            {
                "type": "아재력 새싹",
                "title": "뭔가 조짐이 보이기 시작",
                "content": "아직은 MZ지만... 뭔가 조짐이 보입니다. 가끔 아재개그가 머릿속을 스치고, 예전 노래가 듣고 싶어지기 시작합니다. '요즘 애들 음악은 뭔가...' 라는 생각이 들기 시작하면 위험신호입니다!",
                "min_score": 28,
                "max_score": 30,
            },
            {
                "type": "과도기 인간",
                "title": "MZ와 아재 사이 어딘가",
                "content": "당신은 지금 과도기입니다. 숏폼도 보지만 긴 영상도 봅니다. 밈도 이해하지만 아재개그도 나름 재미있습니다. 친구들은 당신을 MZ로 보지만, 당신은 은근 아재들 말에 공감합니다.",
                "min_score": 31,
                "max_score": 33,
            },
            {
                "type": "아재력 임계점",
                "title": "지금이 마지노선입니다",
                "content": "위험합니다. 아재력이 50%를 넘어섰습니다. 아재개그를 듣고 웃기 시작했고, '요즘 애들은 이런 것도 몰라?'라는 말이 나오기 시작했습니다. 지금이 되돌릴 수 있는 마지막 기회입니다!",
                "min_score": 34,
                "max_score": 36,
            },
            {
                "type": "아재 견습생",
                "title": "본격 아재 입문 단계",
                "content": "축하합니다(?). 당신은 이제 아재 견습생입니다. 아재개그가 자연스럽게 나오기 시작하고, 회식 자리에서 훈훈한 이야기를 하고 싶어집니다. MZ 친구들이 '너 요즘 왜 그래?'라고 걱정하기 시작했다면 이미 늦었습니다.",
                "min_score": 37,
                "max_score": 39,
            },
            {
                "type": "중급 아재",
                "title": "이제 숨길 수 없는 아재력",
                "content": "이제 아재력을 숨길 수 없습니다. 대화 중 아재개그가 자동으로 튀어나오고, 식당에서 사장님과 친해지는 특기가 생겼습니다. '요즘 애들은 참...'이라는 말을 일주일에 3번 이상 합니다.",
                "min_score": 40,
                "max_score": 42,
            },
            {
                "type": "아재 정규직",
                "title": "아재 정규직 전환 완료",
                "content": "정규직 전환을 축하드립니다. 당신은 이제 공식 아재입니다. 아재개그는 기본이고, 인생 조언까지 곁들여집니다. 회식 자리에서 '내가 너희 나이 때는 말이야...'로 시작하는 장문의 스피치가 가능합니다.",
                "min_score": 43,
                "max_score": 45,
            },
            {
                "type": "고급 아재",
                "title": "주변에 아재력 전파 중",
                "content": "당신은 이제 아재력을 전파하는 단계입니다. 주변 사람들이 당신과 있다 보면 자연스럽게 아재력이 상승합니다. 아재개그는 물론이고, 아재 패션, 아재 취미까지 풀 패키지입니다.",
                "min_score": 46,
                "max_score": 48,
            },
            {
                "type": "아재 장인",
                "title": "아재의 경지에 오르다",
                "content": "당신은 아재의 경지에 올랐습니다. 아재개그도 이제 예술의 경지이며, 상황에 맞는 완벽한 타이밍을 알고 있습니다. 젊은이들은 당신의 아재력을 두려워하면서도 존경합니다.",
                "min_score": 49,
                "max_score": 51,
            },
            {
                "type": "아재 마스터",
                "title": "아재계의 인플루언서",
                "content": "당신은 아재계의 인플루언서입니다. 당신의 아재개그는 주변에서 회자되고, 사람들은 당신의 다음 아재력 발현을 기다립니다. 아재력으로 사람들을 웃기고, 분위기를 만드는 진정한 마스터입니다.",
                "min_score": 52,
                "max_score": 53,
            },
            {
                "type": "전설의 아재",
                "title": "아재력 만렙 달성",
                "content": "전설입니다. 당신의 아재력은 이미 만렙을 찍었습니다. 회사에서는 '아재개그의 신'으로 불리고, 후배들은 당신의 아재 어록을 정리합니다. 10년 후에도 사람들은 당신의 아재력을 기억할 것입니다.",
                "min_score": 54,
                "max_score": 55,
            },
            {
                "type": "아재신",
                "title": "신의 경지에 도달한 아재력",
                "content": "당신은 이미 인간의 영역을 벗어났습니다. 아재력이 신의 경지에 도달했습니다. 당신이 입을 열면 아재개그가, 손을 뻗으면 아재력이 흘러나옵니다. 아재의 신, 당신 앞에 고개를 숙입니다.",
                "min_score": 56,
                "max_score": 57,
            },
            {
                "type": "아재 초월자",
                "title": "아재를 넘어선 존재",
                "content": "당신은 아재를 넘어섰습니다. 일반적인 아재력으로는 설명이 불가능한 경지입니다. 당신의 아재개그는 시공간을 초월하고, 과학자들도 당신의 아재력을 연구하고 싶어 합니다.",
                "min_score": 58,
                "max_score": 58,
            },
            {
                "type": "아재 레전드",
                "title": "살아있는 아재력 교과서",
                "content": "역사에 남을 아재력입니다. 후대 사람들은 교과서에서 당신의 아재력을 배울 것입니다. 박물관에 당신의 아재개그가 전시되고, 학자들이 당신의 아재력을 연구합니다.",
                "min_score": 59,
                "max_score": 59,
            },
            {
                "type": "아재의 화신",
                "title": "아재 그 자체",
                "content": "축하합니다. 당신은 완벽한 아재력 100%를 달성했습니다. 당신은 아재이며, 아재는 곧 당신입니다. 당신의 DNA는 아재개그로 이루어져 있고, 혈액형은 아재형입니다. 당신이 곧 아재입니다.",
                "min_score": 60,
                "max_score": 60,
            },
            {
                "type": "아재력 특이점",
                "title": "측정 불가능한 아재력",
                "content": "오류입니다. 당신의 아재력은 측정 범위를 초과했습니다. 과학자들은 당신을 '아재력 특이점'이라고 부릅니다. 당신 주변에서는 물리 법칙이 무너지고, 아재개그가 자연 발생합니다.",
                "min_score": 61,
                "max_score": 999,
            },
        ]

        # 결과 유형 추가
        for rt_data in result_types_data:
            result_type = ResultType(
                id=uuid.uuid4(),
                test_id=test_id,
                result_type=rt_data["type"],
                result_title=rt_data["title"],
                result_content=rt_data["content"],
                min_score=rt_data["min_score"],
                max_score=rt_data["max_score"],
            )
            db.add(result_type)

        # 커밋
        db.commit()
        print("✅ 아재력 테스트 시드 데이터 생성 완료!")
        print(f"   - 테스트 ID: {test_id}")
        print(f"   - 문항 수: 15개")
        print(f"   - 결과 유형: 20개")

    except Exception as e:
        db.rollback()
        print(f"❌ 아재력 테스트 시드 실패: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    # 테이블 생성 확인
    from app.core.database import engine, Base
    Base.metadata.create_all(bind=engine)

    seed_uncle_test()

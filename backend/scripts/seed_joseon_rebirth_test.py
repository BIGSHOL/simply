"""
조선시대 환생하면 나의 신분은? 시드 스크립트

10문항, 8개 결과 유형 (주요 8개만 구현)
실행: python -m scripts.seed_joseon_rebirth_test
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


def seed_joseon_rebirth_test():
    """조선시대 환생 신분 테스트 시드 데이터 생성"""
    db = SessionLocal()

    try:
        # 기존 테스트 확인
        existing = db.query(Test).filter(Test.title.contains("조선시대")).first()
        if existing:
            print("⚠️  조선시대 환생 테스트가 이미 존재합니다. 시드 스킵.")
            return

        # 테스트 ID 생성
        test_id = uuid.uuid4()

        # 테스트 생성
        test = Test(
            id=test_id,
            title="조선시대 환생하면 나의 신분은? 👘",
            description="그대, 조선에 환생하면 무엇이 되겠소? 10개 질문으로 알아보는 나의 전생 신분",
            category="fun",
            thumbnail_url="/images/tests/joseon-rebirth.png",
            play_count=47650,
            like_count=3980,
        )
        db.add(test)

        # 문항 데이터 (A=0, B=3)
        questions_data = [
            {
                "content": "조회 시간(=월요일 아침 회의)에 전하께서 \"의견을 말하라\" 하셨다. 그대의 반응은?",
                "order_num": 1,
                "choices": [
                    {"content": "🗣️ 바로 손 들고 직언 상소! \"전하, 소신의 생각은 이러하옵니다\"", "score": 0, "order_num": 1},
                    {"content": "👀 일단 분위기 파악 먼저... 다른 신하들 눈치를 보며 조용히", "score": 3, "order_num": 2},
                ],
            },
            {
                "content": "관직(=직장)에서 승진 기회가 왔다! 하지만 다른 고을(=타 지역)로 가야 한다면?",
                "order_num": 2,
                "choices": [
                    {"content": "🏃 새로운 고을이라니 신난다! 짐 싸는 건 일도 아니오", "score": 0, "order_num": 1},
                    {"content": "🏡 지금 고을이 편한데... 익숙한 곳에서 천천히 올라가겠소", "score": 3, "order_num": 2},
                ],
            },
            {
                "content": "퇴근 후(=파루 종이 울린 후) 그대의 저녁 시간은?",
                "order_num": 3,
                "choices": [
                    {"content": "🍻 동료들과 주막(=회식)에서 한잔! 사람이 있어야 신나지", "score": 0, "order_num": 1},
                    {"content": "📚 사랑방에서 혼자 독서(=넷플릭스)... 나만의 시간이 최고", "score": 3, "order_num": 2},
                ],
            },
            {
                "content": "고을에 큰 축제(=회사 워크숍)가 열렸다. 그대의 역할은?",
                "order_num": 4,
                "choices": [
                    {"content": "🎯 축제 총괄 담당! 내가 기획하고 진행까지 책임진다", "score": 0, "order_num": 1},
                    {"content": "🎪 기획은 다른 분이... 나는 맡은 파트 열심히 할게요", "score": 3, "order_num": 2},
                ],
            },
            {
                "content": "한양(=서울)에서 새로운 유행이 왔다고! 그대의 반응은?",
                "order_num": 5,
                "choices": [
                    {"content": "🔥 당장 따라해봐야지! 새로운 거 안 해보면 잠이 안 온다", "score": 0, "order_num": 1},
                    {"content": "🤔 글쎄... 내가 하던 거 그대로가 편한데, 유행은 금방 바뀌잖아", "score": 3, "order_num": 2},
                ],
            },
            {
                "content": "동네 사또(=팀장)가 팀 회식을 잡았다. 그대의 속마음은?",
                "order_num": 6,
                "choices": [
                    {"content": "🥳 오 좋다! 이번에 새로 온 사람이랑도 친해져야지", "score": 0, "order_num": 1},
                    {"content": "😅 아... 집에 가고 싶은데... 핑계 거리를 찾아보자", "score": 3, "order_num": 2},
                ],
            },
            {
                "content": "궁궐(=회사)에서 새 프로젝트 공모가 떴다. 그대는?",
                "order_num": 7,
                "choices": [
                    {"content": "✋ 내가 팀장 할게! 내 아이디어로 이끌어보겠소", "score": 0, "order_num": 1},
                    {"content": "🤝 좋은 팀장 밑에서 내 역할을 잘 해내는 게 더 좋소", "score": 3, "order_num": 2},
                ],
            },
            {
                "content": "보름달이 뜬 밤(=주말 저녁), 계획이 없는 그대는?",
                "order_num": 8,
                "choices": [
                    {"content": "🌙 갑자기 야시장(=핫플)을 탐방하러 떠나볼까? 즉흥이 좋아!", "score": 0, "order_num": 1},
                    {"content": "🏠 역시 계획 없는 날은 집이 최고, 이불 속이 제일 안전하오", "score": 3, "order_num": 2},
                ],
            },
            {
                "content": "과거 시험(=자격증 시험) 준비, 그대의 스타일은?",
                "order_num": 9,
                "choices": [
                    {"content": "👥 동문수학(=스터디 그룹)! 같이 공부해야 의욕이 생기오", "score": 0, "order_num": 1},
                    {"content": "🎧 독학이 최고! 혼자 집중해야 머리에 들어오오", "score": 3, "order_num": 2},
                ],
            },
            {
                "content": "임금(=사장님)이 갑자기 \"새 사업을 하겠다\"고 선포했다. 그대의 반응은?",
                "order_num": 10,
                "choices": [
                    {"content": "😰 에? 갑자기? 기존 사업이 안정적인데... 좀 불안하오", "score": 0, "order_num": 1},
                    {"content": "🚀 오! 새로운 도전이라니 두근거린다! 어디 한번 해보자!", "score": 3, "order_num": 2},
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

        # 8개 ResultType (주요 유형만)
        result_types = [
            {
                "result_type": "임금",
                "result_title": "조선의 CEO - 어명이다! 회의실에서도 용상에 앉은 기분",
                "result_content": """그대는 타고난 왕의 관록이로다! 팀플이든 회식이든 자연스럽게 중심에 서는 스타일. "내가 하면 된다"는 자신감으로 무장하고, 사람들을 이끄는 데 거부감이 없소이다. 회의실에서도 어전회의 하듯 의견을 정리하고, 결정을 내리는 게 편하다면 그대는 진정한 조선의 리더. 다만 가끔 "과인이 틀렸느냐?" 모드가 되지 않도록 경계하시게나!

**조선시대 라이프스타일:**
- 매일 아침 어전회의(=팀 미팅) 주재하며 하루 시작
- 신하들(=동료들)의 상소문(=슬랙 메시지) 직접 검토
- 가끔 암행어사(=현장 점검) 나서서 직접 확인

**강점:** 결단력 있는 의사결정으로 조직을 이끄는 카리스마
**성장 포인트:** 모든 걸 혼자 결정하려 하지 말고, 가끔은 신하들의 의견에 귀 기울여 보소서
**현대 직업:** CEO / 스타트업 대표""",
                "min_score": 0,
                "max_score": 3,
            },
            {
                "result_type": "세자",
                "result_title": "조선의 차기 에이스 - 동궁마마 출근길, 배움은 멈추지 않는다",
                "result_content": """그대는 늘 성장하고 배우려는 세자의 기상이 있도다! 리더 자리에 욕심이 있지만, 아직은 실력을 더 쌓고 싶은 마음. 스터디도 열심히, 자기계발도 열심히, "언젠간 내가 이끌 날이 온다"는 야망을 품고 착실하게 준비하는 타입이오. 사람들과 두루 잘 지내면서도 자기만의 비전이 확실하니, 미래의 성군 감이로다!

**조선시대 라이프스타일:**
- 서연(=스터디 그룹)에서 열정적으로 학습
- 동궁전에서 미래 비전 계획 수립
- 세자빈(=절친)과 함께 맛집 탐방(=궁중 수라 품평)

**강점:** 배움에 대한 끝없는 열정과 성장 마인드셋
**성장 포인트:** 준비만 하다가 타이밍을 놓치지 마소서!
**현대 직업:** 대기업 핵심 인재 / 로스쿨 & MBA 준비생""",
                "min_score": 4,
                "max_score": 7,
            },
            {
                "result_type": "한량",
                "result_title": "조선의 워라밸 장인 - 세상 모든 것은 풍류 앞에 무릎 꿇는다",
                "result_content": """그대는 조선 최고의 자유영혼이로다! 관직? 출세? 그런 건 관심 없소. 오늘 날씨 좋으면 산책하고, 기분 좋으면 시 한 수 읊고, 맛집이 생기면 당장 달려가는 삶. "인생 뭐 있어, 즐기면 그만"이 인생 모토. MZ식으로 말하면 완벽한 워라밸의 화신이오. 남들이 야근할 때 칼퇴하고 취미 생활하는 그대, 조선시대였으면 풍류객으로 이름을 날렸을 것이오!

**조선시대 라이프스타일:**
- 아침은 느지막이 일어나 차 한 잔으로 시작
- 오후에는 산수 유람(=카페 투어)하며 풍류 즐김
- 밤에는 시회(=감성 플레이리스트) 들으며 하루 마무리

**강점:** 삶의 여유와 균형을 아는 감성 지능
**성장 포인트:** 풍류도 좋지만, 가끔은 목표를 세우고 도전해보는 것도 새로운 재미가 될 수 있소이다!
**현대 직업:** 프리랜서 / 디지털 노마드""",
                "min_score": 8,
                "max_score": 11,
            },
            {
                "result_type": "어의",
                "result_title": "조선의 인체공학 전문가 - 맥을 짚으면 다 보인다",
                "result_content": """그대는 섬세하고 꼼꼼한 어의의 자질을 갖추었도다! 주변 사람들의 컨디션을 누구보다 먼저 알아차리고, "괜찮아?" 한마디를 건네는 따뜻한 성품. 체계적이고 분석적인 사고를 하면서도, 사람을 향한 마음이 깊은 타입이오. 안정적인 환경에서 전문성을 발휘할 때 빛나는 스타일이니, 그대의 손길이 닿는 곳에 평안이 깃들 것이오!

**조선시대 라이프스타일:**
- 매일 약재(=데이터) 꼼꼼히 분석하며 처방전 작성
- 내의원(=사무실)에서 묵묵히 전문성 발휘
- 가끔 왕의 수라상(=팀 점심) 영양 균형 체크

**강점:** 디테일을 놓치지 않는 꼼꼼함과 분석력
**성장 포인트:** 남을 돌보는 만큼 자기 자신도 챙기소서!
**현대 직업:** 의사 / 데이터 분석가 / 연구원""",
                "min_score": 12,
                "max_score": 15,
            },
            {
                "result_type": "보부상",
                "result_title": "조선의 인플루언서 - 전국 팔도가 내 비즈니스 필드",
                "result_content": """그대는 타고난 장사꾼이요 네트워커로다! 사람 만나는 걸 좋아하고, 새로운 곳에 가는 걸 두려워하지 않으며, "이거 요즘 대세예요" 하며 트렌드를 전파하는 게 일상이오. 전국 장터(=SNS)를 누비며 인맥을 쌓고, 어디서든 "이 사람 알아?"라는 말이 나오는 인싸 of 인싸. 모험심과 사교성을 무기로 조선팔도를 주름잡을 보부상이오!

**조선시대 라이프스타일:**
- 전국 장터(=네트워킹 행사) 순회하며 신상 소개
- 각 고을 인맥(=인스타 팔로워) 관리에 여념 없음
- 새로운 물건(=트렌드) 발굴이 최고의 즐거움

**강점:** 어디서든 통하는 사교성과 커뮤니케이션 능력
**성장 포인트:** 넓게 아는 것도 좋지만, 하나를 깊게 파보는 것도 큰 무기가 될 수 있소이다!
**현대 직업:** 마케터 / 영업 전문가 / 인플루언서""",
                "min_score": 16,
                "max_score": 19,
            },
            {
                "result_type": "기생",
                "result_title": "조선의 멀티 엔터테이너 - 가무에 시에 그림까지",
                "result_content": """그대는 예술적 감성과 사교성을 겸비한 조선 최고의 엔터테이너이로다! 분위기를 읽는 센스가 탁월하고, 어떤 자리에서든 분위기를 살리는 재주가 있소. 가무(=댄스 챌린지)도, 시(=글쓰기)도, 풍류(=감성 콘텐츠)도 다 잘하는 멀티 플레이어. 사람들의 마음을 사로잡는 매력이 넘치지만, 그 안에는 자기만의 확고한 예술 세계가 있으니 그 깊이를 알아보는 자가 진정한 지기이오!

**조선시대 라이프스타일:**
- 매일 가무(=콘텐츠 제작) 연습으로 실력 연마
- 풍류 자리(=모임)에서 분위기 메이킹 담당
- 시와 그림(=SNS 피드)으로 감성 표현

**강점:** 분위기를 읽고 살리는 탁월한 사교 센스
**성장 포인트:** 남의 기대에 맞추느라 정작 자신의 진짜 목소리를 잃지 않도록 주의하소서!
**현대 직업:** 콘텐츠 크리에이터 / 공연 예술가""",
                "min_score": 20,
                "max_score": 23,
            },
            {
                "result_type": "무관",
                "result_title": "조선의 액션 히어로 - 칼 대신 노트북을 들었을 뿐, 실행력 만렙",
                "result_content": """그대는 말보다 행동이 앞서는 무관의 기질을 타고났도다! "일단 해보자"가 인생 모토이고, 계획 세우느라 시간 허비하는 것보다 직접 부딪혀보는 스타일이오. 체력도 좋고, 의지도 강하며, 한번 목표를 정하면 끝까지 밀어붙이는 추진력이 있소. 팀에서는 누구보다 먼저 손 들고 나서는 실행형 인재!

**조선시대 라이프스타일:**
- 새벽 무예 수련(=헬스장)으로 하루 시작
- 전장(=프로젝트)에서 선봉에 서서 돌파
- 동료 무관들과 무예 겨루기(=운동 크루) 즐김

**강점:** 말보다 행동이 빠른 압도적 실행력
**성장 포인트:** 용맹함도 좋지만, 전략 없는 돌진은 위험하오!
**현대 직업:** 스타트업 실행 담당 / 운동 선수""",
                "min_score": 24,
                "max_score": 27,
            },
            {
                "result_type": "궁녀",
                "result_title": "조선의 디테일 장인 - 궁궐 살림은 내게 맡겨라",
                "result_content": """그대는 세심하고 체계적인 궁녀의 자질을 타고났도다! 눈에 보이지 않는 디테일까지 신경 쓰고, 조직이 돌아가도록 뒤에서 묵묵히 일하는 스타일이오. 화려한 스포트라이트보다는 "이 사람이 없으면 안 돌아가지"라는 말을 들을 때 보람을 느끼는 타입. 꼼꼼한 기록과 관리 능력으로 어떤 조직이든 든든한 기둥이 되어주니, 그대야말로 진정한 숨은 실력자이오!

**조선시대 라이프스타일:**
- 매일 궁궐 물품(=업무 리스트) 꼼꼼히 정리
- 마마(=상사)의 일정 관리를 완벽하게 서포트
- 동료 궁녀들(=팀원들)과 소소한 수다로 소통

**강점:** 디테일을 놓치지 않는 꼼꼼한 관리 능력
**성장 포인트:** 뒤에서만 일하지 말고, 가끔은 그대의 공을 당당히 드러내보소서!
**현대 직업:** 프로젝트 매니저 / 비서 / 총무""",
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
        print("✅ 조선시대 환생 테스트 시드 데이터 생성 완료!")
        print(f"   - 테스트 ID: {test_id}")
        print(f"   - 문항 수: 10개")
        print(f"   - 결과 유형: 8개")

    except Exception as e:
        db.rollback()
        print(f"❌ 조선시대 환생 테스트 시드 실패: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    # 테이블 생성 확인
    Base.metadata.create_all(bind=engine)
    seed_joseon_rebirth_test()

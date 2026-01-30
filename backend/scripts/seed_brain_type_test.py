"""
나의 두뇌 유형은? 시드 스크립트
10문항, 8개 결과 유형
실행: python -m scripts.seed_brain_type_test
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


def seed_brain_type_test():
    """나의 두뇌 유형은? 시드 데이터 생성"""
    db = SessionLocal()

    try:
        # 기존 테스트 확인
        existing = db.query(Test).filter(Test.title.contains("두뇌")).first()
        if existing:
            print("⚠️  두뇌 유형 테스트가 이미 존재합니다. 시드 스킵.")
            return

        # 테스트 ID 생성
        test_id = uuid.uuid4()

        # 테스트 생성
        test = Test(
            id=test_id,
            title="나의 두뇌 유형은? 🧠",
            description="논리형? 창의형? 10개 질문으로 당신의 사고방식과 두뇌 작동 원리를 분석해드립니다! MBTI보다 재밌는 두뇌 유형 테스트!",
            category="personality",
            thumbnail_url="/images/tests/brain-type.png",
            play_count=35680,
            like_count=2870,
        )
        db.add(test)

        # 문항 데이터 (10개, A/B 이지선다, A=0점, B=3점)
        questions_data = [
            {
                "content": '친구가 갑자기 "요즘 고민이 있어"라고 말했다. 나는?',
                "order_num": 1,
                "choices": [
                    {"content": '"무슨 일인데? 하나씩 정리해보자"', "score": 0, "order_num": 1},
                    {"content": '"힘들겠다... 일단 밥 먹으러 갈까?"', "score": 3, "order_num": 2},
                ],
            },
            {
                "content": "새로운 프로젝트를 맡았을 때 가장 먼저 하는 행동은?",
                "order_num": 2,
                "choices": [
                    {"content": "유사 사례를 찾아보고 각 요소를 분석한다", "score": 0, "order_num": 1},
                    {"content": "전체 목표와 큰 그림을 먼저 그려본다", "score": 3, "order_num": 2},
                ],
            },
            {
                "content": "문제가 생겼을 때 나는?",
                "order_num": 3,
                "choices": [
                    {"content": "매뉴얼이나 검증된 방법을 찾아본다", "score": 0, "order_num": 1},
                    {"content": '"이렇게 하면 되지 않을까?" 새로운 방법을 시도한다', "score": 3, "order_num": 2},
                ],
            },
            {
                "content": "여행 계획을 세울 때 나는?",
                "order_num": 4,
                "choices": [
                    {"content": "일정표를 만들고 예약을 미리 다 해둔다", "score": 0, "order_num": 1},
                    {"content": "대충 숙소만 정하고 현지에서 즉흥적으로 돌아다닌다", "score": 3, "order_num": 2},
                ],
            },
            {
                "content": "논쟁이 생겼을 때 나의 반응은?",
                "order_num": 5,
                "choices": [
                    {"content": '"근거가 뭔데?" 논리적으로 따져본다', "score": 0, "order_num": 1},
                    {"content": '"왜 저렇게 말했을까?" 상대 감정을 먼저 파악한다', "score": 3, "order_num": 2},
                ],
            },
            {
                "content": "책이나 영화를 볼 때 나는?",
                "order_num": 6,
                "choices": [
                    {"content": "캐릭터 심리, 복선, 설정을 하나하나 분석하며 본다", "score": 0, "order_num": 1},
                    {"content": "전체적인 분위기와 메시지, 여운을 중시한다", "score": 3, "order_num": 2},
                ],
            },
            {
                "content": "회의 시간, 나는 주로?",
                "order_num": 7,
                "choices": [
                    {"content": '"이 방법의 장단점은..." 논리적으로 의견을 제시한다', "score": 0, "order_num": 1},
                    {"content": '"이런 느낌은 어때요?" 직관적인 아이디어를 던진다', "score": 3, "order_num": 2},
                ],
            },
            {
                "content": "정보를 정리할 때 나는?",
                "order_num": 8,
                "choices": [
                    {"content": "카테고리별로 분류하고 세부 항목을 나눈다", "score": 0, "order_num": 1},
                    {"content": "연관된 것들을 연결하며 전체 맥락을 파악한다", "score": 3, "order_num": 2},
                ],
            },
            {
                "content": "새로운 아이디어가 떠올랐을 때 나는?",
                "order_num": 9,
                "choices": [
                    {"content": "실현 가능성을 먼저 따지고 단계별 계획을 세운다", "score": 0, "order_num": 1},
                    {"content": "일단 시도해보고 문제가 생기면 그때 해결한다", "score": 3, "order_num": 2},
                ],
            },
            {
                "content": "친구에게 조언을 해줄 때 나는?",
                "order_num": 10,
                "choices": [
                    {"content": '"이런 방법은 어때?" 구체적 해결책을 제시한다', "score": 0, "order_num": 1},
                    {"content": '"네 마음이 어떤지가 중요해" 감정에 공감한다', "score": 3, "order_num": 2},
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

        # 결과 유형 데이터 (8개)
        result_types_data = [
            {
                "type": "전략가 두뇌",
                "title": "치밀한 계획으로 세상을 정복하는 전략적 사고자",
                "content": """**두뇌 작동 방식**
당신의 두뇌는 논리적 프레임워크 위에서 돌아가는 슈퍼컴퓨터입니다. 모든 상황을 논리적으로 분해하고, 데이터를 꼼꼼히 분석하며, 체계적인 계획을 세워 실행합니다.

**강점**
- 복잡한 문제를 체계적으로 해결
- 장기 프로젝트를 끝까지 완수하는 끈기
- 팀에서 신뢰받는 안정적인 플래너
- 리스크를 최소화하는 의사결정

**약점**
- 과도한 분석으로 실행 지연
- 돌발 상황에 유연하게 대처하기 어려움
- 창의적 아이디어보다 검증된 방법 선호

**활용 팁**
기획자, 전략 컨설턴트, 데이터 분석가, 프로젝트 매니저에 적합합니다. "일단 시작하고 보정하기" 마인드도 연습해보세요.""",
                "min_score": 0,
                "max_score": 3,
            },
            {
                "type": "예술가 두뇌",
                "title": "세상을 감각으로 느끼고 창조하는 자유로운 영혼",
                "content": """**두뇌 작동 방식**
당신의 두뇌는 무한한 상상력이 흐르는 창작 스튜디오입니다. 논리보다는 직관, 분석보다는 전체적인 느낌, 계획보다는 영감이 먼저 찾아옵니다.

**강점**
- 아무도 생각 못한 기발한 아이디어 창출
- 감성적 소통으로 사람들의 마음을 움직임
- 변화무쌍한 환경에서도 유연하게 적응
- 예술, 디자인, 콘텐츠 분야에서 빛남

**약점**
- 체계적 실행이 약해 아이디어만 많고 완성은 어려움
- 디테일한 분석이나 데이터 작업은 지루함
- 마감이나 루틴에 스트레스를 많이 받음

**활용 팁**
아티스트, 마케터, 콘텐츠 크리에이터, 브랜드 기획자에 적합합니다. 실행력 강한 파트너와 협업하면 시너지 폭발!""",
                "min_score": 4,
                "max_score": 7,
            },
            {
                "type": "분석가 두뇌",
                "title": "논리적 탐구로 혁신을 만드는 과학자형 사고자",
                "content": """**두뇌 작동 방식**
당신의 두뇌는 논리와 창의성이 공존하는 실험실입니다. 데이터를 철저히 분석하면서도, 기존 방식에 안주하지 않고 새로운 해결책을 찾아냅니다.

**강점**
- 복잡한 문제의 근본 원인을 찾아냄
- 데이터 기반의 혁신적 솔루션 제시
- 논리와 창의를 동시에 활용하는 균형감
- 연구, 개발, 혁신 분야에서 탁월함

**약점**
- 지나친 탐구로 실행이 늦어질 수 있음
- "왜?"를 너무 많이 물어서 주변이 지칠 수도
- 감성적 소통보다 논리적 설득 선호

**활용 팁**
연구원, 데이터 사이언티스트, UX 리서처, 혁신 전략가에 적합합니다. 탐구와 실행의 균형을 맞추는 연습이 필요해요.""",
                "min_score": 8,
                "max_score": 11,
            },
            {
                "type": "발명가 두뇌",
                "title": "영감을 현실로 만드는 창의적 실행자",
                "content": """**두뇌 작동 방식**
당신의 두뇌는 창의성과 실행력이 만난 혁신 공장입니다. 직관적으로 떠오른 아이디어를 그냥 두지 않고, 구체적인 계획으로 만들어 실현시킵니다.

**강점**
- 아이디어를 실제로 만들어내는 실행력
- 창의성과 체계성의 완벽한 조화
- 스타트업, 신사업 개발에 최적화
- 트렌드를 선도하는 혁신가

**약점**
- 지나치게 많은 프로젝트를 동시에 진행
- 디테일한 분석보다 직관에 의존
- "느낌"이 안 좋으면 계획을 갑자기 바꿀 수도

**활용 팁**
스타트업 창업자, 프로덕트 매니저, 혁신 기획자에 적합합니다. 논리형 파트너와 협업하면 성공 확률 UP!""",
                "min_score": 12,
                "max_score": 15,
            },
            {
                "type": "실행가 두뇌",
                "title": "큰 그림을 보며 착실히 실행하는 완성형 인간",
                "content": """**두뇌 작동 방식**
당신의 두뇌는 목표를 향해 착실히 나아가는 내비게이션입니다. 전체 맥락을 이해하고, 논리적으로 우선순위를 정하며, 계획대로 하나씩 체크하며 완성해갑니다.

**강점**
- 프로젝트를 끝까지 완수하는 강력한 실행력
- 팀에서 가장 믿을 수 있는 마무리 담당
- 복잡한 프로젝트도 체계적으로 관리
- 리더십과 책임감이 강함

**약점**
- 새로운 시도나 실험보다 안정적 방법 선호
- 창의적 발상이 필요한 순간에 막힐 수 있음
- 계획이 틀어지면 스트레스 과다

**활용 팁**
오퍼레이션 매니저, 팀 리더, 운영 기획자에 적합합니다. 가끔은 계획 없이 즉흥적으로 살아보는 것도 좋아요.""",
                "min_score": 16,
                "max_score": 19,
            },
            {
                "type": "중재자 두뇌",
                "title": "공감과 조율로 팀을 하나로 만드는 감성 리더",
                "content": """**두뇌 작동 방식**
당신의 두뇌는 사람들의 감정과 상황을 읽는 레이더입니다. 직관적으로 분위기를 파악하고, 전체 맥락 속에서 각자의 입장을 이해하며, 모두가 만족할 수 있는 계획을 조율합니다.

**강점**
- 팀의 분위기를 읽고 갈등을 중재
- 다양한 이해관계를 조율하는 능력
- 감성 리더십으로 팀원들의 신뢰를 얻음
- HR, 팀 빌딩, 협업 프로젝트에 최적

**약점**
- 논리적 분석이나 데이터 작업은 부담
- 모두를 만족시키려다 결정이 늦어질 수 있음
- 갈등 상황에서 스트레스를 많이 받음

**활용 팁**
HR 매니저, 팀 리더, 기획자, 상담사에 적합합니다. 논리적 근거도 함께 제시하면 설득력 UP!""",
                "min_score": 20,
                "max_score": 23,
            },
            {
                "type": "탐험가 두뇌",
                "title": "디테일을 탐구하며 새로운 길을 찾는 모험가",
                "content": """**두뇌 작동 방식**
당신의 두뇌는 끊임없이 새로운 것을 찾아다니는 탐험가입니다. 직관적으로 흥미로운 주제를 발견하면, 디테일하게 파고들어 분석하고, 창의적인 방식으로 재해석합니다.

**강점**
- 아무도 주목하지 않은 인사이트 발견
- 기존 방식을 뒤집는 창의적 솔루션 제시
- 다양한 분야를 넘나드는 융합 사고
- 연구, 혁신, 콘텐츠 개발에 탁월

**약점**
- 흥미가 옮겨가면 프로젝트를 중단할 수도
- 체계적 실행보다 탐구 자체에 집중
- 루틴이나 반복 작업에 극심한 지루함

**활용 팁**
리서처, 콘텐츠 크리에이터, 혁신가, 작가에 적합합니다. 한 가지에 집중하는 연습도 필요해요.""",
                "min_score": 24,
                "max_score": 27,
            },
            {
                "type": "자유영혼 두뇌",
                "title": "감각적 통찰로 전략을 짜는 예민한 기획자",
                "content": """**두뇌 작동 방식**
당신의 두뇌는 직관과 논리가 조화를 이룬 독특한 시스템입니다. 느낌으로 방향을 잡지만, 디테일을 놓치지 않고 분석하며, 체계적인 계획으로 실행합니다.

**강점**
- 직관과 논리를 모두 활용하는 균형감
- 트렌드를 읽고 전략으로 구체화
- 예민한 감각으로 리스크를 사전에 감지
- 기획, 전략, 브랜딩 분야에 최적

**약점**
- 직관과 분석 사이에서 고민이 많음
- 완벽주의로 실행이 늦어질 수 있음
- 너무 많은 변수를 고려해 결정 지연

**활용 팁**
브랜드 전략가, 마케팅 기획자, 트렌드 애널리스트에 적합합니다. 때로는 직관을 믿고 빠르게 결정하는 연습도 필요해요.""",
                "min_score": 28,
                "max_score": 30,
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
        print("✅ 나의 두뇌 유형은? 시드 데이터 생성 완료!")
        print(f"   - 테스트 ID: {test_id}")
        print(f"   - 문항 수: 10개")
        print(f"   - 결과 유형: 8개")

    except Exception as e:
        db.rollback()
        print(f"❌ 두뇌 유형 테스트 시드 실패: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    # 테이블 생성 확인
    Base.metadata.create_all(bind=engine)
    seed_brain_type_test()

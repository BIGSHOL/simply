"""
나의 회의실 생존 유형은? 시드 스크립트
10문항, 8개 결과 유형
실행: python -m scripts.seed_meeting_survival_test
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


def seed_meeting_survival_test():
    """나의 회의실 생존 유형은? 시드 데이터 생성"""
    db = SessionLocal()

    try:
        # 기존 테스트 확인
        existing = db.query(Test).filter(Test.title.contains("회의")).first()
        if existing:
            print("⚠️  회의실 생존 테스트가 이미 존재합니다. 시드 스킵.")
            return

        # 테스트 ID 생성
        test_id = uuid.uuid4()

        # 테스트 생성
        test = Test(
            id=test_id,
            title="나의 회의실 생존 유형은?",
            description="당신의 회의 스타일은? 의견 적극성, 경청 스타일, 시간 민감도 3가지 축으로 당신의 회의실 페르소나를 찾아보세요. 직장인 극공감 테스트!",
            category="career",
            thumbnail_url="/images/tests/meeting-survival.png",
            play_count=18760,
            like_count=1520,
        )
        db.add(test)

        # 10개 문항 (A=0점, B=3점)
        questions_data = [
            {
                "order_num": 1,
                "content": "새로운 프로젝트 회의에서 아이디어 브레인스토밍 시간이 되었다.",
                "choices": [
                    {"order_num": 1, "content": "일단 다른 사람들 의견 듣고, 좋은 아이디어 나오면 거기에 보탤게요", "score": 0},
                    {"order_num": 2, "content": "\"저는 이렇게 해보면 어떨까 싶은데요!\" 먼저 손들고 의견 제시", "score": 3},
                ],
            },
            {
                "order_num": 2,
                "content": "동료가 회의에서 의견을 냈는데, 당신은 살짝 다른 생각이다.",
                "choices": [
                    {"order_num": 1, "content": "\"좋은 의견인데요! 저도 그렇게 생각해요\" (속으로는 글쎄...)", "score": 0},
                    {"order_num": 2, "content": "\"좋은데 이 부분은 이런 문제가 있지 않을까요?\" 논리적으로 반박", "score": 3},
                ],
            },
            {
                "order_num": 3,
                "content": "회의 중 상사가 \"이 건에 대해 의견 있는 사람?\" 하고 물었다.",
                "choices": [
                    {"order_num": 1, "content": "침묵... (누군가 말하겠지, 나는 카메라 끄고 관전)", "score": 0},
                    {"order_num": 2, "content": "\"제가 말씀드려도 될까요?\" 하며 바로 손듭니다", "score": 3},
                ],
            },
            {
                "order_num": 4,
                "content": "30분 회의인데 이미 25분 지났다. 아직 결론이 안 났다.",
                "choices": [
                    {"order_num": 1, "content": "중요한 얘기 중이니까 조금 늦어져도 괜찮아요, 천천히 논의해요", "score": 0},
                    {"order_num": 2, "content": "\"5분 남았는데 일단 결론부터 내고 세부사항은 메신저로 할까요?\"", "score": 3},
                ],
            },
            {
                "order_num": 5,
                "content": "팀장이 제시한 방향에 명백한 논리적 허점이 보인다.",
                "choices": [
                    {"order_num": 1, "content": "팀장님 말씀이니까... 일단 따라가봐요 (나중에 슬랙으로 조심스럽게 제안)", "score": 0},
                    {"order_num": 2, "content": "\"팀장님, 근데 이 부분은 이러이러해서 문제가 있을 것 같은데요?\"", "score": 3},
                ],
            },
            {
                "order_num": 6,
                "content": "정규 회의 시간이 끝났는데 팀원이 \"잠깐만요, 이것만 더 얘기하고 가요\" 한다.",
                "choices": [
                    {"order_num": 1, "content": "\"그래요, 중요한 거면 조금 더 얘기해봐요!\"", "score": 0},
                    {"order_num": 2, "content": "\"중요한 건 알겠는데 다음 회의 때 안건으로 올려요, 지금은 끝내죠\"", "score": 3},
                ],
            },
            {
                "order_num": 7,
                "content": "회의에서 당신이 발언하는 빈도는?",
                "choices": [
                    {"order_num": 1, "content": "딱 필요할 때만, 또는 호명받을 때만 (1시간 회의에 2-3번?)", "score": 0},
                    {"order_num": 2, "content": "할 말 있으면 바로바로! (1시간 회의에 7-8번 이상)", "score": 3},
                ],
            },
            {
                "order_num": 8,
                "content": "후배가 회의에서 실현 불가능해 보이는 아이디어를 열정적으로 발표하고 있다.",
                "choices": [
                    {"order_num": 1, "content": "\"우와 좋은데요! 참신해요!\" (일단 칭찬하고 나중에 현실화 고민)", "score": 0},
                    {"order_num": 2, "content": "\"아이디어는 좋은데 실제로 하려면 이런저런 문제가 있을 것 같은데?\"", "score": 3},
                ],
            },
            {
                "order_num": 9,
                "content": "회의 전날 밤, 당신의 준비 상태는?",
                "choices": [
                    {"order_num": 1, "content": "안건만 슥 읽어보고, 회의 중에 흐름 보면서 의견 정리", "score": 0},
                    {"order_num": 2, "content": "노션에 발표할 의견 정리하고 PPT까지 준비 완료", "score": 3},
                ],
            },
            {
                "order_num": 10,
                "content": "이상적인 회의 시간은?",
                "choices": [
                    {"order_num": 1, "content": "결론이 날 때까지! 30분이든 2시간이든 상관없어요", "score": 0},
                    {"order_num": 2, "content": "30분 안에 끝! 그 이상은 효율 떨어져요, 차라리 나눠서 해요", "score": 3},
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
                "result_type": "조용한 관찰자",
                "result_title": "조용히 있다가 마지막에 \"저도 그렇게 생각합니다\"",
                "result_content": """## 회의실에서의 모습
당신은 회의실에서 가장 조용한 존재감을 자랑해요. 다른 사람들이 열띤 토론을 할 때 당신은 카메라 끄고 듣기만 해요. "OOO님 의견 어떠세요?" 하고 호명되면 "아 네, 저는 좋을 것 같습니다"라고 대답하는 타입.

## 커뮤니케이션 성향
의견 표현보다는 경청을 선호하는 수동적 스타일. 타인 의견에 공감은 하지만 피드백은 최소화. 회의 시간이 길어져도 크게 신경 쓰지 않음.

## 강점
경청 능력이 뛰어나 전체 흐름을 파악함. 중립적 위치에서 객관적 판단 가능.

## 약점
중요한 의견이 있어도 묻히기 쉬움. 참여도가 낮아 보일 수 있음.

💡 작은 의견이라도 먼저 꺼내보는 연습을 해보세요!""",
                "min_score": 0,
                "max_score": 3,
            },
            {
                "result_type": "시간 지킴이",
                "result_title": "시계 보면서 \"30분 남았는데요...\" 라고 쿡쿡 찌르는 스타일",
                "result_content": """## 회의실에서의 모습
당신은 회의 시작 1분 전부터 줌 대기실에 서 있는 사람이에요. 회의가 길어지면 노트북 시계를 째려보고, "저희 30분 남았는데 다음 안건 넘어가실까요?"라고 슬쩍 압박하는 타입.

## 커뮤니케이션 성향
발언은 적지만 시간 관리에는 민감. 불필요한 대화보다 핵심만 빠르게 처리. 효율성을 최우선 가치로 생각.

## 강점
회의가 산으로 가는 걸 막아주는 타임키퍼. 시간 내 결론 도출을 독려.

## 약점
충분한 논의 전에 서두르는 것처럼 보일 수 있음.

💡 가끔은 여유롭게 아이디어를 나누는 시간도 필요해요!""",
                "min_score": 4,
                "max_score": 7,
            },
            {
                "result_type": "돌직구 리뷰어",
                "result_title": "조용하다가 갑자기 \"근데 그거 문제 있지 않아요?\"",
                "result_content": """## 회의실에서의 모습
평소엔 조용히 듣고만 있다가, 뭔가 이상하다 싶으면 "잠깐만요, 그 논리는 모순 아닌가요?"라고 폭탄을 던지는 타입. 다들 좋다고 할 때 혼자 "그런데요..."로 시작하는 발언을 해서 회의를 1시간 연장시키는 주인공.

## 커뮤니케이션 성향
경청하다가 논리적 오류 발견 시 적극 지적. 비판적 사고가 강하고 분석력이 뛰어남. 시간보다 정확성과 완성도를 중시.

## 강점
문제점을 조기에 발견하는 리스크 관리자. 논리적 허점을 찾아내는 예리한 분석력.

## 약점
분위기를 깨는 사람으로 보일 수 있음.

💡 건설적인 피드백 방식을 연습해보세요!""",
                "min_score": 8,
                "max_score": 11,
            },
            {
                "result_type": "무적의 팔로워",
                "result_title": "\"좋은 지적입니다만, 시간이 없으니 일단 진행하죠\"",
                "result_content": """## 회의실에서의 모습
당신은 회의에서 리더는 아니지만, 가장 쓸모 있는 사람이에요. 누군가 문제를 제기하면 "맞는 말씀이긴 한데, 일단 데드라인이 내일이니까 이렇게 가는 게 어떨까요?"라고 현실적인 대안을 제시해요.

## 커뮤니케이션 성향
문제 인식은 하지만 실용적 해결 우선. 시간 내 결론 도출을 최우선으로. 빠른 의사결정과 실행력 중시.

## 강점
현실적이고 실행 가능한 대안 제시. 논쟁을 정리하고 합의점 도출 능력.

## 약점
너무 타협적이라 근본적 문제 해결 놓칠 수 있음.

💡 효율성과 완성도 사이의 균형을 찾으면 더욱 성장할 수 있어요!""",
                "min_score": 12,
                "max_score": 15,
            },
            {
                "result_type": "아이디어 뱅크",
                "result_title": "\"이거 하면 어때요? 저거 하면 어때요?\" 아이디어 폭포수",
                "result_content": """## 회의실에서의 모습
당신은 회의가 시작되면 아이디어가 샘솟는 크리에이터! "이거 어때요?", "이런 것도 해볼까요?", "아 그럼 이건요?" 하면서 10분에 아이디어 다섯 개는 기본으로 쏟아내요.

## 커뮤니케이션 성향
활발한 발언과 창의적 아이디어 제시. 다른 의견에 긍정적으로 반응하며 확장. 시간 제약보다 아이디어 발전에 집중.

## 강점
창의적 아이디어로 새로운 방향 제시. 팀의 창의성과 혁신을 이끔.

## 약점
너무 많은 아이디어로 초점 흐려질 수 있음. 회의 시간이 길어지는 원인 제공.

💡 핵심 아이디어 3개만 정리해서 우선순위를 정해보세요!""",
                "min_score": 16,
                "max_score": 19,
            },
            {
                "result_type": "엔딩요정",
                "result_title": "\"정리하자면 이거, 저거, 그거죠? 다음 회의 때 봐요!\"",
                "result_content": """## 회의실에서의 모습
당신은 회의를 깔끔하게 끝내는 마법사예요. 회의가 산으로 가면 "자, 정리하면 우리가 결정한 건 A, B, C이고 액션아이템은 누가 언제까지죠?"라고 하며 회의를 정리해요.

## 커뮤니케이션 성향
적극적으로 발언하며 회의 방향 제시. 긍정적이지만 효율성 최우선. 시간 관리에 민감하고 결론 중심.

## 강점
회의를 시간 내 마무리하는 능력. 명확한 결론과 액션 아이템 도출. 칼퇴를 가능하게 하는 구세주.

## 약점
성급한 결론으로 충분한 논의 부족 가능. 소수 의견이 묻힐 수 있음.

💡 가끔은 팀원들의 의견을 충분히 들어주는 여유도 필요해요!""",
                "min_score": 20,
                "max_score": 23,
            },
            {
                "result_type": "급발진 토론왕",
                "result_title": "\"그건 아닌 것 같은데요?\" 논쟁의 불씨를 당기는 당신",
                "result_content": """## 회의실에서의 모습
당신은 회의실의 토론 점화기! 누가 의견을 내면 "그건 이런 이유로 문제가 있지 않나요?"라며 즉시 논쟁을 시작해요. 30분 회의를 2시간으로 만드는 주인공. "잠깐, 제 말 좀 들어보세요"가 입버릇이고, 논리적으로 설명하다 보면 PPT를 10장 넘어가요.

## 커뮤니케이션 성향
적극적 발언과 비판적 사고의 결합. 논리적 토론을 즐기고 깊이 파고듦. 시간보다 완벽한 결론 도출 중시.

## 강점
다각도에서 문제를 분석하는 능력. 잘못된 결정을 막는 강력한 제동장치.

## 약점
회의 시간이 과도하게 길어짐. 과한 논쟁으로 팀원 피로도 증가.

💡 "이기는 것"보다 "좋은 결론"이 목표라는 걸 기억하세요!""",
                "min_score": 24,
                "max_score": 27,
            },
            {
                "result_type": "회의록 장인",
                "result_title": "발언도 하고 정리도 하고, 회의의 전지적 참여자 시점",
                "result_content": """## 회의실에서의 모습
당신은 회의의 만능 플레이어! 의견도 적극적으로 내면서 동시에 "잠깐, 지금 OOO님이 말씀하신 거 정리하면 이거죠?"라며 요약까지 해줘요. 노션에 실시간으로 회의록을 작성하면서도 논리적 허점은 놓치지 않고, 시간 관리까지 완벽한 슈퍼맨.

## 커뮤니케이션 성향
적극적 참여와 비판적 사고의 조화. 경청과 발언의 완벽한 밸런스. 시간 관리와 완성도 모두 중시.

## 강점
모든 영역에서 뛰어난 올라운더. 회의의 방향과 결론을 동시에 관리. 누가 봐도 인정하는 회의 MVP.

## 약점
과도한 책임감으로 번아웃 위험. 완벽주의로 스트레스 받을 수 있음.

💡 가끔은 다른 사람에게 역할을 나눠주고 지켜보는 연습을 해보세요!""",
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
        print("✅ 나의 회의실 생존 유형 시드 데이터 생성 완료!")
        print(f"   - 테스트 ID: {test_id}")
        print(f"   - 문항 수: 10개")
        print(f"   - 결과 유형: 8개")

    except Exception as e:
        db.rollback()
        print(f"❌ 회의실 생존 테스트 시드 실패: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    # 테이블 생성 확인
    Base.metadata.create_all(bind=engine)
    seed_meeting_survival_test()

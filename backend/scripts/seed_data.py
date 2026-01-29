"""
시드 데이터 스크립트

로컬 개발 및 테스트용 샘플 데이터 생성
실행: python -m scripts.seed_data
"""
import sys
import os

# Windows 콘솔 UTF-8 출력 설정
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

# 프로젝트 루트를 path에 추가
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.database import Base
from app.models import Test, Question, Choice, ResultType

# SQLite 로컬 DB
DATABASE_URL = "sqlite:///./simly.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def create_tables():
    """테이블 생성"""
    Base.metadata.create_all(bind=engine)
    print("✅ 테이블 생성 완료")


def seed_tests():
    """테스트 데이터 시드"""
    db = SessionLocal()

    try:
        # 기존 데이터 확인
        existing = db.query(Test).count()
        if existing > 0:
            print(f"⚠️  이미 {existing}개의 테스트가 존재합니다. 시드 스킵.")
            return

        # ===== 테스트 1: MBTI 연애 스타일 =====
        test1 = Test(
            title="MBTI로 알아보는 나의 연애 스타일",
            description="당신의 연애 성향을 분석해 드립니다. 5개의 질문에 답하고 나만의 연애 유형을 확인하세요!",
            category="love",
            play_count=15234,
        )
        db.add(test1)
        db.flush()

        # 질문 & 선택지 (점수: 1~4)
        questions1 = [
            {
                "content": "연인과 데이트할 때 선호하는 방식은?",
                "choices": [
                    ("집에서 영화 보기", 1),
                    ("새로운 맛집 탐방", 2),
                    ("야외 활동 (등산, 자전거 등)", 3),
                    ("문화생활 (전시회, 공연 등)", 4),
                ],
            },
            {
                "content": "연인과 갈등이 생겼을 때 나는?",
                "choices": [
                    ("시간을 두고 생각한 뒤 대화한다", 1),
                    ("글로 내 감정을 전달한다", 2),
                    ("상대가 먼저 말할 때까지 기다린다", 3),
                    ("즉시 대화로 해결하려 한다", 4),
                ],
            },
            {
                "content": "이상적인 연인의 조건은?",
                "choices": [
                    ("경제적으로 안정된 사람", 1),
                    ("같은 취미를 공유하는 사람", 2),
                    ("나를 있는 그대로 받아주는 사람", 3),
                    ("대화가 잘 통하는 사람", 4),
                ],
            },
            {
                "content": "연인에게 사랑을 표현하는 방식은?",
                "choices": [
                    ("함께 시간을 보내며 표현한다", 1),
                    ("스킨십으로 표현한다", 2),
                    ("선물이나 서프라이즈로 표현한다", 3),
                    ("말로 직접 표현한다", 4),
                ],
            },
            {
                "content": "연인과의 미래를 생각할 때 중요한 것은?",
                "choices": [
                    ("안정적인 생활 기반", 1),
                    ("가족과의 조화", 2),
                    ("함께하는 즐거운 추억", 3),
                    ("서로의 성장과 발전", 4),
                ],
            },
        ]

        for i, q_data in enumerate(questions1, 1):
            q = Question(test_id=test1.id, order_num=i, content=q_data["content"])
            db.add(q)
            db.flush()
            for j, (text, score) in enumerate(q_data["choices"], 1):
                db.add(Choice(question_id=q.id, order_num=j, content=text, score=score))

        # 결과 유형 (점수 범위: 5~20)
        result_types1 = [
            {
                "min_score": 5, "max_score": 8,
                "result_type": "신중한 안정형",
                "result_title": "당신은 신중하고 안정적인 연애를 추구해요!",
                "result_content": """## 당신의 연애 스타일

**신중한 안정형**은 안정적이고 편안한 관계를 중요시합니다.

### 특징
- 급하게 관계를 발전시키기보다 천천히 알아가는 것을 선호
- 실용적이고 현실적인 관점으로 연애를 바라봄
- 한번 마음을 주면 깊고 오래가는 사랑을 함

### 연애 팁
💡 가끔은 즉흥적인 데이트도 시도해보세요
💡 감정 표현을 조금 더 적극적으로 해보면 좋아요"""
            },
            {
                "min_score": 9, "max_score": 12,
                "result_type": "배려하는 조율형",
                "result_title": "당신은 상대를 배려하며 균형을 맞추는 타입!",
                "result_content": """## 당신의 연애 스타일

**배려하는 조율형**은 상대방의 감정을 잘 읽고 맞춰주는 능력이 뛰어납니다.

### 특징
- 갈등 상황에서 중재자 역할을 잘 함
- 상대의 기분을 잘 파악하고 배려함
- 안정과 열정 사이에서 균형을 찾으려 함

### 연애 팁
💡 자신의 감정도 솔직하게 표현하는 연습을 해보세요
💡 때로는 자신을 위한 시간도 필요해요"""
            },
            {
                "min_score": 13, "max_score": 16,
                "result_type": "감성적인 로맨티스트",
                "result_title": "당신은 감성적이고 로맨틱한 연애를 해요!",
                "result_content": """## 당신의 연애 스타일

**감성적인 로맨티스트**는 사랑에 있어 감정과 분위기를 중요시합니다.

### 특징
- 기념일이나 특별한 날을 챙기는 것을 좋아함
- 연인과 함께하는 추억을 소중히 여김
- 감정 표현이 풍부하고 애정이 넘침

### 연애 팁
💡 현실적인 부분도 함께 고려해보세요
💡 상대방의 표현 방식도 존중해주세요"""
            },
            {
                "min_score": 17, "max_score": 20,
                "result_type": "열정적인 소통형",
                "result_title": "당신은 열정적으로 사랑하고 소통하는 타입!",
                "result_content": """## 당신의 연애 스타일

**열정적인 소통형**은 적극적인 소통과 열정적인 사랑을 추구합니다.

### 특징
- 솔직하고 직접적인 감정 표현
- 연인과의 깊은 대화를 즐김
- 새로운 경험과 도전을 함께하길 원함

### 연애 팁
💡 상대방의 페이스도 존중해주세요
💡 가끔은 조용한 시간도 필요할 수 있어요"""
            },
        ]

        for rt in result_types1:
            db.add(ResultType(test_id=test1.id, **rt))

        # ===== 테스트 2: 직장 유형 =====
        test2 = Test(
            title="직장에서 나는 어떤 유형?",
            description="직장 내 나의 성격과 업무 스타일을 알아보세요.",
            category="career",
            play_count=8765,
        )
        db.add(test2)
        db.flush()

        questions2 = [
            {
                "content": "팀 프로젝트에서 나의 역할은?",
                "choices": [
                    ("실무를 담당하는 실행자", 1),
                    ("팀원들을 조율하는 조정자", 2),
                    ("아이디어를 내는 기획자", 3),
                    ("전체를 이끄는 리더", 4),
                ],
            },
            {
                "content": "업무 중 스트레스를 받으면?",
                "choices": [
                    ("혼자 조용히 정리한다", 1),
                    ("맛있는 음식을 먹는다", 2),
                    ("운동이나 취미로 해소한다", 3),
                    ("동료와 대화로 푼다", 4),
                ],
            },
            {
                "content": "새로운 업무를 맡으면?",
                "choices": [
                    ("관련 자료를 먼저 찾아본다", 1),
                    ("선배나 동료에게 조언을 구한다", 2),
                    ("계획을 세우고 준비한다", 3),
                    ("바로 실행에 옮긴다", 4),
                ],
            },
            {
                "content": "회의에서 나는?",
                "choices": [
                    ("회의 후 서면으로 의견을 전달한다", 1),
                    ("다른 사람의 의견을 정리한다", 2),
                    ("필요할 때만 발언한다", 3),
                    ("적극적으로 의견을 낸다", 4),
                ],
            },
        ]

        for i, q_data in enumerate(questions2, 1):
            q = Question(test_id=test2.id, order_num=i, content=q_data["content"])
            db.add(q)
            db.flush()
            for j, (text, score) in enumerate(q_data["choices"], 1):
                db.add(Choice(question_id=q.id, order_num=j, content=text, score=score))

        # 결과 유형 (점수 범위: 4~16)
        result_types2 = [
            {
                "min_score": 4, "max_score": 7,
                "result_type": "꼼꼼한 실무형",
                "result_title": "당신은 꼼꼼하고 신뢰받는 실무 전문가!",
                "result_content": """## 직장에서의 당신

**꼼꼼한 실무형**은 맡은 일을 정확하게 처리하는 것을 중요시합니다.

### 강점
- 세부사항을 놓치지 않는 꼼꼼함
- 신뢰할 수 있는 업무 처리 능력
- 안정적이고 일관된 성과

### 성장 포인트
💼 가끔은 큰 그림도 봐보세요
💼 의견 표현을 조금 더 적극적으로!"""
            },
            {
                "min_score": 8, "max_score": 11,
                "result_type": "유연한 조율형",
                "result_title": "당신은 팀의 분위기 메이커이자 조정자!",
                "result_content": """## 직장에서의 당신

**유연한 조율형**은 팀 내 갈등을 중재하고 협력을 이끌어냅니다.

### 강점
- 뛰어난 대인관계 능력
- 다양한 의견을 조율하는 능력
- 팀 분위기를 긍정적으로 만듦

### 성장 포인트
💼 자신의 의견도 명확히 주장해보세요
💼 업무 전문성도 함께 키워보세요"""
            },
            {
                "min_score": 12, "max_score": 16,
                "result_type": "추진력 있는 리더형",
                "result_title": "당신은 목표를 향해 달리는 리더!",
                "result_content": """## 직장에서의 당신

**추진력 있는 리더형**은 목표를 설정하고 팀을 이끄는 능력이 뛰어납니다.

### 강점
- 강한 추진력과 실행력
- 명확한 방향 제시
- 도전을 두려워하지 않는 자세

### 성장 포인트
💼 팀원들의 페이스도 고려해주세요
💼 경청하는 리더십도 중요해요"""
            },
        ]

        for rt in result_types2:
            db.add(ResultType(test_id=test2.id, **rt))

        db.commit()
        print("✅ 시드 데이터 생성 완료")
        print(f"   - 테스트 2개")
        print(f"   - 질문 9개 (점수 포함)")
        print(f"   - 결과 유형 7개")

    except Exception as e:
        db.rollback()
        print(f"❌ 오류 발생: {e}")
        raise
    finally:
        db.close()


def main():
    print("🌱 Simly 시드 데이터 생성 시작...")
    create_tables()
    seed_tests()
    print("🎉 완료!")


if __name__ == "__main__":
    main()

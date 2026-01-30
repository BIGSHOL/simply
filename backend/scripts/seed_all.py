"""
모든 테스트 시드 데이터 한번에 실행

실행: python -m scripts.seed_all
옵션: python -m scripts.seed_all --reset  (DB 초기화 후 시드)

등록된 테스트 목록 (20개):
[성격 카테고리]
 1. 동물 성격 테스트 - seed_animal_test
 2. 색깔 성격 테스트 - seed_color_personality_test
 3. 곤충 테스트 (32종) - seed_insect_test
 4. 두뇌 유형 테스트 - seed_brain_type_test
 5. 음식 성격 테스트 - seed_food_test

[연애 카테고리]
 6. MBTI 연애 테스트 - seed_mbti_love_test
 7. 연애 유형 테스트 - seed_love_test
 8. 플러팅 스타일 테스트 - seed_flirting_style_test
 9. 이별 회복 테스트 - seed_breakup_recovery_test
10. 전생 러브스토리 테스트 - seed_past_life_love_test

[직장 카테고리]
11. 직장 계급 테스트 - seed_rank_test
12. 직장 유형 테스트 - seed_workplace_test
13. 회의실 생존 테스트 - seed_meeting_survival_test
14. 퇴사 후 부캐 테스트 - seed_side_hustle_test
15. 월급 사용 유형 테스트 - seed_salary_spending_test

[재미 카테고리]
16. 아재력 테스트 - seed_uncle_test
17. 무인도 생존 테스트 - seed_island_survival_test
18. 좀비 생존 테스트 - seed_zombie_survival_test
19. 조선시대 환생 테스트 - seed_joseon_rebirth_test
20. 오늘의 운세 테스트 - seed_fortune_type_test
"""
import sys
import os
import argparse

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BACKEND_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BACKEND_DIR)


def reset_database():
    """데이터베이스 초기화 후 재생성 (SQLite + PostgreSQL 모두 지원)"""
    from app.core.database import engine, Base
    from app.models import Test, Question, Choice, ResultType

    db_url = str(engine.url)
    if "sqlite" in db_url:
        db_path = os.path.join(BACKEND_DIR, "simly.db")
        if os.path.exists(db_path):
            os.remove(db_path)
            print("🗑️  기존 SQLite 데이터베이스 삭제 완료")
    else:
        print("🗑️  기존 테이블 삭제 중... (PostgreSQL)")
        Base.metadata.drop_all(bind=engine)
        print("🗑️  기존 테이블 삭제 완료")

    Base.metadata.create_all(bind=engine)
    print("✅ 새 데이터베이스 테이블 생성 완료")


def seed_all_tests(reset: bool = False):
    """모든 테스트 시드 실행"""
    print("\n" + "=" * 50)
    print("🚀 Simly 테스트 시드 데이터 생성 시작")
    print("=" * 50 + "\n")

    if reset:
        reset_database()
        print()
    else:
        # reset 안하면 테이블만 생성 확인
        from app.core.database import engine, Base
        from app.models import Test, Question, Choice, ResultType
        Base.metadata.create_all(bind=engine)

    # 기존 시드 함수 임포트
    from scripts.seed_rank_test import seed_rank_test
    from scripts.seed_animal_test import seed_animal_test
    from scripts.seed_insect_test import seed_insect_test
    from scripts.seed_food_test import seed_food_test
    from scripts.seed_mbti_love_test import seed_mbti_love_test
    from scripts.seed_workplace_test import seed_workplace_test
    from scripts.seed_love_test import seed_love_test
    from scripts.seed_uncle_test import seed_uncle_test

    # 신규 시드 함수 임포트 (12개)
    from scripts.seed_color_personality_test import seed_color_personality_test
    from scripts.seed_brain_type_test import seed_brain_type_test
    from scripts.seed_flirting_style_test import seed_flirting_style_test
    from scripts.seed_breakup_recovery_test import seed_breakup_recovery_test
    from scripts.seed_past_life_love_test import seed_past_life_love_test
    from scripts.seed_meeting_survival_test import seed_meeting_survival_test
    from scripts.seed_side_hustle_test import seed_side_hustle_test
    from scripts.seed_salary_spending_test import seed_salary_spending_test
    from scripts.seed_island_survival_test import seed_island_survival_test
    from scripts.seed_zombie_survival_test import seed_zombie_survival_test
    from scripts.seed_joseon_rebirth_test import seed_joseon_rebirth_test
    from scripts.seed_fortune_type_test import seed_fortune_type_test

    # 순서대로 시드 실행 (카테고리별)
    seeds = [
        # 성격 카테고리
        ("동물 성격 테스트", seed_animal_test),
        ("색깔 성격 테스트", seed_color_personality_test),
        ("곤충 테스트", seed_insect_test),
        ("두뇌 유형 테스트", seed_brain_type_test),
        ("음식 성격 테스트", seed_food_test),
        # 연애 카테고리
        ("MBTI 연애 테스트", seed_mbti_love_test),
        ("연애 유형 테스트", seed_love_test),
        ("플러팅 스타일 테스트", seed_flirting_style_test),
        ("이별 회복 테스트", seed_breakup_recovery_test),
        ("전생 러브스토리 테스트", seed_past_life_love_test),
        # 직장 카테고리
        ("직장 계급 테스트", seed_rank_test),
        ("직장 유형 테스트", seed_workplace_test),
        ("회의실 생존 테스트", seed_meeting_survival_test),
        ("퇴사 후 부캐 테스트", seed_side_hustle_test),
        ("월급 사용 유형 테스트", seed_salary_spending_test),
        # 재미 카테고리
        ("아재력 테스트", seed_uncle_test),
        ("무인도 생존 테스트", seed_island_survival_test),
        ("좀비 생존 테스트", seed_zombie_survival_test),
        ("조선시대 환생 테스트", seed_joseon_rebirth_test),
        ("오늘의 운세 테스트", seed_fortune_type_test),
    ]

    success_count = 0
    for name, seed_func in seeds:
        try:
            print(f"\n📌 {name} 시드 실행...")
            seed_func()
            success_count += 1
        except Exception as e:
            print(f"❌ {name} 시드 실패: {e}")

    print("\n" + "=" * 50)
    print(f"🎉 시드 완료! ({success_count}/{len(seeds)} 성공)")
    print("=" * 50 + "\n")

    # 최종 테스트 목록 출력
    try:
        from app.core.database import SessionLocal
        from app.models import Test
        db = SessionLocal()
        tests = db.query(Test).all()
        print(f"📋 현재 등록된 테스트 ({len(tests)}개):")
        for t in tests:
            q_count = len(t.questions) if t.questions else 0
            r_count = len(t.result_types) if t.result_types else 0
            print(f"   [{t.id}] {t.title} (문항:{q_count}, 결과:{r_count})")
        db.close()
    except Exception as e:
        print(f"테스트 목록 조회 실패: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simly 테스트 시드 데이터 생성")
    parser.add_argument("--reset", action="store_true", help="DB 초기화 후 시드")
    args = parser.parse_args()

    seed_all_tests(reset=args.reset)

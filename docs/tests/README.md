# Simly 심리테스트 마스터 목록

> 카테고리별 5개, 총 20개 테스트
> 기존 8개 + 신규 12개

---

## personality (성격) - 5개

| # | ID | 제목 | 시드 파일 | 콘텐츠 설계 | 상태 |
|---|-----|------|----------|------------|------|
| 1 | `food-personality` | 당신을 음식으로 표현하면? 🍕 | seed_food_test.py | - | 완료 |
| 2 | `insect-type` | 곤충으로 환생한다면 당신은? 🦋 | seed_insect_test.py | - | 완료 |
| 3 | `animal-type` | 내 안에 잠든 야생 동물은? 🦊 | seed_animal_test.py | - | 완료 |
| 4 | `color-personality` | 나를 색깔로 표현하면? 🎨 | - | `color-personality/content.md` | **콘텐츠 완료** |
| 5 | `brain-type` | 나의 두뇌 유형은? 🧠 | - | `brain-type/content.md` | **제작 중** |

---

## love (연애) - 5개

| # | ID | 제목 | 시드 파일 | 콘텐츠 설계 | 상태 |
|---|-----|------|----------|------------|------|
| 1 | `mbti-love-type` | 연애할 때 진짜 내 모습은? 💕 | seed_mbti_love_test.py | - | 완료 |
| 2 | `love-type` | 나의 연애 유형은? 💘 | seed_love_test.py | `love-type/content.md` | 완료 |
| 3 | `past-life-love` | 전생에 나의 러브스토리는? 🏰 | - | `past-life-love/content.md` | **제작 중** |
| 4 | `breakup-recovery` | 이별 후 나의 회복 유형은? 💔 | - | `breakup-recovery/content.md` | **제작 중** |
| 5 | `flirting-style` | 나의 플러팅 스타일은? 😏 | - | `flirting-style/content.md` | **제작 중** |

---

## career (직장/커리어) - 5개

| # | ID | 제목 | 시드 파일 | 콘텐츠 설계 | 상태 |
|---|-----|------|----------|------------|------|
| 1 | `rank-type` | 야근 중인데 테스트나 할까... 내 직장 계급은? | seed_rank_test.py | - | 완료 |
| 2 | `workplace-type` | 회사에서 나는 무슨 캐릭터? 💼 | seed_workplace_test.py | - | 완료 |
| 3 | `side-hustle` | 퇴사 후 나에게 맞는 부캐는? 🚀 | - | `side-hustle/content.md` | **제작 중** |
| 4 | `meeting-survival` | 나의 회의실 생존 유형은? 🗣️ | - | `meeting-survival/content.md` | **제작 중** |
| 5 | `salary-spending` | 나의 월급 사용 유형은? 💰 | - | `salary-spending/content.md` | **제작 중** |

---

## fun (재미) - 5개

| # | ID | 제목 | 시드 파일 | 콘텐츠 설계 | 상태 |
|---|-----|------|----------|------------|------|
| 1 | `ajae-type` | 아재 아니라고요? (확인 좀 해볼게요 ㅎㅎ) | seed_uncle_test.py | `uncle-power/content.md` | 완료 |
| 2 | `zombie-survival` | 좀비 아포칼립스 생존 유형 🧟 | - | `zombie-survival/content.md` | **제작 중** |
| 3 | `island-survival` | 무인도 생존 유형 🏝️ | - | `island-survival/content.md` | **콘텐츠 완료** |
| 4 | `joseon-rebirth` | 조선시대 환생하면 나의 신분은? 👘 | - | `joseon-rebirth/content.md` | **제작 중** |
| 5 | `fortune-type` | 오늘의 운세 테스트 🔮 | - | `fortune-type/content.md` | **제작 중** |

---

## 요약

| 상태 | 수량 |
|------|------|
| 완료 (시드 데이터 존재) | 8개 |
| **콘텐츠 설계 완료** | **2개** |
| **제작 중** | **10개** |
| **총합** | **20개** |

> **참고**: `seed_data.py`의 기본 테스트 2개(연애 스타일 4유형, 직장 유형 3유형)는
> 결과 유형이 적고 다른 테스트와 겹치므로 마스터 목록에서 제외됨

---

## 신규 테스트 제작 순서

| 순서 | ID | 제목 | 카테고리 | 상태 |
|------|-----|------|---------|------|
| 1 | `color-personality` | 나를 색깔로 표현하면? 🎨 | personality | 콘텐츠 완료 |
| 2 | `island-survival` | 무인도 생존 유형 🏝️ | fun | 콘텐츠 완료 |
| 3 | `past-life-love` | 전생에 나의 러브스토리는? 🏰 | love | 제작 중 |
| 4 | `joseon-rebirth` | 조선시대 환생하면 나의 신분은? 👘 | fun | 제작 중 |
| 5 | `zombie-survival` | 좀비 아포칼립스 생존 유형 🧟 | fun | 제작 중 |
| 6 | `breakup-recovery` | 이별 후 나의 회복 유형은? 💔 | love | 제작 중 |
| 7 | `side-hustle` | 퇴사 후 나에게 맞는 부캐는? 🚀 | career | 제작 중 |
| 8 | `meeting-survival` | 나의 회의실 생존 유형은? 🗣️ | career | 제작 중 |
| 9 | `flirting-style` | 나의 플러팅 스타일은? 😏 | love | 제작 중 |
| 10 | `brain-type` | 나의 두뇌 유형은? 🧠 | personality | 제작 중 |
| 11 | `salary-spending` | 나의 월급 사용 유형은? 💰 | career | 제작 중 |
| 12 | `fortune-type` | 오늘의 운세 테스트 🔮 | fun | 제작 중 |

---

## 콘텐츠 설계 공통 구조

각 테스트의 `content.md`는 다음 구조를 따릅니다:

1. **심리학적 프레임워크** - 이론적 배경, 측정 차원 3축, 유형 분류 원리
2. **결과 유형 8개** - 3축 H/L 조합, 유형명, 상세 결과 텍스트
3. **문항 10개** - A/B 이지선다, 차원별 배분
4. **점수 산출 로직** - 차원별 합산, H/L 기준선, 유형 결정

---
description: 새로운 심리테스트를 기획부터 구현까지 전체 워크플로우로 생성합니다. "테스트 만들어줘", "심리테스트 생성", "새 테스트 기획" 등에 반응.
---

# 심리테스트 생성 워크플로우

사용자가 새로운 심리테스트를 만들고 싶어합니다.

## 입력 정보

사용자 요청: $ARGUMENTS

---

## 실행 단계

### 1단계: 요구사항 파악

사용자에게 다음 정보를 확인하세요 (없는 경우):

1. **테스트 주제** (예: 연애 유형, MBTI 밈, 직장인 스트레스)
2. **타겟 사용자** (예: 20대 여성, MZ 직장인)
3. **결과 유형 개수** (권장: 4~8개)
4. **문항 수** (권장: 8~12개)
5. **톤앤매너** (예: 재치있고 위트있는, 진지하고 통찰력 있는)

---

### 2단계: 전문가 에이전트 순차 호출

다음 순서로 Task 도구를 사용하여 전문가 에이전트를 호출합니다:

#### 2-1. 콘텐츠 설계 (psychology-content-specialist)

```
Task(
  subagent_type: "psychology-content-specialist",
  description: "심리테스트 콘텐츠 설계",
  prompt: """
  ## 요청 테스트
  - 주제: {주제}
  - 타겟: {타겟}
  - 결과 유형: {N}개
  - 문항 수: {M}개

  ## 산출물
  1. 심리학적 근거가 있는 테스트 기획서
  2. 전체 문항 목록 (역문항 포함)
  3. 결과 유형별 상세 설명
  4. 점수 체계 및 분류 기준
  """
)
```

#### 2-2. 결과 분석 로직 (result-analysis-specialist)

```
Task(
  subagent_type: "result-analysis-specialist",
  description: "결과 분석 로직 설계",
  prompt: """
  ## 입력
  - 콘텐츠 설계 결과 참조

  ## 산출물
  1. 점수 계산 알고리즘
  2. 결과 분류 로직
  3. AI 결과 생성 프롬프트
  4. 테스트 케이스
  """
)
```

#### 2-3. UX 플로우 설계 (ux-flow-specialist)

```
Task(
  subagent_type: "ux-flow-specialist",
  description: "테스트 UX 플로우 설계",
  prompt: """
  ## 입력
  - 테스트 콘텐츠 참조
  - 문항 수: {M}개

  ## 산출물
  1. 사용자 여정 맵
  2. 화면별 와이어프레임
  3. 인터랙션 명세
  4. 컴포넌트 목록
  """
)
```

---

### 3단계: 구현 (Phase 1)

설계 완료 후, 오케스트레이터를 통해 구현 단계로 진입합니다.

```
/orchestrate Phase 1 테스트 구현 - {테스트명}
```

---

## 출력 형식

최종적으로 다음 산출물이 생성되어야 합니다:

```
📁 산출물 체크리스트

□ docs/tests/{test-id}/
  □ content.md - 문항 및 결과 콘텐츠
  □ analysis.md - 분석 로직 설계
  □ ux-flow.md - UX 플로우 설계

□ backend/
  □ app/models/tests/{test_id}.py - 테스트 모델
  □ app/services/tests/{test_id}_service.py - 분석 로직
  □ tests/tests/test_{test_id}.py - 테스트 코드

□ frontend/
  □ src/app/tests/{test-id}/ - 테스트 페이지
  □ src/components/tests/{test-id}/ - 전용 컴포넌트
```

---

## 빠른 시작 예시

사용자가 "연애 유형 테스트 만들어줘"라고 하면:

1. 기본 설정 제안 (10문항, 6개 유형, MZ 감성)
2. 콘텐츠 전문가 호출하여 문항/결과 설계
3. 분석 전문가 호출하여 로직 설계
4. UX 전문가 호출하여 플로우 설계
5. 사용자 승인 후 구현 진행

---

$ARGUMENTS를 분석하여 심리테스트 생성 워크플로우를 시작하세요.

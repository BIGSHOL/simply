# 연애 유형 테스트 - 결과 분석 로직 설계서

> **Version**: 1.0.0
> **Last Updated**: 2025-01-30
> **Author**: Claude Code
> **Reference**: [content.md](./content.md)

---

## 목차

1. [개요](#1-개요)
2. [점수 계산 알고리즘](#2-점수-계산-알고리즘)
3. [유형 분류 알고리즘](#3-유형-분류-알고리즘)
4. [AI 결과 생성 프롬프트](#4-ai-결과-생성-프롬프트)
5. [테스트 케이스](#5-테스트-케이스)

---

## 1. 개요

### 1.1 분석 시스템 아키텍처

```
┌──────────────┐     ┌──────────────────┐     ┌────────────────┐
│  사용자 응답  │ ──▶ │  점수 계산 엔진   │ ──▶ │  유형 분류기    │
│  (20문항)    │     │  (5차원 점수)     │     │  (20개 유형)    │
└──────────────┘     └──────────────────┘     └───────┬────────┘
                                                      │
                                                      ▼
┌──────────────┐     ┌──────────────────┐     ┌────────────────┐
│  최종 결과    │ ◀── │  AI 결과 생성     │ ◀── │  개인화 데이터  │
│  (Result)    │     │  (OpenAI API)    │     │  (점수+유형)    │
└──────────────┘     └──────────────────┘     └────────────────┘
```

### 1.2 핵심 요구사항

- **정확성**: 5개 차원의 정확한 점수 계산
- **일관성**: 동일 응답 -> 동일 유형 분류 보장
- **경계 처리**: 점수 경계선 케이스 명확한 처리
- **확장성**: 향후 유형 추가/수정 용이한 구조

---

## 2. 점수 계산 알고리즘

### 2.1 타입 정의

```typescript
/**
 * 사용자 응답 인터페이스
 */
export interface Answer {
  questionId: number;  // 1-20
  choice: 'A' | 'B';
}

/**
 * 원점수 (Raw Scores) - 차원별 최대값이 다름
 */
export interface RawScores {
  proactivity: number;    // 적극성: 0-10 (5문항 * 2점)
  expression: number;     // 감정표현: 0-8 (4문항 * 2점)
  independence: number;   // 독립성: 0-8 (4문항 * 2점)
  commitment: number;     // 헌신도: 0-6 (3문항 * 2점)
  romance: number;        // 로맨스: 0-8 (4문항 * 2점)
}

/**
 * 정규화 점수 (Normalized Scores) - 모두 0-100 스케일
 */
export interface DimensionScores {
  proactivity: number;    // 적극성 0-100
  expression: number;     // 감정표현 0-100
  independence: number;   // 독립성 0-100
  commitment: number;     // 헌신도 0-100
  romance: number;        // 로맨스 0-100
}
```

### 2.2 문항-차원 매핑 테이블

```typescript
/**
 * 각 문항이 측정하는 차원과 선택지별 점수
 */
export interface QuestionMapping {
  questionId: number;
  dimension: keyof RawScores;
  scoreA: number;  // A 선택 시 점수
  scoreB: number;  // B 선택 시 점수
}

export const QUESTION_MAPPINGS: QuestionMapping[] = [
  // 적극성 문항 (5개)
  { questionId: 1,  dimension: 'proactivity',  scoreA: 2, scoreB: 0 },
  { questionId: 4,  dimension: 'proactivity',  scoreA: 2, scoreB: 0 },
  { questionId: 8,  dimension: 'proactivity',  scoreA: 2, scoreB: 0 },
  { questionId: 12, dimension: 'proactivity',  scoreA: 2, scoreB: 0 },
  { questionId: 17, dimension: 'proactivity',  scoreA: 2, scoreB: 0 },

  // 감정표현 문항 (4개)
  { questionId: 2,  dimension: 'expression',   scoreA: 2, scoreB: 0 },
  { questionId: 5,  dimension: 'expression',   scoreA: 2, scoreB: 0 },
  { questionId: 9,  dimension: 'expression',   scoreA: 2, scoreB: 0 },
  { questionId: 14, dimension: 'expression',   scoreA: 2, scoreB: 0 },

  // 독립성 문항 (4개) - 주의: Q3, Q20은 역코딩
  { questionId: 3,  dimension: 'independence', scoreA: 0, scoreB: 2 },
  { questionId: 7,  dimension: 'independence', scoreA: 2, scoreB: 0 },
  { questionId: 16, dimension: 'independence', scoreA: 2, scoreB: 0 },
  { questionId: 20, dimension: 'independence', scoreA: 0, scoreB: 2 },

  // 헌신도 문항 (3개)
  { questionId: 10, dimension: 'commitment',   scoreA: 2, scoreB: 0 },
  { questionId: 13, dimension: 'commitment',   scoreA: 2, scoreB: 0 },
  { questionId: 18, dimension: 'commitment',   scoreA: 2, scoreB: 0 },

  // 로맨스 문항 (4개)
  { questionId: 6,  dimension: 'romance',      scoreA: 2, scoreB: 0 },
  { questionId: 11, dimension: 'romance',      scoreA: 2, scoreB: 0 },
  { questionId: 15, dimension: 'romance',      scoreA: 2, scoreB: 0 },
  { questionId: 19, dimension: 'romance',      scoreA: 2, scoreB: 0 },
];

/**
 * 차원별 최대 점수 (정규화용)
 */
export const MAX_SCORES: Record<keyof RawScores, number> = {
  proactivity: 10,   // 5문항 * 2점
  expression: 8,     // 4문항 * 2점
  independence: 8,   // 4문항 * 2점
  commitment: 6,     // 3문항 * 2점
  romance: 8,        // 4문항 * 2점
};
```

### 2.3 점수 계산 함수

```typescript
/**
 * 사용자 응답으로부터 원점수를 계산합니다.
 * @param answers - 20개 문항에 대한 응답 배열
 * @returns 5차원 원점수
 */
export function calculateRawScores(answers: Answer[]): RawScores {
  // 초기화
  const rawScores: RawScores = {
    proactivity: 0,
    expression: 0,
    independence: 0,
    commitment: 0,
    romance: 0,
  };

  // 응답을 Map으로 변환 (빠른 조회)
  const answerMap = new Map<number, 'A' | 'B'>();
  for (const answer of answers) {
    answerMap.set(answer.questionId, answer.choice);
  }

  // 각 문항의 점수 합산
  for (const mapping of QUESTION_MAPPINGS) {
    const choice = answerMap.get(mapping.questionId);
    if (choice === undefined) {
      // 응답이 없는 경우 해당 문항 건너뜀
      console.warn(`Missing answer for question ${mapping.questionId}`);
      continue;
    }

    const score = choice === 'A' ? mapping.scoreA : mapping.scoreB;
    rawScores[mapping.dimension] += score;
  }

  return rawScores;
}

/**
 * 원점수를 0-100 스케일로 정규화합니다.
 * @param rawScores - 원점수
 * @returns 정규화된 점수 (0-100)
 */
export function normalizeScores(rawScores: RawScores): DimensionScores {
  return {
    proactivity: Math.round((rawScores.proactivity / MAX_SCORES.proactivity) * 100),
    expression: Math.round((rawScores.expression / MAX_SCORES.expression) * 100),
    independence: Math.round((rawScores.independence / MAX_SCORES.independence) * 100),
    commitment: Math.round((rawScores.commitment / MAX_SCORES.commitment) * 100),
    romance: Math.round((rawScores.romance / MAX_SCORES.romance) * 100),
  };
}

/**
 * 통합 점수 계산 함수
 * @param answers - 사용자 응답 배열
 * @returns 정규화된 5차원 점수
 */
export function calculateScores(answers: Answer[]): DimensionScores {
  const rawScores = calculateRawScores(answers);
  return normalizeScores(rawScores);
}
```

### 2.4 점수 검증 함수

```typescript
/**
 * 응답 배열의 유효성을 검증합니다.
 * @param answers - 검증할 응답 배열
 * @returns 유효성 검증 결과
 */
export interface ValidationResult {
  isValid: boolean;
  errors: string[];
  warnings: string[];
}

export function validateAnswers(answers: Answer[]): ValidationResult {
  const errors: string[] = [];
  const warnings: string[] = [];
  const seenQuestionIds = new Set<number>();

  // 응답 개수 체크
  if (answers.length !== 20) {
    if (answers.length < 20) {
      errors.push(`응답이 부족합니다. 현재 ${answers.length}개, 필요 20개`);
    } else {
      warnings.push(`응답이 초과되었습니다. 현재 ${answers.length}개`);
    }
  }

  // 각 응답 검증
  for (const answer of answers) {
    // 문항 ID 범위 체크
    if (answer.questionId < 1 || answer.questionId > 20) {
      errors.push(`유효하지 않은 문항 ID: ${answer.questionId}`);
      continue;
    }

    // 중복 응답 체크
    if (seenQuestionIds.has(answer.questionId)) {
      warnings.push(`중복 응답: 문항 ${answer.questionId}`);
    }
    seenQuestionIds.add(answer.questionId);

    // 선택지 유효성 체크
    if (answer.choice !== 'A' && answer.choice !== 'B') {
      errors.push(`유효하지 않은 선택지: 문항 ${answer.questionId}, 선택: ${answer.choice}`);
    }
  }

  // 누락된 문항 체크
  for (let i = 1; i <= 20; i++) {
    if (!seenQuestionIds.has(i)) {
      errors.push(`누락된 응답: 문항 ${i}`);
    }
  }

  return {
    isValid: errors.length === 0,
    errors,
    warnings,
  };
}
```

---

## 3. 유형 분류 알고리즘

### 3.1 유형 정의

```typescript
/**
 * 20개 연애 유형 정의
 */
export type LoveType =
  | 'straight_shooter'     // 01. 직진 러버
  | 'push_pull_master'     // 02. 밀당 장인
  | 'romance_express'      // 03. 로맨틱 폭주기관차
  | 'tsundere_expert'      // 04. 츤데레 마스터
  | 'emotion_translator'   // 05. 감정번역가
  | 'thrill_collector'     // 06. 설렘 수집가
  | 'steady_lover'         // 07. 안정 추구형 연인
  | 'free_spirit'          // 08. 자유영혼 연인
  | 'devoted_partner'      // 09. 헌신형 파트너
  | 'independent_lover'    // 10. 독립형 연애러
  | 'touch_fairy'          // 11. 스킨십 요정
  | 'sweet_talker'         // 12. 말로 하는 사랑꾼
  | 'honest_lover'         // 13. 팩폭 애정러
  | 'mood_creator'         // 14. 로맨틱 무드메이커
  | 'long_distance_pro'    // 15. 장거리 전문가
  | 'daily_companion'      // 16. 일상 동반자
  | 'slow_burner'          // 17. 슬로우 버너
  | 'careful_observer'     // 18. 신중한 관찰자
  | 'practical_lover'      // 19. 현실주의 연인
  | 'emotional_dreamer';   // 20. 감성 몽글러

/**
 * 유형 메타데이터
 */
export interface LoveTypeMetadata {
  id: LoveType;
  code: string;           // "01" ~ "20"
  name: string;           // 한글 유형명
  englishName: string;    // 영문 유형명
  subtitle: string;       // 한줄 설명
  emoji: string;          // 대표 이모지
  hashtags: string[];     // SNS 해시태그
  compatibleTypes: LoveType[];  // 궁합 유형
}

export const LOVE_TYPE_METADATA: Record<LoveType, LoveTypeMetadata> = {
  straight_shooter: {
    id: 'straight_shooter',
    code: '01',
    name: '직진 러버',
    englishName: 'Straight Shooter',
    subtitle: '좋으면 좋다고, 눈빛으로 이미 고백 완료',
    emoji: '🚀',
    hashtags: ['#직진본능', '#솔직한게매력', '#기다림은나의적'],
    compatibleTypes: ['thrill_collector', 'mood_creator'],
  },
  push_pull_master: {
    id: 'push_pull_master',
    code: '02',
    name: '밀당 장인',
    englishName: 'Push & Pull Master',
    subtitle: '밀고 당기기의 예술, 연애 심리전의 프로',
    emoji: '🎭',
    hashtags: ['#밀당마스터', '#연애심리전', '#궁금증유발러'],
    compatibleTypes: ['straight_shooter', 'romance_express'],
  },
  romance_express: {
    id: 'romance_express',
    code: '03',
    name: '로맨틱 폭주기관차',
    englishName: 'Romance Express',
    subtitle: '사랑 앞에선 브레이크 따윈 없다',
    emoji: '🚂',
    hashtags: ['#로맨틱폭주', '#이벤트장인', '#사랑표현1등'],
    compatibleTypes: ['thrill_collector', 'touch_fairy'],
  },
  tsundere_expert: {
    id: 'tsundere_expert',
    code: '04',
    name: '츤데레 마스터',
    englishName: 'Tsundere Expert',
    subtitle: '입으론 퉁퉁, 마음은 콩닥콩닥',
    emoji: '😤',
    hashtags: ['#츤데레모먼트', '#행동으로증명', '#알면알수록'],
    compatibleTypes: ['straight_shooter', 'emotion_translator'],
  },
  emotion_translator: {
    id: 'emotion_translator',
    code: '05',
    name: '감정번역가',
    englishName: 'Emotion Translator',
    subtitle: '네 마음 내가 다 알아, 말 안 해도',
    emoji: '🔮',
    hashtags: ['#공감력만렙', '#감정읽기전문', '#네마음내마음'],
    compatibleTypes: ['tsundere_expert', 'steady_lover'],
  },
  thrill_collector: {
    id: 'thrill_collector',
    code: '06',
    name: '설렘 수집가',
    englishName: 'Thrill Collector',
    subtitle: '심장 뛰는 순간이 사는 이유',
    emoji: '✨',
    hashtags: ['#설렘덕후', '#심쿵모먼트', '#짜릿한연애'],
    compatibleTypes: ['romance_express', 'free_spirit'],
  },
  steady_lover: {
    id: 'steady_lover',
    code: '07',
    name: '안정 추구형 연인',
    englishName: 'Steady Lover',
    subtitle: '요란한 불꽃보다 오래가는 촛불이 좋아',
    emoji: '🕯️',
    hashtags: ['#안정이최고', '#루틴연애', '#편안한사랑'],
    compatibleTypes: ['emotion_translator', 'devoted_partner'],
  },
  free_spirit: {
    id: 'free_spirit',
    code: '08',
    name: '자유영혼 연인',
    englishName: 'Free Spirit',
    subtitle: '사랑해도 내 하늘은 지켜야 해',
    emoji: '🦋',
    hashtags: ['#자유로운연애', '#나도중요', '#건강한거리두기'],
    compatibleTypes: ['independent_lover', 'push_pull_master'],
  },
  devoted_partner: {
    id: 'devoted_partner',
    code: '09',
    name: '헌신형 파트너',
    englishName: 'Devoted Partner',
    subtitle: '네가 행복하면 나도 행복해',
    emoji: '🤲',
    hashtags: ['#헌신적인사랑', '#네가중심', '#사랑에올인'],
    compatibleTypes: ['steady_lover', 'emotion_translator'],
  },
  independent_lover: {
    id: 'independent_lover',
    code: '10',
    name: '독립형 연애러',
    englishName: 'Independent Lover',
    subtitle: '연애해도 나는 나, 너는 너',
    emoji: '🏔️',
    hashtags: ['#독립적연애', '#나다움지키기', '#함께하지만각자'],
    compatibleTypes: ['free_spirit', 'honest_lover'],
  },
  touch_fairy: {
    id: 'touch_fairy',
    code: '11',
    name: '스킨십 요정',
    englishName: 'Touch Fairy',
    subtitle: '사랑은 말보다 손끝에서 느껴지는 것',
    emoji: '🤗',
    hashtags: ['#스킨십러버', '#포옹이좋아', '#터치로전하는사랑'],
    compatibleTypes: ['romance_express', 'devoted_partner'],
  },
  sweet_talker: {
    id: 'sweet_talker',
    code: '12',
    name: '말로 하는 사랑꾼',
    englishName: 'Sweet Talker',
    subtitle: '매일 사랑한다 말해도 부족해',
    emoji: '💬',
    hashtags: ['#달달한연애', '#말로하는사랑', '#연애말모이'],
    compatibleTypes: ['tsundere_expert', 'emotion_translator'],
  },
  honest_lover: {
    id: 'honest_lover',
    code: '13',
    name: '팩폭 애정러',
    englishName: 'Honest Lover',
    subtitle: '진짜 사랑은 솔직함에서 시작돼',
    emoji: '📢',
    hashtags: ['#솔직한게매력', '#팩트폭행', '#진짜를원해'],
    compatibleTypes: ['independent_lover', 'free_spirit'],
  },
  mood_creator: {
    id: 'mood_creator',
    code: '14',
    name: '로맨틱 무드메이커',
    englishName: 'Mood Creator',
    subtitle: '분위기 만드는 건 내가 책임질게',
    emoji: '🌙',
    hashtags: ['#무드메이커', '#데이트장인', '#분위기장인'],
    compatibleTypes: ['straight_shooter', 'thrill_collector'],
  },
  long_distance_pro: {
    id: 'long_distance_pro',
    code: '15',
    name: '장거리 전문가',
    englishName: 'Long Distance Pro',
    subtitle: '거리가 뭐예요, 마음이 가까우면 됐지',
    emoji: '✈️',
    hashtags: ['#장거리연애', '#마음의거리', '#신뢰가바탕'],
    compatibleTypes: ['free_spirit', 'steady_lover'],
  },
  daily_companion: {
    id: 'daily_companion',
    code: '16',
    name: '일상 동반자',
    englishName: 'Daily Companion',
    subtitle: '특별한 이벤트보다 매일의 "밥 먹었어?"가 좋아',
    emoji: '🏠',
    hashtags: ['#일상연애', '#소소한행복', '#평범한게좋아'],
    compatibleTypes: ['steady_lover', 'devoted_partner'],
  },
  slow_burner: {
    id: 'slow_burner',
    code: '17',
    name: '슬로우 버너',
    englishName: 'Slow Burner',
    subtitle: '천천히, 하지만 확실하게 빠져드는 중',
    emoji: '🐢',
    hashtags: ['#슬로우러브', '#천천히깊게', '#스며드는사랑'],
    compatibleTypes: ['push_pull_master', 'steady_lover'],
  },
  careful_observer: {
    id: 'careful_observer',
    code: '18',
    name: '신중한 관찰자',
    englishName: 'Careful Observer',
    subtitle: '좋아하기 전에 일단 분석부터',
    emoji: '🔍',
    hashtags: ['#신중한연애', '#분석형', '#이성적사랑'],
    compatibleTypes: ['slow_burner', 'steady_lover'],
  },
  practical_lover: {
    id: 'practical_lover',
    code: '19',
    name: '현실주의 연인',
    englishName: 'Practical Lover',
    subtitle: '로맨스보다 우리 미래가 궁금해',
    emoji: '📊',
    hashtags: ['#현실적연애', '#실용주의', '#함께하는미래'],
    compatibleTypes: ['daily_companion', 'devoted_partner'],
  },
  emotional_dreamer: {
    id: 'emotional_dreamer',
    code: '20',
    name: '감성 몽글러',
    englishName: 'Emotional Dreamer',
    subtitle: '눈 마주치면 시작되는 내 머릿속 드라마',
    emoji: '💭',
    hashtags: ['#감성연애', '#몽글몽글', '#드라마같은사랑'],
    compatibleTypes: ['romance_express', 'sweet_talker'],
  },
};
```

### 3.2 유형 분류 규칙

```typescript
/**
 * 유형 분류 규칙 정의
 * 우선순위가 높은 규칙부터 순차적으로 평가
 */
export interface TypeClassificationRule {
  type: LoveType;
  priority: number;  // 낮을수록 높은 우선순위
  conditions: {
    proactivity?: { min?: number; max?: number };
    expression?: { min?: number; max?: number };
    independence?: { min?: number; max?: number };
    commitment?: { min?: number; max?: number };
    romance?: { min?: number; max?: number };
  };
  description: string;
}

export const CLASSIFICATION_RULES: TypeClassificationRule[] = [
  // ========================================
  // 1단계: 극단적 점수 기반 분류 (우선순위 1-20)
  // ========================================

  // 적극성 극단값
  {
    type: 'romance_express',
    priority: 1,
    conditions: {
      proactivity: { min: 80 },
      expression: { min: 63 },
      romance: { min: 63 },
    },
    description: '적극성 HIGH + 감정표현 HIGH + 로맨스 HIGH',
  },
  {
    type: 'straight_shooter',
    priority: 2,
    conditions: {
      proactivity: { min: 80 },
      expression: { min: 63 },
      independence: { max: 50 },
    },
    description: '적극성 HIGH + 감정표현 HIGH + 독립성 LOW/MID',
  },
  {
    type: 'mood_creator',
    priority: 3,
    conditions: {
      proactivity: { min: 80 },
      romance: { min: 63 },
    },
    description: '적극성 HIGH + 로맨스 HIGH',
  },
  {
    type: 'straight_shooter',
    priority: 4,
    conditions: {
      proactivity: { min: 80 },
    },
    description: '적극성 매우 HIGH (기본)',
  },

  // 적극성 매우 낮음
  {
    type: 'careful_observer',
    priority: 5,
    conditions: {
      proactivity: { max: 20 },
      expression: { max: 37 },
      commitment: { min: 50 },
    },
    description: '적극성 LOW + 감정표현 LOW + 헌신도 HIGH',
  },
  {
    type: 'slow_burner',
    priority: 6,
    conditions: {
      proactivity: { max: 20 },
      independence: { min: 38 },
    },
    description: '적극성 LOW + 독립성 MID 이상',
  },
  {
    type: 'slow_burner',
    priority: 7,
    conditions: {
      proactivity: { max: 20 },
    },
    description: '적극성 매우 LOW (기본)',
  },

  // ========================================
  // 2단계: 감정표현 기반 분류 (우선순위 21-40)
  // ========================================

  {
    type: 'sweet_talker',
    priority: 21,
    conditions: {
      expression: { min: 88 },
      romance: { min: 38 },
    },
    description: '감정표현 매우 HIGH + 로맨스 MID 이상',
  },
  {
    type: 'emotion_translator',
    priority: 22,
    conditions: {
      expression: { min: 88 },
      commitment: { min: 50 },
    },
    description: '감정표현 매우 HIGH + 헌신도 HIGH',
  },
  {
    type: 'sweet_talker',
    priority: 23,
    conditions: {
      expression: { min: 88 },
    },
    description: '감정표현 매우 HIGH (기본)',
  },

  // 감정표현 매우 낮음
  {
    type: 'tsundere_expert',
    priority: 24,
    conditions: {
      expression: { max: 25 },
      proactivity: { min: 40 },
    },
    description: '감정표현 LOW + 적극성 MID 이상',
  },
  {
    type: 'honest_lover',
    priority: 25,
    conditions: {
      expression: { max: 25 },
      romance: { max: 37 },
    },
    description: '감정표현 LOW + 로맨스 LOW',
  },
  {
    type: 'tsundere_expert',
    priority: 26,
    conditions: {
      expression: { max: 25 },
    },
    description: '감정표현 매우 LOW (기본)',
  },

  // ========================================
  // 3단계: 독립성 기반 분류 (우선순위 41-60)
  // ========================================

  {
    type: 'free_spirit',
    priority: 41,
    conditions: {
      independence: { min: 88 },
      commitment: { max: 50 },
    },
    description: '독립성 매우 HIGH + 헌신도 LOW/MID',
  },
  {
    type: 'independent_lover',
    priority: 42,
    conditions: {
      independence: { min: 88 },
    },
    description: '독립성 매우 HIGH (기본)',
  },

  // 독립성 매우 낮음
  {
    type: 'devoted_partner',
    priority: 43,
    conditions: {
      independence: { max: 25 },
      commitment: { min: 50 },
    },
    description: '독립성 LOW + 헌신도 HIGH',
  },
  {
    type: 'touch_fairy',
    priority: 44,
    conditions: {
      independence: { max: 25 },
      expression: { min: 50 },
    },
    description: '독립성 LOW + 감정표현 HIGH',
  },
  {
    type: 'devoted_partner',
    priority: 45,
    conditions: {
      independence: { max: 25 },
    },
    description: '독립성 매우 LOW (기본)',
  },

  // ========================================
  // 4단계: 헌신도 기반 분류 (우선순위 61-80)
  // ========================================

  {
    type: 'devoted_partner',
    priority: 61,
    conditions: {
      commitment: { min: 84 },
      romance: { min: 50 },
    },
    description: '헌신도 매우 HIGH + 로맨스 HIGH',
  },
  {
    type: 'practical_lover',
    priority: 62,
    conditions: {
      commitment: { min: 84 },
      romance: { max: 50 },
    },
    description: '헌신도 매우 HIGH + 로맨스 LOW/MID',
  },
  {
    type: 'steady_lover',
    priority: 63,
    conditions: {
      commitment: { min: 84 },
    },
    description: '헌신도 매우 HIGH (기본)',
  },

  // 헌신도 매우 낮음
  {
    type: 'thrill_collector',
    priority: 64,
    conditions: {
      commitment: { max: 33 },
      romance: { min: 50 },
    },
    description: '헌신도 LOW + 로맨스 HIGH',
  },
  {
    type: 'free_spirit',
    priority: 65,
    conditions: {
      commitment: { max: 33 },
    },
    description: '헌신도 LOW (기본)',
  },

  // ========================================
  // 5단계: 로맨스 기반 분류 (우선순위 81-100)
  // ========================================

  {
    type: 'romance_express',
    priority: 81,
    conditions: {
      romance: { min: 88 },
      proactivity: { min: 50 },
    },
    description: '로맨스 매우 HIGH + 적극성 HIGH',
  },
  {
    type: 'emotional_dreamer',
    priority: 82,
    conditions: {
      romance: { min: 88 },
    },
    description: '로맨스 매우 HIGH (기본)',
  },

  // 로맨스 매우 낮음
  {
    type: 'practical_lover',
    priority: 83,
    conditions: {
      romance: { max: 25 },
      independence: { min: 50 },
    },
    description: '로맨스 LOW + 독립성 HIGH',
  },
  {
    type: 'daily_companion',
    priority: 84,
    conditions: {
      romance: { max: 25 },
    },
    description: '로맨스 LOW (기본)',
  },

  // ========================================
  // 6단계: 복합 조합 분류 (우선순위 101-120)
  // ========================================

  {
    type: 'push_pull_master',
    priority: 101,
    conditions: {
      proactivity: { min: 40, max: 80 },
      expression: { max: 50 },
    },
    description: '적극성 MID + 감정표현 LOW/MID',
  },
  {
    type: 'emotional_dreamer',
    priority: 102,
    conditions: {
      proactivity: { max: 50 },
      expression: { min: 50 },
      romance: { min: 50 },
    },
    description: '적극성 LOW/MID + 감정표현 HIGH + 로맨스 HIGH',
  },
  {
    type: 'long_distance_pro',
    priority: 103,
    conditions: {
      independence: { min: 50 },
      commitment: { max: 67 },
    },
    description: '독립성 HIGH + 헌신도 LOW/MID',
  },
  {
    type: 'steady_lover',
    priority: 104,
    conditions: {
      independence: { max: 50 },
      commitment: { min: 50 },
    },
    description: '독립성 LOW/MID + 헌신도 HIGH',
  },
  {
    type: 'daily_companion',
    priority: 105,
    conditions: {
      romance: { max: 50 },
      commitment: { min: 50 },
    },
    description: '로맨스 LOW/MID + 헌신도 HIGH',
  },

  // ========================================
  // 기본값 (우선순위 999)
  // ========================================

  {
    type: 'steady_lover',
    priority: 999,
    conditions: {},
    description: '기본 유형 (어떤 규칙도 매칭되지 않은 경우)',
  },
];
```

### 3.3 유형 분류 함수

```typescript
/**
 * 조건이 점수에 부합하는지 확인합니다.
 */
function matchesCondition(
  value: number,
  condition?: { min?: number; max?: number }
): boolean {
  if (!condition) return true;

  const { min, max } = condition;

  if (min !== undefined && value < min) return false;
  if (max !== undefined && value > max) return false;

  return true;
}

/**
 * 규칙이 점수에 부합하는지 확인합니다.
 */
function matchesRule(
  scores: DimensionScores,
  rule: TypeClassificationRule
): boolean {
  const { conditions } = rule;

  return (
    matchesCondition(scores.proactivity, conditions.proactivity) &&
    matchesCondition(scores.expression, conditions.expression) &&
    matchesCondition(scores.independence, conditions.independence) &&
    matchesCondition(scores.commitment, conditions.commitment) &&
    matchesCondition(scores.romance, conditions.romance)
  );
}

/**
 * 5차원 점수를 기반으로 연애 유형을 분류합니다.
 * @param scores - 정규화된 5차원 점수
 * @returns 분류된 연애 유형
 */
export function classifyType(scores: DimensionScores): LoveType {
  // 규칙을 우선순위 순으로 정렬
  const sortedRules = [...CLASSIFICATION_RULES].sort(
    (a, b) => a.priority - b.priority
  );

  // 첫 번째 매칭 규칙 반환
  for (const rule of sortedRules) {
    if (matchesRule(scores, rule)) {
      return rule.type;
    }
  }

  // 기본값 (이론적으로 도달 불가)
  return 'steady_lover';
}

/**
 * 분류 결과와 함께 디버깅 정보를 반환합니다.
 */
export interface ClassificationResult {
  type: LoveType;
  metadata: LoveTypeMetadata;
  matchedRule: TypeClassificationRule;
  scores: DimensionScores;
  scoresSummary: {
    highest: keyof DimensionScores;
    lowest: keyof DimensionScores;
  };
}

export function classifyTypeWithDetails(
  scores: DimensionScores
): ClassificationResult {
  const sortedRules = [...CLASSIFICATION_RULES].sort(
    (a, b) => a.priority - b.priority
  );

  let matchedRule: TypeClassificationRule | null = null;

  for (const rule of sortedRules) {
    if (matchesRule(scores, rule)) {
      matchedRule = rule;
      break;
    }
  }

  if (!matchedRule) {
    matchedRule = CLASSIFICATION_RULES.find(r => r.priority === 999)!;
  }

  // 최고/최저 점수 차원 찾기
  const dimensions = Object.entries(scores) as [keyof DimensionScores, number][];
  dimensions.sort((a, b) => b[1] - a[1]);

  return {
    type: matchedRule.type,
    metadata: LOVE_TYPE_METADATA[matchedRule.type],
    matchedRule,
    scores,
    scoresSummary: {
      highest: dimensions[0][0],
      lowest: dimensions[dimensions.length - 1][0],
    },
  };
}
```

### 3.4 경계 케이스 처리

```typescript
/**
 * 경계 점수에 대한 타이브레이커 로직
 *
 * 두 유형이 동일한 조건을 만족할 때 우선순위:
 * 1. 가장 특화된 조건을 가진 규칙 우선
 * 2. 동일 특화도일 경우, 낮은 priority 값 우선
 * 3. 모호한 경우 secondary 유형 함께 반환
 */
export interface AmbiguousResult {
  primaryType: LoveType;
  secondaryType?: LoveType;
  confidence: 'high' | 'medium' | 'low';
  boundaryDimensions: (keyof DimensionScores)[];
}

/**
 * 경계값 정의 (50점 기준으로 +/- 10점 범위)
 */
const BOUNDARY_THRESHOLD = 10;

function isBoundaryScore(score: number): boolean {
  const middle = 50;
  return Math.abs(score - middle) <= BOUNDARY_THRESHOLD;
}

export function classifyWithConfidence(
  scores: DimensionScores
): AmbiguousResult {
  const primaryType = classifyType(scores);

  // 경계에 있는 차원 찾기
  const boundaryDimensions: (keyof DimensionScores)[] = [];
  for (const [dim, score] of Object.entries(scores)) {
    if (isBoundaryScore(score)) {
      boundaryDimensions.push(dim as keyof DimensionScores);
    }
  }

  // 신뢰도 계산
  let confidence: 'high' | 'medium' | 'low';
  if (boundaryDimensions.length === 0) {
    confidence = 'high';
  } else if (boundaryDimensions.length <= 2) {
    confidence = 'medium';
  } else {
    confidence = 'low';
  }

  // 경계 케이스에서 대안 유형 찾기
  let secondaryType: LoveType | undefined;

  if (confidence !== 'high' && boundaryDimensions.length > 0) {
    // 첫 번째 경계 차원을 반대로 뒤집어서 테스트
    const altScores = { ...scores };
    const firstBoundary = boundaryDimensions[0];
    altScores[firstBoundary] = scores[firstBoundary] >= 50
      ? scores[firstBoundary] - 20
      : scores[firstBoundary] + 20;

    const altType = classifyType(altScores);
    if (altType !== primaryType) {
      secondaryType = altType;
    }
  }

  return {
    primaryType,
    secondaryType,
    confidence,
    boundaryDimensions,
  };
}
```

---

## 4. AI 결과 생성 프롬프트

### 4.1 시스템 프롬프트

```typescript
export const AI_SYSTEM_PROMPT = `당신은 MZ세대를 위한 연애 유형 심리테스트의 결과 분석 전문가입니다.

## 역할
- 사용자의 연애 유형 테스트 결과를 바탕으로 개인화된 분석 리포트를 작성합니다.
- 심리학적 인사이트를 제공하되, 가볍고 재미있는 톤으로 전달합니다.
- 부정적인 표현을 피하고, 모든 특성을 긍정적이고 건설적으로 해석합니다.

## 응답 언어
- 반드시 한국어로 응답합니다.

## 말투 가이드
- MZ세대가 공감할 수 있는 캐주얼하고 위트있는 말투를 사용합니다.
- 너무 진지하거나 딱딱한 표현을 피합니다.
- 적절한 비유와 은유를 사용합니다.
- 공감을 이끌어내는 표현을 사용합니다 (예: "맞아요!", "인정", "찐이네요")
- 이모지는 적절히 사용하되 과하지 않게 합니다.

## 금지 사항
- 부정적인 평가나 판단 금지
- "문제", "결함", "잘못" 등의 부정적 단어 사용 금지
- 다른 유형과의 비교를 통한 폄하 금지
- 지나친 일반화 금지

## 응답 구조
다음 섹션들을 포함해야 합니다:
1. 인트로 (유형 소개, 2-3문장)
2. 당신의 연애 DNA (핵심 특성 3가지)
3. 연애할 때 이런 모습 (구체적 상황 예시 3개)
4. 이런 점이 매력적이에요 (강점 2-3가지)
5. 이것만 주의하면 완벽! (성장 포인트 1-2가지, 긍정적 표현)
6. 찰떡 궁합 유형 (2-3개 유형과 이유)
7. 오늘의 연애 한마디 (짧고 임팩트 있는 조언)`;
```

### 4.2 사용자 프롬프트 템플릿

```typescript
export interface AIPromptVariables {
  type: LoveType;
  metadata: LoveTypeMetadata;
  scores: DimensionScores;
  scoresSummary: {
    highest: keyof DimensionScores;
    lowest: keyof DimensionScores;
  };
  compatibleTypes: LoveTypeMetadata[];
}

export function generateUserPrompt(variables: AIPromptVariables): string {
  const { type, metadata, scores, scoresSummary, compatibleTypes } = variables;

  const dimensionLabels: Record<keyof DimensionScores, string> = {
    proactivity: '적극성',
    expression: '감정표현',
    independence: '독립성',
    commitment: '헌신도',
    romance: '로맨스',
  };

  const compatibleList = compatibleTypes
    .map(t => `${t.name} (${t.subtitle})`)
    .join(', ');

  return `## 사용자 테스트 결과

### 유형 정보
- 유형 ID: ${type}
- 유형명: ${metadata.name}
- 영문명: ${metadata.englishName}
- 한줄 설명: ${metadata.subtitle}
- 대표 이모지: ${metadata.emoji}

### 차원별 점수 (0-100)
- 적극성: ${scores.proactivity}점
- 감정표현: ${scores.expression}점
- 독립성: ${scores.independence}점
- 헌신도: ${scores.commitment}점
- 로맨스: ${scores.romance}점

### 점수 특성
- 가장 높은 차원: ${dimensionLabels[scoresSummary.highest]} (${scores[scoresSummary.highest]}점)
- 가장 낮은 차원: ${dimensionLabels[scoresSummary.lowest]} (${scores[scoresSummary.lowest]}점)

### 궁합 유형
${compatibleList}

### 해시태그
${metadata.hashtags.join(' ')}

---

위 정보를 바탕으로 개인화된 연애 유형 분석 리포트를 작성해주세요.
응답은 반드시 한국어로 작성하고, 마크다운 형식을 사용해주세요.`;
}
```

### 4.3 OpenAI API 호출 함수

```typescript
import OpenAI from 'openai';

export interface AIResultGeneratorConfig {
  apiKey: string;
  model?: string;
  maxTokens?: number;
  temperature?: number;
}

export async function generateAIResult(
  variables: AIPromptVariables,
  config: AIResultGeneratorConfig
): Promise<string> {
  const openai = new OpenAI({
    apiKey: config.apiKey,
  });

  const userPrompt = generateUserPrompt(variables);

  const response = await openai.chat.completions.create({
    model: config.model || 'gpt-4o',
    messages: [
      { role: 'system', content: AI_SYSTEM_PROMPT },
      { role: 'user', content: userPrompt },
    ],
    max_tokens: config.maxTokens || 2000,
    temperature: config.temperature || 0.7,
  });

  const content = response.choices[0]?.message?.content;

  if (!content) {
    throw new Error('AI response is empty');
  }

  return content;
}
```

### 4.4 결과 캐싱 전략

```typescript
/**
 * 유형별 기본 결과 템플릿 (AI 응답 실패 시 폴백)
 */
export const FALLBACK_RESULTS: Record<LoveType, string> = {
  straight_shooter: `## 🚀 직진 러버

당신은 연애에서 망설임이 없는 **직진 본능**의 소유자예요!

### 당신의 연애 DNA
1. **솔직함이 무기** - 좋으면 좋다고, 싫으면 싫다고 바로 표현해요
2. **행동파** - 생각보다 행동이 먼저! 기회를 놓치는 법이 없어요
3. **당당함** - 자신의 감정에 확신이 있고 표현하는 것을 두려워하지 않아요

### 이런 점이 매력적이에요
- 상대방이 당신의 마음을 헷갈릴 일이 없어요
- 연애의 시작을 빠르게 만들어내는 추진력이 있어요

### 이것만 주의하면 완벽!
상대의 템포에 맞춰 가끔은 여유를 갖는 것도 좋아요.
천천히 가도 목적지는 같으니까요!

### 오늘의 연애 한마디
> "기다림은 미덕이 아니라 기회의 낭비다" - 당신의 연애 철학`,

  // ... (나머지 유형들의 폴백 템플릿도 동일한 형식으로 정의)
  // 지면 관계상 생략, 실제 구현 시 20개 모두 작성 필요

  push_pull_master: `## 🎭 밀당 장인\n\n밀고 당기기의 예술을 아는 당신! 연애 심리전의 프로예요.`,
  romance_express: `## 🚂 로맨틱 폭주기관차\n\n사랑 앞에서 브레이크 따윈 없는 당신! 열정 그 자체예요.`,
  tsundere_expert: `## 😤 츤데레 마스터\n\n입으론 퉁퉁대도 마음은 콩닥콩닥! 알면 알수록 매력적인 당신이에요.`,
  emotion_translator: `## 🔮 감정번역가\n\n말 안 해도 다 아는 당신! 공감 능력 만렙이에요.`,
  thrill_collector: `## ✨ 설렘 수집가\n\n심장 뛰는 순간을 수집하는 당신! 연애의 설렘을 가장 잘 아는 사람이에요.`,
  steady_lover: `## 🕯️ 안정 추구형 연인\n\n요란한 불꽃보다 오래가는 촛불 같은 사랑을 원하는 당신이에요.`,
  free_spirit: `## 🦋 자유영혼 연인\n\n사랑해도 내 하늘은 지키는 당신! 건강한 연애의 정석이에요.`,
  devoted_partner: `## 🤲 헌신형 파트너\n\n네가 행복하면 나도 행복! 따뜻한 사랑의 화신이에요.`,
  independent_lover: `## 🏔️ 독립형 연애러\n\n연애해도 나는 나, 너는 너! 성숙한 연애관의 소유자예요.`,
  touch_fairy: `## 🤗 스킨십 요정\n\n말보다 손끝으로 사랑을 전하는 당신! 따뜻함 그 자체예요.`,
  sweet_talker: `## 💬 말로 하는 사랑꾼\n\n매일 사랑한다 말해도 부족한 당신! 표현력 만점이에요.`,
  honest_lover: `## 📢 팩폭 애정러\n\n진짜 사랑은 솔직함에서! 거짓 없는 사랑의 전문가예요.`,
  mood_creator: `## 🌙 로맨틱 무드메이커\n\n분위기 만드는 건 내가 책임! 데이트의 마법사예요.`,
  long_distance_pro: `## ✈️ 장거리 전문가\n\n거리는 문제가 안 돼요! 마음이 가까우면 되니까요.`,
  daily_companion: `## 🏠 일상 동반자\n\n특별한 것보다 매일의 소소함을 사랑하는 당신이에요.`,
  slow_burner: `## 🐢 슬로우 버너\n\n천천히, 하지만 확실하게! 깊은 사랑을 하는 당신이에요.`,
  careful_observer: `## 🔍 신중한 관찰자\n\n좋아하기 전에 일단 분석! 신중한 사랑의 전문가예요.`,
  practical_lover: `## 📊 현실주의 연인\n\n로맨스도 좋지만 우리 미래가 더 중요! 현실적 사랑의 달인이에요.`,
  emotional_dreamer: `## 💭 감성 몽글러\n\n눈 마주치면 시작되는 내 머릿속 드라마! 감성 충만한 로맨티스트예요.`,
};
```

---

## 5. 테스트 케이스

### 5.1 단위 테스트 - 점수 계산

```typescript
import { describe, it, expect } from 'vitest';
import { calculateScores, validateAnswers } from './scoring';

describe('점수 계산 테스트', () => {
  it('모든 A 선택 시 최대 점수', () => {
    const allAAnswers: Answer[] = Array.from({ length: 20 }, (_, i) => ({
      questionId: i + 1,
      choice: 'A' as const,
    }));

    const scores = calculateScores(allAAnswers);

    // 적극성: Q1,4,8,12,17 -> 모두 A = 10점 -> 100%
    expect(scores.proactivity).toBe(100);
    // 감정표현: Q2,5,9,14 -> 모두 A = 8점 -> 100%
    expect(scores.expression).toBe(100);
    // 독립성: Q3,20은 B가 점수, Q7,16은 A가 점수 -> A선택시 4점 -> 50%
    expect(scores.independence).toBe(50);
    // 헌신도: Q10,13,18 -> 모두 A = 6점 -> 100%
    expect(scores.commitment).toBe(100);
    // 로맨스: Q6,11,15,19 -> 모두 A = 8점 -> 100%
    expect(scores.romance).toBe(100);
  });

  it('모든 B 선택 시 최소/특정 점수', () => {
    const allBAnswers: Answer[] = Array.from({ length: 20 }, (_, i) => ({
      questionId: i + 1,
      choice: 'B' as const,
    }));

    const scores = calculateScores(allBAnswers);

    expect(scores.proactivity).toBe(0);
    expect(scores.expression).toBe(0);
    // 독립성: Q3,20은 B가 점수 -> 4점 -> 50%
    expect(scores.independence).toBe(50);
    expect(scores.commitment).toBe(0);
    expect(scores.romance).toBe(0);
  });

  it('응답 검증 - 유효한 응답', () => {
    const validAnswers: Answer[] = Array.from({ length: 20 }, (_, i) => ({
      questionId: i + 1,
      choice: i % 2 === 0 ? 'A' : 'B',
    }));

    const result = validateAnswers(validAnswers);

    expect(result.isValid).toBe(true);
    expect(result.errors).toHaveLength(0);
  });

  it('응답 검증 - 누락된 응답', () => {
    const incompleteAnswers: Answer[] = Array.from({ length: 18 }, (_, i) => ({
      questionId: i + 1,
      choice: 'A' as const,
    }));

    const result = validateAnswers(incompleteAnswers);

    expect(result.isValid).toBe(false);
    expect(result.errors.length).toBeGreaterThan(0);
  });
});
```

### 5.2 통합 테스트 - 유형 분류

```typescript
describe('유형 분류 테스트', () => {
  // 테스트 케이스 1: 직진 러버
  it('직진 러버 - 적극성/감정표현 HIGH', () => {
    const scores: DimensionScores = {
      proactivity: 100,
      expression: 100,
      independence: 25,
      commitment: 67,
      romance: 50,
    };

    const result = classifyType(scores);
    expect(result).toBe('straight_shooter');
  });

  // 테스트 케이스 2: 슬로우 버너
  it('슬로우 버너 - 적극성 LOW, 독립성 MID', () => {
    const scores: DimensionScores = {
      proactivity: 10,
      expression: 25,
      independence: 75,
      commitment: 33,
      romance: 25,
    };

    const result = classifyType(scores);
    expect(result).toBe('slow_burner');
  });

  // 테스트 케이스 3: 로맨틱 폭주기관차
  it('로맨틱 폭주기관차 - 모든 긍정 차원 HIGH', () => {
    const scores: DimensionScores = {
      proactivity: 100,
      expression: 100,
      independence: 25,
      commitment: 100,
      romance: 100,
    };

    const result = classifyType(scores);
    expect(result).toBe('romance_express');
  });

  // 테스트 케이스 4: 자유영혼 연인
  it('자유영혼 연인 - 독립성 HIGH, 헌신도 LOW', () => {
    const scores: DimensionScores = {
      proactivity: 50,
      expression: 50,
      independence: 100,
      commitment: 17,
      romance: 50,
    };

    const result = classifyType(scores);
    expect(result).toBe('free_spirit');
  });

  // 테스트 케이스 5: 감성 몽글러
  it('감성 몽글러 - 로맨스 HIGH, 적극성 LOW', () => {
    const scores: DimensionScores = {
      proactivity: 30,
      expression: 63,
      independence: 50,
      commitment: 50,
      romance: 100,
    };

    const result = classifyType(scores);
    expect(result).toBe('emotional_dreamer');
  });
});
```

### 5.3 경계 케이스 테스트

```typescript
describe('경계 케이스 테스트', () => {
  it('모든 점수가 50점일 때 기본값 반환', () => {
    const scores: DimensionScores = {
      proactivity: 50,
      expression: 50,
      independence: 50,
      commitment: 50,
      romance: 50,
    };

    const result = classifyWithConfidence(scores);

    expect(result.primaryType).toBeDefined();
    expect(result.confidence).toBe('low'); // 모든 차원이 경계
    expect(result.boundaryDimensions).toHaveLength(5);
  });

  it('경계 점수(45-55) 신뢰도 테스트', () => {
    const scores: DimensionScores = {
      proactivity: 48,
      expression: 52,
      independence: 75,
      commitment: 80,
      romance: 25,
    };

    const result = classifyWithConfidence(scores);

    expect(result.confidence).toBe('medium');
    expect(result.boundaryDimensions).toContain('proactivity');
    expect(result.boundaryDimensions).toContain('expression');
  });

  it('극단적 점수는 높은 신뢰도', () => {
    const scores: DimensionScores = {
      proactivity: 100,
      expression: 100,
      independence: 0,
      commitment: 100,
      romance: 100,
    };

    const result = classifyWithConfidence(scores);

    expect(result.confidence).toBe('high');
    expect(result.boundaryDimensions).toHaveLength(0);
  });
});
```

### 5.4 샘플 응답 시나리오

```typescript
/**
 * 실제 사용자 응답 패턴 시뮬레이션
 */
export const SAMPLE_SCENARIOS = [
  {
    name: '활발한 대학생 지민',
    description: '22세, 연애에 적극적이고 로맨틱한 것을 좋아함',
    answers: [
      { questionId: 1, choice: 'A' as const },  // 적극적으로 번호 따기
      { questionId: 2, choice: 'A' as const },  // 깊은 대화 시작
      { questionId: 3, choice: 'A' as const },  // 하루 종일 데이트
      { questionId: 4, choice: 'A' as const },  // 직접적 호감 표현
      { questionId: 5, choice: 'A' as const },  // 바로 대화로 해결
      { questionId: 6, choice: 'A' as const },  // 로맨틱 레스토랑
      { questionId: 7, choice: 'B' as const },  // 연인 시간 아쉬움
      { questionId: 8, choice: 'A' as const },  // 확실한 호감 좋아
      { questionId: 9, choice: 'A' as const },  // 바로 표현
      { questionId: 10, choice: 'A' as const }, // 같이 취미 시도
      { questionId: 11, choice: 'A' as const }, // 분위기 좋은 곳
      { questionId: 12, choice: 'A' as const }, // 먼저 연락
      { questionId: 13, choice: 'A' as const }, // 구체적 계획
      { questionId: 14, choice: 'A' as const }, // 매일 사랑해
      { questionId: 15, choice: 'A' as const }, // 로맨틱 장소
      { questionId: 16, choice: 'B' as const }, // 같이 갔으면
      { questionId: 17, choice: 'A' as const }, // 빠른 고백
      { questionId: 18, choice: 'A' as const }, // 손해 봐도 OK
      { questionId: 19, choice: 'A' as const }, // 감성 카페
      { questionId: 20, choice: 'A' as const }, // 섭섭함 표현
    ],
    expectedType: 'romance_express' as LoveType,
    expectedScores: {
      proactivity: 100,
      expression: 100,
      independence: 0,
      commitment: 100,
      romance: 100,
    },
  },

  {
    name: '신중한 직장인 현수',
    description: '28세, 연애에 조심스럽고 상대를 천천히 알아가는 스타일',
    answers: [
      { questionId: 1, choice: 'B' as const },
      { questionId: 2, choice: 'B' as const },
      { questionId: 3, choice: 'B' as const },
      { questionId: 4, choice: 'B' as const },
      { questionId: 5, choice: 'B' as const },
      { questionId: 6, choice: 'B' as const },
      { questionId: 7, choice: 'A' as const },
      { questionId: 8, choice: 'B' as const },
      { questionId: 9, choice: 'B' as const },
      { questionId: 10, choice: 'B' as const },
      { questionId: 11, choice: 'B' as const },
      { questionId: 12, choice: 'B' as const },
      { questionId: 13, choice: 'A' as const },
      { questionId: 14, choice: 'B' as const },
      { questionId: 15, choice: 'B' as const },
      { questionId: 16, choice: 'A' as const },
      { questionId: 17, choice: 'B' as const },
      { questionId: 18, choice: 'B' as const },
      { questionId: 19, choice: 'B' as const },
      { questionId: 20, choice: 'B' as const },
    ],
    expectedType: 'slow_burner' as LoveType,
    expectedScores: {
      proactivity: 0,
      expression: 0,
      independence: 100,
      commitment: 33,
      romance: 0,
    },
  },

  {
    name: '독립적인 프리랜서 수아',
    description: '26세, 연애해도 개인 시간이 중요하고 각자의 삶 존중',
    answers: [
      { questionId: 1, choice: 'B' as const },
      { questionId: 2, choice: 'B' as const },
      { questionId: 3, choice: 'B' as const },
      { questionId: 4, choice: 'B' as const },
      { questionId: 5, choice: 'B' as const },
      { questionId: 6, choice: 'B' as const },
      { questionId: 7, choice: 'A' as const },
      { questionId: 8, choice: 'B' as const },
      { questionId: 9, choice: 'B' as const },
      { questionId: 10, choice: 'B' as const },
      { questionId: 11, choice: 'B' as const },
      { questionId: 12, choice: 'B' as const },
      { questionId: 13, choice: 'B' as const },
      { questionId: 14, choice: 'B' as const },
      { questionId: 15, choice: 'B' as const },
      { questionId: 16, choice: 'A' as const },
      { questionId: 17, choice: 'B' as const },
      { questionId: 18, choice: 'B' as const },
      { questionId: 19, choice: 'B' as const },
      { questionId: 20, choice: 'B' as const },
    ],
    expectedType: 'free_spirit' as LoveType,
    expectedScores: {
      proactivity: 0,
      expression: 0,
      independence: 100,
      commitment: 0,
      romance: 0,
    },
  },

  {
    name: '감성적인 작가 민재',
    description: '24세, 연애 노래에 감정이입 심하고 상상력이 풍부함',
    answers: [
      { questionId: 1, choice: 'B' as const },
      { questionId: 2, choice: 'A' as const },
      { questionId: 3, choice: 'A' as const },
      { questionId: 4, choice: 'B' as const },
      { questionId: 5, choice: 'A' as const },
      { questionId: 6, choice: 'A' as const },
      { questionId: 7, choice: 'B' as const },
      { questionId: 8, choice: 'B' as const },
      { questionId: 9, choice: 'A' as const },
      { questionId: 10, choice: 'A' as const },
      { questionId: 11, choice: 'A' as const },
      { questionId: 12, choice: 'B' as const },
      { questionId: 13, choice: 'A' as const },
      { questionId: 14, choice: 'A' as const },
      { questionId: 15, choice: 'A' as const },
      { questionId: 16, choice: 'B' as const },
      { questionId: 17, choice: 'B' as const },
      { questionId: 18, choice: 'A' as const },
      { questionId: 19, choice: 'A' as const },
      { questionId: 20, choice: 'A' as const },
    ],
    expectedType: 'emotional_dreamer' as LoveType,
    expectedScores: {
      proactivity: 0,
      expression: 100,
      independence: 0,
      commitment: 100,
      romance: 100,
    },
  },

  {
    name: '현실적인 회계사 은지',
    description: '30세, 연애도 계획적으로, 미래를 함께 그려가는 것 중요',
    answers: [
      { questionId: 1, choice: 'B' as const },
      { questionId: 2, choice: 'B' as const },
      { questionId: 3, choice: 'B' as const },
      { questionId: 4, choice: 'B' as const },
      { questionId: 5, choice: 'B' as const },
      { questionId: 6, choice: 'B' as const },
      { questionId: 7, choice: 'A' as const },
      { questionId: 8, choice: 'A' as const },
      { questionId: 9, choice: 'B' as const },
      { questionId: 10, choice: 'A' as const },
      { questionId: 11, choice: 'B' as const },
      { questionId: 12, choice: 'A' as const },
      { questionId: 13, choice: 'A' as const },
      { questionId: 14, choice: 'B' as const },
      { questionId: 15, choice: 'B' as const },
      { questionId: 16, choice: 'A' as const },
      { questionId: 17, choice: 'B' as const },
      { questionId: 18, choice: 'A' as const },
      { questionId: 19, choice: 'B' as const },
      { questionId: 20, choice: 'B' as const },
    ],
    expectedType: 'practical_lover' as LoveType,
    expectedScores: {
      proactivity: 40,
      expression: 0,
      independence: 100,
      commitment: 100,
      romance: 0,
    },
  },
];

// 시나리오 테스트 실행
describe('샘플 시나리오 테스트', () => {
  for (const scenario of SAMPLE_SCENARIOS) {
    it(`${scenario.name} -> ${scenario.expectedType}`, () => {
      const scores = calculateScores(scenario.answers);
      const type = classifyType(scores);

      expect(type).toBe(scenario.expectedType);
    });
  }
});
```

---

## 부록: 전체 분석 파이프라인

```typescript
/**
 * 테스트 결과 분석의 전체 파이프라인
 */
export interface FullAnalysisResult {
  // 원본 데이터
  answers: Answer[];

  // 점수 정보
  rawScores: RawScores;
  normalizedScores: DimensionScores;

  // 유형 분류
  primaryType: LoveType;
  typeMetadata: LoveTypeMetadata;
  confidence: 'high' | 'medium' | 'low';
  secondaryType?: LoveType;

  // AI 생성 결과
  aiGeneratedContent?: string;

  // 메타 정보
  analyzedAt: string;
  version: string;
}

export async function analyzeTestResult(
  answers: Answer[],
  aiConfig?: AIResultGeneratorConfig
): Promise<FullAnalysisResult> {
  // 1. 검증
  const validation = validateAnswers(answers);
  if (!validation.isValid) {
    throw new Error(`Invalid answers: ${validation.errors.join(', ')}`);
  }

  // 2. 점수 계산
  const rawScores = calculateRawScores(answers);
  const normalizedScores = normalizeScores(rawScores);

  // 3. 유형 분류
  const classificationResult = classifyWithConfidence(normalizedScores);
  const typeMetadata = LOVE_TYPE_METADATA[classificationResult.primaryType];

  // 4. AI 결과 생성 (선택적)
  let aiGeneratedContent: string | undefined;

  if (aiConfig) {
    try {
      const compatibleTypes = typeMetadata.compatibleTypes.map(
        t => LOVE_TYPE_METADATA[t]
      );

      aiGeneratedContent = await generateAIResult(
        {
          type: classificationResult.primaryType,
          metadata: typeMetadata,
          scores: normalizedScores,
          scoresSummary: {
            highest: getHighestDimension(normalizedScores),
            lowest: getLowestDimension(normalizedScores),
          },
          compatibleTypes,
        },
        aiConfig
      );
    } catch (error) {
      console.error('AI generation failed, using fallback:', error);
      aiGeneratedContent = FALLBACK_RESULTS[classificationResult.primaryType];
    }
  }

  return {
    answers,
    rawScores,
    normalizedScores,
    primaryType: classificationResult.primaryType,
    typeMetadata,
    confidence: classificationResult.confidence,
    secondaryType: classificationResult.secondaryType,
    aiGeneratedContent,
    analyzedAt: new Date().toISOString(),
    version: '1.0.0',
  };
}

function getHighestDimension(scores: DimensionScores): keyof DimensionScores {
  return Object.entries(scores).reduce(
    (max, [key, value]) => value > scores[max] ? key as keyof DimensionScores : max,
    'proactivity' as keyof DimensionScores
  );
}

function getLowestDimension(scores: DimensionScores): keyof DimensionScores {
  return Object.entries(scores).reduce(
    (min, [key, value]) => value < scores[min] ? key as keyof DimensionScores : min,
    'proactivity' as keyof DimensionScores
  );
}
```

---

## 변경 이력

| 버전 | 날짜 | 작성자 | 변경 내용 |
|------|------|--------|----------|
| 1.0.0 | 2025-01-30 | Claude Code | 최초 작성 |

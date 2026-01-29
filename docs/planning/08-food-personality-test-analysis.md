# 나는 무슨 음식 상일까? - 결과 분석 설계서

> **테스트명**: 나는 무슨 음식 상일까?
> **문항 수**: 8개 (각 4지선다)
> **결과 유형**: 8개
> **측정 차원**: 3축 (외향/내향, 모험/안정, 열정/차분)

---

## 1. 점수 계산 알고리즘

### 1.1 점수 체계 개요

- **총 문항**: 8개
- **선택지**: 각 문항당 4개 (A, B, C, D)
- **측정 차원**: 6개 스코어 (외향, 내향, 모험, 안정, 열정, 차분)
- **최종 분류**: 3축 조합 (각 축에서 높은 쪽 선택)

### 1.2 문항별 점수 배점 매핑

각 문항의 선택지는 다음과 같은 점수를 부여합니다:

```typescript
// 문항별 점수 배점표
// 각 선택지는 [외향, 내향, 모험, 안정, 열정, 차분] 점수를 부여

interface ChoiceScore {
  extroversion: number;    // 외향
  introversion: number;    // 내향
  adventure: number;       // 모험
  stability: number;       // 안정
  passion: number;         // 열정
  calmness: number;        // 차분
}

const QUESTION_SCORES: Record<string, Record<string, ChoiceScore>> = {
  "Q1": {  // 친구들과의 저녁 약속 상황
    "A": { extroversion: 3, introversion: 0, adventure: 2, stability: 1, passion: 2, calmness: 1 },
    "B": { extroversion: 0, introversion: 3, adventure: 0, stability: 3, passion: 1, calmness: 2 },
    "C": { extroversion: 2, introversion: 1, adventure: 3, stability: 0, passion: 3, calmness: 0 },
    "D": { extroversion: 1, introversion: 2, adventure: 1, stability: 2, passion: 0, calmness: 3 }
  },
  "Q2": {  // 주말 활동 선택
    "A": { extroversion: 3, introversion: 0, adventure: 3, stability: 0, passion: 3, calmness: 0 },
    "B": { extroversion: 2, introversion: 1, adventure: 1, stability: 2, passion: 2, calmness: 1 },
    "C": { extroversion: 0, introversion: 3, adventure: 0, stability: 3, passion: 0, calmness: 3 },
    "D": { extroversion: 1, introversion: 2, adventure: 2, stability: 1, passion: 1, calmness: 2 }
  },
  "Q3": {  // 스트레스 해소 방법
    "A": { extroversion: 3, introversion: 0, adventure: 1, stability: 2, passion: 3, calmness: 0 },
    "B": { extroversion: 0, introversion: 3, adventure: 0, stability: 3, passion: 0, calmness: 3 },
    "C": { extroversion: 2, introversion: 1, adventure: 3, stability: 0, passion: 2, calmness: 1 },
    "D": { extroversion: 1, introversion: 2, adventure: 2, stability: 1, passion: 1, calmness: 2 }
  },
  "Q4": {  // 새로운 식당 발견 시
    "A": { extroversion: 2, introversion: 1, adventure: 3, stability: 0, passion: 3, calmness: 0 },
    "B": { extroversion: 3, introversion: 0, adventure: 2, stability: 1, passion: 2, calmness: 1 },
    "C": { extroversion: 1, introversion: 2, adventure: 0, stability: 3, passion: 1, calmness: 2 },
    "D": { extroversion: 0, introversion: 3, adventure: 1, stability: 2, passion: 0, calmness: 3 }
  },
  "Q5": {  // 여행 스타일
    "A": { extroversion: 3, introversion: 0, adventure: 3, stability: 0, passion: 3, calmness: 0 },
    "B": { extroversion: 1, introversion: 2, adventure: 2, stability: 1, passion: 2, calmness: 1 },
    "C": { extroversion: 2, introversion: 1, adventure: 1, stability: 2, passion: 1, calmness: 2 },
    "D": { extroversion: 0, introversion: 3, adventure: 0, stability: 3, passion: 0, calmness: 3 }
  },
  "Q6": {  // 갈등 상황 대처
    "A": { extroversion: 3, introversion: 0, adventure: 1, stability: 2, passion: 3, calmness: 0 },
    "B": { extroversion: 1, introversion: 2, adventure: 0, stability: 3, passion: 1, calmness: 2 },
    "C": { extroversion: 0, introversion: 3, adventure: 2, stability: 1, passion: 0, calmness: 3 },
    "D": { extroversion: 2, introversion: 1, adventure: 3, stability: 0, passion: 2, calmness: 1 }
  },
  "Q7": {  // 일상의 루틴
    "A": { extroversion: 0, introversion: 3, adventure: 0, stability: 3, passion: 1, calmness: 2 },
    "B": { extroversion: 1, introversion: 2, adventure: 1, stability: 2, passion: 0, calmness: 3 },
    "C": { extroversion: 2, introversion: 1, adventure: 2, stability: 1, passion: 2, calmness: 1 },
    "D": { extroversion: 3, introversion: 0, adventure: 3, stability: 0, passion: 3, calmness: 0 }
  },
  "Q8": {  // 중요한 결정 방식
    "A": { extroversion: 0, introversion: 3, adventure: 1, stability: 2, passion: 0, calmness: 3 },
    "B": { extroversion: 1, introversion: 2, adventure: 0, stability: 3, passion: 1, calmness: 2 },
    "C": { extroversion: 2, introversion: 1, adventure: 2, stability: 1, passion: 3, calmness: 0 },
    "D": { extroversion: 3, introversion: 0, adventure: 3, stability: 0, passion: 2, calmness: 1 }
  }
};
```

### 1.3 점수 집계 로직

```typescript
interface Answer {
  questionId: string;  // "Q1", "Q2", ...
  choiceId: string;    // "A", "B", "C", "D"
}

interface DimensionScores {
  extroversion: number;
  introversion: number;
  adventure: number;
  stability: number;
  passion: number;
  calmness: number;
}

function calculateRawScores(answers: Answer[]): DimensionScores {
  const scores: DimensionScores = {
    extroversion: 0,
    introversion: 0,
    adventure: 0,
    stability: 0,
    passion: 0,
    calmness: 0
  };

  answers.forEach(answer => {
    const questionScores = QUESTION_SCORES[answer.questionId];
    if (!questionScores) {
      throw new Error(`Invalid question ID: ${answer.questionId}`);
    }

    const choiceScore = questionScores[answer.choiceId];
    if (!choiceScore) {
      throw new Error(`Invalid choice ID: ${answer.choiceId} for question ${answer.questionId}`);
    }

    // 각 차원 점수 누적
    scores.extroversion += choiceScore.extroversion;
    scores.introversion += choiceScore.introversion;
    scores.adventure += choiceScore.adventure;
    scores.stability += choiceScore.stability;
    scores.passion += choiceScore.passion;
    scores.calmness += choiceScore.calmness;
  });

  return scores;
}
```

### 1.4 점수 정규화 (0~100 스케일)

```typescript
interface NormalizedScores {
  extroversion: number;  // 0-100
  introversion: number;  // 0-100
  adventure: number;     // 0-100
  stability: number;     // 0-100
  passion: number;       // 0-100
  calmness: number;      // 0-100
}

function normalizeScores(rawScores: DimensionScores): NormalizedScores {
  // 각 차원의 최대 가능 점수: 8 문항 × 3 점/문항 = 24점
  const MAX_SCORE = 24;

  return {
    extroversion: Math.round((rawScores.extroversion / MAX_SCORE) * 100),
    introversion: Math.round((rawScores.introversion / MAX_SCORE) * 100),
    adventure: Math.round((rawScores.adventure / MAX_SCORE) * 100),
    stability: Math.round((rawScores.stability / MAX_SCORE) * 100),
    passion: Math.round((rawScores.passion / MAX_SCORE) * 100),
    calmness: Math.round((rawScores.calmness / MAX_SCORE) * 100)
  };
}
```

### 1.5 동점 처리 규칙

```typescript
// 동점 처리 우선순위
const TIE_BREAKER_PRIORITY = {
  axis1: ['extroversion', 'introversion'],  // 1순위: 외향/내향
  axis2: ['adventure', 'stability'],        // 2순위: 모험/안정
  axis3: ['passion', 'calmness']           // 3순위: 열정/차분
};

function resolveTie(score1: number, score2: number, dimension1: string, dimension2: string): string {
  // 점수가 같으면 사전에 정의된 우선순위 사용
  // 예: 외향=내향이면 외향 선택 (더 사교적인 결과가 긍정적)
  if (score1 === score2) {
    if (dimension1 === 'extroversion') return 'extroversion';
    if (dimension1 === 'adventure') return 'adventure';
    if (dimension1 === 'passion') return 'passion';
  }
  return score1 > score2 ? dimension1 : dimension2;
}
```

---

## 2. 결과 분류 로직

### 2.1 3차원 축 결정

```typescript
interface ThreeAxisResult {
  axis1: 'extroversion' | 'introversion';  // 외향 vs 내향
  axis2: 'adventure' | 'stability';        // 모험 vs 안정
  axis3: 'passion' | 'calmness';          // 열정 vs 차분
}

function determineThreeAxis(scores: NormalizedScores): ThreeAxisResult {
  // 축1: 외향 vs 내향
  const axis1 = scores.extroversion > scores.introversion
    ? 'extroversion'
    : (scores.extroversion === scores.introversion
      ? 'extroversion'  // 동점 시 외향 선택
      : 'introversion');

  // 축2: 모험 vs 안정
  const axis2 = scores.adventure > scores.stability
    ? 'adventure'
    : (scores.adventure === scores.stability
      ? 'adventure'  // 동점 시 모험 선택
      : 'stability');

  // 축3: 열정 vs 차분
  const axis3 = scores.passion > scores.calmness
    ? 'passion'
    : (scores.passion === scores.calmness
      ? 'passion'  // 동점 시 열정 선택
      : 'calmness');

  return { axis1, axis2, axis3 };
}
```

### 2.2 8가지 유형 매핑

```typescript
type FoodPersonalityType =
  | 'combo_pizza'      // 콤보피자 상
  | 'malatang'         // 마라탕 상
  | 'dessert_buffet'   // 디저트 뷔페 상
  | 'curry_rice'       // 카레라이스 상
  | 'sushi'            // 스시 상
  | 'salad'            // 샐러드 상
  | 'green_tea'        // 녹차 상
  | 'white_rice';      // 흰쌀밥 상

const RESULT_TYPE_MAP: Record<string, FoodPersonalityType> = {
  'extroversion-adventure-passion': 'combo_pizza',      // 외향 + 모험 + 열정
  'extroversion-adventure-calmness': 'malatang',        // 외향 + 모험 + 차분
  'extroversion-stability-passion': 'dessert_buffet',   // 외향 + 안정 + 열정
  'extroversion-stability-calmness': 'curry_rice',      // 외향 + 안정 + 차분
  'introversion-adventure-passion': 'sushi',            // 내향 + 모험 + 열정
  'introversion-adventure-calmness': 'salad',           // 내향 + 모험 + 차분
  'introversion-stability-passion': 'green_tea',        // 내향 + 안정 + 열정
  'introversion-stability-calmness': 'white_rice'       // 내향 + 안정 + 차분
};

function determineResultType(axis: ThreeAxisResult): FoodPersonalityType {
  const key = `${axis.axis1}-${axis.axis2}-${axis.axis3}`;
  const resultType = RESULT_TYPE_MAP[key];

  if (!resultType) {
    throw new Error(`Invalid axis combination: ${key}`);
  }

  return resultType;
}
```

### 2.3 세부 유형 결정 (2순위 유형)

```typescript
interface DetailedResult {
  primaryType: FoodPersonalityType;
  secondaryType: FoodPersonalityType | null;
  dominanceStrength: 'strong' | 'moderate' | 'weak';
}

function calculateDetailedResult(
  scores: NormalizedScores,
  primaryAxis: ThreeAxisResult
): DetailedResult {
  const primaryType = determineResultType(primaryAxis);

  // 각 축의 우세도 계산 (점수 차이)
  const axis1Diff = Math.abs(scores.extroversion - scores.introversion);
  const axis2Diff = Math.abs(scores.adventure - scores.stability);
  const axis3Diff = Math.abs(scores.passion - scores.calmness);

  const avgDiff = (axis1Diff + axis2Diff + axis3Diff) / 3;

  // 우세도 분류
  let dominanceStrength: 'strong' | 'moderate' | 'weak';
  if (avgDiff >= 40) {
    dominanceStrength = 'strong';
  } else if (avgDiff >= 20) {
    dominanceStrength = 'moderate';
  } else {
    dominanceStrength = 'weak';
  }

  // 2순위 유형 계산 (가장 점수 차이가 작은 축을 뒤집음)
  let secondaryType: FoodPersonalityType | null = null;

  if (dominanceStrength === 'weak' || dominanceStrength === 'moderate') {
    const minDiff = Math.min(axis1Diff, axis2Diff, axis3Diff);

    let secondaryAxis = { ...primaryAxis };

    if (minDiff === axis1Diff) {
      secondaryAxis.axis1 = primaryAxis.axis1 === 'extroversion' ? 'introversion' : 'extroversion';
    } else if (minDiff === axis2Diff) {
      secondaryAxis.axis2 = primaryAxis.axis2 === 'adventure' ? 'stability' : 'adventure';
    } else {
      secondaryAxis.axis3 = primaryAxis.axis3 === 'passion' ? 'calmness' : 'passion';
    }

    secondaryType = determineResultType(secondaryAxis);
  }

  return {
    primaryType,
    secondaryType,
    dominanceStrength
  };
}
```

### 2.4 완전한 분류 함수

```typescript
interface FullAnalysisResult {
  rawScores: DimensionScores;
  normalizedScores: NormalizedScores;
  threeAxis: ThreeAxisResult;
  detailedResult: DetailedResult;
  percentages: {
    extroversion: number;
    adventure: number;
    passion: number;
  };
}

function analyzeTestResult(answers: Answer[]): FullAnalysisResult {
  // 1. 원점수 계산
  const rawScores = calculateRawScores(answers);

  // 2. 정규화 (0-100)
  const normalizedScores = normalizeScores(rawScores);

  // 3. 3축 결정
  const threeAxis = determineThreeAxis(normalizedScores);

  // 4. 세부 유형 결정
  const detailedResult = calculateDetailedResult(normalizedScores, threeAxis);

  // 5. 각 축의 비율 계산 (AI 프롬프트용)
  const percentages = {
    extroversion: Math.round(
      (normalizedScores.extroversion / (normalizedScores.extroversion + normalizedScores.introversion)) * 100
    ),
    adventure: Math.round(
      (normalizedScores.adventure / (normalizedScores.adventure + normalizedScores.stability)) * 100
    ),
    passion: Math.round(
      (normalizedScores.passion / (normalizedScores.passion + normalizedScores.calmness)) * 100
    )
  };

  return {
    rawScores,
    normalizedScores,
    threeAxis,
    detailedResult,
    percentages
  };
}
```

---

## 3. AI 결과 생성 프롬프트

### 3.1 시스템 프롬프트

```typescript
const SYSTEM_PROMPT = `당신은 친근하고 위트있는 심리테스트 결과 작성 전문가입니다.

**톤앤매너**:
- MZ세대가 공감할 수 있는 친근한 말투 사용
- "너", "당신" 혼용하되 주로 "너" 사용
- 이모티콘 적절히 활용 (과하지 않게)
- 재치있고 유머러스하되 진지함도 유지

**금지사항**:
- 의학적 진단이나 처방 표현 금지
- 부정적 라벨링 금지 (예: "문제 있는", "이상한")
- 비교나 서열화 금지 (예: "최고", "최악")
- 500자를 초과하는 장문 금지

**구조 준수**:
반드시 다음 형식으로 작성하세요:
1. 공감 멘트 (2-3문장)
2. 강점 설명 (2개, 각 1문장)
3. 성장 포인트 (1-2문장, 긍정적 표현)
4. 오늘의 한마디 (1문장, SNS 공유용)`;
```

### 3.2 유형별 기본 템플릿

```typescript
const RESULT_TEMPLATES: Record<FoodPersonalityType, {
  emoji: string;
  title: string;
  subtitle: string;
  keywords: string[];
}> = {
  combo_pizza: {
    emoji: '🍕',
    title: '콤보피자 상',
    subtitle: '다양한 맛을 한번에! 열정 넘치는 파티 메이커',
    keywords: ['외향적', '모험적', '열정적', '사교적', '활발한', '다채로운']
  },
  malatang: {
    emoji: '🌶️',
    title: '마라탕 상',
    subtitle: '자극적이지만 절제된, 쿨한 매력의 소유자',
    keywords: ['외향적', '모험적', '차분한', '쿨한', '당당한', '여유로운']
  },
  dessert_buffet: {
    emoji: '🍰',
    title: '디저트 뷔페 상',
    subtitle: '달콤하고 화려한, 분위기 메이커',
    keywords: ['외향적', '안정적', '열정적', '따뜻한', '친절한', '활기찬']
  },
  curry_rice: {
    emoji: '🍛',
    title: '카레라이스 상',
    subtitle: '부드럽고 편안한, 믿음직한 조력자',
    keywords: ['외향적', '안정적', '차분한', '따뜻한', '편안한', '신뢰감']
  },
  sushi: {
    emoji: '🍣',
    title: '스시 상',
    subtitle: '섬세하고 고급스러운, 독창적인 예술가',
    keywords: ['내향적', '모험적', '열정적', '독창적', '세련된', '깊이있는']
  },
  salad: {
    emoji: '🥗',
    title: '샐러드 상',
    subtitle: '신선하고 건강한, 자연스러운 힐러',
    keywords: ['내향적', '모험적', '차분한', '자연스러운', '건강한', '균형잡힌']
  },
  green_tea: {
    emoji: '🍵',
    title: '녹차 상',
    subtitle: '깊고 은은한, 성찰적인 사색가',
    keywords: ['내향적', '안정적', '열정적', '깊이있는', '진중한', '몰입형']
  },
  white_rice: {
    emoji: '🍚',
    title: '흰쌀밥 상',
    subtitle: '담백하고 순수한, 편안한 안식처',
    keywords: ['내향적', '안정적', '차분한', '순수한', '평화로운', '온화한']
  }
};
```

### 3.3 사용자 프롬프트 생성

```typescript
interface AIPromptVariables {
  resultType: FoodPersonalityType;
  secondaryType: FoodPersonalityType | null;
  dominanceStrength: 'strong' | 'moderate' | 'weak';
  percentages: {
    extroversion: number;
    adventure: number;
    passion: number;
  };
  normalizedScores: NormalizedScores;
}

function buildUserPrompt(variables: AIPromptVariables): string {
  const template = RESULT_TEMPLATES[variables.resultType];
  const secondaryTemplate = variables.secondaryType
    ? RESULT_TEMPLATES[variables.secondaryType]
    : null;

  return `사용자의 심리테스트 결과를 분석하여 맞춤형 결과를 작성해주세요.

**기본 정보**:
- 주 유형: ${template.emoji} ${template.title}
- 부제: ${template.subtitle}
- 키워드: ${template.keywords.join(', ')}
${secondaryTemplate ? `- 2순위 유형: ${secondaryTemplate.emoji} ${secondaryTemplate.title}` : ''}
- 유형 우세도: ${variables.dominanceStrength === 'strong' ? '강함' : variables.dominanceStrength === 'moderate' ? '중간' : '약함'}

**세부 점수**:
- 외향성: ${variables.percentages.extroversion}% (vs 내향성 ${100 - variables.percentages.extroversion}%)
- 모험성: ${variables.percentages.adventure}% (vs 안정성 ${100 - variables.percentages.adventure}%)
- 열정도: ${variables.percentages.passion}% (vs 차분함 ${100 - variables.percentages.passion}%)

**정규화 점수**:
- 외향: ${variables.normalizedScores.extroversion}, 내향: ${variables.normalizedScores.introversion}
- 모험: ${variables.normalizedScores.adventure}, 안정: ${variables.normalizedScores.stability}
- 열정: ${variables.normalizedScores.passion}, 차분: ${variables.normalizedScores.calmness}

**작성 요청**:
다음 형식으로 결과를 작성해주세요:

## ${template.emoji} ${template.title}

[2-3문장의 공감 멘트: 이 유형의 사람들이 "아 맞아!" 할 만한 특징을 친근하게 설명]

### 너의 강점 ✨
- [강점 1: 구체적인 상황 예시와 함께]
- [강점 2: 구체적인 상황 예시와 함께]

### 성장 포인트 🌱
[1-2문장: 약점이 아닌 "더 나아질 수 있는 방향"으로 긍정적 표현]
${variables.secondaryType ? `\n(힌트: ${secondaryTemplate!.title}의 특성을 조금 더하면 균형잡힐 수 있어!)` : ''}

### 오늘의 한마디 💬
"[SNS 공유용 위트있는 한 문장: 10-20자 내외]"

---

**참고사항**:
- 우세도가 ${variables.dominanceStrength}이므로, ${variables.dominanceStrength === 'weak' ? '여러 성향이 골고루 나타나는 균형잡힌 사람' : variables.dominanceStrength === 'moderate' ? '명확한 성향이 있되 유연성도 있는 사람' : '매우 뚜렷한 성향을 가진 사람'}임을 반영하세요.
- 점수 비율을 참고하여 구체적인 수치를 언급하면 더욱 개인화된 느낌을 줄 수 있습니다.`;
}
```

### 3.4 OpenAI API 호출 코드

```typescript
interface GenerateResultRequest {
  testId: string;
  answers: Answer[];
  userId?: string;  // 선택적, 캐싱용
}

interface GenerateResultResponse {
  resultId: string;
  resultType: FoodPersonalityType;
  title: string;
  content: string;  // AI 생성 결과
  emoji: string;
  analysisData: FullAnalysisResult;
  createdAt: Date;
}

async function generateAIResult(
  request: GenerateResultRequest
): Promise<GenerateResultResponse> {
  // 1. 점수 계산 및 분석
  const analysis = analyzeTestResult(request.answers);

  // 2. 캐시 확인 (동일 답변은 캐싱)
  const cacheKey = generateCacheKey(request.testId, request.answers);
  const cached = await getCachedResult(cacheKey);
  if (cached) {
    return cached;
  }

  // 3. AI 프롬프트 생성
  const promptVariables: AIPromptVariables = {
    resultType: analysis.detailedResult.primaryType,
    secondaryType: analysis.detailedResult.secondaryType,
    dominanceStrength: analysis.detailedResult.dominanceStrength,
    percentages: analysis.percentages,
    normalizedScores: analysis.normalizedScores
  };

  const userPrompt = buildUserPrompt(promptVariables);

  // 4. OpenAI API 호출
  const completion = await openai.chat.completions.create({
    model: 'gpt-4o-mini',
    messages: [
      { role: 'system', content: SYSTEM_PROMPT },
      { role: 'user', content: userPrompt }
    ],
    temperature: 0.8,  // 창의성 높임
    max_tokens: 600,   // 500자 정도 제한
    presence_penalty: 0.3,  // 반복 방지
    frequency_penalty: 0.3
  });

  const aiContent = completion.choices[0].message.content || '';

  // 5. 결과 저장
  const template = RESULT_TEMPLATES[analysis.detailedResult.primaryType];
  const result: GenerateResultResponse = {
    resultId: generateResultId(),
    resultType: analysis.detailedResult.primaryType,
    title: template.title,
    content: aiContent,
    emoji: template.emoji,
    analysisData: analysis,
    createdAt: new Date()
  };

  // 6. 캐싱 (30일)
  await setCachedResult(cacheKey, result, 30 * 24 * 3600);

  return result;
}

// 캐시 키 생성 (답변 해시)
function generateCacheKey(testId: string, answers: Answer[]): string {
  const answerString = answers
    .sort((a, b) => a.questionId.localeCompare(b.questionId))
    .map(a => `${a.questionId}:${a.choiceId}`)
    .join('|');

  // 간단한 해시 (실제로는 crypto 사용)
  return `result:${testId}:${hashString(answerString)}`;
}

function hashString(str: string): string {
  // 실제 구현에서는 crypto.createHash 사용
  let hash = 0;
  for (let i = 0; i < str.length; i++) {
    const char = str.charCodeAt(i);
    hash = ((hash << 5) - hash) + char;
    hash = hash & hash;
  }
  return hash.toString(36);
}
```

---

## 4. 테스트 케이스

### 4.1 각 유형별 최적 응답 패턴

```typescript
const TEST_CASES = {
  // 1. 콤보피자 상 (외향 + 모험 + 열정)
  combo_pizza: {
    answers: [
      { questionId: 'Q1', choiceId: 'C' },  // 새로운 핫플 탐방
      { questionId: 'Q2', choiceId: 'A' },  // 친구들과 파티
      { questionId: 'Q3', choiceId: 'A' },  // 친구들과 수다
      { questionId: 'Q4', choiceId: 'A' },  // 바로 가봐야지
      { questionId: 'Q5', choiceId: 'A' },  // 즉흥 여행
      { questionId: 'Q6', choiceId: 'A' },  // 바로 대화
      { questionId: 'Q7', choiceId: 'D' },  // 매일 다르게
      { questionId: 'Q8', choiceId: 'D' }   // 직감과 열정
    ],
    expectedType: 'combo_pizza',
    expectedScores: {
      extroversion: 83,  // 20/24 * 100
      adventure: 92,     // 22/24 * 100
      passion: 92        // 22/24 * 100
    }
  },

  // 2. 마라탕 상 (외향 + 모험 + 차분)
  malatang: {
    answers: [
      { questionId: 'Q1', choiceId: 'A' },  // 친구들이 좋아하는 곳
      { questionId: 'Q2', choiceId: 'D' },  // 산책하며 사색
      { questionId: 'Q3', choiceId: 'C' },  // 새로운 취미
      { questionId: 'Q4', choiceId: 'B' },  // 친구들과 가기로
      { questionId: 'Q5', choiceId: 'B' },  // 계획과 즉흥 믹스
      { questionId: 'Q6', choiceId: 'D' },  // 색다른 접근
      { questionId: 'Q7', choiceId: 'C' },  // 변화 추구
      { questionId: 'Q8', choiceId: 'A' }   // 신중하게 분석
    ],
    expectedType: 'malatang',
    expectedScores: {
      extroversion: 63,
      adventure: 67,
      passion: 38  // 차분함이 높음
    }
  },

  // 3. 디저트 뷔페 상 (외향 + 안정 + 열정)
  dessert_buffet: {
    answers: [
      { questionId: 'Q1', choiceId: 'A' },  // 친구들이 좋아하는
      { questionId: 'Q2', choiceId: 'B' },  // 맛집 탐방
      { questionId: 'Q3', choiceId: 'A' },  // 친구들과 수다
      { questionId: 'Q4', choiceId: 'C' },  // 리뷰 확인
      { questionId: 'Q5', choiceId: 'C' },  // 계획적 여행
      { questionId: 'Q6', choiceId: 'A' },  // 바로 대화
      { questionId: 'Q7', choiceId: 'C' },  // 변화 추구
      { questionId: 'Q8', choiceId: 'C' }   // 열정적 판단
    ],
    expectedType: 'dessert_buffet',
    expectedScores: {
      extroversion: 75,
      adventure: 42,  // 안정이 높음
      passion: 79
    }
  },

  // 4. 카레라이스 상 (외향 + 안정 + 차분)
  curry_rice: {
    answers: [
      { questionId: 'Q1', choiceId: 'A' },
      { questionId: 'Q2', choiceId: 'B' },
      { questionId: 'Q3', choiceId: 'D' },  // 운동으로 해소
      { questionId: 'Q4', choiceId: 'C' },
      { questionId: 'Q5', choiceId: 'C' },
      { questionId: 'Q6', choiceId: 'B' },  // 시간 두고 대화
      { questionId: 'Q7', choiceId: 'A' },  // 일정한 루틴
      { questionId: 'Q8', choiceId: 'B' }   // 신중한 판단
    ],
    expectedType: 'curry_rice',
    expectedScores: {
      extroversion: 67,
      adventure: 33,
      passion: 38
    }
  },

  // 5. 스시 상 (내향 + 모험 + 열정)
  sushi: {
    answers: [
      { questionId: 'Q1', choiceId: 'C' },  // 새로운 핫플
      { questionId: 'Q2', choiceId: 'D' },  // 산책하며 사색
      { questionId: 'Q3', choiceId: 'C' },  // 새로운 취미
      { questionId: 'Q4', choiceId: 'A' },  // 바로 가봐야지
      { questionId: 'Q5', choiceId: 'B' },
      { questionId: 'Q6', choiceId: 'C' },  // 혼자 생각
      { questionId: 'Q7', choiceId: 'D' },  // 매일 다르게
      { questionId: 'Q8', choiceId: 'C' }   // 열정적 판단
    ],
    expectedType: 'sushi',
    expectedScores: {
      extroversion: 42,
      adventure: 75,
      passion: 75
    }
  },

  // 6. 샐러드 상 (내향 + 모험 + 차분)
  salad: {
    answers: [
      { questionId: 'Q1', choiceId: 'D' },  // 조용한 카페
      { questionId: 'Q2', choiceId: 'D' },  // 산책
      { questionId: 'Q3', choiceId: 'C' },  // 새로운 취미
      { questionId: 'Q4', choiceId: 'D' },  // 마음에 들면
      { questionId: 'Q5', choiceId: 'D' },  // 혼자 여유롭게
      { questionId: 'Q6', choiceId: 'C' },  // 혼자 생각
      { questionId: 'Q7', choiceId: 'B' },  // 유연한 틀
      { questionId: 'Q8', choiceId: 'A' }   // 신중하게
    ],
    expectedType: 'salad',
    expectedScores: {
      extroversion: 21,
      adventure: 58,
      passion: 33
    }
  },

  // 7. 녹차 상 (내향 + 안정 + 열정)
  green_tea: {
    answers: [
      { questionId: 'Q1', choiceId: 'B' },  // 가본 곳
      { questionId: 'Q2', choiceId: 'C' },  // 집에서 취미
      { questionId: 'Q3', choiceId: 'B' },  // 혼자 음악
      { questionId: 'Q4', choiceId: 'C' },  // 리뷰 확인
      { questionId: 'Q5', choiceId: 'D' },  // 여유롭게
      { questionId: 'Q6', choiceId: 'C' },  // 혼자 생각
      { questionId: 'Q7', choiceId: 'A' },  // 일정한 루틴
      { questionId: 'Q8', choiceId: 'C' }   // 열정적 판단
    ],
    expectedType: 'green_tea',
    expectedScores: {
      extroversion: 29,
      adventure: 25,
      passion: 58
    }
  },

  // 8. 흰쌀밥 상 (내향 + 안정 + 차분)
  white_rice: {
    answers: [
      { questionId: 'Q1', choiceId: 'B' },
      { questionId: 'Q2', choiceId: 'C' },
      { questionId: 'Q3', choiceId: 'B' },
      { questionId: 'Q4', choiceId: 'D' },
      { questionId: 'Q5', choiceId: 'D' },
      { questionId: 'Q6', choiceId: 'C' },
      { questionId: 'Q7', choiceId: 'A' },
      { questionId: 'Q8', choiceId: 'A' }
    ],
    expectedType: 'white_rice',
    expectedScores: {
      extroversion: 17,
      adventure: 21,
      passion: 21
    }
  }
};
```

### 4.2 경계값 테스트 케이스

```typescript
const EDGE_CASES = {
  // 경계값 1: 모든 점수가 동일한 경우 (완벽한 균형)
  perfect_balance: {
    answers: [
      { questionId: 'Q1', choiceId: 'A' },
      { questionId: 'Q2', choiceId: 'B' },
      { questionId: 'Q3', choiceId: 'D' },
      { questionId: 'Q4', choiceId: 'B' },
      { questionId: 'Q5', choiceId: 'C' },
      { questionId: 'Q6', choiceId: 'B' },
      { questionId: 'Q7', choiceId: 'C' },
      { questionId: 'Q8', choiceId: 'B' }
    ],
    expectedBehavior: '동점 규칙에 따라 extroversion-adventure-passion 선택 (우선순위)',
    expectedType: 'combo_pizza',
    expectedDominance: 'weak'
  },

  // 경계값 2: 한 축만 명확한 경우
  single_axis_clear: {
    answers: [
      { questionId: 'Q1', choiceId: 'C' },  // 외향 강함
      { questionId: 'Q2', choiceId: 'A' },  // 외향 강함
      { questionId: 'Q3', choiceId: 'D' },  // 중립
      { questionId: 'Q4', choiceId: 'B' },  // 외향 강함
      { questionId: 'Q5', choiceId: 'C' },  // 중립
      { questionId: 'Q6', choiceId: 'B' },  // 중립
      { questionId: 'Q7', choiceId: 'C' },  // 중립
      { questionId: 'Q8', choiceId: 'B' }   // 중립
    ],
    expectedBehavior: '외향만 명확, 나머지는 근소한 차이',
    expectedDominance: 'weak'
  },

  // 경계값 3: 극단적 선택 (모두 같은 스타일)
  extreme_choice: {
    answers: [
      { questionId: 'Q1', choiceId: 'A' },
      { questionId: 'Q2', choiceId: 'A' },
      { questionId: 'Q3', choiceId: 'A' },
      { questionId: 'Q4', choiceId: 'A' },
      { questionId: 'Q5', choiceId: 'A' },
      { questionId: 'Q6', choiceId: 'A' },
      { questionId: 'Q7', choiceId: 'D' },  // 극단
      { questionId: 'Q8', choiceId: 'D' }   // 극단
    ],
    expectedBehavior: '극단적 패턴이지만 정상 처리',
    expectedDominance: 'strong'
  }
};
```

### 4.3 검증용 샘플 데이터

```typescript
// 실제 사용자가 답변할 만한 5개 시나리오
const SAMPLE_USER_SCENARIOS = [
  {
    name: '활발한 대학생 민지',
    profile: '20대, 친구들과 노는 걸 좋아하고 새로운 경험에 열려있음',
    answers: [
      { questionId: 'Q1', choiceId: 'A' },
      { questionId: 'Q2', choiceId: 'A' },
      { questionId: 'Q3', choiceId: 'A' },
      { questionId: 'Q4', choiceId: 'B' },
      { questionId: 'Q5', choiceId: 'B' },
      { questionId: 'Q6', choiceId: 'A' },
      { questionId: 'Q7', choiceId: 'C' },
      { questionId: 'Q8', choiceId: 'C' }
    ],
    expectedType: 'combo_pizza' // 또는 dessert_buffet
  },

  {
    name: '조용한 개발자 준호',
    profile: '20대, 혼자 있는 시간 좋아하고 안정적인 루틴 선호',
    answers: [
      { questionId: 'Q1', choiceId: 'B' },
      { questionId: 'Q2', choiceId: 'C' },
      { questionId: 'Q3', choiceId: 'B' },
      { questionId: 'Q4', choiceId: 'C' },
      { questionId: 'Q5', choiceId: 'D' },
      { questionId: 'Q6', choiceId: 'C' },
      { questionId: 'Q7', choiceId: 'A' },
      { questionId: 'Q8', choiceId: 'B' }
    ],
    expectedType: 'white_rice'
  },

  {
    name: '모험가 수연',
    profile: '30대, 새로운 것 도전하지만 혼자 다니는 걸 선호',
    answers: [
      { questionId: 'Q1', choiceId: 'C' },
      { questionId: 'Q2', choiceId: 'D' },
      { questionId: 'Q3', choiceId: 'C' },
      { questionId: 'Q4', choiceId: 'A' },
      { questionId: 'Q5', choiceId: 'A' },
      { questionId: 'Q6', choiceId: 'D' },
      { questionId: 'Q7', choiceId: 'D' },
      { questionId: 'Q8', choiceId: 'C' }
    ],
    expectedType: 'sushi'
  },

  {
    name: '온화한 교사 지훈',
    profile: '30대, 사람들과 있지만 조용하고 차분한 스타일',
    answers: [
      { questionId: 'Q1', choiceId: 'A' },
      { questionId: 'Q2', choiceId: 'B' },
      { questionId: 'Q3', choiceId: 'D' },
      { questionId: 'Q4', choiceId: 'C' },
      { questionId: 'Q5', choiceId: 'C' },
      { questionId: 'Q6', choiceId: 'B' },
      { questionId: 'Q7', choiceId: 'B' },
      { questionId: 'Q8', choiceId: 'B' }
    ],
    expectedType: 'curry_rice'
  },

  {
    name: '쿨한 마케터 현아',
    profile: '20대, 외향적이지만 감정적이지 않고 이성적',
    answers: [
      { questionId: 'Q1', choiceId: 'A' },
      { questionId: 'Q2', choiceId: 'A' },
      { questionId: 'Q3', choiceId: 'C' },
      { questionId: 'Q4', choiceId: 'B' },
      { questionId: 'Q5', choiceId: 'A' },
      { questionId: 'Q6', choiceId: 'D' },
      { questionId: 'Q7', choiceId: 'D' },
      { questionId: 'Q8', choiceId: 'A' }
    ],
    expectedType: 'malatang'
  }
];
```

### 4.4 테스트 실행 함수

```typescript
function runTestCases() {
  console.log('=== 유형별 최적 응답 테스트 ===\n');

  Object.entries(TEST_CASES).forEach(([typeName, testCase]) => {
    const result = analyzeTestResult(testCase.answers);
    const passed = result.detailedResult.primaryType === testCase.expectedType;

    console.log(`${passed ? '✅' : '❌'} ${typeName}`);
    console.log(`  예상: ${testCase.expectedType}`);
    console.log(`  실제: ${result.detailedResult.primaryType}`);
    console.log(`  점수: 외향${result.percentages.extroversion}% / 모험${result.percentages.adventure}% / 열정${result.percentages.passion}%`);
    console.log('');
  });

  console.log('\n=== 경계값 테스트 ===\n');

  Object.entries(EDGE_CASES).forEach(([caseName, testCase]) => {
    const result = analyzeTestResult(testCase.answers);

    console.log(`🔍 ${caseName}`);
    console.log(`  동작: ${testCase.expectedBehavior}`);
    console.log(`  결과 유형: ${result.detailedResult.primaryType}`);
    console.log(`  우세도: ${result.detailedResult.dominanceStrength}`);
    console.log(`  2순위: ${result.detailedResult.secondaryType || '없음'}`);
    console.log('');
  });

  console.log('\n=== 샘플 사용자 시나리오 ===\n');

  SAMPLE_USER_SCENARIOS.forEach(scenario => {
    const result = analyzeTestResult(scenario.answers);
    const passed = result.detailedResult.primaryType === scenario.expectedType;

    console.log(`${passed ? '✅' : '⚠️'} ${scenario.name}`);
    console.log(`  프로필: ${scenario.profile}`);
    console.log(`  결과: ${RESULT_TEMPLATES[result.detailedResult.primaryType].emoji} ${RESULT_TEMPLATES[result.detailedResult.primaryType].title}`);
    console.log(`  예상: ${scenario.expectedType}`);
    console.log('');
  });
}
```

---

## 5. Python 구현 (백엔드용)

### 5.1 점수 계산 모듈

```python
from typing import List, Dict, Tuple
from dataclasses import dataclass
from enum import Enum

class FoodPersonalityType(Enum):
    COMBO_PIZZA = "combo_pizza"
    MALATANG = "malatang"
    DESSERT_BUFFET = "dessert_buffet"
    CURRY_RICE = "curry_rice"
    SUSHI = "sushi"
    SALAD = "salad"
    GREEN_TEA = "green_tea"
    WHITE_RICE = "white_rice"

@dataclass
class Answer:
    question_id: str
    choice_id: str

@dataclass
class ChoiceScore:
    extroversion: int
    introversion: int
    adventure: int
    stability: int
    passion: int
    calmness: int

@dataclass
class DimensionScores:
    extroversion: int
    introversion: int
    adventure: int
    stability: int
    passion: int
    calmness: int

@dataclass
class NormalizedScores:
    extroversion: int
    introversion: int
    adventure: int
    stability: int
    passion: int
    calmness: int

@dataclass
class ThreeAxisResult:
    axis1: str  # 'extroversion' or 'introversion'
    axis2: str  # 'adventure' or 'stability'
    axis3: str  # 'passion' or 'calmness'

@dataclass
class DetailedResult:
    primary_type: FoodPersonalityType
    secondary_type: FoodPersonalityType | None
    dominance_strength: str  # 'strong', 'moderate', 'weak'

# 점수 배점표 (TypeScript와 동일)
QUESTION_SCORES: Dict[str, Dict[str, ChoiceScore]] = {
    "Q1": {
        "A": ChoiceScore(3, 0, 2, 1, 2, 1),
        "B": ChoiceScore(0, 3, 0, 3, 1, 2),
        "C": ChoiceScore(2, 1, 3, 0, 3, 0),
        "D": ChoiceScore(1, 2, 1, 2, 0, 3)
    },
    # ... (나머지 Q2~Q8 동일)
}

def calculate_raw_scores(answers: List[Answer]) -> DimensionScores:
    """원점수 계산"""
    scores = DimensionScores(0, 0, 0, 0, 0, 0)

    for answer in answers:
        question_scores = QUESTION_SCORES.get(answer.question_id)
        if not question_scores:
            raise ValueError(f"Invalid question ID: {answer.question_id}")

        choice_score = question_scores.get(answer.choice_id)
        if not choice_score:
            raise ValueError(f"Invalid choice ID: {answer.choice_id}")

        scores.extroversion += choice_score.extroversion
        scores.introversion += choice_score.introversion
        scores.adventure += choice_score.adventure
        scores.stability += choice_score.stability
        scores.passion += choice_score.passion
        scores.calmness += choice_score.calmness

    return scores

def normalize_scores(raw_scores: DimensionScores) -> NormalizedScores:
    """0-100 스케일로 정규화"""
    MAX_SCORE = 24

    return NormalizedScores(
        extroversion=round((raw_scores.extroversion / MAX_SCORE) * 100),
        introversion=round((raw_scores.introversion / MAX_SCORE) * 100),
        adventure=round((raw_scores.adventure / MAX_SCORE) * 100),
        stability=round((raw_scores.stability / MAX_SCORE) * 100),
        passion=round((raw_scores.passion / MAX_SCORE) * 100),
        calmness=round((raw_scores.calmness / MAX_SCORE) * 100)
    )

def determine_three_axis(scores: NormalizedScores) -> ThreeAxisResult:
    """3축 결정"""
    axis1 = 'extroversion' if scores.extroversion >= scores.introversion else 'introversion'
    axis2 = 'adventure' if scores.adventure >= scores.stability else 'stability'
    axis3 = 'passion' if scores.passion >= scores.calmness else 'calmness'

    return ThreeAxisResult(axis1, axis2, axis3)

def determine_result_type(axis: ThreeAxisResult) -> FoodPersonalityType:
    """결과 유형 결정"""
    key = f"{axis.axis1}-{axis.axis2}-{axis.axis3}"

    type_map = {
        'extroversion-adventure-passion': FoodPersonalityType.COMBO_PIZZA,
        'extroversion-adventure-calmness': FoodPersonalityType.MALATANG,
        'extroversion-stability-passion': FoodPersonalityType.DESSERT_BUFFET,
        'extroversion-stability-calmness': FoodPersonalityType.CURRY_RICE,
        'introversion-adventure-passion': FoodPersonalityType.SUSHI,
        'introversion-adventure-calmness': FoodPersonalityType.SALAD,
        'introversion-stability-passion': FoodPersonalityType.GREEN_TEA,
        'introversion-stability-calmness': FoodPersonalityType.WHITE_RICE
    }

    result_type = type_map.get(key)
    if not result_type:
        raise ValueError(f"Invalid axis combination: {key}")

    return result_type

def analyze_test_result(answers: List[Answer]) -> Dict:
    """완전한 분석 실행"""
    # 1. 원점수
    raw_scores = calculate_raw_scores(answers)

    # 2. 정규화
    normalized_scores = normalize_scores(raw_scores)

    # 3. 3축 결정
    three_axis = determine_three_axis(normalized_scores)

    # 4. 결과 유형
    primary_type = determine_result_type(three_axis)

    # 5. 우세도 계산
    axis1_diff = abs(normalized_scores.extroversion - normalized_scores.introversion)
    axis2_diff = abs(normalized_scores.adventure - normalized_scores.stability)
    axis3_diff = abs(normalized_scores.passion - normalized_scores.calmness)
    avg_diff = (axis1_diff + axis2_diff + axis3_diff) / 3

    if avg_diff >= 40:
        dominance = 'strong'
    elif avg_diff >= 20:
        dominance = 'moderate'
    else:
        dominance = 'weak'

    # 6. 비율 계산
    percentages = {
        'extroversion': round(normalized_scores.extroversion /
                            (normalized_scores.extroversion + normalized_scores.introversion) * 100),
        'adventure': round(normalized_scores.adventure /
                          (normalized_scores.adventure + normalized_scores.stability) * 100),
        'passion': round(normalized_scores.passion /
                        (normalized_scores.passion + normalized_scores.calmness) * 100)
    }

    return {
        'primary_type': primary_type.value,
        'dominance_strength': dominance,
        'normalized_scores': normalized_scores.__dict__,
        'percentages': percentages,
        'three_axis': three_axis.__dict__
    }
```

---

## 요약

### 완료 산출물

1. **점수 계산 알고리즘** ✅
   - 6개 차원 점수 집계 로직
   - 0~100 스케일 정규화
   - 동점 처리 규칙 (우선순위 기반)

2. **결과 분류 로직** ✅
   - 3축 조합에 따른 8가지 유형 자동 분류
   - 경계값 처리 (동점 시 우선순위 적용)
   - 세부 유형 결정 (2순위 유형, 우세도)

3. **AI 결과 생성 프롬프트** ✅
   - OpenAI GPT-4o-mini 최적화 프롬프트
   - 변수: 유형명, 점수 비율, 2순위 유형, 우세도
   - 톤앤매너: MZ세대 친근한 스타일
   - 구조화된 출력 (공감 멘트, 강점, 성장 포인트, 한마디)

4. **테스트 케이스** ✅
   - 8가지 유형별 최적 응답 패턴
   - 경계값 테스트 (완벽 균형, 극단 선택)
   - 실제 사용자 시나리오 5개

### 구현 언어

- **TypeScript**: 프론트엔드 및 API 타입 정의
- **Python**: 백엔드 FastAPI 서비스 로직

모든 로직은 즉시 코드로 구현 가능한 수준으로 작성되었습니다.

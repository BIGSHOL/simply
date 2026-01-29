/**
 * 연애 유형 테스트 MSW Handler
 * Phase 1, T1-LOVE.3
 */
import { http, HttpResponse } from 'msw';
import { LOVE_TEST, LOVE_TYPE_RESULTS } from '../data/loveTestData';
import type { LoveTestAnswer } from '@/types/loveTest';

const BASE_URL = '/api/v1/tests/love-type';

// 점수 계산 로직 (content.md 기반)
interface ChoiceScore {
  proactivity: number;
  expression: number;
  independence: number;
  commitment: number;
  romance: number;
}

const QUESTION_SCORES: Record<string, Record<string, ChoiceScore>> = {
  Q1: {
    A: { proactivity: 2, expression: 0, independence: 0, commitment: 0, romance: 0 },
    B: { proactivity: 0, expression: 0, independence: 0, commitment: 0, romance: 0 },
  },
  Q2: {
    A: { proactivity: 0, expression: 2, independence: 0, commitment: 0, romance: 0 },
    B: { proactivity: 0, expression: 0, independence: 0, commitment: 0, romance: 0 },
  },
  Q3: {
    A: { proactivity: 0, expression: 0, independence: 0, commitment: 0, romance: 0 },
    B: { proactivity: 0, expression: 0, independence: 2, commitment: 0, romance: 0 },
  },
  Q4: {
    A: { proactivity: 2, expression: 0, independence: 0, commitment: 0, romance: 0 },
    B: { proactivity: 0, expression: 0, independence: 0, commitment: 0, romance: 0 },
  },
  Q5: {
    A: { proactivity: 0, expression: 2, independence: 0, commitment: 0, romance: 0 },
    B: { proactivity: 0, expression: 0, independence: 0, commitment: 0, romance: 0 },
  },
  Q6: {
    A: { proactivity: 0, expression: 0, independence: 0, commitment: 0, romance: 2 },
    B: { proactivity: 0, expression: 0, independence: 0, commitment: 0, romance: 0 },
  },
  Q7: {
    A: { proactivity: 0, expression: 0, independence: 2, commitment: 0, romance: 0 },
    B: { proactivity: 0, expression: 0, independence: 0, commitment: 0, romance: 0 },
  },
  Q8: {
    A: { proactivity: 2, expression: 0, independence: 0, commitment: 0, romance: 0 },
    B: { proactivity: 0, expression: 0, independence: 0, commitment: 0, romance: 0 },
  },
  Q9: {
    A: { proactivity: 0, expression: 2, independence: 0, commitment: 0, romance: 0 },
    B: { proactivity: 0, expression: 0, independence: 0, commitment: 0, romance: 0 },
  },
  Q10: {
    A: { proactivity: 0, expression: 0, independence: 0, commitment: 2, romance: 0 },
    B: { proactivity: 0, expression: 0, independence: 0, commitment: 0, romance: 0 },
  },
  Q11: {
    A: { proactivity: 0, expression: 0, independence: 0, commitment: 0, romance: 2 },
    B: { proactivity: 0, expression: 0, independence: 0, commitment: 0, romance: 0 },
  },
  Q12: {
    A: { proactivity: 2, expression: 0, independence: 0, commitment: 0, romance: 0 },
    B: { proactivity: 0, expression: 0, independence: 0, commitment: 0, romance: 0 },
  },
  Q13: {
    A: { proactivity: 0, expression: 0, independence: 0, commitment: 2, romance: 0 },
    B: { proactivity: 0, expression: 0, independence: 0, commitment: 0, romance: 0 },
  },
  Q14: {
    A: { proactivity: 0, expression: 2, independence: 0, commitment: 0, romance: 0 },
    B: { proactivity: 0, expression: 0, independence: 0, commitment: 0, romance: 0 },
  },
  Q15: {
    A: { proactivity: 0, expression: 0, independence: 0, commitment: 0, romance: 2 },
    B: { proactivity: 0, expression: 0, independence: 0, commitment: 0, romance: 0 },
  },
  Q16: {
    A: { proactivity: 0, expression: 0, independence: 2, commitment: 0, romance: 0 },
    B: { proactivity: 0, expression: 0, independence: 0, commitment: 0, romance: 0 },
  },
  Q17: {
    A: { proactivity: 2, expression: 0, independence: 0, commitment: 0, romance: 0 },
    B: { proactivity: 0, expression: 0, independence: 0, commitment: 0, romance: 0 },
  },
  Q18: {
    A: { proactivity: 0, expression: 0, independence: 0, commitment: 2, romance: 0 },
    B: { proactivity: 0, expression: 0, independence: 0, commitment: 0, romance: 0 },
  },
  Q19: {
    A: { proactivity: 0, expression: 0, independence: 0, commitment: 0, romance: 2 },
    B: { proactivity: 0, expression: 0, independence: 0, commitment: 0, romance: 0 },
  },
  Q20: {
    A: { proactivity: 0, expression: 0, independence: 0, commitment: 0, romance: 0 },
    B: { proactivity: 0, expression: 0, independence: 2, commitment: 0, romance: 0 },
  },
};

function calculateScores(answers: LoveTestAnswer[]) {
  const raw = {
    proactivity: 0,
    expression: 0,
    independence: 0,
    commitment: 0,
    romance: 0,
  };

  answers.forEach((answer) => {
    const scoreData = QUESTION_SCORES[answer.questionId]?.[answer.choice];
    if (scoreData) {
      raw.proactivity += scoreData.proactivity;
      raw.expression += scoreData.expression;
      raw.independence += scoreData.independence;
      raw.commitment += scoreData.commitment;
      raw.romance += scoreData.romance;
    }
  });

  // 정규화 (0-100)
  return {
    proactivity: Math.round((raw.proactivity / 10) * 100),
    expression: Math.round((raw.expression / 8) * 100),
    independence: Math.round((raw.independence / 8) * 100),
    commitment: Math.round((raw.commitment / 6) * 100),
    romance: Math.round((raw.romance / 8) * 100),
  };
}

function determineLoveType(scores: ReturnType<typeof calculateScores>): string {
  const { proactivity, expression, independence, commitment, romance } = scores;

  // 간단한 분류 로직 (실제로는 content.md의 복잡한 알고리즘 사용)
  if (proactivity >= 80 && romance >= 80) return 'romance_express';
  if (proactivity >= 70 && expression >= 70) return 'straight_shooter';
  if (proactivity >= 50 && expression < 50) return 'push_pull_master';

  // 기본값
  return 'straight_shooter';
}

export const loveTestHandlers = [
  // GET /api/v1/tests/love-type - 테스트 정보 조회
  http.get(BASE_URL, () => {
    return HttpResponse.json({
      data: LOVE_TEST,
      meta: {
        cached: false,
        generated_at: new Date().toISOString(),
      },
    });
  }),

  // POST /api/v1/tests/love-type/submit - 답변 제출 및 결과 조회
  http.post(`${BASE_URL}/submit`, async ({ request }) => {
    const body = (await request.json()) as { answers: LoveTestAnswer[] };

    // 점수 계산
    const scores = calculateScores(body.answers);

    // 유형 결정
    const typeId = determineLoveType(scores);

    // 결과 데이터
    const baseResult = LOVE_TYPE_RESULTS[typeId] || LOVE_TYPE_RESULTS.straight_shooter;
    const result = {
      ...baseResult,
      scores,
    };

    // 서버 연출을 위한 딜레이 (5초)
    await new Promise((resolve) => setTimeout(resolve, 5000));

    return HttpResponse.json({
      data: result,
      meta: {
        cached: false,
        generated_at: new Date().toISOString(),
      },
    });
  }),
];

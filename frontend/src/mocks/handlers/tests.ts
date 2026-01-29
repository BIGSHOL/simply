/**
 * 테스트 API Mock 핸들러
 *
 * Phase 0, T0.5.3: 프론트엔드 테스트 + MSW Mock
 */
import { http, HttpResponse, delay } from 'msw';
import { mockTestSummaries, mockTestDetail, mockResult } from '../data/mockTests';
import type { ApiResponse, TestSummary, Test, Result } from '@/types';

const API_BASE = 'http://localhost:8000/api/v1';

export const testsHandlers = [
  // GET /api/v1/tests - 테스트 목록 조회
  http.get(`${API_BASE}/tests`, async ({ request }) => {
    await delay(100);

    const url = new URL(request.url);
    const category = url.searchParams.get('category');

    let tests = mockTestSummaries;

    if (category) {
      tests = tests.filter((t) => t.category === category);
    }

    const response: ApiResponse<TestSummary[]> = {
      data: tests,
    };

    return HttpResponse.json(response);
  }),

  // GET /api/v1/tests/:id - 테스트 상세 조회
  http.get(`${API_BASE}/tests/:id`, async ({ params }) => {
    await delay(100);

    const { id } = params;

    if (id === 'not-found') {
      return HttpResponse.json(
        {
          error: {
            code: 'TEST_NOT_FOUND',
            message: '테스트를 찾을 수 없습니다',
          },
        },
        { status: 404 }
      );
    }

    const response: ApiResponse<Test> = {
      data: mockTestDetail,
    };

    return HttpResponse.json(response);
  }),

  // POST /api/v1/tests/:id/submit - 테스트 제출
  http.post(`${API_BASE}/tests/:id/submit`, async ({ params, request }) => {
    await delay(300); // AI 처리 시뮬레이션

    const { id } = params;
    const body = (await request.json()) as { answers: Array<{ question_id: string; choice_id: string }> };

    if (id === 'not-found') {
      return HttpResponse.json(
        {
          error: {
            code: 'TEST_NOT_FOUND',
            message: '테스트를 찾을 수 없습니다',
          },
        },
        { status: 404 }
      );
    }

    if (!body.answers || body.answers.length === 0) {
      return HttpResponse.json(
        {
          error: {
            code: 'INVALID_ANSWERS',
            message: '답변이 유효하지 않습니다',
          },
        },
        { status: 400 }
      );
    }

    const response: ApiResponse<Result> = {
      data: mockResult,
      meta: {
        cached: false,
        generated_at: new Date().toISOString(),
      },
    };

    return HttpResponse.json(response);
  }),
];

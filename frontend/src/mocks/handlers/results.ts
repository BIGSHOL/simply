/**
 * 결과 API Mock 핸들러
 *
 * Phase 0, T0.5.3: 프론트엔드 테스트 + MSW Mock
 */
import { http, HttpResponse, delay } from 'msw';
import { mockResult } from '../data/mockTests';
import type { ApiResponse, Result } from '@/types';

const API_BASE = 'http://localhost:8000/api/v1';

export const resultsHandlers = [
  // GET /api/v1/results/:id - 결과 조회 (ID 또는 share_code)
  http.get(`${API_BASE}/results/:id`, async ({ params }) => {
    await delay(100);

    const { id } = params;

    if (id === 'not-found') {
      return HttpResponse.json(
        {
          error: {
            code: 'RESULT_NOT_FOUND',
            message: '결과를 찾을 수 없습니다',
          },
        },
        { status: 404 }
      );
    }

    if (id === 'expired') {
      return HttpResponse.json(
        {
          error: {
            code: 'RESULT_EXPIRED',
            message: '결과가 만료되었습니다',
          },
        },
        { status: 410 }
      );
    }

    const response: ApiResponse<Result> = {
      data: mockResult,
    };

    return HttpResponse.json(response);
  }),

  // POST /api/v1/results/:id/share - 공유 링크 생성
  http.post(`${API_BASE}/results/:id/share`, async ({ params }) => {
    await delay(100);

    const { id } = params;

    if (id === 'not-found') {
      return HttpResponse.json(
        {
          error: {
            code: 'RESULT_NOT_FOUND',
            message: '결과를 찾을 수 없습니다',
          },
        },
        { status: 404 }
      );
    }

    const response: ApiResponse<{ share_url: string; short_code: string }> = {
      data: {
        share_url: `https://simly.app/r/${mockResult.share_code}`,
        short_code: mockResult.share_code,
      },
    };

    return HttpResponse.json(response);
  }),
];

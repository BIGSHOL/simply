/**
 * Test API 계약
 *
 * 이 파일은 백엔드-프론트엔드 간 API 계약을 정의합니다.
 * 백엔드의 Pydantic 스키마와 프론트엔드의 타입이 이 계약을 따릅니다.
 */

import type {
  TestListResponse,
  TestDetailResponse,
  SubmitRequest,
  SubmitResponse,
  ResultResponse,
} from './types';

// =============================================================================
// GET /api/v1/tests
// =============================================================================
export interface GetTestsContract {
  method: 'GET';
  path: '/api/v1/tests';
  query?: {
    category?: 'personality' | 'love' | 'career' | 'fun';
    limit?: number;
    offset?: number;
  };
  response: TestListResponse;
}

// =============================================================================
// GET /api/v1/tests/:id
// =============================================================================
export interface GetTestDetailContract {
  method: 'GET';
  path: '/api/v1/tests/:id';
  params: {
    id: string; // UUID
  };
  response: TestDetailResponse;
  errors: {
    404: { code: 'TEST_NOT_FOUND'; message: '테스트를 찾을 수 없습니다.' };
  };
}

// =============================================================================
// POST /api/v1/tests/:id/submit
// =============================================================================
export interface SubmitTestContract {
  method: 'POST';
  path: '/api/v1/tests/:id/submit';
  params: {
    id: string; // UUID
  };
  body: SubmitRequest;
  response: SubmitResponse;
  errors: {
    400: { code: 'INVALID_ANSWERS'; message: '답변이 유효하지 않습니다.' };
    404: { code: 'TEST_NOT_FOUND'; message: '테스트를 찾을 수 없습니다.' };
    429: { code: 'RATE_LIMIT_EXCEEDED'; message: '잠시 후 다시 시도해주세요.'; retry_after: number };
    500: { code: 'AI_ERROR'; message: 'AI 분석 중 오류가 발생했습니다.' };
  };
}

// =============================================================================
// GET /api/v1/results/:id
// =============================================================================
export interface GetResultContract {
  method: 'GET';
  path: '/api/v1/results/:id';
  params: {
    id: string; // UUID 또는 share_code
  };
  response: ResultResponse;
  errors: {
    404: { code: 'RESULT_NOT_FOUND'; message: '결과를 찾을 수 없습니다.' };
    410: { code: 'RESULT_EXPIRED'; message: '결과가 만료되었습니다.' };
  };
}

// =============================================================================
// POST /api/v1/results/:id/share
// =============================================================================
export interface CreateShareLinkContract {
  method: 'POST';
  path: '/api/v1/results/:id/share';
  params: {
    id: string; // UUID
  };
  response: {
    data: {
      share_url: string;
      short_code: string;
      expires_at: string;
    };
  };
  errors: {
    404: { code: 'RESULT_NOT_FOUND'; message: '결과를 찾을 수 없습니다.' };
  };
}

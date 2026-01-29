/**
 * Vitest 테스트 설정
 *
 * Phase 0, T0.5.3: 프론트엔드 테스트 + MSW Mock
 */
import '@testing-library/jest-dom/vitest';
import { expect, afterEach, beforeAll, afterAll } from 'vitest';
import { cleanup } from '@testing-library/react';
import { server } from '@/mocks/server';

// MSW 서버 시작
beforeAll(() => {
  server.listen({ onUnhandledRequest: 'warn' });
});

// 각 테스트 후 cleanup
afterEach(() => {
  cleanup();
  server.resetHandlers();
});

// 테스트 완료 후 서버 종료
afterAll(() => {
  server.close();
});

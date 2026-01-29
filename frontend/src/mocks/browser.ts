/**
 * MSW 브라우저 설정 (개발용)
 *
 * Phase 0, T0.5.3: 프론트엔드 테스트 + MSW Mock
 *
 * 사용법:
 * if (process.env.NEXT_PUBLIC_API_MOCKING === 'enabled') {
 *   const { worker } = await import('@/mocks/browser');
 *   worker.start();
 * }
 */
import { setupWorker } from 'msw/browser';
import { handlers } from './handlers';

export const worker = setupWorker(...handlers);

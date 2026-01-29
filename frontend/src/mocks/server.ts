/**
 * MSW 서버 설정 (테스트용)
 *
 * Phase 0, T0.5.3: 프론트엔드 테스트 + MSW Mock
 */
import { setupServer } from 'msw/node';
import { handlers } from './handlers';

export const server = setupServer(...handlers);

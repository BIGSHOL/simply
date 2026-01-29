/**
 * MSW 핸들러 통합
 *
 * Phase 0, T0.5.3: 프론트엔드 테스트 + MSW Mock
 * Phase 1, T1-LOVE.3: 연애 유형 테스트 추가
 */
import { testsHandlers } from './tests';
import { resultsHandlers } from './results';
import { loveTestHandlers } from './loveTest';

export const handlers = [...testsHandlers, ...resultsHandlers, ...loveTestHandlers];

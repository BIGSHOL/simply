/**
 * Tests API 통합 테스트 스켈레톤 (RED 상태)
 *
 * Phase 0, T0.5.3: 프론트엔드 테스트 + MSW Mock
 */
import { describe, it, expect } from 'vitest';
import { getTests, getTest, submitTest } from '@/lib/api';
import { mockTestSummaries, mockTestDetail, mockResult } from '@/mocks/data/mockTests';

describe('Tests API', () => {
  describe('getTests', () => {
    it('테스트 목록을 반환해야 한다', async () => {
      const response = await getTests();
      expect(response.data).toBeDefined();
      expect(Array.isArray(response.data)).toBe(true);
      expect(response.data.length).toBeGreaterThan(0);
    });

    it.skip('카테고리 필터링이 동작해야 한다', async () => {
      // TODO: Phase 1, T1.3에서 구현 예정
      // const response = await getTests({ category: 'love' });
      // expect(response.data.every(t => t.category === 'love')).toBe(true);
    });
  });

  describe('getTest', () => {
    it('테스트 상세 정보를 반환해야 한다', async () => {
      const response = await getTest(mockTestDetail.id);
      expect(response.data).toBeDefined();
      expect(response.data.id).toBe(mockTestDetail.id);
      expect(response.data.questions).toBeDefined();
    });

    it('존재하지 않는 테스트는 에러를 반환해야 한다', async () => {
      await expect(getTest('not-found')).rejects.toThrow();
    });
  });

  describe('submitTest', () => {
    it.skip('AI 결과를 생성해야 한다', async () => {
      // TODO: Phase 2, T2.3에서 구현 예정
      // const answers = mockTestDetail.questions.map((q) => ({
      //   question_id: q.id,
      //   choice_id: q.choices[0].id,
      // }));
      // const response = await submitTest(mockTestDetail.id, answers);
      // expect(response.data.result_title).toBeDefined();
      // expect(response.data.result_content).toBeDefined();
    });

    it.skip('잘못된 답변은 에러를 반환해야 한다', async () => {
      // TODO: Phase 2, T2.3에서 구현 예정
      // await expect(submitTest(mockTestDetail.id, [])).rejects.toThrow();
    });

    it.skip('캐시된 결과는 meta.cached가 true여야 한다', async () => {
      // TODO: Phase 2, T2.3에서 구현 예정
    });
  });
});

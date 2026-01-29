/**
 * Results API 통합 테스트 스켈레톤 (RED 상태)
 *
 * Phase 0, T0.5.3: 프론트엔드 테스트 + MSW Mock
 */
import { describe, it, expect } from 'vitest';
import { getResult } from '@/lib/api';
import { mockResult } from '@/mocks/data/mockTests';

describe('Results API', () => {
  describe('getResult', () => {
    it('결과를 ID로 조회할 수 있어야 한다', async () => {
      const response = await getResult(mockResult.id);
      expect(response.data).toBeDefined();
      expect(response.data.id).toBe(mockResult.id);
    });

    it('결과를 share_code로 조회할 수 있어야 한다', async () => {
      const response = await getResult(mockResult.share_code);
      expect(response.data).toBeDefined();
      expect(response.data.share_code).toBe(mockResult.share_code);
    });

    it('존재하지 않는 결과는 에러를 반환해야 한다', async () => {
      await expect(getResult('not-found')).rejects.toThrow();
    });

    it.skip('만료된 결과는 410 에러를 반환해야 한다', async () => {
      // TODO: Phase 3, T3.2에서 구현 예정
      // await expect(getResult('expired')).rejects.toThrow('결과가 만료되었습니다');
    });
  });

  describe('createShareLink', () => {
    it.skip('공유 링크를 생성할 수 있어야 한다', async () => {
      // TODO: Phase 3, T3.2에서 구현 예정
      // const response = await createShareLink(mockResult.id);
      // expect(response.data.share_url).toBeDefined();
      // expect(response.data.short_code).toBeDefined();
    });
  });
});

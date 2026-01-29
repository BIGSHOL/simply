/**
 * 테스트 상세/시작 페이지
 *
 * Phase 2, T2.2: 테스트 진행 화면
 */
'use client';

import { useEffect, useState } from 'react';
import { useParams, useRouter } from 'next/navigation';
import { Button, Card } from '@/components/ui';
import { getTest } from '@/lib/api';
import { useTestStore } from '@/stores/testStore';
import type { Test } from '@/types';

const categoryLabels: Record<string, string> = {
  personality: '성격',
  love: '연애',
  career: '직장',
  fun: '재미',
};

export default function TestDetailPage() {
  const params = useParams();
  const router = useRouter();
  const testId = params.id as string;

  const [test, setTest] = useState<Test | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const { setTest: setStoreTest, reset } = useTestStore();

  useEffect(() => {
    async function fetchTest() {
      try {
        setIsLoading(true);
        setError(null);
        const response = await getTest(testId);
        setTest(response.data);
      } catch (err) {
        setError('테스트를 불러오는데 실패했습니다.');
        console.error('Failed to fetch test:', err);
      } finally {
        setIsLoading(false);
      }
    }

    if (testId) {
      fetchTest();
    }
  }, [testId]);

  const handleStart = () => {
    if (test) {
      reset();
      setStoreTest(test);
      router.push(`/tests/${testId}/play`);
    }
  };

  if (isLoading) {
    return (
      <div className="max-w-[600px] mx-auto px-4 sm:px-5 py-8">
        <div className="animate-pulse">
          <div className="h-8 w-3/4 bg-gray-200 rounded mb-4" />
          <div className="h-5 w-full bg-gray-200 rounded mb-2" />
          <div className="h-5 w-2/3 bg-gray-200 rounded mb-6" />
          <div className="h-12 w-full bg-gray-200 rounded" />
        </div>
      </div>
    );
  }

  if (error || !test) {
    return (
      <div className="max-w-[600px] mx-auto px-4 sm:px-5 py-8">
        <Card className="text-center py-10">
          <p className="text-[#EF4444] mb-4">{error || '테스트를 찾을 수 없습니다.'}</p>
          <Button variant="secondary" onClick={() => router.push('/')}>
            홈으로 돌아가기
          </Button>
        </Card>
      </div>
    );
  }

  return (
    <div className="max-w-[600px] mx-auto px-4 sm:px-5 py-8">
      {/* 테스트 정보 */}
      <div className="text-center mb-8">
        <span className="inline-block text-sm px-3 py-1.5 rounded-full bg-[#E0E7FF] text-[#6366F1] font-medium mb-4">
          {categoryLabels[test.category] || test.category}
        </span>

        <h1 className="text-xl sm:text-2xl font-bold text-[#111827] mb-3">
          {test.title}
        </h1>

        <p className="text-[#6B7280] mb-4">
          {test.description}
        </p>

        <div className="flex items-center justify-center gap-4 text-sm text-[#9CA3AF]">
          <span>{test.question_count}문항</span>
          <span>•</span>
          <span>{test.play_count.toLocaleString()}명 참여</span>
        </div>
      </div>

      {/* 시작 버튼 */}
      <div className="space-y-4">
        <Button fullWidth size="large" onClick={handleStart}>
          테스트 시작하기
        </Button>

        <p className="text-center text-xs text-[#9CA3AF]">
          AI가 당신의 답변을 분석하여 맞춤 결과를 알려드려요
        </p>
      </div>
    </div>
  );
}

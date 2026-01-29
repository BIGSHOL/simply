/**
 * TestList 컴포넌트
 *
 * Phase 2, T2.1: 테스트 목록 화면
 */
'use client';

import { useEffect, useState } from 'react';
import TestCard from './TestCard';
import { getTests } from '@/lib/api';
import type { TestSummary } from '@/types';

interface TestListProps {
  category?: string;
}

export default function TestList({ category }: TestListProps) {
  const [tests, setTests] = useState<TestSummary[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function fetchTests() {
      try {
        setIsLoading(true);
        setError(null);
        const response = await getTests();
        setTests(response.data);
      } catch (err) {
        setError('테스트 목록을 불러오는데 실패했습니다.');
        console.error('Failed to fetch tests:', err);
      } finally {
        setIsLoading(false);
      }
    }

    fetchTests();
  }, [category]);

  if (isLoading) {
    return (
      <div className="flex flex-col gap-4">
        {[1, 2, 3].map((i) => (
          <div
            key={i}
            className="bg-white border border-[#E5E7EB] rounded-2xl p-4 animate-pulse"
          >
            <div className="flex items-center gap-2 mb-3">
              <div className="h-5 w-12 bg-gray-200 rounded-full" />
              <div className="h-4 w-10 bg-gray-200 rounded" />
            </div>
            <div className="h-5 w-3/4 bg-gray-200 rounded mb-2" />
            <div className="h-4 w-full bg-gray-200 rounded mb-3" />
            <div className="flex justify-between">
              <div className="h-4 w-20 bg-gray-200 rounded" />
              <div className="h-4 w-24 bg-gray-200 rounded" />
            </div>
          </div>
        ))}
      </div>
    );
  }

  if (error) {
    return (
      <div className="bg-red-50 border border-red-200 rounded-xl p-4 text-center">
        <p className="text-red-600 text-sm">{error}</p>
        <button
          onClick={() => window.location.reload()}
          className="mt-2 text-sm text-[#6366F1] font-medium"
        >
          다시 시도
        </button>
      </div>
    );
  }

  if (tests.length === 0) {
    return (
      <div className="text-center py-10">
        <p className="text-[#6B7280]">아직 등록된 테스트가 없습니다.</p>
      </div>
    );
  }

  return (
    <div className="flex flex-col gap-4">
      {tests.map((test) => (
        <TestCard key={test.id} test={test} />
      ))}
    </div>
  );
}

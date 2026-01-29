/**
 * CategoryList 컴포넌트
 *
 * 카테고리별 테스트 목록 - 아코디언 형태
 */
'use client';

import { useEffect, useState } from 'react';
import CategoryCard, { CATEGORIES, CategoryId } from './CategoryCard';
import { getTests } from '@/lib/api';
import type { TestSummary } from '@/types';

export default function CategoryList() {
  const [tests, setTests] = useState<TestSummary[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [expandedCategory, setExpandedCategory] = useState<CategoryId | null>(null);

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
  }, []);

  // 카테고리별 테스트 분류
  const testsByCategory = (categoryId: CategoryId) =>
    tests.filter((test) => test.category === categoryId);

  // 카테고리별 테스트 개수 계산
  const getCategoryCount = (categoryId: CategoryId) =>
    testsByCategory(categoryId).length;

  // 카테고리 토글
  const handleToggle = (categoryId: CategoryId) => {
    setExpandedCategory(expandedCategory === categoryId ? null : categoryId);
  };

  if (isLoading) {
    return (
      <div className="flex flex-col gap-4">
        {[1, 2, 3, 4].map((i) => (
          <div
            key={i}
            className="bg-white border border-[#E5E7EB] rounded-2xl p-5 animate-pulse"
          >
            <div className="flex items-center gap-4">
              <div className="w-14 h-14 bg-gray-200 rounded-xl" />
              <div className="flex-1">
                <div className="h-5 w-32 bg-gray-200 rounded mb-2" />
                <div className="h-4 w-48 bg-gray-200 rounded" />
              </div>
              <div className="h-6 w-12 bg-gray-200 rounded-full" />
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

  // 테스트가 있는 카테고리만 표시 (또는 모든 카테고리 표시)
  const categoryIds = Object.keys(CATEGORIES) as CategoryId[];

  return (
    <div className="flex flex-col">
      {categoryIds.map((categoryId) => (
        <CategoryCard
          key={categoryId}
          categoryId={categoryId}
          tests={testsByCategory(categoryId)}
          isExpanded={expandedCategory === categoryId}
          onToggle={() => handleToggle(categoryId)}
        />
      ))}

      {/* 전체 테스트 수 표시 */}
      <div className="mt-6 text-center">
        <p className="text-sm text-[#9CA3AF]">
          총 <span className="font-medium text-[#6366F1]">{tests.length}</span>개의 테스트가 준비되어 있어요!
        </p>
      </div>
    </div>
  );
}

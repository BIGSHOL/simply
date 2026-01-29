/**
 * CategoryCard 컴포넌트
 *
 * 카테고리 카드 - 클릭하면 해당 카테고리의 테스트 목록이 펼쳐짐
 */
'use client';

import { useState } from 'react';
import TestCard from './TestCard';
import type { TestSummary } from '@/types';

// 카테고리 정보
export const CATEGORIES = {
  personality: {
    id: 'personality',
    name: '성격 테스트',
    emoji: '🧠',
    description: '나의 성격과 성향을 알아보세요',
    color: 'from-purple-500 to-indigo-500',
    bgColor: 'bg-purple-50',
    borderColor: 'border-purple-200',
  },
  love: {
    id: 'love',
    name: '연애 테스트',
    emoji: '💕',
    description: '나의 연애 스타일은?',
    color: 'from-pink-500 to-rose-500',
    bgColor: 'bg-pink-50',
    borderColor: 'border-pink-200',
  },
  career: {
    id: 'career',
    name: '직장/커리어',
    emoji: '💼',
    description: '직장에서 나의 유형 파악하기',
    color: 'from-blue-500 to-cyan-500',
    bgColor: 'bg-blue-50',
    borderColor: 'border-blue-200',
  },
  fun: {
    id: 'fun',
    name: '재미 테스트',
    emoji: '🎮',
    description: '재미로 즐기는 테스트',
    color: 'from-amber-500 to-orange-500',
    bgColor: 'bg-amber-50',
    borderColor: 'border-amber-200',
  },
} as const;

export type CategoryId = keyof typeof CATEGORIES;

interface CategoryCardProps {
  categoryId: CategoryId;
  tests: TestSummary[];
  isExpanded: boolean;
  onToggle: () => void;
}

export default function CategoryCard({
  categoryId,
  tests,
  isExpanded,
  onToggle,
}: CategoryCardProps) {
  const category = CATEGORIES[categoryId];
  const testCount = tests.length;

  return (
    <div className="mb-4">
      {/* 카테고리 헤더 (클릭 가능) */}
      <button
        onClick={onToggle}
        className={`
          w-full text-left rounded-2xl p-5 transition-all duration-300
          ${isExpanded
            ? `${category.bgColor} ${category.borderColor} border-2 shadow-md`
            : 'bg-white border border-[#E5E7EB] hover:border-[#D1D5DB] hover:shadow-sm'
          }
        `}
      >
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-4">
            {/* 이모지 아이콘 */}
            <div className={`
              w-14 h-14 rounded-xl flex items-center justify-center text-2xl
              bg-gradient-to-br ${category.color} shadow-lg
            `}>
              {category.emoji}
            </div>

            {/* 카테고리 정보 */}
            <div>
              <h3 className="text-lg font-bold text-[#111827]">
                {category.name}
              </h3>
              <p className="text-sm text-[#6B7280]">
                {category.description}
              </p>
            </div>
          </div>

          {/* 테스트 개수 + 화살표 */}
          <div className="flex items-center gap-3">
            <span className={`
              px-3 py-1 rounded-full text-sm font-medium
              ${isExpanded ? 'bg-white text-[#6366F1]' : 'bg-[#F3F4F6] text-[#6B7280]'}
            `}>
              {testCount}개
            </span>
            <svg
              className={`w-5 h-5 text-[#9CA3AF] transition-transform duration-300 ${
                isExpanded ? 'rotate-180' : ''
              }`}
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
            </svg>
          </div>
        </div>
      </button>

      {/* 테스트 목록 (펼쳐질 때) */}
      <div
        className={`
          overflow-hidden transition-all duration-300 ease-in-out
          ${isExpanded ? 'max-h-[2000px] opacity-100 mt-3' : 'max-h-0 opacity-0'}
        `}
      >
        <div className="pl-4 border-l-2 border-[#E5E7EB] ml-7 flex flex-col gap-3">
          {tests.length > 0 ? (
            tests.map((test) => (
              <TestCard key={test.id} test={test} compact />
            ))
          ) : (
            <p className="text-sm text-[#9CA3AF] py-4">
              아직 등록된 테스트가 없습니다.
            </p>
          )}
        </div>
      </div>
    </div>
  );
}

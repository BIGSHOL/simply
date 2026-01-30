/**
 * TestCard 컴포넌트
 *
 * Phase 2, T2.1: 테스트 목록 화면
 * compact 모드: 카테고리 내 테스트 목록용 간결한 버전
 */
'use client';

import Link from 'next/link';
import { Card } from '@/components/ui';
import type { TestSummary } from '@/types';

interface TestCardProps {
  test: TestSummary;
  compact?: boolean;
}

const categoryLabels: Record<string, string> = {
  personality: '성격',
  love: '연애',
  career: '직장',
  fun: '재미',
};

const categoryColors: Record<string, string> = {
  personality: 'bg-purple-100 text-purple-700',
  love: 'bg-pink-100 text-pink-700',
  career: 'bg-blue-100 text-blue-700',
  fun: 'bg-yellow-100 text-yellow-700',
};

function formatPlayCount(count: number): string {
  if (count >= 10000) {
    return `${(count / 10000).toFixed(1)}만`;
  }
  if (count >= 1000) {
    return `${(count / 1000).toFixed(1)}천`;
  }
  return count.toLocaleString();
}

export default function TestCard({ test, compact = false }: TestCardProps) {
  // Compact 모드 (카테고리 내 테스트 목록용)
  if (compact) {
    return (
      <Link href={`/tests/${test.id}`}>
        <div className="bg-white border border-[#E5E7EB] rounded-xl p-4 hover:border-[#6366F1] hover:shadow-sm transition-all cursor-pointer">
          <div className="flex items-center justify-between">
            <div className="flex-1 min-w-0">
              <h4 className="text-base font-medium text-[#111827] line-clamp-2">
                {test.title}
              </h4>
              <div className="flex items-center gap-2 mt-1">
                <span className="text-xs text-[#9CA3AF]">
                  {test.question_count}문항
                </span>
                <span className="text-xs text-[#9CA3AF]">•</span>
                <span className="text-xs text-[#9CA3AF]">
                  {formatPlayCount(test.play_count)}명 참여
                </span>
              </div>
            </div>
            <div className="ml-4 flex-shrink-0">
              <span className="text-sm text-[#6366F1] font-medium whitespace-nowrap">
                시작 →
              </span>
            </div>
          </div>
        </div>
      </Link>
    );
  }

  // 기본 모드 (전체 목록용)
  return (
    <Link href={`/tests/${test.id}`}>
      <Card className="cursor-pointer">
        <div className="flex flex-col gap-2">
          <div className="flex items-center gap-2">
            <span
              className={`text-xs px-2 py-0.5 rounded-full font-medium ${
                categoryColors[test.category] || 'bg-gray-100 text-gray-700'
              }`}
            >
              {categoryLabels[test.category] || test.category}
            </span>
            <span className="text-xs text-[#9CA3AF]">
              {test.question_count}문항
            </span>
          </div>

          <h3 className="text-base font-semibold text-[#111827]">
            {test.title}
          </h3>

          <p className="text-sm text-[#6B7280] line-clamp-2">
            {test.description}
          </p>

          <div className="flex items-center justify-between mt-1">
            <span className="text-xs text-[#9CA3AF]">
              {formatPlayCount(test.play_count)}명 참여
            </span>
            <span className="text-sm text-[#6366F1] font-medium">
              테스트 하기 →
            </span>
          </div>
        </div>
      </Card>
    </Link>
  );
}

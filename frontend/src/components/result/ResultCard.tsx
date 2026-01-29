/**
 * ResultCard 컴포넌트
 *
 * Phase 3, T3.2: 결과 페이지 UI
 */
'use client';

import Image from 'next/image';
import Link from 'next/link';
import { Button } from '@/components/ui';
import type { Result } from '@/types';

interface ResultCardProps {
  result: Result;
  onShare: (shareCode: string) => void;
}

export default function ResultCard({ result, onShare }: ResultCardProps) {
  return (
    <div className="bg-white rounded-2xl shadow-lg overflow-hidden">
      {/* 결과 이미지 */}
      {result.result_image_url && (
        <div className="relative w-full aspect-video">
          <Image
            src={result.result_image_url}
            alt={result.result_title}
            fill
            className="object-cover"
          />
        </div>
      )}

      {/* 결과 내용 */}
      <div className="p-4 sm:p-6">
        {/* 결과 타입 배지 */}
        <div className="flex justify-center mb-4">
          <span className="inline-block px-4 py-2 rounded-full bg-[#E0E7FF] text-[#6366F1] font-bold text-sm">
            {result.result_type}
          </span>
        </div>

        {/* 결과 제목 */}
        <h1 className="text-xl sm:text-2xl font-bold text-center text-[#111827] mb-6">
          {result.result_title}
        </h1>

        {/* 결과 내용 (마크다운 렌더링) */}
        <div
          className="prose prose-sm max-w-none text-[#374151]"
          dangerouslySetInnerHTML={{ __html: parseMarkdown(result.result_content) }}
        />

        {/* 버튼 영역 */}
        <div className="mt-8 space-y-3">
          <Button
            fullWidth
            onClick={() => onShare(result.share_code)}
            aria-label="결과 공유하기"
          >
            결과 공유하기
          </Button>

          <Link href={`/tests/${result.test_id}`}>
            <Button fullWidth variant="secondary">
              다시 테스트하기
            </Button>
          </Link>
        </div>
      </div>
    </div>
  );
}

/**
 * 마크다운 파서 (헤더, 볼드, 리스트, 이모지, 구분선)
 * MZ 감성 결과 화면용 확장 파서
 */
function parseMarkdown(text: string): string {
  return text
    // 구분선
    .replace(/^---$/gm, '<hr class="my-4 border-t border-[#E5E7EB]" />')
    // 헤더
    .replace(/^### (.*$)/gm, '<h4 class="text-base font-bold mt-4 mb-2 text-[#374151] flex items-center gap-2">$1</h4>')
    .replace(/^## (.*$)/gm, '<h3 class="text-lg font-bold mt-5 mb-3 text-[#111827]">$1</h3>')
    .replace(/^# (.*$)/gm, '<h2 class="text-xl font-bold mt-5 mb-3 text-[#111827]">$1</h2>')
    // 볼드
    .replace(/\*\*(.*?)\*\*/g, '<strong class="font-semibold text-[#111827]">$1</strong>')
    // 이탤릭 (공유 멘트 등)
    .replace(/^\*(.*?)\*$/gm, '<p class="italic text-[#6B7280] text-sm mt-4 text-center">$1</p>')
    // 리스트
    .replace(/^- (.*$)/gm, '<li class="ml-4 my-1 list-disc list-inside">$1</li>')
    // 이모지 라벨 (궁합 등)
    .replace(/^([💘👍👎💪📝🔥💡🎯❤️⭐✅🍕🌶️🍰🍛🍣🥗🍵🍚]) (.*$)/gm, '<p class="flex items-start gap-2 my-2"><span class="text-lg">$1</span><span>$2</span></p>')
    // 화살표 리스트 (TMI 등)
    .replace(/^→ (.*$)/gm, '<p class="flex items-start gap-2 my-1 pl-2"><span class="text-[#FB923C]">→</span><span>$2</span></p>')
    // 줄바꿈
    .replace(/\n\n/g, '</p><p class="my-2">')
    .replace(/\n/g, '<br />');
}

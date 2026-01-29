/**
 * 결과 페이지 클라이언트 컴포넌트
 *
 * Phase 3, T3.2-T3.3: 결과 페이지 UI & 공유 기능
 */
'use client';

import { useRouter } from 'next/navigation';
import { Button, Card } from '@/components/ui';
import { ResultCard, ShareButtons } from '@/components/result';
import { AdSense } from '@/components/ads';
import type { Result } from '@/types';

interface ResultPageClientProps {
  result: Result;
  testTitle?: string;
}

export default function ResultPageClient({ result, testTitle }: ResultPageClientProps) {
  const router = useRouter();

  const getShareUrl = () => {
    if (typeof window === 'undefined') return '';
    return `${window.location.origin}/results/${result.share_code || result.id}`;
  };

  const handleShare = async (shareCode: string) => {
    const shareUrl = `${window.location.origin}/results/${shareCode}`;

    // Web Share API 시도
    if (navigator.share) {
      try {
        await navigator.share({
          title: result.result_title || '심리 테스트 결과',
          text: `나의 결과: ${result.result_type}`,
          url: shareUrl,
        });
        return;
      } catch (err) {
        if ((err as Error).name !== 'AbortError') {
          console.error('Share failed:', err);
        }
      }
    }

    // 클립보드에 복사
    if (navigator.clipboard) {
      try {
        await navigator.clipboard.writeText(shareUrl);
        alert('링크가 복사되었습니다!');
        return;
      } catch (err) {
        console.error('Clipboard copy failed:', err);
      }
    }

    // 폴백: 프롬프트로 표시
    prompt('결과 링크를 복사하세요:', shareUrl);
  };

  const handleTryTest = () => {
    router.push(`/tests/${result.test_id}`);
  };

  return (
    <div className="max-w-[600px] mx-auto px-4 sm:px-5 py-8">
      {/* 결과 카드 */}
      <ResultCard result={result} onShare={handleShare} />

      {/* SNS 공유 버튼 */}
      <div className="mt-8 p-4 sm:p-6 bg-white rounded-2xl shadow-lg">
        <ShareButtons
          shareUrl={getShareUrl()}
          title={`${result.result_type} - ${result.result_title}`}
          description="AI 심리 테스트 결과를 확인해보세요!"
        />
      </div>

      {/* 나도 해보기 버튼 */}
      <div className="mt-6 p-4 sm:p-6 bg-gradient-to-r from-[#E0E7FF] to-[#EDE9FE] rounded-2xl text-center">
        <p className="text-[#4B5563] mb-3">
          {testTitle ? `"${testTitle}"` : '이 테스트'}가 궁금하다면?
        </p>
        <Button onClick={handleTryTest} size="large" fullWidth>
          나도 해보러 가기! 🎯
        </Button>
      </div>

      {/* 다른 테스트 보러가기 */}
      <div className="mt-4 p-4 sm:p-6 bg-[#F9FAFB] rounded-2xl text-center border border-[#E5E7EB]">
        <p className="text-[#6B7280] mb-3">
          다른 심리테스트도 궁금하지 않으세요? 🤔
        </p>
        <Button
          onClick={() => router.push('/')}
          variant="secondary"
          size="large"
          fullWidth
        >
          다른 테스트 둘러보기 📂
        </Button>
      </div>

      {/* 광고 영역 */}
      <div className="mt-8">
        <AdSense
          slot="RESULT_BOTTOM_SLOT"
          format="rectangle"
          className="rounded-xl overflow-hidden"
        />
      </div>
    </div>
  );
}

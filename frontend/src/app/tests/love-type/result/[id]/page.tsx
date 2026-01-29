/**
 * 연애 유형 테스트 - 결과 페이지
 * Phase 1, T1-LOVE.3
 */
'use client';

import React from 'react';
import Link from 'next/link';
import { useParams } from 'next/navigation';
import { useLoveTestStore } from '@/stores/loveTestStore';
import { ResultCard, ShareButtons } from '@/components/loveTest';
import type { SharePlatform } from '@/types/loveTest';

export default function LoveTypeResultPage() {
  const params = useParams();
  const typeId = params.id as string;
  const { result, reset } = useLoveTestStore();

  // 결과가 없으면 랜딩으로 리다이렉트 (실제로는 useEffect + router 사용)
  if (!result) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-pink-50 to-purple-50 flex items-center justify-center">
        <div className="text-center space-y-4">
          <p className="text-gray-600">결과를 불러오는 중...</p>
          <Link
            href="/tests/love-type"
            className="inline-block text-pink-600 hover:text-pink-700 font-medium"
          >
            테스트 페이지로 돌아가기 →
          </Link>
        </div>
      </div>
    );
  }

  const handleShare = (platform: SharePlatform) => {
    console.log('Share to:', platform);
    // 실제 공유 로직
  };

  const handleRetry = () => {
    reset();
  };

  const shareData = {
    title: `나의 연애 유형: ${result.typeName}`,
    description: result.tagline,
    imageUrl: result.characterImage || '/images/love-type-thumbnail.png',
    url: `https://simly.kr/tests/love-type/result/${typeId}`,
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-pink-50 to-purple-50">
      <div className="max-w-4xl mx-auto px-4 py-8 space-y-8">
        {/* 고정 헤더 */}
        <div className="sticky top-0 z-10 bg-white/80 backdrop-blur-sm rounded-xl p-4 shadow-md flex justify-between items-center">
          <Link
            href="/tests/love-type"
            className="text-gray-600 hover:text-gray-800 font-medium"
          >
            ← 홈
          </Link>
          <button
            onClick={() => {
              /* Share bottom sheet */
            }}
            className="bg-gradient-to-r from-pink-500 to-purple-500 text-white font-bold px-6 py-2 rounded-full shadow-md hover:shadow-lg transition-all"
          >
            공유하기
          </button>
        </div>

        {/* 결과 카드 */}
        <ResultCard result={result} showAnimation={true} variant="full" />

        {/* 공유 버튼 */}
        <div className="bg-white rounded-2xl shadow-xl p-6">
          <ShareButtons shareData={shareData} onShare={handleShare} />
        </div>

        {/* 액션 버튼 */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <Link
            href="/tests/love-type"
            onClick={handleRetry}
            className="block bg-white text-center border-2 border-gray-300 text-gray-700 font-bold px-6 py-4 rounded-xl shadow-md hover:shadow-lg transition-all"
          >
            다시 테스트하기
          </Link>

          <Link
            href="/"
            className="block bg-gradient-to-r from-purple-500 to-pink-500 text-center text-white font-bold px-6 py-4 rounded-xl shadow-md hover:shadow-lg transition-all"
          >
            다른 테스트 보기
          </Link>
        </div>

        {/* 추가 정보 */}
        <div className="text-center space-y-2 text-sm text-gray-600">
          <p>이 결과는 심리학 이론에 기반한 분석이에요</p>
          <p>재미로 즐겨주세요! 💕</p>
        </div>
      </div>
    </div>
  );
}

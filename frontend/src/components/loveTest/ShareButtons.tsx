/**
 * 연애 유형 테스트 - 공유 버튼 컴포넌트
 * Phase 1, T1-LOVE.3
 */
'use client';

import React, { useState } from 'react';
import type { SharePlatform, ShareData } from '@/types/loveTest';

interface ShareButtonsProps {
  shareData: ShareData;
  onShare?: (platform: SharePlatform) => void;
}

export const ShareButtons: React.FC<ShareButtonsProps> = ({ shareData, onShare }) => {
  const [copied, setCopied] = useState(false);

  const handleCopyLink = async () => {
    try {
      await navigator.clipboard.writeText(shareData.url);
      setCopied(true);
      onShare?.('copy');

      setTimeout(() => setCopied(false), 2000);
    } catch (error) {
      console.error('Failed to copy link:', error);
    }
  };

  const handleKakaoShare = () => {
    // 실제로는 Kakao SDK 사용
    console.log('Kakao share:', shareData);
    onShare?.('kakao');
    alert('카카오톡 공유 기능은 준비 중입니다.');
  };

  const handleTwitterShare = () => {
    const text = `${shareData.title} - ${shareData.description}`;
    const url = `https://twitter.com/intent/tweet?text=${encodeURIComponent(text)}&url=${encodeURIComponent(shareData.url)}`;
    window.open(url, '_blank', 'width=550,height=420');
    onShare?.('twitter');
  };

  return (
    <div className="space-y-4">
      <h3 className="text-lg font-bold text-gray-800 text-center">결과 공유하기</h3>

      <div className="grid grid-cols-2 gap-3">
        {/* 카카오톡 */}
        <button
          onClick={handleKakaoShare}
          className="flex flex-col items-center justify-center p-4 bg-yellow-400 hover:bg-yellow-500 rounded-xl transition-colors space-y-2"
        >
          <span className="text-2xl">💬</span>
          <span className="text-sm font-medium text-gray-800">카카오톡</span>
        </button>

        {/* 링크 복사 */}
        <button
          onClick={handleCopyLink}
          className="flex flex-col items-center justify-center p-4 bg-gray-200 hover:bg-gray-300 rounded-xl transition-colors space-y-2"
        >
          <span className="text-2xl">🔗</span>
          <span className="text-sm font-medium text-gray-800">
            {copied ? '복사됨!' : '링크 복사'}
          </span>
        </button>

        {/* 트위터 */}
        <button
          onClick={handleTwitterShare}
          className="flex flex-col items-center justify-center p-4 bg-blue-400 hover:bg-blue-500 rounded-xl transition-colors space-y-2"
        >
          <span className="text-2xl">🐦</span>
          <span className="text-sm font-medium text-white">트위터</span>
        </button>

        {/* 저장 */}
        <button
          onClick={() => onShare?.('download')}
          className="flex flex-col items-center justify-center p-4 bg-purple-400 hover:bg-purple-500 rounded-xl transition-colors space-y-2"
        >
          <span className="text-2xl">💾</span>
          <span className="text-sm font-medium text-white">이미지 저장</span>
        </button>
      </div>

      <p className="text-center text-sm text-gray-600">친구들도 테스트해보게 공유해보세요!</p>
    </div>
  );
};

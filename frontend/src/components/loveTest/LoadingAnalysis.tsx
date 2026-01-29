/**
 * 연애 유형 테스트 - 분석 로딩 컴포넌트
 * Phase 1, T1-LOVE.3
 */
'use client';

import React, { useEffect, useState } from 'react';
import type { LoadingPhase } from '@/types/loveTest';

interface LoadingAnalysisProps {
  onComplete?: () => void;
}

const DIMENSIONS = [
  { name: '적극성', icon: '🎯' },
  { name: '감정표현', icon: '💬' },
  { name: '독립성', icon: '🆓' },
  { name: '헌신도', icon: '💍' },
  { name: '로맨스', icon: '💕' },
];

const LOADING_MESSAGES: Record<LoadingPhase, string> = {
  analyzing: '응답을 분석하고 있어요...',
  calculating: '당신의 연애 패턴을 파악 중...',
  matching: '20가지 유형 중 매칭하는 중...',
  complete: '찾았어요! 당신의 연애 유형은...',
};

export const LoadingAnalysis: React.FC<LoadingAnalysisProps> = ({ onComplete }) => {
  const [phase, setPhase] = useState<LoadingPhase>('analyzing');
  const [activeDimension, setActiveDimension] = useState(0);
  const [progress, setProgress] = useState(0);

  useEffect(() => {
    // Phase 전환
    const phaseTimer = setInterval(() => {
      setPhase((current) => {
        if (current === 'analyzing') return 'calculating';
        if (current === 'calculating') return 'matching';
        if (current === 'matching') return 'complete';
        return current;
      });
    }, 1500);

    // 차원 순차 활성화
    const dimensionTimer = setInterval(() => {
      setActiveDimension((current) => (current + 1) % DIMENSIONS.length);
    }, 300);

    // 프로그레스 증가
    const progressTimer = setInterval(() => {
      setProgress((current) => {
        if (current >= 100) {
          onComplete?.();
          return 100;
        }
        return current + 2;
      });
    }, 100);

    return () => {
      clearInterval(phaseTimer);
      clearInterval(dimensionTimer);
      clearInterval(progressTimer);
    };
  }, [onComplete]);

  return (
    <div className="fixed inset-0 bg-gradient-to-br from-pink-100 to-purple-100 flex items-center justify-center z-50">
      <div className="text-center space-y-8 max-w-md px-6">
        {/* 메인 애니메이션 */}
        <div className="relative">
          <div className="w-32 h-32 mx-auto">
            <svg className="animate-spin-slow" viewBox="0 0 100 100">
              <circle
                cx="50"
                cy="50"
                r="40"
                fill="none"
                stroke="#ec4899"
                strokeWidth="4"
                strokeDasharray="60 251.2"
                strokeLinecap="round"
              />
            </svg>
            <div className="absolute inset-0 flex items-center justify-center">
              <span className="text-4xl animate-pulse">💕</span>
            </div>
          </div>
        </div>

        {/* 5축 아이콘 */}
        <div className="flex justify-center space-x-2">
          {DIMENSIONS.map((dim, index) => (
            <div
              key={dim.name}
              className={`w-12 h-12 flex items-center justify-center rounded-full transition-all duration-300 ${
                index <= activeDimension
                  ? 'bg-pink-500 text-white scale-110'
                  : 'bg-gray-300 text-gray-500 scale-90'
              }`}
              title={dim.name}
            >
              <span className="text-xl">{dim.icon}</span>
            </div>
          ))}
        </div>

        {/* 프로그레스 바 */}
        <div className="space-y-2">
          <div className="h-2 bg-white rounded-full overflow-hidden">
            <div
              className="h-full bg-gradient-to-r from-pink-500 to-purple-500 transition-all duration-200 ease-out"
              style={{ width: `${progress}%` }}
            />
          </div>
        </div>

        {/* 메시지 */}
        <div className="space-y-2">
          <p className="text-xl font-bold text-gray-800 animate-fade-in">
            {LOADING_MESSAGES[phase]}
          </p>
          <p className="text-sm text-gray-600">잠시만 기다려주세요</p>
        </div>
      </div>
    </div>
  );
};

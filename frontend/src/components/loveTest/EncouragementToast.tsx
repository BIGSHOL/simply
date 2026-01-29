/**
 * 연애 유형 테스트 - 격려 토스트 컴포넌트
 * Phase 1, T1-LOVE.3
 */
'use client';

import React, { useEffect, useState } from 'react';

interface EncouragementToastProps {
  message: string;
  isVisible: boolean;
  duration?: number; // 표시 시간 (ms)
  position?: 'top' | 'bottom';
  onClose?: () => void;
}

export const EncouragementToast: React.FC<EncouragementToastProps> = ({
  message,
  isVisible,
  duration = 2000,
  position = 'bottom',
  onClose,
}) => {
  const [show, setShow] = useState(false);

  useEffect(() => {
    if (isVisible) {
      setShow(true);

      const timer = setTimeout(() => {
        setShow(false);
        onClose?.();
      }, duration);

      return () => clearTimeout(timer);
    }
  }, [isVisible, duration, onClose]);

  if (!show) return null;

  const positionClass = position === 'top' ? 'top-20' : 'bottom-20';

  return (
    <div
      className={`fixed ${positionClass} left-1/2 transform -translate-x-1/2 z-50 animate-slide-up`}
      role="alert"
      aria-live="polite"
    >
      <div className="bg-gradient-to-r from-pink-500 to-purple-500 text-white px-6 py-3 rounded-full shadow-lg flex items-center space-x-2">
        <svg className="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
          <path
            fillRule="evenodd"
            d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
            clipRule="evenodd"
          />
        </svg>
        <span className="font-medium">{message}</span>
      </div>
    </div>
  );
};

// 격려 메시지 헬퍼
export const getEncouragementMessage = (questionNum: number): string | null => {
  const messages: Record<number, string> = {
    5: '좋아요! 술술 풀리네요 ✨',
    10: '절반 왔어요! 내 유형이 서서히 드러나고 있어요',
    15: '대단해요! 이제 조금만 더!',
    20: '끝! 드디어 결과를 볼 시간이에요 🎉',
  };

  return messages[questionNum] || null;
};

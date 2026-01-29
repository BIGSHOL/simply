/**
 * TestProgress 컴포넌트 (진행바)
 *
 * Phase 2, T2.2: 테스트 진행 화면
 * MZ 감성 UX 개선: 색상 그라디언트 + 격려 메시지
 */
'use client';

import { useEffect, useState } from 'react';

interface TestProgressProps {
  current: number;
  total: number;
}

export default function TestProgress({ current, total }: TestProgressProps) {
  const [showMessage, setShowMessage] = useState(false);
  const progress = total > 0 ? ((current + 1) / total) * 100 : 0;
  const questionNum = current + 1;

  // 진행률에 따른 색상 그라디언트
  const getProgressColor = () => {
    if (progress < 25) return 'from-[#EF4444] to-[#F97316]'; // 빨강 → 주황
    if (progress < 50) return 'from-[#F97316] to-[#F59E0B]'; // 주황 → 노랑
    if (progress < 75) return 'from-[#F59E0B] to-[#10B981]'; // 노랑 → 초록
    return 'from-[#10B981] to-[#6366F1]'; // 초록 → 보라
  };

  // 격려 메시지
  const getEncouragementMessage = () => {
    if (progress === 50) return '절반 넘었어요! 👏';
    if (progress >= 85 && progress < 100) return '거의 다 왔어요! 💪';
    return null;
  };

  const message = getEncouragementMessage();

  // 메시지 토스트 표시
  useEffect(() => {
    if (message) {
      setShowMessage(true);
      const timer = setTimeout(() => setShowMessage(false), 2000);
      return () => clearTimeout(timer);
    }
  }, [message, current]);

  return (
    <div className="w-full relative">
      {/* 격려 메시지 토스트 */}
      {showMessage && message && (
        <div className="absolute -top-10 left-1/2 -translate-x-1/2 bg-[#111827] text-white text-sm px-4 py-2 rounded-full animate-bounce shadow-lg z-10">
          {message}
        </div>
      )}

      <div className="flex justify-between text-sm text-[#6B7280] mb-2">
        <span className="font-medium">
          Q{questionNum}/{total}
        </span>
        <span className="font-medium">{Math.round(progress)}%</span>
      </div>
      <div className="w-full h-2 bg-[#E5E7EB] rounded-full overflow-hidden">
        <div
          className={`h-full bg-gradient-to-r ${getProgressColor()} rounded-full transition-all duration-500 ease-out`}
          style={{ width: `${progress}%` }}
        />
      </div>
    </div>
  );
}

/**
 * TestChoice 컴포넌트 (선택지)
 *
 * Phase 2, T2.2: 테스트 진행 화면
 * MZ 감성 UX 개선: 선택 애니메이션 + 진동 피드백 + 체크 아이콘
 */
'use client';

import { useState } from 'react';
import type { Choice } from '@/types';

interface TestChoiceProps {
  choice: Choice;
  isSelected: boolean;
  onSelect: (choiceId: string) => void;
}

export default function TestChoice({ choice, isSelected, onSelect }: TestChoiceProps) {
  const [isAnimating, setIsAnimating] = useState(false);

  const handleClick = () => {
    // 진동 피드백 (모바일)
    if (navigator.vibrate) {
      navigator.vibrate(50);
    }

    // 선택 애니메이션
    setIsAnimating(true);
    setTimeout(() => setIsAnimating(false), 200);

    onSelect(choice.id);
  };

  return (
    <button
      type="button"
      onClick={handleClick}
      className={`
        relative w-full py-4 px-4 min-h-[52px] text-left rounded-xl border-2
        transition-all duration-200 ease-out
        ${isAnimating ? 'scale-[0.98]' : 'scale-100'}
        ${
          isSelected
            ? 'border-[#FB923C] bg-[#FFF4E6] text-[#111827] shadow-md'
            : 'border-[#E5E7EB] bg-white hover:border-[#D1D5DB] hover:bg-[#FAFAFA] hover:-translate-y-0.5 hover:shadow-sm'
        }
      `}
    >
      {/* 체크 아이콘 */}
      {isSelected && (
        <div className="absolute top-3 right-3 w-6 h-6 bg-[#FB923C] rounded-full flex items-center justify-center animate-[scaleIn_0.2s_ease-out]">
          <svg
            className="w-4 h-4 text-white"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
            strokeWidth={3}
          >
            <path strokeLinecap="round" strokeLinejoin="round" d="M5 13l4 4L19 7" />
          </svg>
        </div>
      )}

      <span className={`text-base pr-8 ${isSelected ? 'font-medium' : ''}`}>
        {choice.content}
      </span>
    </button>
  );
}

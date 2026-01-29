/**
 * 연애 유형 테스트 - 문항 카드 컴포넌트
 * Phase 1, T1-LOVE.3
 */
'use client';

import React, { useState } from 'react';
import type { LoveTypeQuestion } from '@/types/loveTest';

interface QuestionCardProps {
  question: LoveTypeQuestion;
  selectedOption?: 'A' | 'B' | null;
  onSelect: (choice: 'A' | 'B') => void;
  disabled?: boolean;
}

export const QuestionCard: React.FC<QuestionCardProps> = ({
  question,
  selectedOption,
  onSelect,
  disabled = false,
}) => {
  const [hoveredOption, setHoveredOption] = useState<'A' | 'B' | null>(null);

  const handleSelect = (choice: 'A' | 'B') => {
    if (disabled) return;
    onSelect(choice);
  };

  const getOptionStyle = (choice: 'A' | 'B') => {
    const isSelected = selectedOption === choice;
    const isOtherSelected = selectedOption && selectedOption !== choice;
    const isHovered = hoveredOption === choice;

    let baseStyle =
      'w-full p-4 rounded-lg border-2 transition-all duration-200 cursor-pointer text-left ';

    if (isSelected) {
      baseStyle +=
        'border-pink-500 bg-gradient-to-r from-pink-50 to-pink-100 shadow-md transform scale-[1.02]';
    } else if (isOtherSelected) {
      baseStyle += 'border-gray-200 bg-gray-50 opacity-50';
    } else if (isHovered) {
      baseStyle += 'border-pink-300 bg-pink-50 shadow-sm transform -translate-y-1';
    } else {
      baseStyle += 'border-gray-300 bg-white hover:border-pink-200';
    }

    if (disabled) {
      baseStyle += ' cursor-not-allowed';
    }

    return baseStyle;
  };

  return (
    <div className="w-full max-w-2xl mx-auto space-y-6">
      {/* 문항 이미지 (있는 경우) */}
      {question.imageUrl && (
        <div className="w-full aspect-video rounded-lg overflow-hidden bg-gray-100">
          <img
            src={question.imageUrl}
            alt={`문항 ${question.orderNum} 이미지`}
            className="w-full h-full object-cover"
          />
        </div>
      )}

      {/* 문항 텍스트 */}
      <div className="text-center space-y-2">
        <h2 className="text-2xl font-bold text-gray-800">{question.content}</h2>
      </div>

      {/* 선택지 */}
      <div className="space-y-4">
        {/* 선택지 A */}
        <button
          onClick={() => handleSelect('A')}
          onMouseEnter={() => !disabled && setHoveredOption('A')}
          onMouseLeave={() => setHoveredOption(null)}
          className={getOptionStyle('A')}
          disabled={disabled}
          aria-label={`A 선택: ${question.choiceA}`}
        >
          <div className="flex items-center justify-between">
            <div className="flex-1">
              <div className="flex items-start space-x-3">
                <span className="inline-flex items-center justify-center w-8 h-8 rounded-full bg-pink-500 text-white font-bold text-sm flex-shrink-0">
                  A
                </span>
                <span className="text-gray-800 leading-relaxed">{question.choiceA}</span>
              </div>
            </div>
            {selectedOption === 'A' && (
              <svg
                className="w-6 h-6 text-pink-500 flex-shrink-0 ml-2"
                fill="currentColor"
                viewBox="0 0 20 20"
              >
                <path
                  fillRule="evenodd"
                  d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z"
                  clipRule="evenodd"
                />
              </svg>
            )}
          </div>
        </button>

        {/* 선택지 B */}
        <button
          onClick={() => handleSelect('B')}
          onMouseEnter={() => !disabled && setHoveredOption('B')}
          onMouseLeave={() => setHoveredOption(null)}
          className={getOptionStyle('B')}
          disabled={disabled}
          aria-label={`B 선택: ${question.choiceB}`}
        >
          <div className="flex items-center justify-between">
            <div className="flex-1">
              <div className="flex items-start space-x-3">
                <span className="inline-flex items-center justify-center w-8 h-8 rounded-full bg-purple-500 text-white font-bold text-sm flex-shrink-0">
                  B
                </span>
                <span className="text-gray-800 leading-relaxed">{question.choiceB}</span>
              </div>
            </div>
            {selectedOption === 'B' && (
              <svg
                className="w-6 h-6 text-purple-500 flex-shrink-0 ml-2"
                fill="currentColor"
                viewBox="0 0 20 20"
              >
                <path
                  fillRule="evenodd"
                  d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z"
                  clipRule="evenodd"
                />
              </svg>
            )}
          </div>
        </button>
      </div>

      {/* 네비게이션 힌트 */}
      {selectedOption && (
        <p className="text-center text-sm text-gray-500 animate-fade-in">
          ← 스와이프하거나 다음 버튼을 눌러주세요 →
        </p>
      )}
    </div>
  );
};

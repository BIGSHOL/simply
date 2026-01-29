/**
 * 연애 유형 테스트 - 결과 카드 컴포넌트
 * Phase 1, T1-LOVE.3
 */
'use client';

import React from 'react';
import type { LoveTypeResult } from '@/types/loveTest';

interface ResultCardProps {
  result: LoveTypeResult;
  showAnimation?: boolean;
  variant?: 'full' | 'compact' | 'share';
}

export const ResultCard: React.FC<ResultCardProps> = ({
  result,
  showAnimation = true,
  variant = 'full',
}) => {
  if (variant === 'compact') {
    return (
      <div className="bg-white rounded-lg shadow-md p-6 text-center">
        <h2 className="text-2xl font-bold text-gray-800 mb-2">{result.typeName}</h2>
        <p className="text-gray-600 italic">{result.englishName}</p>
        <p className="text-gray-700 mt-4">{result.tagline}</p>
      </div>
    );
  }

  return (
    <div
      className={`bg-gradient-to-br from-pink-50 to-purple-50 rounded-2xl shadow-xl p-8 space-y-6 ${
        showAnimation ? 'animate-fade-in-scale' : ''
      }`}
    >
      {/* 헤더 */}
      <div className="text-center space-y-3">
        <div className="inline-block">
          <span className="text-4xl">⭐</span>
        </div>
        <h1 className="text-3xl font-bold text-gray-800">당신의 연애 유형은?</h1>
      </div>

      {/* 캐릭터 이미지 (있는 경우) */}
      {result.characterImage && (
        <div className="flex justify-center">
          <div className="w-48 h-48 rounded-full overflow-hidden bg-white shadow-md">
            <img
              src={result.characterImage}
              alt={result.typeName}
              className="w-full h-full object-cover"
            />
          </div>
        </div>
      )}

      {/* 유형명 */}
      <div className="text-center space-y-2 bg-white rounded-xl p-6 shadow-sm">
        <h2 className="text-4xl font-bold text-pink-600">{result.typeName}</h2>
        <p className="text-gray-600 text-lg italic">{result.englishName}</p>
        <p className="text-gray-700 text-xl font-medium mt-4">&quot;{result.tagline}&quot;</p>
      </div>

      {/* 5축 점수 */}
      <div className="bg-white rounded-xl p-6 shadow-sm space-y-3">
        <h3 className="text-lg font-bold text-gray-800 mb-4">당신의 연애 성향</h3>
        {[
          { key: 'proactivity', label: '적극성', value: result.scores.proactivity },
          { key: 'expression', label: '감정표현', value: result.scores.expression },
          { key: 'independence', label: '독립성', value: result.scores.independence },
          { key: 'commitment', label: '헌신도', value: result.scores.commitment },
          { key: 'romance', label: '로맨스', value: result.scores.romance },
        ].map((score) => (
          <div key={score.key} className="space-y-1">
            <div className="flex justify-between text-sm">
              <span className="text-gray-700 font-medium">{score.label}</span>
              <span className="text-pink-600 font-bold">{score.value}%</span>
            </div>
            <div className="h-2 bg-gray-200 rounded-full overflow-hidden">
              <div
                className="h-full bg-gradient-to-r from-pink-500 to-purple-500 transition-all duration-1000 ease-out"
                style={{ width: `${score.value}%` }}
              />
            </div>
          </div>
        ))}
      </div>

      {/* 상세 설명 */}
      <div className="bg-white rounded-xl p-6 shadow-sm space-y-4">
        <h3 className="text-lg font-bold text-gray-800">상세 설명</h3>
        <p className="text-gray-700 leading-relaxed">{result.description}</p>
      </div>

      {/* 연애 스타일 특징 */}
      <div className="bg-white rounded-xl p-6 shadow-sm space-y-3">
        <h3 className="text-lg font-bold text-gray-800">연애 스타일 특징</h3>
        <ul className="space-y-2">
          {result.traits.map((trait, index) => (
            <li key={index} className="flex items-start space-x-2">
              <span className="text-pink-500 mt-1">✓</span>
              <span className="text-gray-700">{trait}</span>
            </li>
          ))}
        </ul>
      </div>

      {/* 강점 & 성장 포인트 */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {/* 강점 */}
        <div className="bg-green-50 rounded-xl p-6 shadow-sm space-y-3">
          <h3 className="text-lg font-bold text-green-800">💪 강점</h3>
          <ul className="space-y-2">
            {result.strengths.map((strength, index) => (
              <li key={index} className="text-green-700 text-sm">
                {index + 1}. {strength}
              </li>
            ))}
          </ul>
        </div>

        {/* 성장 포인트 */}
        <div className="bg-blue-50 rounded-xl p-6 shadow-sm space-y-3">
          <h3 className="text-lg font-bold text-blue-800">🌱 성장 포인트</h3>
          <ul className="space-y-2">
            {result.growthPoints.map((point, index) => (
              <li key={index} className="text-blue-700 text-sm">
                {point}
              </li>
            ))}
          </ul>
        </div>
      </div>

      {/* 궁합 유형 */}
      <div className="bg-white rounded-xl p-6 shadow-sm space-y-3">
        <h3 className="text-lg font-bold text-gray-800">💕 베스트 궁합</h3>
        <div className="flex flex-wrap gap-2">
          {result.compatibleTypes.map((type, index) => (
            <span
              key={index}
              className="px-4 py-2 bg-pink-100 text-pink-700 rounded-full text-sm font-medium"
            >
              {type}
            </span>
          ))}
        </div>
      </div>

      {/* 해시태그 */}
      <div className="text-center space-y-2">
        <div className="flex flex-wrap justify-center gap-2">
          {result.hashtags.map((tag, index) => (
            <span key={index} className="text-purple-600 text-sm font-medium">
              {tag}
            </span>
          ))}
        </div>
      </div>
    </div>
  );
};

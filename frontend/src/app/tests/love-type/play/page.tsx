/**
 * 연애 유형 테스트 - 진행 페이지
 * Phase 1, T1-LOVE.3
 */
'use client';

import React, { useEffect, useState } from 'react';
import { useRouter } from 'next/navigation';
import { useLoveTestStore } from '@/stores/loveTestStore';
import {
  ProgressBar,
  QuestionCard,
  EncouragementToast,
  getEncouragementMessage,
  LoadingAnalysis,
} from '@/components/loveTest';
import { LOVE_TEST_QUESTIONS } from '@/mocks/data/loveTestData';
import type { LoveTestAnswer, LoveTypeResult } from '@/types/loveTest';

export default function LoveTypePlayPage() {
  const router = useRouter();
  const {
    currentQuestion,
    answers,
    isCompleted,
    isSubmitting,
    setAnswer,
    nextQuestion,
    previousQuestion,
    setResult,
    setSubmitting,
    saveProgress,
    loadProgress,
  } = useLoveTestStore();

  const [showEncouragement, setShowEncouragement] = useState(false);
  const [encouragementMessage, setEncouragementMessage] = useState('');
  const [showLoading, setShowLoading] = useState(false);

  // 진행 상황 복원
  useEffect(() => {
    const saved = loadProgress();
    if (saved && saved.answers.length > 0) {
      // "이어하시겠어요?" 모달은 생략하고 바로 복원
      // 실제로는 ContinueModal 컴포넌트 사용 가능
    }
  }, [loadProgress]);

  // 답변 선택 핸들러
  const handleSelect = (choice: 'A' | 'B') => {
    const questionId = `Q${currentQuestion}`;
    setAnswer(questionId, choice);

    // 격려 메시지 표시
    const message = getEncouragementMessage(currentQuestion);
    if (message) {
      setEncouragementMessage(message);
      setShowEncouragement(true);
    }

    // 자동 다음 문항 이동 (500ms 후)
    setTimeout(() => {
      if (currentQuestion < 20) {
        nextQuestion();
      }
    }, 500);
  };

  // 완료 처리
  useEffect(() => {
    if (isCompleted && answers.length === 20 && !isSubmitting && !showLoading) {
      handleSubmit();
    }
  }, [isCompleted, answers, isSubmitting, showLoading]);

  const handleSubmit = async () => {
    setSubmitting(true);
    setShowLoading(true);

    try {
      // API 호출
      const response = await fetch('/api/v1/tests/love-type/submit', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ answers }),
      });

      if (!response.ok) {
        throw new Error('Failed to submit answers');
      }

      const data = await response.json();
      const result: LoveTypeResult = data.data;

      setResult(result);

      // 로딩 완료 후 결과 페이지로 이동
      setTimeout(() => {
        router.push(`/tests/love-type/result/${result.id}`);
      }, 5000);
    } catch (error) {
      console.error('Submit error:', error);
      setSubmitting(false);
      setShowLoading(false);
      alert('결과를 불러오는데 실패했습니다. 다시 시도해주세요.');
    }
  };

  // 현재 문항 데이터
  const currentQuestionData = LOVE_TEST_QUESTIONS[currentQuestion - 1];
  const currentAnswer = answers.find((a) => a.questionId === `Q${currentQuestion}`)?.choice;

  if (showLoading) {
    return <LoadingAnalysis />;
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-pink-50 to-purple-50">
      <div className="max-w-4xl mx-auto px-4 py-8">
        {/* 헤더 */}
        <div className="mb-8 space-y-4">
          <div className="flex items-center justify-between">
            <button
              onClick={previousQuestion}
              disabled={currentQuestion === 1}
              className="text-gray-600 hover:text-gray-800 disabled:opacity-30 disabled:cursor-not-allowed"
            >
              ← 이전
            </button>
            <span className="text-sm font-medium text-gray-600">Q.{currentQuestion}</span>
          </div>

          <ProgressBar current={currentQuestion} total={20} />
        </div>

        {/* 문항 카드 */}
        <div className="mb-8">
          <QuestionCard
            question={currentQuestionData}
            selectedOption={currentAnswer}
            onSelect={handleSelect}
            disabled={isSubmitting}
          />
        </div>

        {/* 네비게이션 버튼 */}
        {currentAnswer && currentQuestion < 20 && (
          <div className="text-center">
            <button
              onClick={nextQuestion}
              className="bg-gradient-to-r from-pink-500 to-purple-500 text-white font-bold px-8 py-3 rounded-full shadow-lg hover:shadow-xl transform hover:scale-105 transition-all duration-200"
            >
              다음 문항 →
            </button>
          </div>
        )}

        {/* 격려 토스트 */}
        <EncouragementToast
          message={encouragementMessage}
          isVisible={showEncouragement}
          onClose={() => setShowEncouragement(false)}
        />
      </div>
    </div>
  );
}

/**
 * 테스트 진행 페이지
 *
 * Phase 2, T2.2: 테스트 진행 화면
 * MZ 감성 UX: 로딩 화면 + 슬라이드 전환 애니메이션
 */
'use client';

import { useEffect, useState } from 'react';
import { useParams, useRouter } from 'next/navigation';
import { Button } from '@/components/ui';
import { TestQuestion, TestProgress, TestLoading } from '@/components/test';
import { useTestStore } from '@/stores/testStore';
import { submitTest } from '@/lib/api';

export default function TestPlayPage() {
  const params = useParams();
  const router = useRouter();
  const testId = params.id as string;
  const [showLoading, setShowLoading] = useState(false);
  const [slideDirection, setSlideDirection] = useState<'left' | 'right'>('left');

  const {
    test,
    currentQuestionIndex,
    answers,
    isSubmitting,
    error,
    selectAnswer,
    nextQuestion,
    previousQuestion,
    setResult,
    setSubmitting,
    setError,
    resetToFirstQuestion,
  } = useTestStore();

  // 뒤로가기 버튼 방지 (질문 조작 방지)
  useEffect(() => {
    // 히스토리에 현재 상태 추가
    const pushState = () => {
      window.history.pushState({ testInProgress: true }, '');
    };

    // 초기 상태 추가
    pushState();

    // popstate 이벤트 핸들러 (뒤로가기 감지)
    const handlePopState = (event: PopStateEvent) => {
      // 테스트 진행 중 뒤로가기 시 첫 질문으로 리셋
      if (test) {
        resetToFirstQuestion();
        // 다시 히스토리 상태 추가하여 추가 뒤로가기 방지
        pushState();
      }
    };

    window.addEventListener('popstate', handlePopState);

    return () => {
      window.removeEventListener('popstate', handlePopState);
    };
  }, [test, resetToFirstQuestion]);

  // 테스트 데이터가 없으면 상세 페이지로 리다이렉트
  useEffect(() => {
    if (!test) {
      router.replace(`/tests/${testId}`);
    }
  }, [test, testId, router]);

  if (!test) {
    return (
      <div className="max-w-[600px] mx-auto px-4 sm:px-5 py-8 text-center">
        <p className="text-[#6B7280]">로딩 중...</p>
      </div>
    );
  }

  const currentQuestion = test.questions[currentQuestionIndex];
  const currentAnswer = answers.find(
    (a) => a.question_id === currentQuestion?.id
  );
  const isLastQuestion = currentQuestionIndex === test.questions.length - 1;
  const canProceed = !!currentAnswer;

  const handleNext = async () => {
    if (!canProceed) return;

    if (isLastQuestion) {
      // 로딩 화면 표시 후 제출
      setShowLoading(true);
      try {
        setSubmitting(true);
        setError(null);
        const response = await submitTest(testId, answers);
        setResult(response.data);
        // 로딩 애니메이션 완료 후 결과 페이지로 이동
        setTimeout(() => {
          router.push(`/results/${response.data.id}`);
        }, 2500);
      } catch (err) {
        setShowLoading(false);
        setError('결과를 가져오는데 실패했습니다. 다시 시도해주세요.');
        console.error('Failed to submit test:', err);
      } finally {
        setSubmitting(false);
      }
    } else {
      setSlideDirection('left');
      nextQuestion();
    }
  };

  const handlePrevious = () => {
    setSlideDirection('right');
    previousQuestion();
  };

  // 로딩 화면
  if (showLoading) {
    return <TestLoading testTitle={test?.title} />;
  }

  return (
    <div className="max-w-[600px] mx-auto px-4 sm:px-5 py-6 min-h-[calc(100vh-120px)] flex flex-col">
      {/* 진행바 */}
      <div className="mb-6">
        <TestProgress
          current={currentQuestionIndex}
          total={test.questions.length}
        />
      </div>

      {/* 질문 영역 - 슬라이드 애니메이션 */}
      <div className="flex-1 overflow-hidden">
        {currentQuestion && (
          <div
            key={currentQuestion.id}
            className={`animate-slideIn ${slideDirection === 'left' ? 'animate-slideInLeft' : 'animate-slideInRight'}`}
          >
            <TestQuestion
              question={currentQuestion}
              selectedAnswer={currentAnswer}
              onAnswer={({ question_id, choice_id }) => {
                selectAnswer(question_id, choice_id);
                // 선택 후 자동으로 다음 질문으로 이동
                if (!isLastQuestion) {
                  setSlideDirection('left');
                  setTimeout(() => nextQuestion(), 300);
                }
              }}
            />
          </div>
        )}
      </div>

      {/* 에러 메시지 */}
      {error && (
        <div className="mb-4 p-3 bg-red-50 border border-red-200 rounded-xl">
          <p className="text-sm text-red-600">{error}</p>
        </div>
      )}

      {/* 네비게이션 버튼 */}
      <div className="mt-6 flex gap-3">
        {currentQuestionIndex > 0 && (
          <Button
            variant="secondary"
            onClick={handlePrevious}
            disabled={isSubmitting}
            className="!px-4 min-w-[44px]"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="20"
              height="20"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              strokeWidth="2"
              strokeLinecap="round"
              strokeLinejoin="round"
            >
              <path d="M15 18l-6-6 6-6" />
            </svg>
          </Button>
        )}

        <Button
          fullWidth
          onClick={handleNext}
          disabled={!canProceed || isSubmitting}
          isLoading={isSubmitting}
        >
          {isLastQuestion ? '결과 보기 🎯' : '다음'}
        </Button>
      </div>
    </div>
  );
}

/**
 * 테스트 상태 관리 (Zustand)
 *
 * Phase 2, T2.2: 테스트 진행 화면
 */
import { create } from 'zustand';
import type { Test, Answer, Result } from '@/types';

interface TestState {
  // 현재 테스트 데이터
  test: Test | null;

  // 진행 상태
  currentQuestionIndex: number;
  answers: Answer[];

  // 결과
  result: Result | null;

  // 상태 플래그
  isLoading: boolean;
  isSubmitting: boolean;
  error: string | null;

  // 액션
  setTest: (test: Test) => void;
  selectAnswer: (questionId: string, choiceId: string) => void;
  nextQuestion: () => void;
  previousQuestion: () => void;
  setResult: (result: Result) => void;
  setLoading: (loading: boolean) => void;
  setSubmitting: (submitting: boolean) => void;
  setError: (error: string | null) => void;
  reset: () => void;
  resetToFirstQuestion: () => void; // 첫 질문으로 리셋 (답변 초기화)
}

const initialState = {
  test: null,
  currentQuestionIndex: 0,
  answers: [],
  result: null,
  isLoading: false,
  isSubmitting: false,
  error: null,
};

export const useTestStore = create<TestState>((set, get) => ({
  ...initialState,

  setTest: (test) => set({ test, currentQuestionIndex: 0, answers: [], result: null }),

  selectAnswer: (questionId, choiceId) => {
    const { answers } = get();
    const existingIndex = answers.findIndex((a) => a.question_id === questionId);

    if (existingIndex >= 0) {
      // 기존 답변 수정
      const newAnswers = [...answers];
      newAnswers[existingIndex] = { question_id: questionId, choice_id: choiceId };
      set({ answers: newAnswers });
    } else {
      // 새 답변 추가
      set({ answers: [...answers, { question_id: questionId, choice_id: choiceId }] });
    }
  },

  nextQuestion: () => {
    const { currentQuestionIndex, test } = get();
    if (test && currentQuestionIndex < test.questions.length - 1) {
      set({ currentQuestionIndex: currentQuestionIndex + 1 });
    }
  },

  previousQuestion: () => {
    const { currentQuestionIndex } = get();
    if (currentQuestionIndex > 0) {
      set({ currentQuestionIndex: currentQuestionIndex - 1 });
    }
  },

  setResult: (result) => set({ result }),

  setLoading: (isLoading) => set({ isLoading }),

  setSubmitting: (isSubmitting) => set({ isSubmitting }),

  setError: (error) => set({ error }),

  reset: () => set(initialState),

  // 첫 질문으로 리셋 (테스트 데이터는 유지, 답변만 초기화)
  resetToFirstQuestion: () => set({ currentQuestionIndex: 0, answers: [], error: null }),
}));

/**
 * 연애 유형 테스트 상태 관리 (Zustand)
 * Phase 1, T1-LOVE.3
 */
import { create } from 'zustand';
import type { LoveTestAnswer, LoveTypeResult, LoveTestProgress } from '@/types/loveTest';

interface LoveTestState {
  // 진행 상태
  currentQuestion: number; // 1-20
  answers: LoveTestAnswer[];
  isCompleted: boolean;

  // 결과
  result: LoveTypeResult | null;

  // 로딩 상태
  isLoading: boolean;
  isSubmitting: boolean;

  // 액션
  setAnswer: (questionId: string, choice: 'A' | 'B') => void;
  nextQuestion: () => void;
  previousQuestion: () => void;
  setResult: (result: LoveTypeResult) => void;
  setLoading: (loading: boolean) => void;
  setSubmitting: (submitting: boolean) => void;
  reset: () => void;

  // 자동 저장/복원
  saveProgress: () => void;
  loadProgress: () => LoveTestProgress | null;
  clearProgress: () => void;
}

const STORAGE_KEY = 'love-type-progress';
const EXPIRY_MS = 30 * 60 * 1000; // 30분

const initialState = {
  currentQuestion: 1,
  answers: [],
  isCompleted: false,
  result: null,
  isLoading: false,
  isSubmitting: false,
};

export const useLoveTestStore = create<LoveTestState>((set, get) => ({
  ...initialState,

  setAnswer: (questionId, choice) => {
    const { answers, currentQuestion } = get();
    const existingIndex = answers.findIndex((a) => a.questionId === questionId);

    let newAnswers: LoveTestAnswer[];
    if (existingIndex >= 0) {
      // 기존 답변 수정
      newAnswers = [...answers];
      newAnswers[existingIndex] = { questionId, choice };
    } else {
      // 새 답변 추가
      newAnswers = [...answers, { questionId, choice }];
    }

    set({ answers: newAnswers });

    // 자동 저장
    get().saveProgress();

    // 20번째 문항이면 완료 처리
    if (currentQuestion === 20) {
      set({ isCompleted: true });
    }
  },

  nextQuestion: () => {
    const { currentQuestion } = get();
    if (currentQuestion < 20) {
      set({ currentQuestion: currentQuestion + 1 });
      get().saveProgress();
    }
  },

  previousQuestion: () => {
    const { currentQuestion } = get();
    if (currentQuestion > 1) {
      set({ currentQuestion: currentQuestion - 1 });
      get().saveProgress();
    }
  },

  setResult: (result) => set({ result }),

  setLoading: (isLoading) => set({ isLoading }),

  setSubmitting: (isSubmitting) => set({ isSubmitting }),

  reset: () => {
    set(initialState);
    get().clearProgress();
  },

  saveProgress: () => {
    const { currentQuestion, answers } = get();
    const progress: LoveTestProgress = {
      currentQuestion,
      answers,
      startedAt: Date.now(),
      lastUpdated: Date.now(),
    };

    if (typeof window !== 'undefined') {
      sessionStorage.setItem(STORAGE_KEY, JSON.stringify(progress));
    }
  },

  loadProgress: () => {
    if (typeof window === 'undefined') return null;

    const saved = sessionStorage.getItem(STORAGE_KEY);
    if (!saved) return null;

    try {
      const progress: LoveTestProgress = JSON.parse(saved);

      // 만료 확인
      const now = Date.now();
      if (now - progress.lastUpdated > EXPIRY_MS) {
        sessionStorage.removeItem(STORAGE_KEY);
        return null;
      }

      return progress;
    } catch (error) {
      console.error('Failed to load progress:', error);
      return null;
    }
  },

  clearProgress: () => {
    if (typeof window !== 'undefined') {
      sessionStorage.removeItem(STORAGE_KEY);
    }
  },
}));

/**
 * 연애 유형 테스트 Zustand Store 테스트
 * Phase 1, T1-LOVE.3
 */
import { describe, it, expect, beforeEach } from 'vitest';
import { renderHook, act } from '@testing-library/react';
import { useLoveTestStore } from '@/stores/loveTestStore';

describe('useLoveTestStore', () => {
  beforeEach(() => {
    const { result } = renderHook(() => useLoveTestStore());
    act(() => {
      result.current.reset();
    });
  });

  it('초기 상태가 올바르게 설정된다', () => {
    const { result } = renderHook(() => useLoveTestStore());

    expect(result.current.currentQuestion).toBe(1);
    expect(result.current.answers).toEqual([]);
    expect(result.current.isCompleted).toBe(false);
    expect(result.current.result).toBeNull();
  });

  it('setAnswer로 답변을 추가할 수 있다', () => {
    const { result } = renderHook(() => useLoveTestStore());

    act(() => {
      result.current.setAnswer('Q1', 'A');
    });

    expect(result.current.answers).toHaveLength(1);
    expect(result.current.answers[0]).toEqual({ questionId: 'Q1', choice: 'A' });
  });

  it('같은 문항의 답변은 덮어쓴다', () => {
    const { result } = renderHook(() => useLoveTestStore());

    act(() => {
      result.current.setAnswer('Q1', 'A');
      result.current.setAnswer('Q1', 'B');
    });

    expect(result.current.answers).toHaveLength(1);
    expect(result.current.answers[0].choice).toBe('B');
  });

  it('nextQuestion으로 다음 문항으로 이동한다', () => {
    const { result } = renderHook(() => useLoveTestStore());

    act(() => {
      result.current.nextQuestion();
    });

    expect(result.current.currentQuestion).toBe(2);
  });

  it('20번째 문항을 초과하여 이동하지 않는다', () => {
    const { result } = renderHook(() => useLoveTestStore());

    act(() => {
      for (let i = 0; i < 25; i++) {
        result.current.nextQuestion();
      }
    });

    expect(result.current.currentQuestion).toBe(20);
  });

  it('previousQuestion으로 이전 문항으로 이동한다', () => {
    const { result } = renderHook(() => useLoveTestStore());

    act(() => {
      result.current.nextQuestion();
      result.current.nextQuestion();
      result.current.previousQuestion();
    });

    expect(result.current.currentQuestion).toBe(2);
  });

  it('1번째 문항 이하로 이동하지 않는다', () => {
    const { result } = renderHook(() => useLoveTestStore());

    act(() => {
      result.current.previousQuestion();
    });

    expect(result.current.currentQuestion).toBe(1);
  });

  it('20번째 문항에 답변하면 isCompleted가 true가 된다', () => {
    const { result } = renderHook(() => useLoveTestStore());

    act(() => {
      for (let i = 1; i <= 19; i++) {
        result.current.nextQuestion();
      }
      result.current.setAnswer('Q20', 'A');
    });

    expect(result.current.isCompleted).toBe(true);
  });

  it('reset으로 모든 상태를 초기화한다', () => {
    const { result } = renderHook(() => useLoveTestStore());

    act(() => {
      result.current.setAnswer('Q1', 'A');
      result.current.nextQuestion();
      result.current.reset();
    });

    expect(result.current.currentQuestion).toBe(1);
    expect(result.current.answers).toEqual([]);
    expect(result.current.isCompleted).toBe(false);
  });
});

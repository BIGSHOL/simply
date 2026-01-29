/**
 * 연애 유형 테스트 컴포넌트 통합 테스트
 * Phase 1, T1-LOVE.3
 *
 * TDD RED: 테스트 먼저 작성
 */
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { ProgressBar } from '@/components/loveTest/ProgressBar';
import { QuestionCard } from '@/components/loveTest/QuestionCard';
import { ResultCard } from '@/components/loveTest/ResultCard';
import { EncouragementToast, getEncouragementMessage } from '@/components/loveTest/EncouragementToast';
import { LOVE_TEST_QUESTIONS } from '@/mocks/data/loveTestData';
import { LOVE_TYPE_RESULTS } from '@/mocks/data/loveTestData';

describe('ProgressBar', () => {
  it('현재 진행 상황을 표시한다', () => {
    render(<ProgressBar current={8} total={20} />);
    expect(screen.getByText('8/20')).toBeInTheDocument();
  });

  it('프로그레스 바가 올바른 퍼센트를 표시한다', () => {
    render(<ProgressBar current={10} total={20} />);
    expect(screen.getByText('50% 완료')).toBeInTheDocument();
  });

  it('마일스톤이 올바르게 표시된다', () => {
    const { container } = render(<ProgressBar current={5} total={20} milestones={[5, 10, 15, 20]} />);
    const milestones = container.querySelectorAll('[title*="번째 문항"]');
    expect(milestones).toHaveLength(4);
  });

  it('접근성: progressbar role과 aria 속성이 있다', () => {
    render(<ProgressBar current={8} total={20} />);
    const progressbar = screen.getByRole('progressbar');
    expect(progressbar).toHaveAttribute('aria-valuenow', '8');
    expect(progressbar).toHaveAttribute('aria-valuemin', '1');
    expect(progressbar).toHaveAttribute('aria-valuemax', '20');
  });
});

describe('QuestionCard', () => {
  const mockQuestion = LOVE_TEST_QUESTIONS[0];
  const mockOnSelect = vi.fn();

  beforeEach(() => {
    mockOnSelect.mockClear();
  });

  it('문항 텍스트를 표시한다', () => {
    render(<QuestionCard question={mockQuestion} onSelect={mockOnSelect} />);
    expect(screen.getByText(mockQuestion.content)).toBeInTheDocument();
  });

  it('A, B 선택지를 표시한다', () => {
    render(<QuestionCard question={mockQuestion} onSelect={mockOnSelect} />);
    expect(screen.getByText(mockQuestion.choiceA)).toBeInTheDocument();
    expect(screen.getByText(mockQuestion.choiceB)).toBeInTheDocument();
  });

  it('선택지를 클릭하면 onSelect가 호출된다', () => {
    render(<QuestionCard question={mockQuestion} onSelect={mockOnSelect} />);

    const choiceA = screen.getByLabelText(`A 선택: ${mockQuestion.choiceA}`);
    fireEvent.click(choiceA);

    expect(mockOnSelect).toHaveBeenCalledWith('A');
  });

  it('선택된 옵션이 시각적으로 표시된다', () => {
    const { container } = render(<QuestionCard question={mockQuestion} selectedOption="A" onSelect={mockOnSelect} />);

    // SVG 체크마크가 표시되어야 함
    const checkmarks = container.querySelectorAll('svg');
    expect(checkmarks.length).toBeGreaterThan(0);
  });

  it('disabled 상태에서는 클릭이 동작하지 않는다', () => {
    render(<QuestionCard question={mockQuestion} onSelect={mockOnSelect} disabled={true} />);

    const choiceA = screen.getByLabelText(`A 선택: ${mockQuestion.choiceA}`);
    fireEvent.click(choiceA);

    expect(mockOnSelect).not.toHaveBeenCalled();
  });
});

describe('ResultCard', () => {
  const mockResult = LOVE_TYPE_RESULTS.straight_shooter;

  it('유형명을 표시한다', () => {
    render(<ResultCard result={mockResult} />);
    expect(screen.getByText(mockResult.typeName)).toBeInTheDocument();
    expect(screen.getByText(mockResult.englishName)).toBeInTheDocument();
  });

  it('한줄 설명을 표시한다', () => {
    render(<ResultCard result={mockResult} />);
    expect(screen.getByText(`"${mockResult.tagline}"`)).toBeInTheDocument();
  });

  it('상세 설명을 표시한다', () => {
    render(<ResultCard result={mockResult} />);
    expect(screen.getByText(mockResult.description)).toBeInTheDocument();
  });

  it('5축 점수를 모두 표시한다', () => {
    render(<ResultCard result={mockResult} />);
    expect(screen.getByText('적극성')).toBeInTheDocument();
    expect(screen.getByText('감정표현')).toBeInTheDocument();
    expect(screen.getByText('독립성')).toBeInTheDocument();
    expect(screen.getByText('헌신도')).toBeInTheDocument();
    expect(screen.getByText('로맨스')).toBeInTheDocument();
  });

  it('연애 스타일 특징 리스트를 표시한다', () => {
    render(<ResultCard result={mockResult} />);
    mockResult.traits.forEach((trait) => {
      expect(screen.getByText(trait)).toBeInTheDocument();
    });
  });

  it('compact 모드에서는 간단한 정보만 표시한다', () => {
    const { container } = render(<ResultCard result={mockResult} variant="compact" />);
    expect(screen.getByText(mockResult.typeName)).toBeInTheDocument();
    expect(screen.getByText(mockResult.tagline)).toBeInTheDocument();

    // 상세 설명은 표시되지 않음
    expect(screen.queryByText('연애 스타일 특징')).not.toBeInTheDocument();
  });
});

describe('EncouragementToast', () => {
  it('isVisible이 true일 때 메시지를 표시한다', () => {
    render(<EncouragementToast message="좋아요!" isVisible={true} />);
    expect(screen.getByText('좋아요!')).toBeInTheDocument();
  });

  it('isVisible이 false일 때는 표시하지 않는다', () => {
    render(<EncouragementToast message="좋아요!" isVisible={false} />);
    expect(screen.queryByText('좋아요!')).not.toBeInTheDocument();
  });

  it('duration 후에 onClose가 호출된다', async () => {
    const mockOnClose = vi.fn();
    render(
      <EncouragementToast message="좋아요!" isVisible={true} duration={100} onClose={mockOnClose} />
    );

    await waitFor(
      () => {
        expect(mockOnClose).toHaveBeenCalled();
      },
      { timeout: 200 }
    );
  });
});

describe('getEncouragementMessage', () => {
  it('5번째 문항에서 격려 메시지를 반환한다', () => {
    const message = getEncouragementMessage(5);
    expect(message).toBe('좋아요! 술술 풀리네요 ✨');
  });

  it('10번째 문항에서 격려 메시지를 반환한다', () => {
    const message = getEncouragementMessage(10);
    expect(message).toBe('절반 왔어요! 내 유형이 서서히 드러나고 있어요');
  });

  it('15번째 문항에서 격려 메시지를 반환한다', () => {
    const message = getEncouragementMessage(15);
    expect(message).toBe('대단해요! 이제 조금만 더!');
  });

  it('20번째 문항에서 격려 메시지를 반환한다', () => {
    const message = getEncouragementMessage(20);
    expect(message).toBe('끝! 드디어 결과를 볼 시간이에요 🎉');
  });

  it('다른 문항 번호에서는 null을 반환한다', () => {
    const message = getEncouragementMessage(7);
    expect(message).toBeNull();
  });
});

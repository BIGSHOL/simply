/**
 * TestQuestion 컴포넌트 테스트
 *
 * Phase 2, T2.2: 테스트 진행 화면
 */
import { describe, it, expect, vi } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import { TestQuestion } from '@/components/test';
import { mockTestDetail } from '@/mocks/data/mockTests';

describe('TestQuestion', () => {
  const mockQuestion = mockTestDetail.questions[0];
  const mockOnAnswer = vi.fn();

  beforeEach(() => {
    mockOnAnswer.mockClear();
  });

  it('질문 내용을 표시해야 한다', () => {
    render(<TestQuestion question={mockQuestion} onAnswer={mockOnAnswer} />);
    expect(screen.getByText(mockQuestion.content)).toBeInTheDocument();
  });

  it('모든 선택지를 표시해야 한다', () => {
    render(<TestQuestion question={mockQuestion} onAnswer={mockOnAnswer} />);
    mockQuestion.choices.forEach((choice) => {
      expect(screen.getByText(choice.content)).toBeInTheDocument();
    });
  });

  it('선택지 클릭 시 onAnswer가 호출되어야 한다', () => {
    render(<TestQuestion question={mockQuestion} onAnswer={mockOnAnswer} />);
    fireEvent.click(screen.getByText(mockQuestion.choices[0].content));
    expect(mockOnAnswer).toHaveBeenCalledWith({
      question_id: mockQuestion.id,
      choice_id: mockQuestion.choices[0].id,
    });
  });

  it('선택된 선택지는 강조 표시되어야 한다', () => {
    const selectedAnswer = {
      question_id: mockQuestion.id,
      choice_id: mockQuestion.choices[1].id,
    };
    render(
      <TestQuestion
        question={mockQuestion}
        selectedAnswer={selectedAnswer}
        onAnswer={mockOnAnswer}
      />
    );
    // 선택된 선택지의 버튼이 선택 스타일을 가져야 함
    const selectedButton = screen.getByText(mockQuestion.choices[1].content).closest('button');
    expect(selectedButton).toHaveClass('border-[#6366F1]');
  });

  it('선택되지 않은 선택지는 기본 스타일이어야 한다', () => {
    const selectedAnswer = {
      question_id: mockQuestion.id,
      choice_id: mockQuestion.choices[1].id,
    };
    render(
      <TestQuestion
        question={mockQuestion}
        selectedAnswer={selectedAnswer}
        onAnswer={mockOnAnswer}
      />
    );
    // 선택되지 않은 선택지는 기본 border 색상
    const unselectedButton = screen.getByText(mockQuestion.choices[0].content).closest('button');
    expect(unselectedButton).toHaveClass('border-[#E5E7EB]');
  });

  it('다른 선택지를 클릭하면 새로운 선택으로 onAnswer가 호출되어야 한다', () => {
    const selectedAnswer = {
      question_id: mockQuestion.id,
      choice_id: mockQuestion.choices[0].id,
    };
    render(
      <TestQuestion
        question={mockQuestion}
        selectedAnswer={selectedAnswer}
        onAnswer={mockOnAnswer}
      />
    );

    // 다른 선택지 클릭
    fireEvent.click(screen.getByText(mockQuestion.choices[2].content));
    expect(mockOnAnswer).toHaveBeenCalledWith({
      question_id: mockQuestion.id,
      choice_id: mockQuestion.choices[2].id,
    });
  });
});

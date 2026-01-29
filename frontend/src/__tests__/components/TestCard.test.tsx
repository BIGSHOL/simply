/**
 * TestCard 컴포넌트 테스트
 *
 * Phase 2, T2.1: 테스트 목록 화면
 */
import { describe, it, expect, vi } from 'vitest';
import { render, screen } from '@testing-library/react';
import { TestCard } from '@/components/test';
import { mockTestSummaries } from '@/mocks/data/mockTests';

// Next.js 라우터 모킹
vi.mock('next/navigation', () => ({
  useRouter: () => ({
    push: vi.fn(),
    replace: vi.fn(),
  }),
}));

describe('TestCard', () => {
  const mockTest = mockTestSummaries[0]; // MBTI 연애 스타일 테스트

  it('테스트 제목을 표시해야 한다', () => {
    render(<TestCard test={mockTest} />);
    expect(screen.getByText(mockTest.title)).toBeInTheDocument();
  });

  it('테스트 설명을 표시해야 한다', () => {
    render(<TestCard test={mockTest} />);
    expect(screen.getByText(mockTest.description)).toBeInTheDocument();
  });

  it('카테고리 뱃지를 표시해야 한다', () => {
    render(<TestCard test={mockTest} />);
    // love 카테고리 → "연애" 라벨
    expect(screen.getByText('연애')).toBeInTheDocument();
  });

  it('참여 수를 표시해야 한다', () => {
    render(<TestCard test={mockTest} />);
    // 12,345 → 1.2만
    expect(screen.getByText(/1.2만명 참여/)).toBeInTheDocument();
  });

  it('문항 수를 표시해야 한다', () => {
    render(<TestCard test={mockTest} />);
    expect(screen.getByText(`${mockTest.question_count}문항`)).toBeInTheDocument();
  });

  it('테스트 하기 버튼을 표시해야 한다', () => {
    render(<TestCard test={mockTest} />);
    expect(screen.getByText(/테스트 하기/)).toBeInTheDocument();
  });

  it('클릭하면 테스트 상세 페이지로 이동해야 한다', () => {
    render(<TestCard test={mockTest} />);
    const link = screen.getByRole('link');
    expect(link).toHaveAttribute('href', `/tests/${mockTest.id}`);
  });
});

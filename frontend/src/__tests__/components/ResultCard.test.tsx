/**
 * ResultCard 컴포넌트 테스트
 *
 * Phase 3, T3.2: 결과 페이지 UI
 */
import { describe, it, expect, vi } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import { ResultCard } from '@/components/result';
import { mockResult } from '@/mocks/data/mockTests';

// Next.js 라우터 모킹
vi.mock('next/navigation', () => ({
  useRouter: () => ({
    push: vi.fn(),
    replace: vi.fn(),
  }),
}));

describe('ResultCard', () => {
  const mockOnShare = vi.fn();

  beforeEach(() => {
    mockOnShare.mockClear();
  });

  it('결과 타입을 표시해야 한다', () => {
    render(<ResultCard result={mockResult} onShare={mockOnShare} />);
    expect(screen.getByText(mockResult.result_type)).toBeInTheDocument();
  });

  it('결과 제목을 표시해야 한다', () => {
    render(<ResultCard result={mockResult} onShare={mockOnShare} />);
    // h1 태그로 결과 제목 표시
    expect(screen.getByRole('heading', { level: 1, name: mockResult.result_title })).toBeInTheDocument();
  });

  it('결과 내용을 마크다운으로 렌더링해야 한다', () => {
    render(<ResultCard result={mockResult} onShare={mockOnShare} />);
    // 마크다운 내용 중 일부 확인 (연애 성향 섹션)
    expect(screen.getByText(/연애 성향/)).toBeInTheDocument();
    expect(screen.getByText(/감정 표현에 솔직하고 적극적입니다/)).toBeInTheDocument();
  });

  it('공유 버튼을 표시해야 한다', () => {
    render(<ResultCard result={mockResult} onShare={mockOnShare} />);
    expect(screen.getByRole('button', { name: /공유/i })).toBeInTheDocument();
  });

  it('공유 버튼 클릭 시 onShare가 호출되어야 한다', () => {
    render(<ResultCard result={mockResult} onShare={mockOnShare} />);
    fireEvent.click(screen.getByRole('button', { name: /공유/i }));
    expect(mockOnShare).toHaveBeenCalledWith(mockResult.share_code);
  });

  it('다시 테스트하기 버튼을 표시해야 한다', () => {
    render(<ResultCard result={mockResult} onShare={mockOnShare} />);
    expect(screen.getByRole('link', { name: /다시 테스트/i })).toBeInTheDocument();
  });

  it('다시 테스트하기 링크가 올바른 href를 가져야 한다', () => {
    render(<ResultCard result={mockResult} onShare={mockOnShare} />);
    const link = screen.getByRole('link', { name: /다시 테스트/i });
    expect(link).toHaveAttribute('href', `/tests/${mockResult.test_id}`);
  });
});

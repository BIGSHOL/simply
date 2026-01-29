/**
 * Layout 컴포넌트 테스트
 *
 * Phase 1, T1.2: 메인 레이아웃 & 라우팅
 */
import { describe, it, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
import { Header } from '@/components/Layout';
import { Footer } from '@/components/Layout';
import { Button, Card } from '@/components/ui';

describe('Header', () => {
  it('로고를 표시해야 한다', () => {
    render(<Header />);
    expect(screen.getByText('Simly')).toBeInTheDocument();
  });

  it('홈 링크를 포함해야 한다', () => {
    render(<Header />);
    expect(screen.getByText('홈')).toBeInTheDocument();
  });
});

describe('Footer', () => {
  it('저작권 정보를 표시해야 한다', () => {
    render(<Footer />);
    expect(screen.getByText(/Simly. All rights reserved/)).toBeInTheDocument();
  });

  it('설명 문구를 표시해야 한다', () => {
    render(<Footer />);
    expect(screen.getByText(/AI가 만들어주는 재미있는 심리테스트/)).toBeInTheDocument();
  });
});

describe('Button', () => {
  it('primary 버튼을 렌더링해야 한다', () => {
    render(<Button variant="primary">테스트 시작</Button>);
    expect(screen.getByRole('button', { name: '테스트 시작' })).toBeInTheDocument();
  });

  it('secondary 버튼을 렌더링해야 한다', () => {
    render(<Button variant="secondary">다시 하기</Button>);
    expect(screen.getByRole('button', { name: '다시 하기' })).toBeInTheDocument();
  });

  it('로딩 상태를 표시해야 한다', () => {
    render(<Button isLoading>제출</Button>);
    expect(screen.getByText('로딩 중...')).toBeInTheDocument();
  });

  it('disabled 상태에서 클릭이 안 되어야 한다', () => {
    render(<Button disabled>비활성</Button>);
    expect(screen.getByRole('button')).toBeDisabled();
  });
});

describe('Card', () => {
  it('기본 카드를 렌더링해야 한다', () => {
    render(<Card>카드 내용</Card>);
    expect(screen.getByText('카드 내용')).toBeInTheDocument();
  });

  it('result 변형 카드를 렌더링해야 한다', () => {
    render(<Card variant="result">결과 카드</Card>);
    expect(screen.getByText('결과 카드')).toBeInTheDocument();
  });
});

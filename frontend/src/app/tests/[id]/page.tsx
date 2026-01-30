/**
 * 테스트 상세/시작 페이지 (서버 컴포넌트)
 *
 * Phase 2, T2.2: 테스트 진행 화면
 * 동적 OG 메타데이터 지원
 */
import { Metadata } from 'next';
import TestDetailClient from './TestDetailClient';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api/v1';

interface PageProps {
  params: Promise<{ id: string }>;
}

async function getTestData(id: string) {
  try {
    const response = await fetch(`${API_BASE_URL}/tests/${id}`, {
      next: { revalidate: 300 },
    });
    if (!response.ok) return null;
    const data = await response.json();
    return data.data;
  } catch {
    return null;
  }
}

const categoryLabels: Record<string, string> = {
  personality: '성격',
  love: '연애',
  career: '직장',
  fun: '재미',
};

export async function generateMetadata({ params }: PageProps): Promise<Metadata> {
  const { id } = await params;
  const test = await getTestData(id);

  if (!test) {
    return {
      title: '테스트를 찾을 수 없습니다 | Simly',
      description: '요청하신 테스트를 찾을 수 없습니다.',
    };
  }

  const category = categoryLabels[test.category] || test.category;
  const title = `${test.title} | Simly`;
  const description = `[${category}] ${test.description} - ${test.question_count}문항, ${test.play_count?.toLocaleString() || 0}명 참여`;
  const siteUrl = process.env.NEXT_PUBLIC_SITE_URL || 'https://simly-tau.vercel.app';

  return {
    title,
    description,
    openGraph: {
      title: test.title,
      description,
      type: 'website',
      siteName: 'Simly',
      url: `${siteUrl}/tests/${id}`,
      images: test.thumbnail_url
        ? [{ url: test.thumbnail_url, width: 1200, height: 630, alt: test.title }]
        : undefined,
    },
    twitter: {
      card: 'summary_large_image',
      title: test.title,
      description,
      images: test.thumbnail_url ? [test.thumbnail_url] : undefined,
    },
  };
}

export default function TestDetailPage() {
  return <TestDetailClient />;
}

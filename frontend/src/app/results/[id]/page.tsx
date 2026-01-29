/**
 * 결과 페이지 (서버 컴포넌트)
 *
 * Phase 3, T3.2-T3.3: 결과 페이지 UI & 공유 기능
 * 동적 OG 메타데이터 지원
 */
import { Metadata } from 'next';
import { notFound } from 'next/navigation';
import ResultPageClient from './ResultPageClient';
import { Card, Button } from '@/components/ui';
import Link from 'next/link';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api/v1';

interface PageProps {
  params: Promise<{ id: string }>;
}

// 서버에서 결과 데이터 가져오기
async function getResultData(id: string) {
  try {
    const response = await fetch(`${API_BASE_URL}/results/${id}`, {
      next: { revalidate: 60 }, // 1분 캐싱
    });

    if (!response.ok) {
      if (response.status === 404 || response.status === 410) {
        return null;
      }
      throw new Error('Failed to fetch result');
    }

    const data = await response.json();
    return data.data;
  } catch (error) {
    console.error('Error fetching result:', error);
    return null;
  }
}

// 테스트 정보 가져오기
async function getTestData(testId: string) {
  try {
    const response = await fetch(`${API_BASE_URL}/tests/${testId}`, {
      next: { revalidate: 300 }, // 5분 캐싱
    });

    if (!response.ok) return null;

    const data = await response.json();
    return data.data;
  } catch {
    return null;
  }
}

// 동적 OG 메타데이터 생성
export async function generateMetadata({ params }: PageProps): Promise<Metadata> {
  const { id } = await params;
  const result = await getResultData(id);

  if (!result) {
    return {
      title: '결과를 찾을 수 없습니다 | Simly',
      description: '요청하신 테스트 결과를 찾을 수 없습니다.',
    };
  }

  const test = await getTestData(result.test_id);
  const title = `${result.result_type} - ${result.result_title}`;
  const description = `"${test?.title || '심리 테스트'}" 결과: ${result.result_type}. 나도 테스트 해보기!`;
  const siteUrl = process.env.NEXT_PUBLIC_SITE_URL || 'https://simly.kr';

  return {
    title: `${title} | Simly`,
    description,
    openGraph: {
      title,
      description,
      type: 'website',
      siteName: 'Simly',
      url: `${siteUrl}/results/${result.share_code || id}`,
      images: result.result_image_url
        ? [
            {
              url: result.result_image_url,
              width: 1200,
              height: 630,
              alt: title,
            },
          ]
        : undefined,
    },
    twitter: {
      card: 'summary_large_image',
      title,
      description,
      images: result.result_image_url ? [result.result_image_url] : undefined,
    },
  };
}

export default async function ResultPage({ params }: PageProps) {
  const { id } = await params;
  const result = await getResultData(id);

  if (!result) {
    return (
      <div className="max-w-[600px] mx-auto px-5 py-8">
        <Card className="text-center py-10">
          <p className="text-[#EF4444] mb-4">결과를 찾을 수 없거나 만료되었습니다.</p>
          <Link href="/">
            <Button variant="secondary">홈으로 돌아가기</Button>
          </Link>
        </Card>
      </div>
    );
  }

  const test = await getTestData(result.test_id);

  return <ResultPageClient result={result} testTitle={test?.title} />;
}

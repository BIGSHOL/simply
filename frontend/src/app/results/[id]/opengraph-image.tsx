/**
 * 결과 페이지 동적 OG 이미지 생성
 *
 * 결과 공유 시 텍스트만 나오는 문제 해결
 * 결과 유형 + 제목 + 테스트명을 시각적 카드로 렌더링
 */
import { ImageResponse } from 'next/og';

export const runtime = 'edge';

export const alt = 'Simly 심리테스트 결과';
export const size = {
  width: 1200,
  height: 630,
};
export const contentType = 'image/png';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api/v1';

// 카테고리별 색상 테마
const CATEGORY_THEMES: Record<string, { gradient: string; accent: string; emoji: string }> = {
  personality: {
    gradient: 'linear-gradient(135deg, #7C3AED 0%, #6366F1 50%, #4F46E5 100%)',
    accent: '#A78BFA',
    emoji: '🧠',
  },
  love: {
    gradient: 'linear-gradient(135deg, #EC4899 0%, #F43F5E 50%, #E11D48 100%)',
    accent: '#FB7185',
    emoji: '💕',
  },
  career: {
    gradient: 'linear-gradient(135deg, #3B82F6 0%, #2563EB 50%, #1D4ED8 100%)',
    accent: '#60A5FA',
    emoji: '💼',
  },
  fun: {
    gradient: 'linear-gradient(135deg, #F59E0B 0%, #F97316 50%, #EA580C 100%)',
    accent: '#FBBF24',
    emoji: '🎮',
  },
};

const DEFAULT_THEME = {
  gradient: 'linear-gradient(135deg, #4F46E5 0%, #7C3AED 50%, #EC4899 100%)',
  accent: '#A78BFA',
  emoji: '🧠',
};

export default async function Image({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;

  // 폰트 로드 + 데이터 fetch 병렬 처리
  const [fontBold, fontRegular, resultRes] = await Promise.all([
    fetch(
      'https://fonts.gstatic.com/s/notosanskr/v36/PbyxFmXiEBPT4ITbgNA5Cgms3VYcOA-vvnIzzuozeLTq8H4hfeE.ttf'
    ).then((res) => res.arrayBuffer()),
    fetch(
      'https://fonts.gstatic.com/s/notosanskr/v36/PbyxFmXiEBPT4ITbgNA5Cgms3VYcOA-vvnIzzuoyeLTq8H4hfeE.ttf'
    ).then((res) => res.arrayBuffer()),
    fetch(`${API_BASE_URL}/results/${id}`, { next: { revalidate: 60 } }).catch(() => null),
  ]);

  // 결과 데이터 파싱
  let resultType = '심리테스트 결과';
  let resultTitle = '나의 유형은?';
  let testTitle = 'AI 심리테스트';
  let category = '';

  if (resultRes?.ok) {
    const resultData = await resultRes.json();
    const result = resultData.data;
    if (result) {
      resultType = result.result_type || resultType;
      resultTitle = result.result_title || resultTitle;

      // 테스트 정보 가져오기
      try {
        const testRes = await fetch(`${API_BASE_URL}/tests/${result.test_id}`, {
          next: { revalidate: 300 },
        });
        if (testRes.ok) {
          const testData = await testRes.json();
          testTitle = testData.data?.title || testTitle;
          category = testData.data?.category || '';
        }
      } catch {}
    }
  }

  const theme = CATEGORY_THEMES[category] || DEFAULT_THEME;

  return new ImageResponse(
    (
      <div
        style={{
          width: '100%',
          height: '100%',
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          justifyContent: 'center',
          background: theme.gradient,
          position: 'relative',
          overflow: 'hidden',
        }}
      >
        {/* 배경 장식 */}
        <div
          style={{
            position: 'absolute',
            top: '-60px',
            right: '-60px',
            width: '280px',
            height: '280px',
            borderRadius: '50%',
            background: 'rgba(255, 255, 255, 0.07)',
            display: 'flex',
          }}
        />
        <div
          style={{
            position: 'absolute',
            bottom: '-80px',
            left: '-40px',
            width: '320px',
            height: '320px',
            borderRadius: '50%',
            background: 'rgba(255, 255, 255, 0.05)',
            display: 'flex',
          }}
        />

        {/* 메인 카드 */}
        <div
          style={{
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            padding: '48px 64px',
            borderRadius: '28px',
            background: 'rgba(255, 255, 255, 0.13)',
            border: '1px solid rgba(255, 255, 255, 0.2)',
            maxWidth: '900px',
          }}
        >
          {/* 테스트 이름 */}
          <div
            style={{
              display: 'flex',
              alignItems: 'center',
              gap: '8px',
              marginBottom: '20px',
              padding: '6px 20px',
              borderRadius: '50px',
              background: 'rgba(255, 255, 255, 0.15)',
              fontFamily: 'Noto Sans KR',
              fontSize: '20px',
              color: 'rgba(255, 255, 255, 0.85)',
            }}
          >
            {theme.emoji} {testTitle}
          </div>

          {/* 결과 유형 (가장 큰 글씨) */}
          <div
            style={{
              fontFamily: 'Noto Sans KR Bold',
              fontSize: '56px',
              fontWeight: 700,
              color: '#FFFFFF',
              marginBottom: '12px',
              display: 'flex',
              textAlign: 'center',
              lineHeight: 1.2,
            }}
          >
            {resultType}
          </div>

          {/* 결과 제목 */}
          <div
            style={{
              fontFamily: 'Noto Sans KR',
              fontSize: '28px',
              color: 'rgba(255, 255, 255, 0.85)',
              marginBottom: '28px',
              display: 'flex',
              textAlign: 'center',
            }}
          >
            {resultTitle}
          </div>

          {/* CTA */}
          <div
            style={{
              display: 'flex',
              padding: '12px 36px',
              borderRadius: '50px',
              background: 'rgba(255, 255, 255, 0.95)',
              fontFamily: 'Noto Sans KR Bold',
              fontSize: '22px',
              fontWeight: 700,
              color: '#4F46E5',
            }}
          >
            나도 테스트 해보기 →
          </div>
        </div>

        {/* 하단 브랜드 */}
        <div
          style={{
            position: 'absolute',
            bottom: '24px',
            display: 'flex',
            alignItems: 'center',
            gap: '8px',
          }}
        >
          <div
            style={{
              fontFamily: 'Noto Sans KR Bold',
              fontSize: '20px',
              fontWeight: 700,
              color: 'rgba(255, 255, 255, 0.6)',
              display: 'flex',
            }}
          >
            Simly
          </div>
          <div
            style={{
              fontFamily: 'Noto Sans KR',
              fontSize: '16px',
              color: 'rgba(255, 255, 255, 0.4)',
              display: 'flex',
            }}
          >
            AI 심리테스트
          </div>
        </div>
      </div>
    ),
    {
      ...size,
      fonts: [
        {
          name: 'Noto Sans KR Bold',
          data: fontBold,
          style: 'normal',
          weight: 700,
        },
        {
          name: 'Noto Sans KR',
          data: fontRegular,
          style: 'normal',
          weight: 400,
        },
      ],
    }
  );
}

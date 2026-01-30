/**
 * Open Graph Image Generator
 *
 * Next.js 14 built-in ImageResponse API를 사용한 동적 OG 이미지 생성
 * 1200x630px 표준 OG 이미지 크기
 */
import { ImageResponse } from 'next/og';

export const runtime = 'edge';
export const alt = 'Simly - AI가 분석하는 나만의 심리테스트';
export const size = { width: 1200, height: 630 };
export const contentType = 'image/png';

export default async function Image() {
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
          background: 'linear-gradient(135deg, #6366F1 0%, #8B5CF6 50%, #A855F7 100%)',
          fontFamily: 'system-ui, -apple-system, sans-serif',
          position: 'relative',
        }}
      >
        {/* 배경 장식 요소 */}
        <div
          style={{
            position: 'absolute',
            top: 40,
            right: 60,
            fontSize: 120,
            opacity: 0.2,
            display: 'flex',
          }}
        >
          🧠
        </div>
        <div
          style={{
            position: 'absolute',
            bottom: 60,
            left: 80,
            fontSize: 100,
            opacity: 0.2,
            display: 'flex',
          }}
        >
          🔮
        </div>
        <div
          style={{
            position: 'absolute',
            top: 80,
            left: 100,
            fontSize: 80,
            opacity: 0.2,
            display: 'flex',
          }}
        >
          💜
        </div>

        {/* 메인 콘텐츠 */}
        <div
          style={{
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            justifyContent: 'center',
            textAlign: 'center',
            padding: '60px',
            zIndex: 1,
          }}
        >
          {/* 로고/사이트명 */}
          <div
            style={{
              fontSize: 96,
              fontWeight: 900,
              color: '#FFFFFF',
              marginBottom: 20,
              display: 'flex',
              letterSpacing: '-0.02em',
            }}
          >
            Simly
          </div>

          {/* 메인 태그라인 */}
          <div
            style={{
              fontSize: 48,
              fontWeight: 600,
              color: '#FFFFFF',
              marginBottom: 40,
              display: 'flex',
              opacity: 0.95,
            }}
          >
            AI가 분석하는 나만의 심리테스트
          </div>

          {/* 카테고리 태그들 */}
          <div
            style={{
              display: 'flex',
              flexWrap: 'wrap',
              gap: 16,
              justifyContent: 'center',
              alignItems: 'center',
            }}
          >
            <div
              style={{
                background: 'rgba(255, 255, 255, 0.25)',
                backdropFilter: 'blur(10px)',
                borderRadius: 24,
                padding: '12px 28px',
                fontSize: 28,
                fontWeight: 600,
                color: '#FFFFFF',
                display: 'flex',
                border: '2px solid rgba(255, 255, 255, 0.3)',
              }}
            >
              성격
            </div>
            <div
              style={{
                background: 'rgba(255, 255, 255, 0.25)',
                backdropFilter: 'blur(10px)',
                borderRadius: 24,
                padding: '12px 28px',
                fontSize: 28,
                fontWeight: 600,
                color: '#FFFFFF',
                display: 'flex',
                border: '2px solid rgba(255, 255, 255, 0.3)',
              }}
            >
              연애
            </div>
            <div
              style={{
                background: 'rgba(255, 255, 255, 0.25)',
                backdropFilter: 'blur(10px)',
                borderRadius: 24,
                padding: '12px 28px',
                fontSize: 28,
                fontWeight: 600,
                color: '#FFFFFF',
                display: 'flex',
                border: '2px solid rgba(255, 255, 255, 0.3)',
              }}
            >
              직장
            </div>
            <div
              style={{
                background: 'rgba(255, 255, 255, 0.25)',
                backdropFilter: 'blur(10px)',
                borderRadius: 24,
                padding: '12px 28px',
                fontSize: 28,
                fontWeight: 600,
                color: '#FFFFFF',
                display: 'flex',
                border: '2px solid rgba(255, 255, 255, 0.3)',
              }}
            >
              재미
            </div>
          </div>
        </div>

        {/* 하단 서브텍스트 */}
        <div
          style={{
            position: 'absolute',
            bottom: 40,
            display: 'flex',
            fontSize: 24,
            color: 'rgba(255, 255, 255, 0.8)',
            fontWeight: 500,
          }}
        >
          지금 바로 나를 알아가는 여정을 시작하세요 ✨
        </div>
      </div>
    ),
    {
      ...size,
    }
  );
}

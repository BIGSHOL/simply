/**
 * 루트 레이아웃
 *
 * Phase 1, T1.2: 메인 레이아웃 & 라우팅
 * Phase 3, T3.3-T3.4: 공유 & AdSense 연동
 */
import type { Metadata, Viewport } from 'next';
import Script from 'next/script';
import { Header, Footer } from '@/components/Layout';
import './globals.css';

const siteUrl = process.env.NEXT_PUBLIC_SITE_URL || 'https://simly-tau.vercel.app';

export const metadata: Metadata = {
  metadataBase: new URL(siteUrl),
  title: '내 안의 진짜 나를 찾아보세요 | Simly',
  description: '10개 질문이면 충분해요. AI가 당신의 성격, 연애 스타일, 숨겨진 본능까지 분석해드립니다. 친구들도 놀란 정확도!',
  keywords: ['심리테스트', 'AI', 'MBTI', '성격테스트', '연애테스트', '직장테스트', '심리분석'],
  openGraph: {
    title: '🧠 10개 질문으로 알아보는 진짜 내 모습',
    description: 'AI가 분석하는 성격, 연애, 직장, 재미 심리테스트. 친구들이 놀란 그 정확도, 직접 확인해보세요!',
    type: 'website',
    siteName: 'Simly',
    url: siteUrl,
    locale: 'ko_KR',
  },
  twitter: {
    card: 'summary_large_image',
    title: '🧠 10개 질문으로 알아보는 진짜 내 모습',
    description: 'AI가 분석하는 성격, 연애, 직장, 재미 심리테스트. 친구들이 놀란 그 정확도!',
  },
};

export const viewport: Viewport = {
  width: 'device-width',
  initialScale: 1,
  maximumScale: 1,
  themeColor: '#6366F1',
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  const adsenseClientId = process.env.NEXT_PUBLIC_ADSENSE_CLIENT_ID;
  const kakaoJsKey = process.env.NEXT_PUBLIC_KAKAO_JS_KEY;

  return (
    <html lang="ko">
      <head>
        {/* Google AdSense */}
        {adsenseClientId && (
          <Script
            async
            src={`https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=${adsenseClientId}`}
            crossOrigin="anonymous"
            strategy="afterInteractive"
          />
        )}

        {/* Kakao SDK */}
        {kakaoJsKey && (
          <Script
            src="https://t1.kakaocdn.net/kakao_js_sdk/2.6.0/kakao.min.js"
            integrity="sha384-6MFdIr0zOira1CHQkedUqJVql0YtcZA1P0nbPrQYJXVJZUkTk/oX4U9GhsVfhq+K"
            crossOrigin="anonymous"
            strategy="afterInteractive"
          />
        )}
      </head>
      <body className="min-h-screen flex flex-col antialiased">
        <Header />
        <main className="flex-1">{children}</main>
        <Footer />
      </body>
    </html>
  );
}

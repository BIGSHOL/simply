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

export const metadata: Metadata = {
  title: 'Simly - AI 심리테스트',
  description: 'AI가 만들어주는 나만의 심리테스트 결과',
  keywords: ['심리테스트', 'AI', 'MBTI', '성격테스트', '연애테스트'],
  openGraph: {
    title: 'Simly - AI 심리테스트',
    description: 'AI가 만들어주는 나만의 심리테스트 결과',
    type: 'website',
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

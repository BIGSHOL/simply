/**
 * AdSense 컴포넌트
 *
 * Phase 3, T3.4: AdSense 연동
 *
 * 사용법:
 * 1. Google AdSense 계정에서 광고 단위를 생성
 * 2. .env.local에 NEXT_PUBLIC_ADSENSE_CLIENT_ID 설정
 * 3. 광고 슬롯 ID를 slot prop으로 전달
 */
'use client';

import { useEffect, useRef } from 'react';

interface AdSenseProps {
  slot: string;
  format?: 'auto' | 'rectangle' | 'horizontal' | 'vertical';
  responsive?: boolean;
  className?: string;
}

export default function AdSense({
  slot,
  format = 'auto',
  responsive = true,
  className = '',
}: AdSenseProps) {
  const adRef = useRef<HTMLModElement>(null);
  const isLoaded = useRef(false);

  useEffect(() => {
    // 개발 환경에서는 광고 로드하지 않음
    if (process.env.NODE_ENV === 'development') {
      return;
    }

    // 클라이언트 ID가 없으면 광고 로드하지 않음
    const clientId = process.env.NEXT_PUBLIC_ADSENSE_CLIENT_ID;
    if (!clientId) {
      console.warn('AdSense client ID not configured');
      return;
    }

    // 이미 로드되었으면 스킵
    if (isLoaded.current) {
      return;
    }

    try {
      // AdSense 스크립트가 로드되었는지 확인
      if (typeof window !== 'undefined' && (window as any).adsbygoogle) {
        ((window as any).adsbygoogle = (window as any).adsbygoogle || []).push({});
        isLoaded.current = true;
      }
    } catch (err) {
      console.error('AdSense error:', err);
    }
  }, []);

  // 개발 환경에서는 플레이스홀더 표시
  if (process.env.NODE_ENV === 'development') {
    return (
      <div
        className={`bg-gray-100 border-2 border-dashed border-gray-300 rounded-xl flex items-center justify-center text-gray-400 text-sm ${className}`}
        style={{ minHeight: format === 'horizontal' ? '90px' : '250px' }}
      >
        광고 영역 (개발 모드)
      </div>
    );
  }

  const clientId = process.env.NEXT_PUBLIC_ADSENSE_CLIENT_ID;
  if (!clientId) {
    return null;
  }

  return (
    <ins
      ref={adRef}
      className={`adsbygoogle ${className}`}
      style={{ display: 'block' }}
      data-ad-client={clientId}
      data-ad-slot={slot}
      data-ad-format={format}
      data-full-width-responsive={responsive ? 'true' : 'false'}
    />
  );
}

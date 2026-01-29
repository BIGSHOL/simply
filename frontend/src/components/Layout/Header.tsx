/**
 * Header 컴포넌트
 *
 * Phase 1, T1.2: 메인 레이아웃 & 라우팅
 */
'use client';

import Link from 'next/link';

export default function Header() {
  return (
    <header className="sticky top-0 z-50 bg-white/80 backdrop-blur-sm border-b border-[#E5E7EB]">
      <div className="max-w-[600px] mx-auto px-4 sm:px-5 h-14 flex items-center justify-between">
        <Link href="/" className="flex items-center gap-2">
          <span className="text-xl font-bold text-[#6366F1]">Simly</span>
        </Link>

        <nav className="flex items-center gap-4">
          <Link
            href="/"
            className="text-sm text-[#6B7280] hover:text-[#111827] transition-colors"
          >
            홈
          </Link>
        </nav>
      </div>
    </header>
  );
}

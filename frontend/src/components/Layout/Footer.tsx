/**
 * Footer 컴포넌트
 *
 * Phase 1, T1.2: 메인 레이아웃 & 라우팅
 */
export default function Footer() {
  const currentYear = new Date().getFullYear();

  return (
    <footer className="border-t border-[#E5E7EB] bg-white">
      <div className="max-w-[600px] mx-auto px-4 sm:px-5 py-6">
        <div className="flex flex-col items-center gap-3 text-center">
          <p className="text-sm text-[#6B7280]">
            AI가 만들어주는 재미있는 심리테스트
          </p>
          <p className="text-xs text-[#9CA3AF]">
            © {currentYear} Simly. All rights reserved.
          </p>
        </div>
      </div>
    </footer>
  );
}

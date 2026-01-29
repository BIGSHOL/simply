/**
 * 메인 페이지
 *
 * Phase 2, T2.1: 테스트 목록 화면
 * 카테고리 기반 UI로 개선
 */
import { CategoryList } from '@/components/test';

export default function HomePage() {
  return (
    <div className="max-w-[600px] mx-auto px-4 sm:px-5 py-8">
      {/* 히어로 섹션 */}
      <section className="text-center mb-10">
        <h1 className="text-xl sm:text-2xl md:text-3xl font-bold text-[#111827] mb-3">
          AI가 분석하는
          <br />
          <span className="text-[#6366F1]">나만의 심리테스트</span>
        </h1>
        <p className="text-[#6B7280] text-base">
          카테고리를 선택하고 나에게 딱 맞는 테스트를 찾아보세요!
        </p>
      </section>

      {/* 카테고리별 테스트 섹션 */}
      <section>
        <h2 className="text-lg font-semibold text-[#111827] mb-4 flex items-center gap-2">
          <span>📂</span>
          <span>테스트 카테고리</span>
        </h2>

        <CategoryList />
      </section>
    </div>
  );
}

/**
 * 결과 페이지 레이아웃
 *
 * Phase 3, T3.3: 공유 기능
 * 메타데이터는 page.tsx의 generateMetadata에서 동적으로 처리
 */

export default function ResultLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return <>{children}</>;
}

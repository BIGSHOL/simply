/**
 * 연애 유형 테스트 - 프로그레스 바 컴포넌트
 * Phase 1, T1-LOVE.3
 */
import React from 'react';

interface ProgressBarProps {
  current: number; // 현재 문항 (1-20)
  total: number; // 전체 문항 수 (20)
  milestones?: number[]; // 마일스톤 위치 [5, 10, 15, 20]
  showLabel?: boolean; // "8/20" 라벨 표시
}

const DEFAULT_MILESTONES = [5, 10, 15, 20];

export const ProgressBar: React.FC<ProgressBarProps> = ({
  current,
  total,
  milestones = DEFAULT_MILESTONES,
  showLabel = true,
}) => {
  const percentage = (current / total) * 100;

  // 구간별 색상 (워밍업 → 몰입 → 도전 → 스퍼트)
  const getSectionColor = () => {
    if (current <= 5) return '#FF6B6B'; // 핑크
    if (current <= 10) return '#7B68EE'; // 퍼플
    if (current <= 15) return '#50C878'; // 민트
    return '#FFA500'; // 오렌지
  };

  return (
    <div className="w-full space-y-2">
      {/* 프로그레스 바 */}
      <div className="relative h-2 bg-gray-200 rounded-full overflow-hidden">
        <div
          className="h-full transition-all duration-400 ease-out rounded-full"
          style={{
            width: `${percentage}%`,
            backgroundColor: getSectionColor(),
          }}
          role="progressbar"
          aria-valuenow={current}
          aria-valuemin={1}
          aria-valuemax={total}
          aria-label={`20문항 중 ${current}번째`}
        />

        {/* 마일스톤 표시 */}
        {milestones.map((milestone) => {
          const milestonePos = (milestone / total) * 100;
          const isPassed = current >= milestone;

          return (
            <div
              key={milestone}
              className="absolute top-1/2 transform -translate-y-1/2 -translate-x-1/2"
              style={{ left: `${milestonePos}%` }}
            >
              <div
                className={`w-3 h-3 rounded-full border-2 border-white transition-colors duration-200 ${
                  isPassed ? 'bg-yellow-400' : 'bg-gray-300'
                }`}
                title={`${milestone}번째 문항`}
              />
            </div>
          );
        })}
      </div>

      {/* 라벨 */}
      {showLabel && (
        <div className="flex justify-between items-center text-sm">
          <span className="font-medium text-gray-700">
            {current}/{total}
          </span>
          <span className="text-gray-500">{Math.round(percentage)}% 완료</span>
        </div>
      )}
    </div>
  );
};

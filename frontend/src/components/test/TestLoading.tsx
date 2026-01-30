/**
 * TestLoading 컴포넌트 (결과 분석 중 로딩 화면)
 *
 * MZ 감성 UX: 카테고리별 이모지 회전 애니메이션 + 단계별 체크리스트
 */
'use client';

import { useEffect, useState } from 'react';

// 테스트별 로딩 테마 설정
export interface LoadingTheme {
  emojis: string[];
  messages: string[];
  title: string;
  gradient: { from: string; to: string };
  accent: string;
}

// 테스트 ID별 커스텀 테마 (각 테스트마다 고유한 로딩 화면)
export const TEST_LOADING_THEMES: Record<string, LoadingTheme> = {
  // 음식 성격 테스트
  'food-personality': {
    emojis: ['🍕', '🌶️', '🍰', '🍛', '🍣', '🥗', '🍵', '🍚'],
    messages: [
      '당신의 음식 DNA를 분석 중...',
      '셰프가 레시피를 확인하고 있어요 👨‍🍳',
      '맛집 데이터베이스 검색 중...',
      '당신에게 딱 맞는 음식을 찾는 중...',
    ],
    title: '당신의 음식 상을\n분석하고 있어요...',
    gradient: { from: '#FFF7ED', to: '#FEF3C7' },
    accent: '#FB923C',
  },
  // 연애 유형 테스트
  'love-type': {
    emojis: ['💕', '💘', '💝', '💗', '💓', '💞', '💖', '🥰'],
    messages: [
      '당신의 연애 DNA를 분석 중...',
      '큐피드가 화살을 조준하고 있어요 💘',
      '연애 패턴 데이터베이스 검색 중...',
      '당신에게 딱 맞는 연애 유형을 찾는 중...',
    ],
    title: '당신의 연애 유형을\n분석하고 있어요...',
    gradient: { from: '#FDF2F8', to: '#FCE7F3' },
    accent: '#EC4899',
  },
  // 직장인 테스트
  'career-type': {
    emojis: ['💼', '📊', '🎯', '💡', '🚀', '📈', '⭐', '🏆'],
    messages: [
      '당신의 직장인 DNA를 분석 중...',
      '커리어 코치가 검토하고 있어요 👔',
      '직장 적성 데이터베이스 검색 중...',
      '당신에게 딱 맞는 업무 스타일을 찾는 중...',
    ],
    title: '당신의 직장인 유형을\n분석하고 있어요...',
    gradient: { from: '#EFF6FF', to: '#DBEAFE' },
    accent: '#3B82F6',
  },
  // 곤충 테스트
  'insect-type': {
    emojis: ['🐛', '🦋', '🐝', '🐞', '🦗', '🪲', '🦟', '🪳'],
    messages: [
      '당신의 곤충 DNA를 분석 중...',
      '곤충 박사가 현미경을 들여다보고 있어요 🔬',
      '곤충 도감 데이터베이스 검색 중...',
      '당신과 닮은 곤충을 찾는 중...',
    ],
    title: '당신과 닮은 곤충을\n찾고 있어요...',
    gradient: { from: '#ECFDF5', to: '#D1FAE5' },
    accent: '#10B981',
  },
  // 동물 테스트
  'animal-type': {
    emojis: ['🦁', '🐯', '🐻', '🦊', '🐰', '🐨', '🐼', '🦄'],
    messages: [
      '당신의 동물 DNA를 분석 중...',
      '동물의 왕국에서 검색 중 🌿',
      '야생의 본능을 깨우는 중...',
      '당신의 동물 친구를 찾는 중...',
    ],
    title: '당신과 닮은 동물을\n찾고 있어요...',
    gradient: { from: '#FEF9C3', to: '#FEF08A' },
    accent: '#EAB308',
  },
  // MBTI 테스트
  'mbti-type': {
    emojis: ['🧠', '💭', '🔮', '✨', '🎯', '💫', '🌟', '🪐'],
    messages: [
      '당신의 성격 유형을 분석 중...',
      'MBTI 전문가가 검토하고 있어요 🧐',
      '16가지 유형 중 매칭 중...',
      '당신만의 특별한 유형을 찾는 중...',
    ],
    title: '당신의 MBTI 유형을\n분석하고 있어요...',
    gradient: { from: '#F5F3FF', to: '#EDE9FE' },
    accent: '#8B5CF6',
  },
  // 아재력 테스트
  'ajae-type': {
    emojis: ['👴', '🍺', '⛳', '📰', '🧦', '👔', '📺', '🎣'],
    messages: [
      '당신의 아재력을 측정 중...',
      '아재 개그 데이터베이스 검색 중... 킹받네~ 😂',
      '오~ 이 정도면 프로 아재인데?',
      '아버지... 저도 커서 아재가 되나요?',
    ],
    title: '당신의 아재력을\n측정하고 있어요...',
    gradient: { from: '#FEF3C7', to: '#FDE68A' },
    accent: '#D97706',
  },
  // 오늘의 운세 테스트
  'fortune-type': {
    emojis: ['🔮', '⭐', '🌙', '✨', '🎴', '🪬', '🌟', '💫'],
    messages: [
      '오늘의 별자리를 분석 중...',
      '운명의 카드를 뽑고 있어요 🎴',
      '우주의 기운을 읽는 중...',
      '당신의 행운이 다가오고 있어요!',
    ],
    title: '오늘의 운세를\n점치고 있어요...',
    gradient: { from: '#1E1B4B', to: '#312E81' },
    accent: '#A78BFA',
  },
  // 직장 계급 테스트
  'rank-type': {
    emojis: ['👑', '🎖️', '⚔️', '🏰', '🛡️', '⚜️', '🗡️', '🎪'],
    messages: [
      '당신의 직장 내 서열을 분석 중...',
      '조직 내 위치를 파악하고 있어요 📊',
      '당신의 리더십 DNA 검사 중...',
      '직장 내 포지션을 찾는 중...',
    ],
    title: '당신의 직장 계급을\n분석하고 있어요...',
    gradient: { from: '#FEF2F2', to: '#FEE2E2' },
    accent: '#DC2626',
  },
  // 회사 캐릭터 테스트
  'workplace-type': {
    emojis: ['🏢', '💻', '☕', '📋', '🖨️', '📊', '🗂️', '⏰'],
    messages: [
      '당신의 회사 생활을 분석 중...',
      '사무실에서 당신을 관찰하고 있어요 👀',
      '직장 동료들의 증언을 수집 중...',
      '당신만의 회사 생존법을 찾는 중...',
    ],
    title: '회사에서 당신은\n어떤 캐릭터일까요...',
    gradient: { from: '#F0FDF4', to: '#DCFCE7' },
    accent: '#16A34A',
  },
  // MBTI 연애 테스트 (기존 mbti-type과 별도)
  'mbti-love-type': {
    emojis: ['💕', '🧠', '💘', '✨', '🔮', '💝', '🌟', '💫'],
    messages: [
      '당신의 MBTI 연애 코드를 분석 중...',
      '16가지 유형 중 연애 스타일 매칭 중 💕',
      '심리학자가 검토하고 있어요 🧐',
      '당신만의 연애 패턴을 찾는 중...',
    ],
    title: '연애할 때 진짜 내 모습을\n찾고 있어요...',
    gradient: { from: '#FDF4FF', to: '#FAE8FF' },
    accent: '#D946EF',
  },
  // --- 신규 테스트 ---
  // [personality] 색깔 성격 테스트
  'color-personality': {
    emojis: ['🔴', '🟠', '🟡', '🟢', '🔵', '🟣', '⚪', '⚫'],
    messages: [
      '당신의 색깔 DNA를 분석 중...',
      '컬러 전문가가 팔레트를 조합하고 있어요 🎨',
      '무지개 스펙트럼 스캔 중...',
      '당신만의 컬러를 찾는 중...',
    ],
    title: '당신의 색깔을\n찾고 있어요...',
    gradient: { from: '#FDF2F8', to: '#EDE9FE' },
    accent: '#A855F7',
  },
  // [love] 전생 러브스토리 테스트
  'past-life-love': {
    emojis: ['🏰', '⚔️', '👑', '📜', '🕯️', '💍', '🌹', '🗝️'],
    messages: [
      '전생의 기억을 불러오는 중...',
      '타임머신이 과거로 이동 중 ⏳',
      '전생의 인연을 추적하고 있어요...',
      '당신의 전생 러브스토리를 발굴 중...',
    ],
    title: '전생의 러브스토리를\n되살리고 있어요...',
    gradient: { from: '#FEF3C7', to: '#F5E6D3' },
    accent: '#B45309',
  },
  // [love] 이별 회복 유형 테스트
  'breakup-recovery': {
    emojis: ['💔', '🩹', '🌱', '☀️', '💪', '🎵', '📖', '✈️'],
    messages: [
      '당신의 회복 패턴을 분석 중...',
      '마음의 상처 치유 경로를 탐색 중 🩹',
      '회복 탄력성 지수를 측정하고 있어요...',
      '더 강해진 당신을 찾는 중...',
    ],
    title: '이별 후 당신의 회복법을\n분석하고 있어요...',
    gradient: { from: '#F0F9FF', to: '#E0F2FE' },
    accent: '#0EA5E9',
  },
  // [career] 퇴사 후 부캐 테스트
  'side-hustle': {
    emojis: ['🚀', '💰', '🎬', '☕', '💻', '📸', '🎸', '✍️'],
    messages: [
      '당신의 숨겨진 재능을 스캔 중...',
      '부캐 적성 데이터베이스 검색 중 🔍',
      '퇴사 시뮬레이션 돌리는 중...',
      '당신의 제2의 인생을 설계 중...',
    ],
    title: '퇴사 후 당신의 부캐를\n찾고 있어요...',
    gradient: { from: '#FFFBEB', to: '#FEF3C7' },
    accent: '#F59E0B',
  },
  // [career] 회의실 생존 유형 테스트
  'meeting-survival': {
    emojis: ['🗣️', '📊', '😴', '✋', '📝', '🤔', '👏', '🙄'],
    messages: [
      '당신의 회의 패턴을 분석 중...',
      '지난 회의록을 검토하고 있어요 📋',
      '회의실 CCTV 분석 중...',
      '당신의 회의 생존법을 찾는 중...',
    ],
    title: '회의실에서 당신은\n어떤 유형일까요...',
    gradient: { from: '#F8FAFC', to: '#E2E8F0' },
    accent: '#475569',
  },
  // [fun] 좀비 아포칼립스 생존 유형
  'zombie-survival': {
    emojis: ['🧟', '🔫', '🏥', '🔥', '🚗', '🪓', '🧬', '💀'],
    messages: [
      '좀비 바이러스 시뮬레이션 중...',
      '생존 적성을 테스트하고 있어요 🧟',
      '최적의 은신처를 탐색 중...',
      '당신의 생존 확률을 계산하는 중...',
    ],
    title: '좀비 세계에서 당신의\n역할을 찾고 있어요...',
    gradient: { from: '#1A1A2E', to: '#16213E' },
    accent: '#E74C3C',
  },
  // [fun] 무인도 생존 유형
  'island-survival': {
    emojis: ['🏝️', '🌊', '🔥', '🥥', '🐚', '⛺', '🎣', '🌴'],
    messages: [
      '무인도 생존 시뮬레이션 가동 중...',
      '당신의 야생 본능을 깨우는 중 🌊',
      '생존 장비를 체크하고 있어요...',
      '무인도에서 당신의 역할을 찾는 중...',
    ],
    title: '무인도에서 당신은\n어떤 생존자일까요...',
    gradient: { from: '#ECFDF5', to: '#CFFAFE' },
    accent: '#0D9488',
  },
  // [love] 플러팅 스타일 테스트
  'flirting-style': {
    emojis: ['😏', '💌', '👀', '🫣', '😘', '🤭', '💋', '🦋'],
    messages: [
      '당신의 플러팅 DNA를 분석 중...',
      '호감 신호 패턴을 해독하고 있어요 👀',
      '연애 고수들의 데이터와 비교 중...',
      '당신만의 플러팅 기술을 찾는 중...',
    ],
    title: '당신의 플러팅 스타일을\n분석하고 있어요...',
    gradient: { from: '#FFF1F2', to: '#FFE4E6' },
    accent: '#F43F5E',
  },
  // [personality] 뇌 유형 테스트
  'brain-type': {
    emojis: ['🧠', '💡', '⚡', '🔬', '🎨', '📐', '💭', '🧩'],
    messages: [
      '당신의 뇌 회로를 스캔 중...',
      '좌뇌와 우뇌의 밸런스를 측정 중 🧠',
      '시냅스 연결 패턴을 분석하고 있어요...',
      '당신의 뇌 유형을 찾는 중...',
    ],
    title: '당신의 뇌 유형을\n분석하고 있어요...',
    gradient: { from: '#EFF6FF', to: '#E0E7FF' },
    accent: '#6366F1',
  },
  // [career] 월급 사용 유형 테스트
  'salary-spending': {
    emojis: ['💸', '💰', '🛍️', '📊', '💳', '🏦', '🎰', '✈️'],
    messages: [
      '당신의 소비 DNA를 분석 중...',
      '통장 잔고 시뮬레이션 돌리는 중 💸',
      '월급날부터 다음 월급날까지 추적 중...',
      '당신의 소비 유형을 찾는 중...',
    ],
    title: '당신의 월급 사용법을\n분석하고 있어요...',
    gradient: { from: '#ECFDF5', to: '#D1FAE5' },
    accent: '#059669',
  },
  // [fun] 조선시대 환생 신분 테스트
  'joseon-rebirth': {
    emojis: ['👘', '📜', '🏯', '🎎', '⚔️', '🍶', '🖌️', '👑'],
    messages: [
      '조선왕조실록을 검색 중...',
      '전생의 호적을 확인하고 있어요 📜',
      '사주팔자를 분석하는 중...',
      '조선시대 당신의 신분을 찾는 중...',
    ],
    title: '조선시대 당신의 신분을\n찾고 있어요...',
    gradient: { from: '#FFFBEB', to: '#FEF9C3' },
    accent: '#92400E',
  },
};

// 타이틀 키워드 → 테마 ID 매핑 (testId가 없을 때 타이틀로 매칭)
const TITLE_KEYWORD_MAP: Record<string, string> = {
  // personality
  '음식': 'food-personality',
  '곤충': 'insect-type',
  '동물': 'animal-type',
  '야생': 'animal-type',
  '색깔': 'color-personality',
  '컬러': 'color-personality',
  // love
  '연애 유형': 'love-type',
  '연애 스타일': 'mbti-love-type',
  '전생': 'past-life-love',
  '러브스토리': 'past-life-love',
  '이별': 'breakup-recovery',
  '회복': 'breakup-recovery',
  // career
  '직장인': 'career-type',
  '직장 계급': 'rank-type',
  '계급': 'rank-type',
  '회사': 'workplace-type',
  '캐릭터': 'workplace-type',
  '퇴사': 'side-hustle',
  '부캐': 'side-hustle',
  '회의': 'meeting-survival',
  // fun
  '아재': 'ajae-type',
  '운세': 'fortune-type',
  '좀비': 'zombie-survival',
  '무인도': 'island-survival',
  '생존': 'island-survival',
  '조선': 'joseon-rebirth',
  '환생': 'joseon-rebirth',
  // general
  'MBTI': 'mbti-type',
  '내면': 'mbti-type',
};

/**
 * 테스트 타이틀에서 적절한 테마를 찾습니다
 */
export function getThemeByTitle(title: string): LoadingTheme {
  for (const [keyword, themeId] of Object.entries(TITLE_KEYWORD_MAP)) {
    if (title.includes(keyword)) {
      return TEST_LOADING_THEMES[themeId] || DEFAULT_THEME;
    }
  }
  return DEFAULT_THEME;
}

// 기본 테마 (매칭되는 테스트가 없을 때)
const DEFAULT_THEME: LoadingTheme = {
  emojis: ['✨', '🎯', '💫', '🌟', '⭐', '🔮', '🎪', '🎨'],
  messages: [
    '당신의 숨겨진 매력을 분석 중...',
    '결과가 거의 나왔어요! 😎',
    '당신만의 특별함을 찾는 중...',
    '흥미로운 결과가 기다리고 있어요!',
  ],
  title: '결과를 분석하고 있어요...',
  gradient: { from: '#F8FAFC', to: '#F1F5F9' },
  accent: '#6366F1',
};

const ANALYSIS_STEPS = [
  '성격 유형 분석',
  '취향 패턴 매칭',
  '최종 결과 생성',
];

interface TestLoadingProps {
  /** 테스트 ID (테스트별 고유 테마 적용) */
  testId?: string;
  /** 테스트 타이틀 (ID 매칭 실패 시 키워드로 테마 찾기) */
  testTitle?: string;
  /** 커스텀 테마 (직접 지정 시 testId/testTitle보다 우선) */
  customTheme?: Partial<LoadingTheme>;
  onComplete?: () => void;
}

export default function TestLoading({ testId, testTitle, customTheme, onComplete }: TestLoadingProps) {
  const [currentStep, setCurrentStep] = useState(0);
  const [messageIndex, setMessageIndex] = useState(0);

  // 테마 결정: customTheme > testId 매칭 > testTitle 키워드 매칭 > 기본 테마
  const getBaseTheme = (): LoadingTheme => {
    if (testId && TEST_LOADING_THEMES[testId]) {
      return TEST_LOADING_THEMES[testId];
    }
    if (testTitle) {
      return getThemeByTitle(testTitle);
    }
    return DEFAULT_THEME;
  };

  const baseTheme = getBaseTheme();
  const theme: LoadingTheme = customTheme ? { ...baseTheme, ...customTheme } : baseTheme;

  // 단계별 진행 애니메이션
  useEffect(() => {
    const stepTimers = ANALYSIS_STEPS.map((_, index) =>
      setTimeout(() => {
        setCurrentStep(index + 1);
        if (index === ANALYSIS_STEPS.length - 1 && onComplete) {
          setTimeout(onComplete, 500);
        }
      }, (index + 1) * 800)
    );

    return () => stepTimers.forEach(clearTimeout);
  }, [onComplete]);

  // 메시지 로테이션
  useEffect(() => {
    const interval = setInterval(() => {
      setMessageIndex((prev) => (prev + 1) % theme.messages.length);
    }, 2000);

    return () => clearInterval(interval);
  }, [theme.messages.length]);

  return (
    <div
      className="fixed inset-0 flex flex-col items-center justify-center z-50"
      style={{
        background: `linear-gradient(to bottom, ${theme.gradient.from}, ${theme.gradient.to})`
      }}
    >
      {/* 이모지 회전 애니메이션 */}
      <div className="relative w-40 h-40 mb-8">
        {theme.emojis.map((emoji, index) => {
          const angle = (index * 360) / theme.emojis.length;
          const delay = index * 0.1;
          return (
            <div
              key={emoji}
              className="absolute text-3xl animate-spin"
              style={{
                left: '50%',
                top: '50%',
                transform: `rotate(${angle}deg) translateY(-60px) rotate(-${angle}deg)`,
                animationDuration: '3s',
                animationDelay: `${delay}s`,
              }}
            >
              {emoji}
            </div>
          );
        })}
        {/* 중앙 그라디언트 원 */}
        <div className="absolute inset-0 flex items-center justify-center">
          <div
            className="w-16 h-16 rounded-full animate-pulse shadow-lg"
            style={{ background: `linear-gradient(to bottom right, ${theme.accent}, ${theme.accent}dd)` }}
          />
        </div>
      </div>

      {/* 메인 메시지 */}
      <h2 className="text-xl font-bold text-[#111827] mb-2 text-center whitespace-pre-line">
        {theme.title}
      </h2>

      {/* 서브 메시지 (로테이션) */}
      <p className="text-[#6B7280] text-sm mb-8 h-5 transition-opacity duration-300">
        {theme.messages[messageIndex]}
      </p>

      {/* 분석 단계 체크리스트 */}
      <div className="bg-white/80 backdrop-blur rounded-2xl p-4 sm:p-5 shadow-lg w-[280px] max-w-[85vw]">
        {ANALYSIS_STEPS.map((step, index) => (
          <div
            key={step}
            className={`flex items-center gap-3 py-2 transition-all duration-300 ${
              index < currentStep ? 'opacity-100' : 'opacity-40'
            }`}
          >
            {/* 아이콘 */}
            <div
              className={`w-6 h-6 rounded-full flex items-center justify-center transition-all duration-300 ${
                index < currentStep
                  ? 'bg-[#10B981] text-white'
                  : index === currentStep
                  ? 'text-white animate-pulse'
                  : 'bg-[#E5E7EB] text-[#9CA3AF]'
              }`}
              style={index === currentStep ? { backgroundColor: theme.accent } : undefined}
            >
              {index < currentStep ? (
                <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={3}>
                  <path strokeLinecap="round" strokeLinejoin="round" d="M5 13l4 4L19 7" />
                </svg>
              ) : index === currentStep ? (
                <div className="w-2 h-2 bg-white rounded-full" />
              ) : (
                <div className="w-2 h-2 bg-current rounded-full" />
              )}
            </div>

            {/* 텍스트 */}
            <span
              className={`text-sm ${
                index < currentStep
                  ? 'text-[#111827] font-medium'
                  : index === currentStep
                  ? 'font-medium'
                  : 'text-[#9CA3AF]'
              }`}
              style={index === currentStep ? { color: theme.accent } : undefined}
            >
              {step}
              {index < currentStep && ' 완료'}
              {index === currentStep && '...'}
            </span>
          </div>
        ))}
      </div>
    </div>
  );
}

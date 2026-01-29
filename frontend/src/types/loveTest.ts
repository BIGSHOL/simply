// 연애 유형 테스트 전용 타입 정의
// Phase 1, T1-LOVE.3

export interface LoveTestAnswer {
  questionId: string; // "Q1", "Q2", ...
  choice: 'A' | 'B';
}

export interface DimensionScores {
  proactivity: number; // 적극성 0-100
  expression: number; // 감정표현 0-100
  independence: number; // 독립성 0-100
  commitment: number; // 헌신도 0-100
  romance: number; // 로맨스 0-100
}

export interface LoveTypeQuestion {
  id: string; // "Q1", "Q2", ...
  orderNum: number; // 1-20
  content: string; // 문항 텍스트
  choiceA: string; // A 선택지
  choiceB: string; // B 선택지
  imageUrl?: string; // 일러스트 (선택)
}

export interface LoveTypeResult {
  id: string; // 유형 ID
  typeName: string; // "직진 러버"
  englishName: string; // "Straight Shooter"
  tagline: string; // 한줄 설명
  description: string; // 상세 설명
  traits: string[]; // 연애 스타일 특징
  strengths: string[]; // 강점
  growthPoints: string[]; // 성장 포인트
  compatibleTypes: string[]; // 궁합 유형
  hashtags: string[]; // SNS 해시태그
  characterImage?: string; // 캐릭터 이미지
  scores: DimensionScores; // 5축 점수
}

export interface LoveTest {
  id: string;
  title: string;
  description: string;
  thumbnailUrl?: string;
  questionCount: number;
  questions: LoveTypeQuestion[];
}

export interface LoveTestProgress {
  currentQuestion: number; // 1-20
  answers: LoveTestAnswer[];
  startedAt: number; // timestamp
  lastUpdated: number; // timestamp
}

export type LoadingPhase = 'analyzing' | 'calculating' | 'matching' | 'complete';

export type SharePlatform = 'kakao' | 'copy' | 'download' | 'instagram' | 'twitter' | 'more';

export interface ShareData {
  title: string;
  description: string;
  imageUrl: string;
  url: string;
}

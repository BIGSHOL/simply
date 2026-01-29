/**
 * Mock 테스트 데이터
 *
 * Phase 0, T0.5.3: 프론트엔드 테스트 + MSW Mock
 */
import type { TestSummary, Test, Result } from '@/types';

export const mockTestSummaries: TestSummary[] = [
  {
    id: 'test-1',
    title: 'MBTI로 알아보는 나의 연애 스타일',
    description: '당신의 연애 성향을 MBTI 기반으로 분석해 드립니다',
    thumbnail_url: '/images/tests/love-mbti.jpg',
    category: 'love',
    question_count: 10,
    play_count: 12345,
  },
  {
    id: 'test-2',
    title: '직장에서 나는 어떤 유형?',
    description: '직장 내 나의 성격과 업무 스타일을 알아보세요',
    thumbnail_url: '/images/tests/career-type.jpg',
    category: 'career',
    question_count: 8,
    play_count: 8765,
  },
  {
    id: 'test-3',
    title: '숨겨진 내면의 나',
    description: 'AI가 분석하는 당신의 진짜 성격',
    thumbnail_url: '/images/tests/personality-hidden.jpg',
    category: 'personality',
    question_count: 12,
    play_count: 5432,
  },
  {
    id: 'test-4',
    title: '오늘의 운세 테스트',
    description: '재미로 보는 오늘의 운세',
    thumbnail_url: null,
    category: 'fun',
    question_count: 5,
    play_count: 3210,
  },
];

export const mockTestDetail: Test = {
  id: 'test-1',
  title: 'MBTI로 알아보는 나의 연애 스타일',
  description: '당신의 연애 성향을 MBTI 기반으로 분석해 드립니다',
  thumbnail_url: '/images/tests/love-mbti.jpg',
  category: 'love',
  question_count: 3,
  play_count: 12345,
  questions: [
    {
      id: 'q-1',
      order_num: 1,
      content: '연인과 데이트할 때 선호하는 방식은?',
      image_url: null,
      choices: [
        { id: 'c-1-1', order_num: 1, content: '집에서 영화 보기' },
        { id: 'c-1-2', order_num: 2, content: '새로운 맛집 탐방' },
        { id: 'c-1-3', order_num: 3, content: '야외 활동 (등산, 자전거 등)' },
        { id: 'c-1-4', order_num: 4, content: '문화생활 (전시회, 공연 등)' },
      ],
    },
    {
      id: 'q-2',
      order_num: 2,
      content: '연인과 갈등이 생겼을 때 나는?',
      image_url: null,
      choices: [
        { id: 'c-2-1', order_num: 1, content: '즉시 대화로 해결하려 한다' },
        { id: 'c-2-2', order_num: 2, content: '시간을 두고 생각한 뒤 대화한다' },
        { id: 'c-2-3', order_num: 3, content: '상대가 먼저 말할 때까지 기다린다' },
        { id: 'c-2-4', order_num: 4, content: '글로 내 감정을 전달한다' },
      ],
    },
    {
      id: 'q-3',
      order_num: 3,
      content: '이상적인 연인의 조건은?',
      image_url: null,
      choices: [
        { id: 'c-3-1', order_num: 1, content: '대화가 잘 통하는 사람' },
        { id: 'c-3-2', order_num: 2, content: '같은 취미를 공유하는 사람' },
        { id: 'c-3-3', order_num: 3, content: '경제적으로 안정된 사람' },
        { id: 'c-3-4', order_num: 4, content: '나를 있는 그대로 받아주는 사람' },
      ],
    },
  ],
};

export const mockResult: Result = {
  id: 'result-1',
  test_id: 'test-1',
  result_type: 'ENFP형 연애 스타일',
  result_title: '열정적인 로맨티스트',
  result_content: `당신은 **열정적인 로맨티스트** 유형입니다!

## 연애 성향
- 감정 표현에 솔직하고 적극적입니다
- 새로운 경험을 함께 하는 것을 좋아합니다
- 상대방의 감정에 공감하는 능력이 뛰어납니다

## 연애할 때 강점
✨ 분위기 메이커로 관계에 활력을 불어넣습니다
✨ 상대방의 이야기에 귀 기울이고 공감합니다
✨ 창의적인 데이트 아이디어가 풍부합니다

## 주의할 점
💡 감정의 기복이 있을 수 있어요
💡 현실적인 부분도 함께 챙겨보세요

## 잘 맞는 유형
INTJ, INFJ 유형과 좋은 케미를 보입니다!`,
  result_image_url: '/images/results/romantic.jpg',
  share_code: 'abc123',
};

export function findTestById(id: string): Test | undefined {
  if (id === mockTestDetail.id) {
    return mockTestDetail;
  }
  return undefined;
}

export function findTestSummaryById(id: string): TestSummary | undefined {
  return mockTestSummaries.find((t) => t.id === id);
}

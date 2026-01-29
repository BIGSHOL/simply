/**
 * 연애 유형 테스트 Mock 데이터
 * Phase 1, T1-LOVE.3
 * content.md 기반
 */
import type { LoveTest, LoveTypeQuestion, LoveTypeResult } from '@/types/loveTest';

export const LOVE_TEST_QUESTIONS: LoveTypeQuestion[] = [
  {
    id: 'Q1',
    orderNum: 1,
    content: '마음에 드는 사람이 생겼어! 어떻게 할 거야?',
    choiceA: '일단 번호부터 따고 본다. 기회는 내가 만드는 거지!',
    choiceB: '자연스럽게 친해지면서 상대 반응을 살펴본다',
  },
  {
    id: 'Q2',
    orderNum: 2,
    content: '연인이 "요즘 힘들어"라고 말했을 때 나는?',
    choiceA: '"무슨 일이야? 나한테 다 얘기해" 하고 깊은 대화를 시작한다',
    choiceB: '일단 곁에 있어주고, 상대가 말할 때까지 기다린다',
  },
  {
    id: 'Q3',
    orderNum: 3,
    content: '연인과 주말 데이트! 나의 이상적인 모습은?',
    choiceA: '거의 하루 종일 붙어있는 풀코스 데이트',
    choiceB: '반나절 데이트 후 각자 시간을 갖는 게 좋아',
  },
  {
    id: 'Q4',
    orderNum: 4,
    content: '썸 타는 상대에게 호감을 표현할 때 나는?',
    choiceA: '직접적으로 "너 좋아해" 분위기를 낸다',
    choiceB: '은근히 관심을 보이며 상대의 반응을 확인한다',
  },
  {
    id: 'Q5',
    orderNum: 5,
    content: '연인과 작은 다툼이 생겼어. 나의 대처법은?',
    choiceA: '바로 대화해서 풀어야 직성이 풀린다',
    choiceB: '서로 시간을 두고 생각을 정리한 후에 얘기한다',
  },
  {
    id: 'Q6',
    orderNum: 6,
    content: '100일 기념! 어떤 데이트가 더 끌려?',
    choiceA: '분위기 좋은 레스토랑에서 선물 교환하는 이벤트',
    choiceB: '집에서 편하게 영화 보며 치킨 먹기',
  },
  {
    id: 'Q7',
    orderNum: 7,
    content: '연인이 "오늘 친구 만나서 늦을 것 같아"라고 하면?',
    choiceA: '"그래! 재밌게 놀아~" 하고 나도 내 시간을 즐긴다',
    choiceB: '괜찮다고 하면서도 은근히 아쉽고 보고 싶다',
  },
  {
    id: 'Q8',
    orderNum: 8,
    content: '연애 초반, 상대에게 더 끌리는 포인트는?',
    choiceA: '확실하게 좋아한다는 티를 내주는 사람',
    choiceB: '알쏭달쏭하게 밀당하는 매력이 있는 사람',
  },
  {
    id: 'Q9',
    orderNum: 9,
    content: '연인에게 화가 났을 때 나는?',
    choiceA: '참지 않고 바로 표현한다. 속으로 삭히는 건 못해',
    choiceB: '일단 참고, 나중에 기회 봐서 얘기한다',
  },
  {
    id: 'Q10',
    orderNum: 10,
    content: '연인의 취미가 나와 완전 다르다면?',
    choiceA: '같이 해보려고 노력한다. 연인의 관심사가 곧 내 관심사!',
    choiceB: '서로 다른 취미 존중! 각자 즐기면 돼',
  },
  {
    id: 'Q11',
    orderNum: 11,
    content: '데이트 계획을 세울 때 나는?',
    choiceA: '분위기 좋은 곳, 포토존 있는 곳 위주로 서치',
    choiceB: '맛집 가서 맛있는 거 먹는 게 최고! 분위기는 옵션',
  },
  {
    id: 'Q12',
    orderNum: 12,
    content: '연인과 1주일 연락이 뜸했어. 나의 반응은?',
    choiceA: '먼저 연락해서 무슨 일인지 확인한다',
    choiceB: '연락 오기를 기다린다. 바쁜가 보다 하고',
  },
  {
    id: 'Q13',
    orderNum: 13,
    content: '연인과의 미래에 대해 생각할 때 나는?',
    choiceA: '결혼, 동거 등 구체적인 계획을 세우고 싶다',
    choiceB: '지금 이 순간이 좋으면 됐지, 미래는 나중에',
  },
  {
    id: 'Q14',
    orderNum: 14,
    content: '연인에게 "사랑해"라고 말하는 빈도는?',
    choiceA: '하루에도 몇 번씩, 사랑은 말로 해야 해',
    choiceB: '특별한 날이나 가끔, 말보다 행동으로 보여주는 편',
  },
  {
    id: 'Q15',
    orderNum: 15,
    content: '연인과 여행을 간다면?',
    choiceA: '예쁜 카페, 야경 스팟 등 로맨틱한 장소 위주로!',
    choiceB: '맛집, 관광지 위주로 알차게 돌아다니기!',
  },
  {
    id: 'Q16',
    orderNum: 16,
    content: '연인이 나 없이 친구들과 놀러 간다고 하면?',
    choiceA: '좋지! 나도 이 시간에 내 할 일 하면 돼',
    choiceB: '괜찮긴 한데... 같이 갔으면 좋았을 것 같아',
  },
  {
    id: 'Q17',
    orderNum: 17,
    content: '고백 타이밍! 언제가 좋을까?',
    choiceA: '감정이 확실해지면 빠르게! 눈치 싸움은 피곤해',
    choiceB: '충분히 알아가고, 상대 마음도 확인된 후에',
  },
  {
    id: 'Q18',
    orderNum: 18,
    content: '연인의 부탁이라면 나는?',
    choiceA: '내가 좀 손해 봐도 들어주는 편',
    choiceB: '합리적인 범위 내에서 들어준다',
  },
  {
    id: 'Q19',
    orderNum: 19,
    content: '비 오는 날 연인과 함께라면?',
    choiceA: '창가 자리 카페에서 빗소리 들으며 감성 데이트',
    choiceB: '비 오니까 집에서 따뜻하게 라면 끓여 먹기',
  },
  {
    id: 'Q20',
    orderNum: 20,
    content: '연인과 3일째 바쁘다고 연락 없음. 나의 마인드는?',
    choiceA: '이해는 하지만 섭섭해. 바빠도 연락은 해줘야지',
    choiceB: '그럴 수 있지! 내 할 일 하면서 기다리면 돼',
  },
];

export const LOVE_TEST: LoveTest = {
  id: 'love-type',
  title: '나의 연애 유형은?',
  description: '3분만에 알아보는 나의 연애 DNA! 20가지 유형 중 당신은 어떤 러버일까요?',
  thumbnailUrl: '/images/love-type-thumbnail.png',
  questionCount: 20,
  questions: LOVE_TEST_QUESTIONS,
};

export const LOVE_TYPE_RESULTS: Record<string, LoveTypeResult> = {
  straight_shooter: {
    id: 'straight_shooter',
    typeName: '직진 러버',
    englishName: 'Straight Shooter',
    tagline: '좋으면 좋다고, 눈빛으로 이미 고백 완료',
    description:
      '마음에 드는 사람이 생기면 망설임 없이 다가가는 타입이에요. "언제 고백하지?" 고민하는 동안 이미 연락처 교환하고 카톡까지 보내버리는 스타일. 솔직한 감정 표현으로 상대를 설레게 만들지만, 가끔은 그 직진 본능이 너무 빨라서 상대가 당황할 수도 있어요. 하지만 그 거침없는 에너지가 바로 당신의 매력!',
    traits: [
      '좋아하면 티가 확 나는 솔직한 스타일',
      '연락도 데이트 신청도 내가 먼저',
      '밀당? 그게 뭔데 먹는 건가요?',
    ],
    strengths: ['연애 시작이 빠르고 기회를 놓치지 않음', '상대방이 내 마음을 의심할 필요가 없음'],
    growthPoints: ['상대의 템포에 맞춰 가끔은 여유를 갖는 연습을 하면 더 깊은 관계로 발전할 수 있어요'],
    compatibleTypes: ['설렘 수집가', '로맨틱 무드메이커'],
    hashtags: ['#직진본능', '#솔직한게매력', '#기다림은나의적'],
    scores: {
      proactivity: 85,
      expression: 75,
      independence: 55,
      commitment: 60,
      romance: 70,
    },
  },
  push_pull_master: {
    id: 'push_pull_master',
    typeName: '밀당 장인',
    englishName: 'Push & Pull Master',
    tagline: '밀고 당기기의 예술, 연애 심리전의 프로',
    description:
      '연애는 타이밍과 심리전이라는 걸 본능적으로 아는 타입! 좋아해도 티를 안 내다가 절묘한 타이밍에 관심을 보여주는 기술이 있어요. 상대방을 궁금하게 만드는 게 일상이고, "이 사람 나 좋아하는 건가?" 하는 긴장감을 즐겨요. 하지만 과한 밀당은 금물! 진심을 숨기다 타이밍을 놓치지 않도록 주의하세요.',
    traits: [
      '읽씹은 기본, 답장 텀 조절은 센스',
      '절묘한 타이밍에 던지는 의미심장한 말 한마디',
      '상대방 반응 보면서 전략 수정하는 능력 탑재',
    ],
    strengths: ['설렘과 긴장감을 오래 유지시키는 능력', '연애 초반 상대의 관심을 끌어내는 기술'],
    growthPoints: [
      '관계가 깊어지면 밀당보다 진심을 표현하는 연습을 해보세요. 진정한 친밀감은 솔직함에서 와요',
    ],
    compatibleTypes: ['직진 러버', '로맨틱 폭주기관차'],
    hashtags: ['#밀당마스터', '#연애심리전', '#궁금증유발러'],
    scores: {
      proactivity: 60,
      expression: 35,
      independence: 65,
      commitment: 40,
      romance: 55,
    },
  },
  romance_express: {
    id: 'romance_express',
    typeName: '로맨틱 폭주기관차',
    englishName: 'Romance Express',
    tagline: '사랑 앞에선 브레이크 따윈 없다',
    description:
      '사랑에 빠지면 온 세상이 핑크빛으로 보이는 타입! 100일 기념, 월별 기념일은 기본이고, 깜짝 이벤트와 로맨틱한 서프라이즈를 기획하는 게 취미예요. 연애하면 SNS에 커플 피드가 도배되고, 친구들은 "또 시작이야" 하지만 당신은 아랑곳하지 않아요. 사랑을 표현하는 데 부끄러움이 없는 당신, 그게 바로 매력이에요!',
    traits: [
      '기념일 챙기기는 기본 중의 기본',
      '연인 사진 찍어주는 건 내 담당',
      '사랑한다는 말 하루에 열 번은 기본',
    ],
    strengths: ['상대방을 항상 특별하게 느끼게 만드는 능력', '연애의 설렘과 열정을 오래 유지'],
    growthPoints: [
      '가끔은 일상적인 순간의 소중함도 느껴보세요. 평범한 날도 특별할 수 있어요',
    ],
    compatibleTypes: ['감성 몽글러', '설렘 수집가'],
    hashtags: ['#로맨스폭주', '#기념일챙겨야해', '#사랑은이벤트'],
    scores: {
      proactivity: 90,
      expression: 88,
      independence: 40,
      commitment: 75,
      romance: 95,
    },
  },
};

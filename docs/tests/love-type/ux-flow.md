# 연애 유형 테스트 - UX 플로우 설계서

> **Version**: 1.0.0
> **Last Updated**: 2025-01-30
> **Author**: Claude Code
> **타겟**: 20대 MZ세대
> **문항 수**: 20개 (A/B 이지선다)
> **예상 소요시간**: 3-4분

---

## 목차

1. [사용자 여정 맵](#1-사용자-여정-맵)
2. [화면별 와이어프레임](#2-화면별-와이어프레임)
3. [인터랙션 명세](#3-인터랙션-명세)
4. [이탈 방지 전략](#4-이탈-방지-전략)
5. [컴포넌트 목록](#5-컴포넌트-목록)
6. [애니메이션/마이크로인터랙션](#6-애니메이션마이크로인터랙션)

---

## 1. 사용자 여정 맵

### 1.1 전체 플로우 개요

```
┌─────────┐    ┌─────────────┐    ┌────────────┐    ┌─────────────┐    ┌─────────┐    ┌─────────┐
│  랜딩   │ -> │ 테스트 시작  │ -> │ 문항 1-20  │ -> │ 로딩/연출   │ -> │  결과   │ -> │  공유   │
│  페이지  │    │   (인트로)   │    │   (진행)   │    │ (서스펜스)  │    │  화면   │    │  화면   │
└─────────┘    └─────────────┘    └────────────┘    └─────────────┘    └─────────┘    └─────────┘
     │               │                  │                  │               │              │
     │               │                  │                  │               │              │
   3-5초          5-10초           3-4분            5-7초          30초-2분       10-30초
  (체류)         (몰입 유도)       (핵심 경험)       (기대감 고조)    (결과 확인)    (바이럴)
```

### 1.2 단계별 상세 설계

#### STAGE 1: 랜딩 페이지

| 항목 | 내용 |
|------|------|
| **목표** | 테스트 참여 유도 (클릭 전환) |
| **체류 시간** | 3-5초 |
| **핵심 메시지** | "3분만에 알아보는 나의 연애 DNA" |
| **훅 포인트** | - 매력적인 비주얼 (핑크/퍼플 그라데이션)<br>- 참여자 수 실시간 표시 ("23만명이 참여한")<br>- 결과 미리보기 티저 (유형 카드 일부 노출) |
| **이탈 방지** | - 3초 내 CTA 버튼 노출<br>- 스크롤 없이 핵심 정보 전달<br>- 예상 소요시간 명시 (부담 감소) |
| **전환 트리거** | "내 연애 유형 알아보기" 버튼 |

#### STAGE 2: 테스트 시작 (인트로)

| 항목 | 내용 |
|------|------|
| **목표** | 몰입감 형성 및 기대감 증폭 |
| **체류 시간** | 5-10초 |
| **핵심 메시지** | "솔직하게 답해야 진짜 결과가 나와요!" |
| **훅 포인트** | - 간단한 가이드 애니메이션<br>- 결과 유형 힌트 ("20가지 유형 중 당신은?")<br>- 본능적으로 선택하세요 (thinking fast) |
| **이탈 방지** | - 스킵 가능 옵션 제공<br>- 자동 진행 (3초 카운트다운) |
| **전환 트리거** | "시작하기" 버튼 또는 자동 진행 |

#### STAGE 3: 문항 진행 (1-20)

| 항목 | 내용 |
|------|------|
| **목표** | 20문항 완주, 정확한 응답 수집 |
| **체류 시간** | 3-4분 (문항당 9-12초) |
| **핵심 경험** | 직관적 선택, 리듬감 있는 진행 |
| **훅 포인트** | - 진행률 시각화 (프로그레스 바)<br>- 격려 메시지 (5, 10, 15번째)<br>- 재치있는 문항으로 지루함 방지 |
| **이탈 방지** | - 자동 저장 (세션 스토리지)<br>- 뒤로가기 가능 (수정 허용)<br>- 구간별 변화 주기 (아래 상세) |
| **전환 트리거** | 20번 문항 선택 완료 |

**문항 구간별 전략:**

```
문항 01-05: [워밍업 존]
├── 목표: 테스트에 몰입하게 만들기
├── 특징: 쉽고 재미있는 문항으로 시작
├── 전환: 부드러운 슬라이드
└── 격려: 5번째에 "좋아요! 술술 풀리네요"

문항 06-10: [몰입 존]
├── 목표: 리듬감 있는 진행
├── 특징: 핵심 성격 문항 배치
├── 전환: 빠른 전환 (템포 업)
└── 격려: 10번째에 "벌써 절반! 내 유형이 보이기 시작해요"

문항 11-15: [도전 존]
├── 목표: 깊은 자기 탐색
├── 특징: 생각하게 만드는 문항
├── 전환: 약간의 숨 돌림
└── 격려: 15번째에 "대단해요! 거의 다 왔어요"

문항 16-20: [스퍼트 존]
├── 목표: 완주 동기 극대화
├── 특징: 결정적 문항 + 기대감 고조
├── 전환: 점점 빨라지는 전환
└── 격려: 20번째에 "마지막 하나! 결과 보러 가볼까요?"
```

#### STAGE 4: 로딩/연출 (서스펜스)

| 항목 | 내용 |
|------|------|
| **목표** | 결과에 대한 기대감 극대화 |
| **체류 시간** | 5-7초 (최적의 서스펜스 타임) |
| **핵심 경험** | "분석 중" 연출로 가치 인식 |
| **훅 포인트** | - 5축 분석 애니메이션<br>- 타이핑 효과 텍스트<br>- 결과 힌트 살짝 노출 |
| **이탈 방지** | - 건너뛰기 불가 (경험 완성도)<br>- 짧지만 임팩트 있는 연출 |
| **전환 트리거** | 애니메이션 완료 시 자동 진행 |

**로딩 시퀀스:**

```
[0-2초] "응답을 분석하고 있어요..."
        ├── 5개 차원 아이콘 순차 점등
        └── 프로그레스 서클 애니메이션

[2-4초] "당신의 연애 패턴을 파악 중..."
        ├── 레이더 차트 스캔 효과
        └── 점수가 올라가는 카운터

[4-6초] "20가지 유형 중 매칭하는 중..."
        ├── 유형 카드 슬롯머신 효과
        └── 점점 느려지다가 멈춤

[6-7초] "찾았어요! 당신의 연애 유형은..."
        ├── 화면 페이드 아웃
        └── 결과 화면으로 전환
```

#### STAGE 5: 결과 화면

| 항목 | 내용 |
|------|------|
| **목표** | 결과 만족 + 공유 유도 |
| **체류 시간** | 30초-2분 |
| **핵심 경험** | "나를 정확히 맞췄다!" 공감 |
| **훅 포인트** | - 임팩트 있는 유형명<br>- 공감가는 상세 설명<br>- 5축 점수 시각화<br>- 궁합 유형 (호기심 유발) |
| **이탈 방지** | - 스크롤 유도 (더 많은 콘텐츠)<br>- 공유 버튼 상단 고정 |
| **전환 트리거** | 공유 버튼 또는 재도전 버튼 |

#### STAGE 6: 공유 화면

| 항목 | 내용 |
|------|------|
| **목표** | 바이럴 확산 |
| **체류 시간** | 10-30초 |
| **핵심 경험** | 쉽고 빠른 공유 |
| **훅 포인트** | - 공유용 이미지 자동 생성<br>- 카카오톡 원클릭 공유<br>- "친구 유형 알아보기" 메시지 |
| **이탈 방지** | - 공유 후에도 결과 화면 유지<br>- 재도전/다른 테스트 유도 |
| **성공 지표** | 공유율, 유입 전환율 |

---

## 2. 화면별 와이어프레임

### 2.1 랜딩 페이지

```
┌────────────────────────────────────────┐
│  ←                              [≡]    │ <- 네비게이션
├────────────────────────────────────────┤
│                                        │
│           ♡  ♡  ♡  ♡  ♡               │ <- 데코레이션
│                                        │
│    ┌──────────────────────────────┐    │
│    │                              │    │
│    │      [히어로 일러스트]         │    │ <- 메인 비주얼
│    │       커플 캐릭터 or          │    │
│    │       하트 모양 그래픽         │    │
│    │                              │    │
│    └──────────────────────────────┘    │
│                                        │
│         나의 연애 유형은?              │ <- 메인 타이틀
│                                        │
│    ┌──────────────────────────────┐    │
│    │  3분만에 알아보는 나의 연애    │    │ <- 서브 타이틀
│    │  DNA! 20가지 유형 중          │    │
│    │  당신은 어떤 러버일까요?       │    │
│    └──────────────────────────────┘    │
│                                        │
│         23만명이 참여했어요 🔥         │ <- 소셜 프루프
│                                        │
│    ╔══════════════════════════════╗    │
│    ║                              ║    │
│    ║    내 연애 유형 알아보기       ║    │ <- CTA 버튼
│    ║         (약 3분 소요)          ║    │
│    ║                              ║    │
│    ╚══════════════════════════════╝    │
│                                        │
│    ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐    │
│    │직진 │ │밀당 │ │로맨틱│ │???  │    │ <- 결과 티저
│    │러버 │ │장인 │ │폭주 │ │     │    │
│    └─────┘ └─────┘ └─────┘ └─────┘    │
│       ↑ 20가지 유형 미리보기           │
│                                        │
└────────────────────────────────────────┘
```

### 2.2 문항 화면

```
┌────────────────────────────────────────┐
│  ←  [이전]                    [Q.08]   │ <- 문항 번호
├────────────────────────────────────────┤
│                                        │
│  ■■■■■■■■□□□□□□□□□□□□  8/20           │ <- 프로그레스 바
│  ────────────────────────────────────  │
│                                        │
│  ┌──────────────────────────────────┐  │
│  │                                  │  │
│  │        [상황 일러스트]            │  │ <- 문항 이미지
│  │         (선택사항)                │  │
│  │                                  │  │
│  └──────────────────────────────────┘  │
│                                        │
│  ┌──────────────────────────────────┐  │
│  │                                  │  │
│  │   연인과 데이트 장소를 정할 때,    │  │ <- 문항 텍스트
│  │   나는 주로...                    │  │
│  │                                  │  │
│  └──────────────────────────────────┘  │
│                                        │
│  ┌──────────────────────────────────┐  │
│  │                                  │  │
│  │   A. 내가 먼저 장소를 제안하고    │  │ <- 선택지 A
│  │      계획을 짜는 편이야           │  │
│  │                                  │  │
│  │                           [ ]    │  │
│  └──────────────────────────────────┘  │
│                                        │
│  ┌──────────────────────────────────────┐
│  │                                  │  │
│  │   B. 상대방 의견을 먼저 물어보고   │  │ <- 선택지 B
│  │      맞춰주는 편이야              │  │
│  │                                  │  │
│  │                           [ ]    │  │
│  └──────────────────────────────────┘  │
│                                        │
│  ─────────────────────────────────────  │
│          벌써 절반! 잘하고 있어요       │ <- 격려 메시지
│                  (조건부 노출)          │
│                                        │
└────────────────────────────────────────┘
```

### 2.3 선택 완료 상태

```
┌────────────────────────────────────────┐
│  ←  [이전]                    [Q.08]   │
├────────────────────────────────────────┤
│                                        │
│  ■■■■■■■■□□□□□□□□□□□□  8/20           │
│  ────────────────────────────────────  │
│                                        │
│   연인과 데이트 장소를 정할 때,         │
│   나는 주로...                         │
│                                        │
│  ╔══════════════════════════════════╗  │
│  ║                                  ║  │
│  ║   A. 내가 먼저 장소를 제안하고    ║  │ <- 선택됨
│  ║      계획을 짜는 편이야           ║  │    (강조 스타일)
│  ║                                  ║  │
│  ║                           [✓]    ║  │
│  ╚══════════════════════════════════╝  │
│                                        │
│  ┌──────────────────────────────────┐  │
│  │                                  │  │ <- 미선택
│  │   B. 상대방 의견을 먼저 물어보고   │  │    (흐린 스타일)
│  │      맞춰주는 편이야              │  │
│  │                                  │  │
│  │                           [ ]    │  │
│  └──────────────────────────────────┘  │
│                                        │
│    ← 스와이프해서 다음 문항으로 →       │ <- 안내 텍스트
│                                        │
│           ◀ ● ● ● ● ● ● ● ▶           │ <- 페이지 인디케이터
│                                        │
└────────────────────────────────────────┘
```

### 2.4 로딩/연출 화면

```
┌────────────────────────────────────────┐
│                                        │
│                                        │
│                                        │
│         ┌──────────────────┐           │
│         │                  │           │
│         │    [분석 중...]    │           │ <- 메인 애니메이션
│         │                  │           │
│         │    ◠ ◠ ◠ ◠ ◠     │           │    (펄스 효과)
│         │   (  ●    )      │           │
│         │    ◡ ◡ ◡ ◡ ◡     │           │
│         │                  │           │
│         └──────────────────┘           │
│                                        │
│                                        │
│      ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐│
│      │적극│ │감정│ │독립│ │헌신│ │로맨││ <- 5축 아이콘
│      │ ✓ │ │ ✓ │ │ ○ │ │ ○ │ │ ○ ││    (순차 점등)
│      │성  │ │표현│ │성  │ │도  │ │스  ││
│      └────┘ └────┘ └────┘ └────┘ └────┘│
│                                        │
│      ════════════════════════════      │ <- 프로그레스 바
│      ████████████░░░░░░░░░░░░░░░░      │
│                                        │
│                                        │
│       "당신의 연애 패턴을                │ <- 타이핑 텍스트
│        분석하고 있어요..."              │
│                                        │
│                                        │
│                                        │
└────────────────────────────────────────┘
```

### 2.5 결과 화면 (메인)

```
┌────────────────────────────────────────┐
│  [공유하기]                    [X]     │ <- 상단 고정 버튼
├────────────────────────────────────────┤
│                                        │
│  ╔══════════════════════════════════╗  │
│  ║                                  ║  │
│  ║        ★ 당신의 연애 유형 ★       ║  │ <- 타이틀
│  ║                                  ║  │
│  ║   ┌────────────────────────┐     ║  │
│  ║   │                        │     ║  │
│  ║   │    [유형 캐릭터 일러스트]  │     ║  │ <- 메인 비주얼
│  ║   │                        │     ║  │
│  ║   └────────────────────────┘     ║  │
│  ║                                  ║  │
│  ║         직진 러버               ║  │ <- 유형명
│  ║      Straight Shooter           ║  │
│  ║                                  ║  │
│  ║  "좋으면 좋다고,                 ║  │ <- 한줄 설명
│  ║   눈빛으로 이미 고백 완료"        ║  │
│  ║                                  ║  │
│  ╚══════════════════════════════════╝  │
│                                        │
│  ┌──────────────────────────────────┐  │
│  │         [ 5축 레이더 차트 ]        │  │
│  │                                  │  │
│  │            적극성                 │  │
│  │              85                  │  │ <- 레이더 차트
│  │         ╱    ╲                   │  │
│  │   로맨스 ─     ─ 감정표현          │  │
│  │     70    ╲ ╱    75              │  │
│  │            X                     │  │
│  │         ╱   ╲                    │  │
│  │   헌신도 ─     ─ 독립성           │  │
│  │     60          55               │  │
│  │                                  │  │
│  └──────────────────────────────────┘  │
│                                        │
│                 ↓ 스크롤               │
└────────────────────────────────────────┘
```

### 2.6 결과 화면 (스크롤)

```
┌────────────────────────────────────────┐
│  [공유하기]                    [X]     │
├────────────────────────────────────────┤
│                                        │
│  ━━━━ 상세 설명 ━━━━━━━━━━━━━━━━━━━━   │
│                                        │
│  마음에 드는 사람이 생기면 망설임 없이   │
│  다가가는 타입이에요. "언제 고백하지?"   │ <- 상세 설명
│  고민하는 동안 이미 연락처 교환하고      │
│  카톡까지 보내버리는 스타일...          │
│                                        │
│  ━━━━ 연애 스타일 특징 ━━━━━━━━━━━━━   │
│                                        │
│  ┌────────────────────────────────┐    │
│  │ ✓ 좋아하면 티가 확 나는 솔직파   │    │ <- 특징 리스트
│  │ ✓ 연락도 데이트 신청도 내가 먼저 │    │
│  │ ✓ 밀당? 그게 뭔데 먹는 건가요?  │    │
│  └────────────────────────────────┘    │
│                                        │
│  ━━━━ 강점 & 성장 포인트 ━━━━━━━━━━━   │
│                                        │
│  ┌───────────────┐ ┌───────────────┐   │
│  │    강점        │ │  성장 포인트   │   │
│  │               │ │               │   │
│  │ 기회를 놓치지  │ │ 상대 템포에   │   │
│  │ 않는 추진력   │ │ 맞추는 여유   │   │
│  └───────────────┘ └───────────────┘   │
│                                        │
│  ━━━━ 베스트 궁합 ━━━━━━━━━━━━━━━━━━   │
│                                        │
│  ┌───────────────┐ ┌───────────────┐   │
│  │   설렘 수집가  │ │ 로맨틱 무드   │   │ <- 궁합 유형
│  │               │ │   메이커      │   │
│  │    💕 95%     │ │    💕 88%     │   │
│  │   [알아보기]   │ │   [알아보기]   │   │
│  └───────────────┘ └───────────────┘   │
│                                        │
│  ━━━━ #해시태그 ━━━━━━━━━━━━━━━━━━━━   │
│                                        │
│  #직진본능 #솔직한게매력 #기다림은나의적  │
│                                        │
└────────────────────────────────────────┘
```

### 2.7 공유 화면 (바텀시트)

```
┌────────────────────────────────────────┐
│                                        │
│           (결과 화면 배경)              │
│              (흐림 처리)               │
│                                        │
├────────────────────────────────────────┤
│  ════════════ 공유하기 ════════════    │ <- 바텀시트 헤더
│                 ─                      │    (드래그 핸들)
│                                        │
│  ┌──────────────────────────────────┐  │
│  │                                  │  │
│  │    [공유용 카드 이미지 미리보기]    │  │ <- 공유 이미지
│  │                                  │  │
│  │       나의 연애 유형은            │  │
│  │        직진 러버                 │  │
│  │                                  │  │
│  │      simly.kr/love-type          │  │
│  │                                  │  │
│  └──────────────────────────────────┘  │
│                                        │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐  │
│  │         │ │         │ │         │  │
│  │ 카카오톡 │ │ 링크복사 │ │  저장   │  │ <- 공유 버튼
│  │   💬    │ │   🔗    │ │   💾   │  │
│  │         │ │         │ │         │  │
│  └─────────┘ └─────────┘ └─────────┘  │
│                                        │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐  │
│  │         │ │         │ │         │  │
│  │ 인스타   │ │ 트위터   │ │  더보기 │  │ <- 추가 공유
│  │   📸    │ │   🐦    │ │   ...   │  │
│  │         │ │         │ │         │  │
│  └─────────┘ └─────────┘ └─────────┘  │
│                                        │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│                                        │
│  ╔══════════════════════════════════╗  │
│  ║       친구들도 테스트하게 하기     ║  │ <- 바이럴 CTA
│  ╚══════════════════════════════════╝  │
│                                        │
│  ┌──────────────────────────────────┐  │
│  │         다시 테스트하기           │  │ <- 재도전
│  └──────────────────────────────────┘  │
│                                        │
└────────────────────────────────────────┘
```

---

## 3. 인터랙션 명세

### 3.1 선택지 인터랙션

| 액션 | 인터랙션 | 피드백 | 타이밍 |
|------|---------|--------|--------|
| **선택지 탭** | 터치/클릭 | 바운스 효과 + 배경색 변경 | 즉시 (0ms) |
| **선택 완료** | 선택지 활성화 | 체크마크 나타남 + 보더 강조 | 150ms |
| **미선택 처리** | 반대 선택지 | 투명도 50% + 흐림 | 200ms |
| **자동 진행** | 다음 문항 이동 | 슬라이드 전환 | 500ms 딜레이 후 |
| **호버 (데스크톱)** | 마우스 오버 | 그림자 확대 + 살짝 위로 | 100ms |

### 3.2 화면 전환 인터랙션

| 액션 | 인터랙션 | 피드백 | 타이밍 |
|------|---------|--------|--------|
| **다음 문항** | 좌 슬라이드 | 현재 화면 좌로 사라짐 + 새 화면 우에서 등장 | 300ms |
| **이전 문항** | 우 슬라이드 | 현재 화면 우로 사라짐 + 이전 화면 좌에서 등장 | 300ms |
| **스와이프** | 제스처 감지 | 손가락 따라 화면 이동 + 인디케이터 변화 | 실시간 |
| **결과 이동** | 페이드 + 스케일 | 화면 중앙에서 확대되며 페이드 인 | 500ms |
| **바텀시트 열기** | 아래에서 위로 | 배경 흐림 + 시트 슬라이드 업 | 300ms |

### 3.3 결과 공개 인터랙션

| 액션 | 인터랙션 | 피드백 | 타이밍 |
|------|---------|--------|--------|
| **유형명 등장** | 타이핑 효과 | 글자 하나씩 타이핑 | 1000ms |
| **캐릭터 등장** | 바운스 인 | 위에서 떨어지며 바운스 | 600ms |
| **레이더 차트** | 드로잉 효과 | 중심에서 바깥으로 확장 | 800ms |
| **점수 카운터** | 카운트 업 | 0에서 실제 점수까지 증가 | 1200ms |
| **설명 텍스트** | 페이드 인 | 순차적 페이드 인 | 각 200ms |
| **공유 버튼** | 펄스 효과 | 주기적 확대/축소 애니메이션 | 반복 |

### 3.4 격려 메시지 타이밍

| 문항 번호 | 메시지 | 트리거 |
|-----------|--------|--------|
| 5번 완료 | "좋아요! 술술 풀리네요" | 5번 선택 직후 |
| 10번 완료 | "벌써 절반! 내 유형이 보이기 시작해요" | 10번 선택 직후 |
| 15번 완료 | "대단해요! 거의 다 왔어요" | 15번 선택 직후 |
| 20번 완료 | "마지막! 결과 보러 가볼까요?" | 20번 선택 직후 |

---

## 4. 이탈 방지 전략

### 4.1 20문항 지루함 방지 전략

#### 1) 시각적 다양성

```typescript
// 문항 구간별 테마 색상 변경
const SECTION_THEMES = {
  warmup: { bg: '#FFF5F5', accent: '#FF6B6B' },   // 1-5: 따뜻한 핑크
  immerse: { bg: '#F5F5FF', accent: '#7B68EE' },  // 6-10: 퍼플
  challenge: { bg: '#F5FFF5', accent: '#50C878' }, // 11-15: 민트
  sprint: { bg: '#FFF5E5', accent: '#FFA500' },    // 16-20: 오렌지
};
```

#### 2) 템포 조절

```
문항 1-5:  전환 속도 0.4s  (여유있게)
문항 6-10: 전환 속도 0.35s (약간 빠르게)
문항 11-15: 전환 속도 0.3s  (리듬감 있게)
문항 16-20: 전환 속도 0.25s (스퍼트!)
```

#### 3) 프로그레스 게이미피케이션

```
┌─────────────────────────────────────────┐
│  ■■■■■ ★ ■■■■■ ★ ■■■■■ ★ ■■■■■ ★     │
│  1   5   6   10  11  15  16  20        │
│      ↑       ↑       ↑       ↑          │
│   마일스톤  마일스톤  마일스톤  완료!      │
└─────────────────────────────────────────┘
```

#### 4) 재미 요소

- 문항별 미니 일러스트/아이콘
- 선택 시 귀여운 사운드 효과 (옵션)
- 가끔 등장하는 이스터에그 문항

### 4.2 중간 저장 로직

```typescript
// 자동 저장 전략
const AUTO_SAVE_STRATEGY = {
  // 저장 방식
  storage: 'sessionStorage',  // 브라우저 닫으면 삭제
  key: 'love-type-progress',

  // 저장 데이터 구조
  data: {
    currentQuestion: number,   // 현재 문항 번호
    answers: Answer[],         // 지금까지의 응답
    startedAt: timestamp,      // 시작 시간
    lastUpdated: timestamp,    // 마지막 업데이트
  },

  // 저장 타이밍
  triggers: [
    'on_answer',      // 매 답변 시
    'on_visibility_change',  // 탭 전환 시
    'on_beforeunload',       // 페이지 이탈 시
  ],

  // 복원 로직
  restoration: {
    showModal: true,  // "이어서 하시겠어요?" 모달
    expiry: 30 * 60 * 1000,  // 30분 후 만료
  }
};
```

#### 이어하기 모달

```
┌────────────────────────────────────────┐
│                                        │
│     ┌──────────────────────────┐       │
│     │                          │       │
│     │    이전에 하다 말았네요!   │       │
│     │                          │       │
│     │    📝 12/20 완료          │       │
│     │                          │       │
│     │  ┌───────┐  ┌───────┐    │       │
│     │  │이어하기│  │처음부터│    │       │
│     │  └───────┘  └───────┘    │       │
│     │                          │       │
│     └──────────────────────────┘       │
│                                        │
└────────────────────────────────────────┘
```

### 4.3 격려 메시지 시스템

```typescript
interface EncouragementConfig {
  // 기본 격려 메시지
  milestones: {
    5: "좋아요! 술술 풀리네요 ✨",
    10: "절반 왔어요! 내 유형이 서서히 드러나고 있어요",
    15: "대단해요! 이제 조금만 더!",
    20: "끝! 드디어 결과를 볼 시간이에요 🎉"
  },

  // 빠른 응답자 칭찬
  fastResponder: {
    condition: 'avgTime < 5s',
    message: "와, 직감이 빠르시네요! 🚀"
  },

  // 신중한 응답자 격려
  thoughtfulResponder: {
    condition: 'avgTime > 15s',
    message: "신중하게 고민하시는군요, 좋아요! 💭"
  },

  // 표시 방식
  display: {
    position: 'bottom',
    duration: 2000,
    animation: 'slideUp'
  }
}
```

### 4.4 이탈 시도 대응

```typescript
// 뒤로가기/새로고침 시도 감지
const EXIT_INTENT_HANDLER = {
  // beforeunload 이벤트
  onBeforeUnload: {
    condition: 'progress > 0 && progress < 100',
    message: "지금 나가면 진행 상황이 사라져요! 정말 나가시겠어요?",
  },

  // 뒤로가기 버튼
  onBackButton: {
    condition: 'progress > 0',
    action: 'showConfirmModal',
    modal: {
      title: "잠깐! 🛑",
      message: "지금까지의 답변이 저장되어 있어요.\n돌아가면 처음부터 해야 해요.",
      buttons: ["계속하기", "그래도 나가기"]
    }
  }
};
```

---

## 5. 컴포넌트 목록

### 5.1 페이지 컴포넌트

```typescript
// 페이지 레벨 컴포넌트
├── pages/
│   ├── LoveTypeLandingPage.tsx     // 랜딩 페이지
│   ├── LoveTypeTestPage.tsx        // 테스트 진행 페이지
│   ├── LoveTypeLoadingPage.tsx     // 로딩/연출 페이지
│   └── LoveTypeResultPage.tsx      // 결과 페이지
```

### 5.2 공통 컴포넌트

#### ProgressBar

```typescript
interface ProgressBarProps {
  current: number;          // 현재 문항 (1-20)
  total: number;            // 전체 문항 수 (20)
  milestones?: number[];    // 마일스톤 위치 [5, 10, 15, 20]
  showLabel?: boolean;      // "8/20" 라벨 표시
  animated?: boolean;       // 애니메이션 효과
  theme?: 'default' | 'gradient';  // 테마
}
```

#### QuestionCard

```typescript
interface QuestionCardProps {
  questionNumber: number;           // 문항 번호
  questionText: string;             // 문항 텍스트
  illustration?: string;            // 일러스트 URL (선택)
  optionA: OptionProps;             // A 선택지
  optionB: OptionProps;             // B 선택지
  selectedOption?: 'A' | 'B' | null; // 현재 선택
  onSelect: (option: 'A' | 'B') => void;
  disabled?: boolean;               // 비활성화 상태
}

interface OptionProps {
  label: string;    // "A" or "B"
  text: string;     // 선택지 텍스트
}
```

#### OptionButton

```typescript
interface OptionButtonProps {
  label: 'A' | 'B';
  text: string;
  isSelected: boolean;
  isDisabled: boolean;
  onSelect: () => void;
  animationState?: 'idle' | 'hover' | 'selected' | 'deselected';
}
```

#### EncouragementToast

```typescript
interface EncouragementToastProps {
  message: string;
  isVisible: boolean;
  duration?: number;        // 표시 시간 (ms)
  position?: 'top' | 'bottom';
  onClose?: () => void;
}
```

### 5.3 결과 컴포넌트

#### ResultCard

```typescript
interface ResultCardProps {
  resultType: LoveType;     // 유형 데이터
  scores: DimensionScores;  // 5축 점수
  showAnimation?: boolean;  // 등장 애니메이션
  variant?: 'full' | 'compact' | 'share';  // 표시 방식
}

interface LoveType {
  id: string;
  name: string;           // "직진 러버"
  englishName: string;    // "Straight Shooter"
  tagline: string;        // 한줄 설명
  description: string;    // 상세 설명
  traits: string[];       // 특징 리스트
  strengths: string[];    // 강점
  growthPoints: string[]; // 성장 포인트
  compatibleTypes: string[]; // 궁합 유형
  hashtags: string[];     // SNS 해시태그
  characterImage: string; // 캐릭터 이미지 URL
}
```

#### RadarChart

```typescript
interface RadarChartProps {
  scores: DimensionScores;
  size?: number;          // 차트 크기 (px)
  showLabels?: boolean;   // 축 라벨 표시
  showValues?: boolean;   // 점수 값 표시
  animated?: boolean;     // 그리기 애니메이션
  colors?: {
    fill: string;
    stroke: string;
    label: string;
  };
}

interface DimensionScores {
  proactivity: number;   // 적극성 0-100
  expression: number;    // 감정표현 0-100
  independence: number;  // 독립성 0-100
  commitment: number;    // 헌신도 0-100
  romance: number;       // 로맨스 0-100
}
```

#### CompatibilityCard

```typescript
interface CompatibilityCardProps {
  typeName: string;       // 궁합 유형명
  matchPercentage: number; // 궁합도 (%)
  thumbnail?: string;     // 미리보기 이미지
  onClick?: () => void;   // 클릭 핸들러
}
```

### 5.4 공유 컴포넌트

#### ShareBottomSheet

```typescript
interface ShareBottomSheetProps {
  isOpen: boolean;
  onClose: () => void;
  shareData: ShareData;
  onShare: (platform: SharePlatform) => void;
}

interface ShareData {
  title: string;
  description: string;
  imageUrl: string;
  url: string;
}

type SharePlatform =
  | 'kakao'
  | 'copy'
  | 'download'
  | 'instagram'
  | 'twitter'
  | 'more';
```

#### ShareButton

```typescript
interface ShareButtonProps {
  platform: SharePlatform;
  onClick: () => void;
  disabled?: boolean;
  showLabel?: boolean;
}
```

#### ShareImageCard

```typescript
interface ShareImageCardProps {
  resultType: LoveType;
  scores: DimensionScores;
  ref?: RefObject<HTMLDivElement>;  // 이미지 캡처용
}
```

### 5.5 로딩 컴포넌트

#### AnalyzingLoader

```typescript
interface AnalyzingLoaderProps {
  currentPhase: LoadingPhase;
  progress: number;       // 0-100
  messages: string[];     // 단계별 메시지
}

type LoadingPhase =
  | 'analyzing'
  | 'calculating'
  | 'matching'
  | 'complete';
```

#### DimensionIndicator

```typescript
interface DimensionIndicatorProps {
  dimensions: Array<{
    name: string;
    icon: string;
    isActive: boolean;
  }>;
  animationDelay?: number;
}
```

### 5.6 유틸리티 컴포넌트

#### SwipeContainer

```typescript
interface SwipeContainerProps {
  children: ReactNode;
  onSwipeLeft: () => void;
  onSwipeRight: () => void;
  threshold?: number;     // 스와이프 인식 거리
  disabled?: boolean;
}
```

#### ConfirmModal

```typescript
interface ConfirmModalProps {
  isOpen: boolean;
  title: string;
  message: string;
  confirmText?: string;
  cancelText?: string;
  onConfirm: () => void;
  onCancel: () => void;
  variant?: 'default' | 'danger';
}
```

#### ContinueModal

```typescript
interface ContinueModalProps {
  isOpen: boolean;
  savedProgress: number;  // 저장된 진행률 (1-20)
  onContinue: () => void;
  onRestart: () => void;
}
```

---

## 6. 애니메이션/마이크로인터랙션

### 6.1 선택 시 애니메이션

#### 선택지 탭 피드백

```css
/* 선택지 터치 시 바운스 효과 */
@keyframes optionBounce {
  0% { transform: scale(1); }
  50% { transform: scale(0.95); }
  100% { transform: scale(1); }
}

.option-button:active {
  animation: optionBounce 150ms ease-out;
}
```

#### 선택 완료 효과

```css
/* 선택된 옵션 강조 */
@keyframes selectPulse {
  0% {
    box-shadow: 0 0 0 0 rgba(255, 107, 107, 0.4);
    border-color: transparent;
  }
  50% {
    box-shadow: 0 0 0 10px rgba(255, 107, 107, 0);
    border-color: #FF6B6B;
  }
  100% {
    box-shadow: 0 0 0 0 rgba(255, 107, 107, 0);
    border-color: #FF6B6B;
  }
}

.option-button.selected {
  animation: selectPulse 400ms ease-out;
  background: linear-gradient(135deg, #FFF5F5 0%, #FFE5E5 100%);
  border: 2px solid #FF6B6B;
}
```

#### 체크마크 등장

```css
/* 체크마크 애니메이션 */
@keyframes checkmarkDraw {
  0% {
    stroke-dashoffset: 50;
    opacity: 0;
  }
  50% {
    opacity: 1;
  }
  100% {
    stroke-dashoffset: 0;
    opacity: 1;
  }
}

.checkmark-icon {
  stroke-dasharray: 50;
  animation: checkmarkDraw 300ms ease-out forwards;
}
```

### 6.2 화면 전환 효과

#### 문항 전환 (슬라이드)

```typescript
// Framer Motion 설정
const slideVariants = {
  enter: (direction: number) => ({
    x: direction > 0 ? '100%' : '-100%',
    opacity: 0,
  }),
  center: {
    x: 0,
    opacity: 1,
  },
  exit: (direction: number) => ({
    x: direction > 0 ? '-100%' : '100%',
    opacity: 0,
  }),
};

const slideTransition = {
  type: 'spring',
  stiffness: 300,
  damping: 30,
};
```

#### 결과 화면 전환 (페이드 + 스케일)

```typescript
const resultEntranceVariants = {
  hidden: {
    opacity: 0,
    scale: 0.8,
  },
  visible: {
    opacity: 1,
    scale: 1,
    transition: {
      duration: 0.5,
      ease: [0.25, 0.46, 0.45, 0.94],
    },
  },
};
```

#### 바텀시트 전환

```typescript
const bottomSheetVariants = {
  hidden: {
    y: '100%',
    opacity: 0,
  },
  visible: {
    y: 0,
    opacity: 1,
    transition: {
      type: 'spring',
      damping: 25,
      stiffness: 300,
    },
  },
  exit: {
    y: '100%',
    opacity: 0,
    transition: {
      duration: 0.2,
    },
  },
};
```

### 6.3 결과 공개 연출

#### 시퀀스 타임라인

```typescript
const RESULT_REVEAL_SEQUENCE = {
  // 총 소요 시간: 약 3.5초
  timeline: [
    {
      element: 'background',
      animation: 'fadeIn',
      start: 0,
      duration: 300,
    },
    {
      element: 'character',
      animation: 'bounceIn',
      start: 200,
      duration: 600,
    },
    {
      element: 'typeName',
      animation: 'typewriter',
      start: 600,
      duration: 800,
    },
    {
      element: 'tagline',
      animation: 'fadeSlideUp',
      start: 1200,
      duration: 400,
    },
    {
      element: 'radarChart',
      animation: 'drawExpand',
      start: 1400,
      duration: 800,
    },
    {
      element: 'scores',
      animation: 'countUp',
      start: 1600,
      duration: 1200,
    },
    {
      element: 'shareButton',
      animation: 'pulseFadeIn',
      start: 2500,
      duration: 500,
    },
  ],
};
```

#### 유형명 타이핑 효과

```typescript
// 타이핑 애니메이션 컴포넌트
interface TypewriterProps {
  text: string;
  speed?: number;  // ms per character
  onComplete?: () => void;
}

const TypewriterText: React.FC<TypewriterProps> = ({
  text,
  speed = 80,
  onComplete,
}) => {
  const [displayedText, setDisplayedText] = useState('');

  useEffect(() => {
    let i = 0;
    const interval = setInterval(() => {
      if (i < text.length) {
        setDisplayedText(text.slice(0, i + 1));
        i++;
      } else {
        clearInterval(interval);
        onComplete?.();
      }
    }, speed);

    return () => clearInterval(interval);
  }, [text, speed, onComplete]);

  return <span>{displayedText}<span className="cursor">|</span></span>;
};
```

#### 레이더 차트 드로잉

```css
/* SVG 레이더 차트 그리기 애니메이션 */
@keyframes radarExpand {
  0% {
    transform: scale(0);
    opacity: 0;
  }
  60% {
    transform: scale(1.1);
    opacity: 0.8;
  }
  100% {
    transform: scale(1);
    opacity: 1;
  }
}

.radar-area {
  transform-origin: center;
  animation: radarExpand 800ms ease-out forwards;
}
```

#### 점수 카운트업

```typescript
// 점수 카운트업 훅
const useCountUp = (
  end: number,
  duration: number = 1200,
  delay: number = 0
) => {
  const [count, setCount] = useState(0);

  useEffect(() => {
    const timeout = setTimeout(() => {
      const startTime = Date.now();
      const animate = () => {
        const elapsed = Date.now() - startTime;
        const progress = Math.min(elapsed / duration, 1);

        // Ease out cubic
        const eased = 1 - Math.pow(1 - progress, 3);
        setCount(Math.floor(eased * end));

        if (progress < 1) {
          requestAnimationFrame(animate);
        }
      };
      requestAnimationFrame(animate);
    }, delay);

    return () => clearTimeout(timeout);
  }, [end, duration, delay]);

  return count;
};
```

### 6.4 마이크로인터랙션 상세

#### 프로그레스 바 업데이트

```css
/* 프로그레스 바 채우기 애니메이션 */
.progress-fill {
  transition: width 400ms cubic-bezier(0.4, 0, 0.2, 1);
}

/* 마일스톤 도달 시 파티클 효과 */
@keyframes milestoneSparkle {
  0% { transform: scale(0) rotate(0deg); opacity: 1; }
  50% { transform: scale(1.2) rotate(180deg); opacity: 0.8; }
  100% { transform: scale(0) rotate(360deg); opacity: 0; }
}

.milestone-particle {
  animation: milestoneSparkle 600ms ease-out forwards;
}
```

#### 격려 토스트 등장

```css
/* 토스트 슬라이드 업 */
@keyframes toastSlideUp {
  0% {
    transform: translateY(100%) translateX(-50%);
    opacity: 0;
  }
  100% {
    transform: translateY(0) translateX(-50%);
    opacity: 1;
  }
}

.encouragement-toast {
  position: fixed;
  bottom: 100px;
  left: 50%;
  animation: toastSlideUp 300ms ease-out forwards;
}

/* 토스트 퇴장 */
@keyframes toastSlideDown {
  0% {
    transform: translateY(0) translateX(-50%);
    opacity: 1;
  }
  100% {
    transform: translateY(100%) translateX(-50%);
    opacity: 0;
  }
}

.encouragement-toast.exiting {
  animation: toastSlideDown 200ms ease-in forwards;
}
```

#### 공유 버튼 펄스

```css
/* 공유 유도 펄스 효과 */
@keyframes sharePulse {
  0%, 100% {
    transform: scale(1);
    box-shadow: 0 4px 12px rgba(255, 107, 107, 0.3);
  }
  50% {
    transform: scale(1.05);
    box-shadow: 0 6px 20px rgba(255, 107, 107, 0.5);
  }
}

.share-button-cta {
  animation: sharePulse 2s ease-in-out infinite;
}

/* 호버 시 펄스 정지 */
.share-button-cta:hover {
  animation-play-state: paused;
  transform: scale(1.05);
}
```

#### 로딩 차원 아이콘 점등

```css
/* 5축 아이콘 순차 점등 */
@keyframes iconActivate {
  0% {
    opacity: 0.3;
    transform: scale(0.9);
    filter: grayscale(100%);
  }
  50% {
    transform: scale(1.1);
  }
  100% {
    opacity: 1;
    transform: scale(1);
    filter: grayscale(0%);
  }
}

.dimension-icon {
  opacity: 0.3;
  filter: grayscale(100%);
}

.dimension-icon.active {
  animation: iconActivate 400ms ease-out forwards;
}

/* 순차 딜레이 */
.dimension-icon:nth-child(1).active { animation-delay: 0ms; }
.dimension-icon:nth-child(2).active { animation-delay: 300ms; }
.dimension-icon:nth-child(3).active { animation-delay: 600ms; }
.dimension-icon:nth-child(4).active { animation-delay: 900ms; }
.dimension-icon:nth-child(5).active { animation-delay: 1200ms; }
```

---

## 7. 기술 구현 참고사항

### 7.1 성능 최적화

```typescript
// 이미지 사전 로딩
const PRELOAD_IMAGES = [
  '/images/result-characters/*.png',  // 결과 캐릭터
  '/images/loading-animation.json',   // Lottie 애니메이션
];

// 결과 컴포넌트 코드 스플리팅
const ResultPage = lazy(() => import('./pages/LoveTypeResultPage'));

// 애니메이션 라이브러리 선택
// - Framer Motion: 페이지 전환, 복잡한 시퀀스
// - CSS Animation: 단순 반복, 마이크로인터랙션
// - Lottie: 로딩 애니메이션, 복잡한 일러스트
```

### 7.2 접근성 고려사항

```typescript
// 키보드 네비게이션 지원
const handleKeyDown = (e: KeyboardEvent) => {
  if (e.key === '1' || e.key === 'a') selectOption('A');
  if (e.key === '2' || e.key === 'b') selectOption('B');
  if (e.key === 'ArrowRight') goToNext();
  if (e.key === 'ArrowLeft') goToPrevious();
};

// 스크린리더 지원
<div
  role="progressbar"
  aria-valuenow={currentQuestion}
  aria-valuemin={1}
  aria-valuemax={20}
  aria-label={`20문항 중 ${currentQuestion}번째`}
/>

// 모션 감소 설정 존중
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

### 7.3 에러 처리

```typescript
// 네트워크 에러 시 오프라인 모드
const OFFLINE_FALLBACK = {
  // 기본 결과 계산은 클라이언트에서 수행
  calculateLocally: true,
  // AI 생성 결과는 캐싱된 템플릿 사용
  useTemplateResult: true,
  // 공유 기능 일부 제한
  limitedSharing: ['copy', 'download'],
};
```

---

## 8. 참고 문서

- [content.md](./content.md) - 테스트 콘텐츠 설계서
- [analysis.md](./analysis.md) - 결과 분석 로직 설계서

---

> **Document History**
> - v1.0.0 (2025-01-30): 초안 작성

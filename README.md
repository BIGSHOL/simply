# Simly - AI 심리테스트 플랫폼

AI가 분석해주는 개인화된 심리테스트 결과를 제공하는 웹 플랫폼입니다.

## 기술 스택

### Backend
- FastAPI + Python 3.11+
- SQLAlchemy 2.0
- SQLite (개발) / PostgreSQL (프로덕션)
- OpenAI API (gpt-4o-mini)

### Frontend
- Next.js 14 (App Router)
- TypeScript
- TailwindCSS
- Zustand (상태관리)

## 빠른 시작 (로컬 개발)

### 1. 백엔드 설정

```bash
cd backend

# 가상환경 (선택)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 의존성 설치
pip install -r requirements.txt

# 환경변수 설정 (OpenAI API 키 필요)
cp .env.example .env
# .env 파일에서 OPENAI_API_KEY 설정

# 시드 데이터 생성
python -m scripts.seed_data

# 서버 실행
uvicorn app.main:app --reload --port 8000
```

### 2. 프론트엔드 설정

```bash
cd frontend

# 의존성 설치
npm install

# 환경변수 설정
cp .env.example .env.local

# 개발 서버 실행
npm run dev
```

### 3. 접속

- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

## API 엔드포인트

| Method | Endpoint | 설명 |
|--------|----------|------|
| GET | /api/v1/tests | 테스트 목록 조회 |
| GET | /api/v1/tests/{id} | 테스트 상세 조회 (질문/선택지 포함) |
| POST | /api/v1/tests/{id}/submit | 테스트 제출 & AI 결과 생성 |
| GET | /api/v1/results/{id} | 결과 조회 (ID 또는 공유코드) |

## 테스트 실행

```bash
# 백엔드 (26 tests)
cd backend && pytest -v

# 프론트엔드 (36 tests)
cd frontend && npm test
```

## 주요 기능

- **테스트 목록**: 카테고리별 심리테스트 조회
- **테스트 진행**: 질문에 순차적으로 답변
- **AI 결과 생성**: OpenAI API로 맞춤 결과 분석
- **결과 캐싱**: 동일 답변은 DB 캐시 사용 (AI 호출 절약)
- **결과 공유**: SNS 공유 (카카오톡, X, 페이스북)
- **AdSense 연동**: 광고 수익화 준비

## 프로젝트 구조

```
simly/
├── backend/
│   ├── app/
│   │   ├── api/v1/        # API 라우터
│   │   ├── core/          # 설정, 데이터베이스
│   │   ├── models/        # SQLAlchemy 모델
│   │   ├── schemas/       # Pydantic 스키마
│   │   └── services/      # 비즈니스 로직
│   ├── scripts/           # 유틸리티 스크립트
│   └── tests/             # pytest 테스트
│
├── frontend/
│   ├── src/
│   │   ├── app/           # Next.js 페이지
│   │   ├── components/    # React 컴포넌트
│   │   ├── lib/           # API 클라이언트
│   │   ├── stores/        # Zustand 스토어
│   │   ├── types/         # TypeScript 타입
│   │   └── mocks/         # MSW Mock 데이터
│   └── __tests__/         # Vitest 테스트
│
└── docs/planning/         # 기획 문서
```

## 환경변수

### Backend (.env)
```
DATABASE_URL=sqlite:///./simly.db
OPENAI_API_KEY=sk-your-api-key
DEBUG=true
```

### Frontend (.env.local)
```
NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1
NEXT_PUBLIC_ADSENSE_CLIENT_ID=  # 선택 (광고)
NEXT_PUBLIC_KAKAO_JS_KEY=       # 선택 (카카오 공유)
```

## 문서

- [PRD](docs/planning/01-prd.md) - 제품 요구사항
- [TRD](docs/planning/02-trd.md) - 기술 요구사항
- [TASKS](docs/planning/06-tasks.md) - 태스크 목록

## 라이선스

MIT

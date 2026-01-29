# Coding Convention & AI Collaboration Guide

> 고품질/유지보수/보안을 위한 인간-AI 협업 운영 지침서입니다.

---

## MVP 캡슐

| # | 항목 | 내용 |
|---|------|------|
| 1 | 목표 | AdSense 부업 수익 창출을 위한 AI 심리테스트 플랫폼 |
| 2 | 페르소나 | 10~30대 (중고등학생, 대학생, 직장인) |
| 3 | 핵심 기능 | FEAT-1: AI 심리테스트 (개인화된 결과 생성) |
| 4 | 성공 지표 (노스스타) | AdSense 월 수익 |
| 5 | 입력 지표 | 테스트 완료율, 공유 전환율 |
| 6 | 비기능 요구 | 빠른 로딩 속도 (3초 이내) |
| 7 | Out-of-scope | 프리미엄 유료화, 소셜 로그인, 회원가입 |
| 8 | Top 리스크 | AI API 비용이 수익보다 높아질 수 있음 |
| 9 | 완화/실험 | 결과 캐싱, API 호출 최적화, 비용 모니터링 |
| 10 | 다음 단계 | MVP 개발 시작 - 테스트 1개로 검증 |

---

## 1. 핵심 원칙

### 1.1 신뢰하되, 검증하라 (Don't Trust, Verify)

AI가 생성한 코드는 반드시 검증해야 합니다:

- [ ] 코드 리뷰: 생성된 코드 직접 확인
- [ ] 테스트 실행: 자동화 테스트 통과 확인
- [ ] 보안 검토: 민감 정보 노출 여부 확인
- [ ] 동작 확인: 실제로 실행하여 기대 동작 확인

### 1.2 최종 책임은 인간에게

- AI는 도구이고, 최종 결정과 책임은 개발자에게 있습니다
- 이해하지 못하는 코드는 사용하지 않습니다
- 의심스러운 부분은 반드시 질문합니다

---

## 2. 프로젝트 구조

### 2.1 디렉토리 구조

```
simly/
├── frontend/                    # Next.js 프론트엔드
│   ├── src/
│   │   ├── app/                # App Router 페이지
│   │   │   ├── (mobile)/       # 모바일 버전 라우트 그룹
│   │   │   ├── (desktop)/      # PC 버전 라우트 그룹
│   │   │   └── api/            # API Routes (필요시)
│   │   ├── components/         # 재사용 컴포넌트
│   │   │   ├── ui/             # 기본 UI 컴포넌트
│   │   │   ├── test/           # 테스트 관련 컴포넌트
│   │   │   └── result/         # 결과 관련 컴포넌트
│   │   ├── hooks/              # 커스텀 훅
│   │   ├── lib/                # 유틸리티, API 클라이언트
│   │   ├── stores/             # Zustand 스토어
│   │   ├── types/              # TypeScript 타입
│   │   └── mocks/              # MSW Mock 핸들러
│   ├── public/                 # 정적 파일
│   └── e2e/                    # E2E 테스트
│
├── backend/                     # FastAPI 백엔드
│   ├── app/
│   │   ├── api/                # API 라우터
│   │   │   └── v1/             # v1 엔드포인트
│   │   ├── core/               # 설정, 의존성
│   │   ├── models/             # SQLAlchemy 모델
│   │   ├── schemas/            # Pydantic 스키마
│   │   ├── services/           # 비즈니스 로직
│   │   └── utils/              # 유틸리티
│   └── tests/                  # pytest 테스트
│
├── contracts/                   # API 계약 (BE/FE 공유)
│   ├── types.ts                # 공통 타입
│   └── test.contract.ts        # 테스트 API 계약
│
├── docs/
│   └── planning/               # 기획 문서 (소크라테스 산출물)
│
├── docker-compose.yml
├── docker-compose.dev.yml
└── README.md
```

### 2.2 네이밍 규칙

| 대상 | 규칙 | 예시 |
|------|------|------|
| 파일 (React 컴포넌트) | PascalCase | `TestCard.tsx` |
| 파일 (훅) | camelCase + use 접두사 | `useTestProgress.ts` |
| 파일 (유틸) | camelCase | `formatResult.ts` |
| 파일 (Python) | snake_case | `test_service.py` |
| React 컴포넌트 | PascalCase | `TestCard` |
| 함수/변수 (JS) | camelCase | `getTestById` |
| 함수/변수 (Python) | snake_case | `get_test_by_id` |
| 상수 | UPPER_SNAKE | `MAX_QUESTIONS` |
| CSS 클래스 | Tailwind 사용 | `flex items-center` |
| 환경 변수 | UPPER_SNAKE | `DATABASE_URL` |

---

## 3. 아키텍처 원칙

### 3.1 뼈대 먼저 (Skeleton First)

1. 전체 구조를 먼저 잡고
2. 빈 함수/컴포넌트로 스켈레톤 생성
3. 하나씩 구현 채워나가기

### 3.2 작은 모듈로 분해

| 대상 | 권장 라인 |
|------|----------|
| 파일 | 200줄 이하 |
| 함수 | 50줄 이하 |
| React 컴포넌트 | 100줄 이하 |

### 3.3 관심사 분리

**프론트엔드:**
| 레이어 | 역할 | 위치 |
|--------|------|------|
| UI | 화면 표시 | `components/` |
| 상태 | 데이터 관리 | `stores/` |
| 서비스 | API 통신 | `lib/api.ts` |
| 유틸 | 순수 함수 | `lib/utils.ts` |

**백엔드:**
| 레이어 | 역할 | 위치 |
|--------|------|------|
| Router | 요청 수신/응답 | `api/` |
| Schema | 검증/직렬화 | `schemas/` |
| Service | 비즈니스 로직 | `services/` |
| Model | 데이터 접근 | `models/` |

---

## 4. 코드 스타일

### 4.1 TypeScript (Frontend)

```typescript
// 타입 정의 - interface 선호
interface Test {
  id: string;
  title: string;
  questions: Question[];
}

// 컴포넌트 - 화살표 함수 + Props 타입
interface TestCardProps {
  test: Test;
  onSelect: (id: string) => void;
}

export function TestCard({ test, onSelect }: TestCardProps) {
  return (
    <div onClick={() => onSelect(test.id)}>
      {test.title}
    </div>
  );
}

// 훅 - use 접두사
export function useTestProgress(testId: string) {
  const [progress, setProgress] = useState(0);
  // ...
  return { progress, next, prev };
}
```

### 4.2 Python (Backend)

```python
# 서비스 - 비동기 함수
async def get_test_by_id(db: AsyncSession, test_id: UUID) -> Test | None:
    """테스트 ID로 테스트 조회"""
    result = await db.execute(
        select(Test).where(Test.id == test_id)
    )
    return result.scalar_one_or_none()


# 스키마 - Pydantic
class TestResponse(BaseModel):
    id: UUID
    title: str
    question_count: int

    model_config = ConfigDict(from_attributes=True)


# 라우터 - FastAPI
@router.get("/{test_id}", response_model=TestResponse)
async def get_test(
    test_id: UUID,
    db: AsyncSession = Depends(get_db),
) -> Test:
    """테스트 상세 조회"""
    test = await test_service.get_test_by_id(db, test_id)
    if not test:
        raise HTTPException(status_code=404, detail="Test not found")
    return test
```

---

## 5. AI 소통 원칙

### 5.1 하나의 채팅 = 하나의 작업

- 한 번에 하나의 명확한 작업만 요청
- 작업 완료 후 다음 작업 진행
- 컨텍스트가 길어지면 새 대화 시작

### 5.2 컨텍스트 명시

**좋은 예:**
```
TASKS 문서의 T2.1을 구현해주세요.
- Database Design의 TEST 테이블 참조
- TRD의 API 설계 원칙 준수
- 기존 코드 스타일 따르기
```

**나쁜 예:**
```
API 만들어줘
```

### 5.3 프롬프트 템플릿

```markdown
## 작업
{{무엇을 해야 하는지}}

## 참조 문서
- PRD 섹션 {{번호}}
- TRD 섹션 {{번호}}

## 제약 조건
- {{지켜야 할 것}}

## 예상 결과
- {{생성될 파일}}
- {{기대 동작}}
```

---

## 6. 보안 체크리스트

### 6.1 절대 금지

- [ ] API 키 하드코딩 금지
- [ ] .env 파일 커밋 금지
- [ ] SQL 직접 문자열 조합 금지
- [ ] 사용자 입력 그대로 출력 금지

### 6.2 필수 적용

- [ ] 모든 입력 Pydantic 검증
- [ ] Rate Limiting (AI API 보호)
- [ ] HTTPS 사용
- [ ] CORS 허용 도메인 제한

### 6.3 환경 변수 관리

```bash
# .env.example (커밋 O)
DATABASE_URL=postgresql://user:pass@localhost:5432/simly
REDIS_URL=redis://localhost:6379
OPENAI_API_KEY=sk-your-key-here

# .env (커밋 X) - .gitignore에 추가
DATABASE_URL=postgresql://real:real@prod:5432/simly
OPENAI_API_KEY=sk-real-key
```

---

## 7. 테스트 워크플로우

### 7.1 테스트 명령어

```bash
# 백엔드
cd backend
pytest -v                           # 전체 테스트
pytest tests/api/ -v                # API 테스트만
pytest --cov=app --cov-report=html  # 커버리지

# 프론트엔드
cd frontend
npm run test                        # Vitest 실행
npm run test:coverage               # 커버리지
npm run test:e2e                    # Playwright E2E
```

### 7.2 테스트 작성 규칙

**백엔드:**
```python
# tests/api/test_test.py
async def test_get_test_returns_test(client: AsyncClient, test_fixture: Test):
    """테스트 조회 - 성공"""
    response = await client.get(f"/api/v1/tests/{test_fixture.id}")
    assert response.status_code == 200
    assert response.json()["title"] == test_fixture.title


async def test_get_test_not_found(client: AsyncClient):
    """테스트 조회 - 404"""
    fake_id = uuid4()
    response = await client.get(f"/api/v1/tests/{fake_id}")
    assert response.status_code == 404
```

**프론트엔드:**
```typescript
// src/__tests__/components/TestCard.test.tsx
describe('TestCard', () => {
  it('테스트 제목을 표시한다', () => {
    render(<TestCard test={mockTest} onSelect={vi.fn()} />);
    expect(screen.getByText('테스트 제목')).toBeInTheDocument();
  });

  it('클릭 시 onSelect를 호출한다', async () => {
    const onSelect = vi.fn();
    render(<TestCard test={mockTest} onSelect={onSelect} />);
    await userEvent.click(screen.getByRole('button'));
    expect(onSelect).toHaveBeenCalledWith(mockTest.id);
  });
});
```

### 7.3 오류 로그 공유 규칙

오류 발생 시 AI에게 전달할 정보:

```markdown
## 에러
TypeError: Cannot read property 'id' of undefined

## 코드
const testId = test.id;  // line 42

## 재현
1. 테스트 목록 페이지에서
2. 존재하지 않는 테스트 클릭

## 시도한 것
- test가 undefined인지 확인 → undefined
```

---

## 8. Git 워크플로우

### 8.1 브랜치 전략

```
main              # 프로덕션 배포
├── develop       # 개발 통합
│   ├── feature/feat-1-ai-test    # 기능 개발
│   ├── feature/feat-0-setup      # 초기 설정
│   └── fix/result-cache          # 버그 수정
```

### 8.2 커밋 메시지

```
<type>(<scope>): <subject>

<body>
```

**타입:**
| 타입 | 설명 |
|------|------|
| `feat` | 새 기능 |
| `fix` | 버그 수정 |
| `refactor` | 리팩토링 |
| `docs` | 문서 |
| `test` | 테스트 |
| `chore` | 기타 (설정, 빌드 등) |

**예시:**
```
feat(test): AI 결과 생성 API 추가

- OpenAI API 연동
- 결과 캐싱 로직 구현
- TRD 섹션 4.1 구현 완료
```

### 8.3 PR 규칙

```markdown
## 변경 사항
- [ ] 기능 설명

## 테스트
- [ ] 단위 테스트 통과
- [ ] E2E 테스트 통과 (해당시)

## 체크리스트
- [ ] 코드 리뷰 요청
- [ ] 린트 통과
- [ ] 타입 체크 통과
```

---

## 9. 코드 품질 도구

### 9.1 프론트엔드 설정

```json
// package.json scripts
{
  "lint": "eslint src --ext .ts,.tsx",
  "lint:fix": "eslint src --ext .ts,.tsx --fix",
  "format": "prettier --write src",
  "type-check": "tsc --noEmit"
}
```

### 9.2 백엔드 설정

```toml
# pyproject.toml
[tool.ruff]
line-length = 88
select = ["E", "F", "I", "N", "W"]

[tool.black]
line-length = 88

[tool.mypy]
python_version = "3.11"
strict = true
```

### 9.3 Pre-commit 훅

```yaml
# .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: frontend-lint
        name: Frontend Lint
        entry: npm run lint --prefix frontend
        language: system
        pass_filenames: false
      - id: backend-lint
        name: Backend Lint
        entry: ruff check backend
        language: system
        pass_filenames: false
```

---

## 10. 배포 체크리스트

### 10.1 프로덕션 배포 전

- [ ] 모든 테스트 통과
- [ ] 환경 변수 설정 확인
- [ ] API 키 유효성 확인
- [ ] CORS 설정 확인
- [ ] Rate Limit 설정 확인
- [ ] 에러 모니터링 설정

### 10.2 배포 명령어

```bash
# Frontend (Vercel)
vercel --prod

# Backend (Railway/Render)
git push origin main  # 자동 배포
```

---

## Decision Log

| ID | 항목 | 선택 | 근거 |
|----|------|------|------|
| D-C01 | 린터 (FE) | ESLint | 표준 |
| D-C02 | 린터 (BE) | Ruff | 빠름, 통합 |
| D-C03 | 포매터 | Prettier/Black | 표준 |
| D-C04 | 테스트 (FE) | Vitest | Vite 호환, 빠름 |
| D-C05 | 테스트 (BE) | pytest | Python 표준 |

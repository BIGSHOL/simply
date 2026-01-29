# Simly 명령어 참조

## Backend 명령어

### 서버 실행
```bash
cd backend

# 개발 서버 실행 (자동 리로드)
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# 프로덕션 서버 실행
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### 데이터베이스 시드

```bash
cd backend

# 전체 테스트 시드 (권장)
python scripts/seed_all.py

# 전체 테스트 시드 + DB 초기화
python scripts/seed_all.py --reset

# 개별 테스트 시드
python scripts/seed_data.py           # 기본 테이블 생성 + 샘플 데이터
python scripts/seed_rank_test.py      # 직장 계급 테스트 (12문항, 10결과)
python scripts/seed_animal_test.py    # 동물 성격 테스트 (10문항, 12결과)
python scripts/seed_insect_test.py    # 곤충 테스트 (20문항, 32결과)
python scripts/seed_food_test.py      # 음식 테스트 (8문항, 16결과)
python scripts/seed_mbti_love_test.py # MBTI 연애 테스트 (12문항, 16결과)
python scripts/seed_workplace_test.py # 직장 유형 테스트 (12문항, 16결과)
python scripts/seed_love_test.py      # 연애 유형 테스트 (20문항, 20결과)
python scripts/seed_uncle_test.py     # 아재력 테스트 (15문항, 20결과)
```

### 테스트 실행
```bash
cd backend

# 전체 테스트
python -m pytest

# 특정 파일 테스트
python -m pytest tests/test_example.py

# 커버리지 포함
python -m pytest --cov=app --cov-report=html

# 상세 출력
python -m pytest -v
```

### 의존성 관리
```bash
cd backend

# 의존성 설치
python -m pip install -r requirements.txt

# 새 패키지 추가 후 requirements.txt 갱신
python -m pip freeze > requirements.txt

# 개별 패키지 설치
python -m pip install <package-name>
```

---

## Frontend 명령어

### 개발 서버
```bash
cd frontend

# 개발 서버 실행 (http://localhost:3000)
npm run dev

# Turbopack 사용 (기본값)
npm run dev -- --turbo
```

### 빌드
```bash
cd frontend

# 프로덕션 빌드
npm run build

# 빌드 후 서버 실행
npm run start

# 빌드 결과물 미리보기
npm run start -- -p 3000
```

### 코드 품질
```bash
cd frontend

# 린트 검사
npm run lint

# 린트 자동 수정
npm run lint -- --fix

# 타입 체크
npx tsc --noEmit
```

### 의존성 관리
```bash
cd frontend

# 의존성 설치
npm install

# 새 패키지 추가
npm install <package-name>

# 개발 의존성 추가
npm install -D <package-name>

# 패키지 업데이트
npm update

# 취약점 검사
npm audit

# 취약점 자동 수정
npm audit fix
```

---

## Docker 명령어 (옵션)

```bash
# 전체 서비스 빌드 & 실행
docker-compose up --build

# 백그라운드 실행
docker-compose up -d

# 서비스 중지
docker-compose down

# 로그 확인
docker-compose logs -f

# 특정 서비스만 실행
docker-compose up backend
docker-compose up frontend
```

---

## Git 명령어

### 기본 워크플로우
```bash
# 상태 확인
git status

# 변경사항 스테이징
git add .
git add <file>

# 커밋
git commit -m "feat: 기능 추가"

# 푸시
git push origin <branch>

# 풀
git pull origin <branch>
```

### 브랜치 관리
```bash
# 브랜치 목록
git branch -a

# 새 브랜치 생성 & 체크아웃
git checkout -b feature/new-feature

# 브랜치 전환
git checkout main

# 브랜치 삭제
git branch -d feature/old-feature
```

### 커밋 컨벤션
```
feat: 새로운 기능 추가
fix: 버그 수정
docs: 문서 수정
style: 코드 포맷팅
refactor: 코드 리팩토링
test: 테스트 코드 추가
chore: 빌드, 패키지 매니저 설정
```

---

## 유용한 명령어

### 포트 확인 (Windows)
```bash
# 특정 포트 사용 확인
netstat -ano | findstr :3000
netstat -ano | findstr :8000

# 프로세스 종료
taskkill /PID <PID> /F
```

### 포트 확인 (Mac/Linux)
```bash
# 특정 포트 사용 확인
lsof -i :3000
lsof -i :8000

# 프로세스 종료
kill -9 <PID>
```

### SQLite 데이터베이스 확인
```bash
cd backend

# SQLite CLI 접속
sqlite3 simly.db

# 테이블 목록
.tables

# 테이블 스키마 확인
.schema tests

# 데이터 조회
SELECT * FROM tests;
SELECT COUNT(*) FROM questions;

# 종료
.quit
```

### 환경변수 설정

#### Backend (.env)
```env
DATABASE_URL=sqlite:///./simly.db
SECRET_KEY=your-secret-key
DEBUG=true
CORS_ORIGINS=http://localhost:3000
```

#### Frontend (.env.local)
```env
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_SITE_URL=http://localhost:3000
```

---

## 자주 사용하는 명령어 조합

### 개발 환경 시작
```bash
# 터미널 1: Backend
cd backend
python scripts/seed_all.py --reset
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# 터미널 2: Frontend
cd frontend
npm run dev
```

### 빠른 DB 리셋 & 재시드
```bash
cd backend
python scripts/seed_all.py --reset
```

### 프로덕션 빌드 테스트
```bash
cd frontend
npm run build
npm run start
```

### 첫 설치 후 전체 셋업
```bash
# Backend
cd backend
python -m pip install -r requirements.txt
python scripts/seed_all.py --reset
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Frontend (새 터미널)
cd frontend
npm install
npm run dev
```

---

## 문제 해결

### Backend 서버 시작 안됨
```bash
# 포트 충돌 확인
netstat -ano | findstr :8000

# 설치된 패키지 확인
python -m pip list

# uvicorn 설치
python -m pip install uvicorn[standard]
```

### pip/uvicorn 명령어 안됨
```bash
# python -m 을 앞에 붙여서 실행
python -m pip install <package>
python -m uvicorn app.main:app --reload
```

### Frontend 빌드 실패
```bash
# node_modules 재설치
rm -rf node_modules package-lock.json
npm install

# 캐시 클리어
npm cache clean --force
```

### 데이터베이스 오류
```bash
# DB 파일 삭제 후 재생성
cd backend
rm simly.db
python scripts/seed_all.py
```

---

## 버전 정보

- Python: 3.11+
- Node.js: 18+
- Next.js: 16.x
- FastAPI: 0.100+
- SQLAlchemy: 2.x

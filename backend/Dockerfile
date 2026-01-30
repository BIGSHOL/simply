FROM python:3.11-slim

WORKDIR /app

# 시스템 패키지 설치
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# 의존성 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 소스 복사
COPY . .

# 포트 설정 (Railway는 $PORT 환경변수를 주입)
EXPOSE ${PORT:-8000}

# 서버 실행 (Railway $PORT 환경변수 사용)
CMD uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}

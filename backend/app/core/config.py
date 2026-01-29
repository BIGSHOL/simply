"""
앱 설정

환경변수를 통해 설정을 관리합니다.
"""
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    # Database (기본값: 로컬 SQLite)
    database_url: str = "sqlite:///./simly.db"

    # Redis
    redis_url: str = "redis://localhost:6379"

    # OpenAI
    openai_api_key: str = ""

    # Application
    debug: bool = True
    secret_key: str = "your-secret-key-change-in-production"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()

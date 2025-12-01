from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastApi initializer"
    API_V1_STR: str = '/api/v1'

    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    ALGORITHM: str = 'HS256'

    SQLALCHEMY_DATABASE_URL: str

    ENVIRONMENT: str = 'local'

    class Config:
        env_file = '.env'
        case_sensitive = True

@lru_cache
def get_settings() -> Settings:
    return Settings()        


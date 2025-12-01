from app.core.config import get_settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

settings = get_settings()

engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(autoflush=False,bind=engine)


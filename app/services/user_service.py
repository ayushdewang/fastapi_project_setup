# app/services/user_service.py
from sqlalchemy.orm import Session

from app.core.security import get_hash_pw, verify_password
from app.models.user_model import User
from app.schemas.user_schema import UserCreate
import uuid


def create_user(db: Session, user_in: UserCreate) -> User:
    user = User(
        id=str(uuid.uuid4()),
        email=user_in.email,
        full_name=user_in.full_name,
        hashed_password=get_hash_pw(user_in.password),
    
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def authenticate_user(db: Session, email: str, password: str) -> User | None:
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user

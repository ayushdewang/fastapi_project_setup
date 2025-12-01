# app/api/v1/users.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_current_user, get_db
from app.core.security import get_hash_pw
from app.models.user_model import User
from app.schemas.user_schema import UserRead, UserUpdate

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me", response_model=UserRead)
def read_user_me(
    current_user: User = Depends(get_current_user),
):
    return current_user

@router.delete('/delete',)
def delete_user(
    current_user: User = Depends(get_current_user),db: Session = Depends(get_db)
):
    db.delete(current_user)
    db.commit()
    return "User deleted successful."

@router.put('/update')
def update_user(

       user_in: UserUpdate ,current_usr: User = Depends(get_current_user),db: Session = Depends(get_db)
):
    current_user = current_usr
    if user_in.full_name is not None:
        current_user.full_name = user_in.full_name
    if user_in.password is not None:
        current_user.hashed_password = get_hash_pw(user_in.password)    

    db.commit()
    db.refresh(current_user)
    return current_user


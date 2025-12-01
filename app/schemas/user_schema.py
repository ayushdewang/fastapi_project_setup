
from pydantic import BaseModel, EmailStr,UUID4


class UserBase(BaseModel):
    email: EmailStr
    full_name: str | None
    is_active: bool | None

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: str

class UserUpdate(BaseModel):
    full_name: str | None
    password: str | None   

class UserRead(UserBase):
    id: str

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = 'bearer'
    message: str = "success"

class TokenPayload(BaseModel):
    sub: str | None
    type: str | None



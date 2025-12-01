from app.db.session import Base
from sqlalchemy import Column,String,Boolean


class User(Base):
    __tablename__ = 'users'

    id = Column(String,primary_key=True)
    email = Column(String,unique=True,nullable=False)
    hashed_password = Column(String,nullable=False)
    full_name = Column(String,nullable=False)
    is_active = Column(Boolean,default=True)


from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr
    username: str
    is_active: bool = True

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    password: str | None = None

class User(UserBase):
    id: int
    is_superuser: bool = False

    class Config:
        from_attributes = True

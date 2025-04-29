from pydantic import BaseModel

class CategoryBase(BaseModel):
    name: str
    description: str | None = None
    is_active: bool = True

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int

    class Config:
        from_attributes = True 
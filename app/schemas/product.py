from pydantic import BaseModel, Field
from typing import Optional

class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float = Field(gt=0)
    is_active: bool = True
    category_id: int

class ProductCreate(ProductBase):
    class Config:
        from_attributes = True

class Product(ProductBase):
    id: int

    class Config:
        from_attributes = True 
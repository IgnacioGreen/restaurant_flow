from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.product import Product
from app.models.category import Category
from app.schemas.product import ProductCreate

def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def get_product_by_name(db: Session, name: str):
    return db.query(Product).filter(Product.name == name).first()

def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Product).offset(skip).limit(limit).all()

def get_products_by_category(db: Session, category_id: int):
    return db.query(Product).filter(Product.category_id == category_id).all()

def create_product(db: Session, product: ProductCreate):
    category = db.query(Category).filter(Category.id == product.category_id).first()
    if not category:
        raise HTTPException(
            status_code=404,
            detail=f"Category with id {product.category_id} not found"
        )
    
    if not category.is_active:
        raise HTTPException(
            status_code=400,
            detail=f"Category with id {product.category_id} is not active"
        )
    
    db_product = Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product(db: Session, product_id: int, product: ProductCreate):
    db_product = get_product(db, product_id)
    if not db_product:
        raise HTTPException(
            status_code=404,
            detail=f"Product with id {product_id} not found"
        )

    category = db.query(Category).filter(Category.id == product.category_id).first()
    if not category:
        raise HTTPException(
            status_code=404,
            detail=f"Category with id {product.category_id} not found"
        )
    
    if not category.is_active:
        raise HTTPException(
            status_code=400,
            detail=f"Category with id {product.category_id} is not active"
        )
    
    for key, value in product.model_dump().items():
        setattr(db_product, key, value)
    
    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    db_product = get_product(db, product_id)
    if not db_product:
        raise HTTPException(
            status_code=404,
            detail=f"Product with id {product_id} not found"
        )
    db.delete(db_product)
    db.commit()
    return db_product 
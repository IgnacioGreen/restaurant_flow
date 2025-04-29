from fastapi import FastAPI
from app.routers import auth, category, product
from app.database import engine
from app.models import product as product_model, user, category as category_model


user.Base.metadata.create_all(bind=engine)
category_model.Base.metadata.create_all(bind=engine)
product_model.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(category.router)
app.include_router(product.router)

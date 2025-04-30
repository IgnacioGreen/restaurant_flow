from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth, category, product
from app.database import engine
from app.models import user, category as category_model, product as product_model
from app.core.config import settings

# Crear las tablas
user.Base.metadata.create_all(bind=engine)
category_model.Base.metadata.create_all(bind=engine)
product_model.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especifica los orígenes permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(auth.router)
app.include_router(category.router)
app.include_router(product.router)

from fastapi import APIRouter
from app.api.v1.routes import dName

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(dName.router, tags=["Appointments"])
# api_router.include_router(auth.router, tags=["Auth"])

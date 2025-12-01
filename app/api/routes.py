# app/api/routes.py
from fastapi import APIRouter

from app.api import auth_route, user_route

api_router = APIRouter()
api_router.include_router(auth_route.router)
api_router.include_router(user_route.router)

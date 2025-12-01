# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import api_router
from app.db.base import Base
from app.core.config import get_settings
from app.db.session import engine

settings = get_settings()


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version="1.0.0",
    )

    # # CORS (configure as you like)
    # app.add_middleware(
    #     CORSMiddleware,
    #     allow_origins=["*"],
    #     allow_credentials=True,
    #     allow_methods=["*"],
    #     allow_headers=["*"],
    # )

    # Include versioned API router
    app.include_router(api_router, prefix=settings.API_V1_STR)

   

    return app


app = create_app()
# Base.metadata.create_all(engine)

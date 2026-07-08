from fastapi import FastAPI

from .routes.article import router

app = FastAPI(
    title="Article API"
)

app.include_router(router)
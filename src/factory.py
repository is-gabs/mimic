from fastapi import FastAPI

from src.api import regiter_routers


def create_app():
    app = FastAPI()
    regiter_routers(app)
    return app


app = create_app()
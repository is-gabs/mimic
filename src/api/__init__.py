from src.api.clients.routers import router as clients_router


def regiter_routers(app):
    app.include_router(clients_router)
    return app
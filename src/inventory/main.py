from fastapi import FastAPI

from inventory.routers import health, items
from inventory.store import ItemStore


def create_app() -> FastAPI:
    app = FastAPI(title="Workshop Inventory", version="0.1.0")
    app.state.store = ItemStore()
    app.include_router(health.router)
    app.include_router(items.router)
    return app


app = create_app()

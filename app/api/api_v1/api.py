from fastapi import APIRouter

from app.api.api_v1.endpoints import item_router


router = APIRouter(prefix="/api/v1")

router.include_router(item_router.router, prefix="/items", tags=["items"])

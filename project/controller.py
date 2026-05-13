from fastapi import APIRouter
from service import stat_service

router = APIRouter(prefix="/api")

@router.get("/stats") 
async def get_stats():
    return stat_service.get_stats()

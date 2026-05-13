
# [1] 라우터 : 특정 도메인(주소)한 묶어주는 역할
from fastapi import APIRouter

# APIRouter(prefix='/공통도메인')
# vs @ReqeustMapping("공통도메인")
router = APIRouter(prefix="/api")
# [2] REST API 정의
# (1) GET
@router.get("/item")
async def item() :
    return "item"

# (1-1) GET
@router.get("/items")
async def item() :
    return "items"

# (2) POST
@router.post("/save")
async def save() :
    return "save"

# (3) PUT
@router.put("/update")
async def update() :
    return "update"

# (4) DELETE
@router.delete("/delete")
async def delete() :
    return "delete" 

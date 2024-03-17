from fastapi import APIRouter

home_router = APIRouter(
    prefix="/home",
    tags=["home"],
)


@home_router.put("/")
async def home():
    return ""


@home_router.put("/dogs")
async def dogs():
    return ""

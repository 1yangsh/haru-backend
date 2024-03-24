from fastapi import APIRouter, HTTPException

from end_points.user.schema.register.request import RegisterUserRequest
from end_points.user.schema.register.response import RegisterUserResponse
from user_cases.auth.kakao import UserKakaoAuthHandler
from user_cases.user.register import UserRegisterHandler

user_router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@user_router.post("/register")
async def register(req: RegisterUserRequest) -> RegisterUserResponse:
    if req.userRequest.userRole not in ("DAD", "MOM", "UNNIE", "OPPA", "NUNA", "HYEONG", "YOUNGER"):
        raise HTTPException(
            status_code=404,
            detail="userRole should be 'DAD', 'MOM', 'UNNIE', 'OPPA', 'NUNA', 'HYEONG' or 'YOUNGER'"
        )
    if req.dogRequest.gender not in ("MALE", "FEMALE"):
        raise HTTPException(
            status_code=404,
            detail="gender show be 'MALE' or 'FEMALE'"
        )
    try:
        uow = UserRegisterHandler(req=req)
        return uow.handle()
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@user_router.post("/invitation/{homeId}")
async def invitation():
    return ""


@user_router.get("/auth/login/kakao")
async def login(code: str):
    uow = UserKakaoAuthHandler(code)
    return uow.handle()


@user_router.post("/withdraw")
async def withdraw():
    return ""


@user_router.post("/auth/logout")
async def logout():
    return ""


@user_router.post("/auth/refresh")
async def refresh():
    return ""


@user_router.put("/profile")
async def profile():
    return ""

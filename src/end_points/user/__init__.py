from fastapi import APIRouter

from end_points.user.schema.register.request import RegisterUserRequest
from end_points.user.schema.register.response import RegisterUserResponse
from user_cases.user.register import UserRegisterHandler

user_router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@user_router.post("/register")
async def register(req: RegisterUserRequest) -> RegisterUserResponse:
    return UserRegisterHandler.handle(req=req)


@user_router.post("/invitation/{homeId}")
async def invitation():
    return ""


@user_router.get("/auth/login/kakao")
async def login(code: str):
    return ""


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

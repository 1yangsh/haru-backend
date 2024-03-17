from fastapi import APIRouter

noticiations_router = APIRouter(
    prefix="/notifications",
    tags=["notifications"],
)


@noticiations_router.get("/")
def get():
    return ""


@noticiations_router.put("/")
def set():
    return ""

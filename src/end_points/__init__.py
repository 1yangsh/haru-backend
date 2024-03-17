from fastapi import APIRouter

from end_points.home import home_router
from end_points.notification import noticiations_router
from end_points.schedules import schedules_router
from end_points.user import user_router

api_router = APIRouter(prefix="/api")
health_router = APIRouter(prefix="/health")

api_router.include_router(user_router)
api_router.include_router(home_router)
api_router.include_router(schedules_router)
api_router.include_router(noticiations_router)


@health_router.get("")
def health():
    return "I'm Alive"

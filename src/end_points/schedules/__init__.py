from fastapi import APIRouter

schedules_router = APIRouter(
    prefix="/schedules",
    tags=["schedules"],
)


@schedules_router.put("")
async def main():
    return ""


@schedules_router.delete("/{scheduleId}")
async def delete():
    return ""


@schedules_router.put("{scheduleId}")
async def modify():
    return ""


@schedules_router.post("{scheduleId}/replace")
async def replace():
    return ""


@schedules_router.put("{scheduleId}/status")
async def status():
    return ""


@schedules_router.get("home/{homeId}")
async def home():
    return ""


@schedules_router.get("schedules/{scheduleId}")
async def get():
    return ""

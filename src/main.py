from typing import Optional

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from config import RESTConfig
from end_points import api_router

app = FastAPI()


def create_app(rest_config: Optional[RESTConfig]) -> FastAPI:
    app = FastAPI(
        title="haru-api",
        description="REST API 문서입니다.",
        # version=get_version(),
        contact={
            "name": "seunghyeon",
        },
        docs_url=f"{rest_config.url_prefix}/docs",
        redoc_url=f"{rest_config.url_prefix}/redoc",
        openapi_url=f"{rest_config.url_prefix}/openapi.json",
    )
    app.include_router(api_router, prefix=rest_config.url_prefix)
    # app.add_exception_handler(Error, handle_error)
    _add_cors(app, rest_config.cors_allowed_origins)
    return app


def _add_cors(app: FastAPI, cors_allowed_origin: str) -> None:
    origins = cors_allowed_origin.strip().split(",")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


if __name__ == "__main__":
    app = create_app(rest_config=RESTConfig())
    uvicorn.run(app, host="0.0.0.0", port=8080)

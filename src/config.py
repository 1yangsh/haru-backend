import os
from enum import Enum

from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()


class DBConfigItem(BaseModel):
    host: str = Field(default="localhost")
    port: int = Field(default=3306)
    user: str = Field(default="")
    password: str = Field(default="")
    database: str = Field(default="")


class APIConfigItem(BaseModel):
    OAUTH_KAKAO_REST_API_KEY: str = Field(default="")
    OAUTH_KAKAO_SECRET: str = Field(default="")


class DBConfig(BaseModel):
    MYSQL_DATABASE: DBConfigItem = Field(
        default=DBConfigItem(
            host=os.getenv("MYSQL_DATABASE_HOST", ""),
            port=os.getenv("MYSQL_DATABASE_PORT", 3306),
            user=os.getenv("MYSQL_DATABASE_USERNAME", ""),
            password=os.getenv("DB_PASSWORD", ""),
            database=os.getenv("MYSQL_DATABASE_PASSWORD", ""),
        )
    )


class ApiConfig(BaseModel):
    API_KEY: APIConfigItem = Field(
        default=APIConfigItem(
            OAUTH_KAKAO_REST_API_KEY=os.getenv("OAUTH_KAKAO_REST_API_KEY", ""),
            OAUTH_KAKAO_SECRET=os.getenv("OAUTH_KAKAO_SECRET", ""),
        )
    )


class LoggingLevel(str, Enum):
    INFO = "INFO"
    DEBUG = "DEBUG"
    WARNING = "WARNING"
    ERROR = "ERROR"


class Config(BaseModel):
    db: DBConfig = Field(default_factory=DBConfig)
    api_key: ApiConfig = Field(default_factory=ApiConfig)
    logging_level: LoggingLevel = Field(default="INFO", env="LOGGING_LEVEL")


class RESTConfig(Config):
    host: str = Field(default="0.0.0.0", env="REST_HOST")
    port: int = Field(default=8000, env="REST_PORT")
    workers: int = Field(default=1, env="REST_WORKERS")
    url_prefix: str = Field(default="", env="REST_URL_PREFIX")
    cors_allowed_origins: str = Field(default="*", env="REST_CORS_ALLOWED_ORIGINS")

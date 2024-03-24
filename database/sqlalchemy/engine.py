import os
from abc import ABC, abstractmethod

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv(verbose=True)


default_engine = create_engine(
    url=f"mysql://"
    f"{os.getenv('MYSQL_DATABASE_USERNAME')}:"
    f"{os.getenv('MYSQL_DATABASE_PASSWORD')}@"
    f"{os.getenv('MYSQL_DATABASE_HOST')}:"
    f"{os.getenv('MYSQL_DATABASE_PORT')}/"
    f"{os.getenv('MYSQL_DATABASE_NAME')}",
    connect_args={"charset": "utf8"},
)


class AbstractDatabaseSession(ABC):
    def __init__(self):
        self._engine = default_engine
        self._Session = sessionmaker(bind=self._engine)

    @abstractmethod
    def create_session(self):
        pass

    @abstractmethod
    def close_session(self):
        pass

from contextlib import contextmanager

from database.sqlalchemy.engine import AbstractDatabaseSession


class DatabaseSession(AbstractDatabaseSession):
    def __init__(self):
        super().__init__()
        self._session = None

    @contextmanager
    def create_session(self):
        self._session = self._Session()
        try:
            yield self._session
        finally:
            self.close_session()

    def close_session(self):
        if self._session is not None:
            self._session.close()

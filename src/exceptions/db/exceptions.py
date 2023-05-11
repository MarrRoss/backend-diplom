from typing import Optional

from sqlalchemy.exc import DatabaseError


class ExceptionSQLError(Exception):
    def __init__(
        self,
        detail: str,
        code: int,
        sql_detail: Optional[str] = None,
        exc: Optional[DatabaseError] = None,
    ):
        self.code = code
        self.detail = detail
        self.sql_detail = sql_detail
        self._exc = exc

    @property
    def original_exception(self):
        if isinstance(self._exc, DatabaseError):
            return self._exc.orig.__cause__
        else:
            return self._exc

    @property
    def original_message(self):
        return getattr(self.original_exception, "message", None)

    @property
    def original_detail(self):
        return getattr(self.original_exception, "detail", None)


class NotFoundError(ExceptionSQLError):
    def __init__(
        self,
        detail: str,
        code: int,
        sql_detail: Optional[str] = None,
        exc: Optional[DatabaseError] = None,
    ):
        super(NotFoundError, self).__init__(
            detail=detail,
            code=code,
            sql_detail=sql_detail,
            exc=exc,
        )


class AlreadyExistsError(ExceptionSQLError):
    def __init__(
        self,
        detail: str,
        code: int,
        sql_detail: Optional[str] = None,
        exc: Optional[DatabaseError] = None,
    ):
        super(AlreadyExistsError, self).__init__(
            detail=detail, code=code, sql_detail=sql_detail, exc=exc
        )

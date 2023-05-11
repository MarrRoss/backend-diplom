from typing import Optional

from asyncpg import UniqueViolationError, ForeignKeyViolationError
from sqlalchemy.exc import DBAPIError, DatabaseError, NoResultFound

from exceptions.db.exceptions import NotFoundError, ExceptionSQLError, AlreadyExistsError


def handle_unique_error(exc: DatabaseError, sql_detail: Optional[str] = None):
    if exc.orig.sqlstate == UniqueViolationError.sqlstate:
        raise AlreadyExistsError(
            code=400,
            detail="Запись уже существует в базе данных",
            sql_detail=sql_detail,
            exc=exc,
        ) from exc


def handle_foreign_key_error(exc: DatabaseError):
    if exc.orig.sqlstate == ForeignKeyViolationError.sqlstate:
        table_name = exc.orig.__cause__.__dict__.get("table_name")
        raise ExceptionSQLError(
            code=400,
            detail=f"Произошла ошибка с таблицей {table_name}: {exc.orig.__cause__.detail}",
            exc=exc,
        ) from exc


def handle_not_found_error(
    exc: Optional[NoResultFound] = None, __: Optional[str] = None
):
    raise NotFoundError(
        code=404,
        detail="Запись, которую вы ищите или удаляете, отсутствует в базе данных",
        exc=exc,
    )


def handle_db_api_error(
    exc: Optional[DBAPIError] = None, sql_detail: Optional[str] = None
):
    raise ExceptionSQLError(
        code=400,
        detail="Произошла внутренняя ошибка базы данных при обработке запроса",
        sql_detail=str(exc),
        exc=exc,
    ) from exc

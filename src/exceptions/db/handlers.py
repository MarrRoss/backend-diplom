from starlette.requests import Request
from starlette.responses import JSONResponse

from exceptions.db.schemas import NotFoundSchema, AlreadyExistsSchema
from exceptions.db.exceptions import NotFoundError, ExceptionSQLError, AlreadyExistsError


def sql_exception_handler(_: Request, exc: ExceptionSQLError):
    return JSONResponse(
        status_code=exc.code,
        content={
            "detail": exc.detail,
            "sql_detail": exc.sql_detail,
        },
    )


def sql_already_exists_handler(_: Request, exc: AlreadyExistsError):
    return JSONResponse(
        status_code=exc.code,
        content=AlreadyExistsSchema(
            detail=exc.detail,
            sql_detail=exc.sql_detail,
        ).dict(),
    )


def sql_not_found_handler(_: Request, exc: NotFoundError):
    return JSONResponse(
        status_code=exc.code,
        content=NotFoundSchema(
            detail=exc.detail,
            sql_detail=exc.sql_detail,
        ).dict(),
    )

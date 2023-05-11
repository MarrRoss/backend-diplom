import logging
from typing import Any, TypeVar, Callable, ParamSpec, cast

from sqlalchemy.exc import DBAPIError, NoResultFound, IntegrityError

from exceptions.db.parsers import (
    handle_db_api_error,
    handle_unique_error,
    handle_not_found_error,
    handle_foreign_key_error,
)

logger = logging.getLogger(__name__)

P = ParamSpec("P")
T = TypeVar("T")
FuncT = TypeVar("FuncT", bound=Callable[..., Any])


def orm_error_handler(fn: FuncT) -> FuncT:
    async def decorator(*args: P.args, **kwargs: P.kwargs) -> T:
        try:
            return await fn(*args, **kwargs)

        except IntegrityError as exc:
            logger.warning(msg="error orm_error_handler", exc_info=exc)
            sql_detail = str(exc.orig.__cause__.detail)
            handle_unique_error(exc=exc, sql_detail=sql_detail)
            handle_foreign_key_error(exc=exc)

        except NoResultFound as exc:
            logger.warning(msg="error orm_error_handler", exc_info=exc)
            handle_not_found_error(exc=exc)

        except DBAPIError as exc:
            logger.warning(msg="error orm_error_handler", exc_info=exc)

            sql_detail = str(exc.orig.__cause__.detail)
            handle_db_api_error(exc=exc, sql_detail=sql_detail)

        except Exception as exc:
            logger.warning(msg="error orm_error_handler", exc_info=exc)
            raise exc

    return cast(FuncT, decorator)

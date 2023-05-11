from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware

from api.v1.binding import own_router_v1
from di.dependencies import fastapi_dependency_overrides
from di.factory import ConfigFactory


def create_application() -> FastAPI:
    config = ConfigFactory()

    application = FastAPI(
        debug=True,
        title="Stud",
        version="1.0.0",
    )
    dependency_overrides = fastapi_dependency_overrides(config=config)
    application.dependency_overrides = dependency_overrides

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])

    # application = setup_exception_handlers(app=application)

    application.include_router(own_router_v1)

    return application


app = create_application()

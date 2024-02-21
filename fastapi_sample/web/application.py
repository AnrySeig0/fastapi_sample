import logging
from importlib import metadata
from pathlib import Path

import sentry_sdk
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.staticfiles import StaticFiles
from sentry_sdk.integrations.fastapi import FastApiIntegration
from sentry_sdk.integrations.logging import LoggingIntegration
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration

from fastapi_sample.settings import settings
from fastapi_sample.web.api.base_response import ProjectJSONResponse
from fastapi_sample.web.api.exception import (
    ProjectException,
    project_http_exception_handler,
    value_error_exception_handler,
)
from fastapi_sample.web.api.router import api_router
from fastapi_sample.web.lifetime import register_shutdown_event, register_startup_event

APP_ROOT = Path(__file__).parent.parent


def get_app() -> FastAPI:
    """
    Get FastAPI application.

    This is the main constructor of an application.

    :return: application.
    """
    if settings.sentry_dsn:
        # Enables sentry integration.
        sentry_sdk.init(
            dsn=settings.sentry_dsn,
            traces_sample_rate=settings.sentry_sample_rate,
            environment=settings.environment,
            integrations=[
                FastApiIntegration(transaction_style="endpoint"),
                LoggingIntegration(
                    level=logging.getLevelName(
                        settings.log_level.value,
                    ),
                    event_level=logging.ERROR,
                ),
                SqlalchemyIntegration(),
            ],
        )
    app = FastAPI(
        title="fastapi_sample",
        version=metadata.version("fastapi_sample"),
        docs_url=None,
        redoc_url=None,
        openapi_url="/api/openapi.json",
        default_response_class=ProjectJSONResponse,  # global response for project
    )

    # add Exception Handler
    app.add_exception_handler(ProjectException, project_http_exception_handler)
    app.add_exception_handler(RequestValidationError, value_error_exception_handler)

    # Adds startup and shutdown events.
    register_startup_event(app)
    register_shutdown_event(app)

    # Main router for the API.
    app.include_router(router=api_router, prefix="/api")
    # Adds static directory.
    # This directory is used to access swagger files.
    app.mount(
        "/static",
        StaticFiles(directory=APP_ROOT / "static"),
        name="static",
    )

    return app

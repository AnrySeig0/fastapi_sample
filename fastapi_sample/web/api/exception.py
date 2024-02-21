from typing import Optional

from fastapi.exceptions import RequestValidationError
from pydantic import Field
from starlette.requests import Request
from starlette.responses import JSONResponse

from fastapi_sample.web.api.base_response import ResponseModelDTO


class ProjectException(Exception):
    """
    Base exception for ALL project
    """

    def __init__(self, code: str, msg: str, status_code: int):
        self.code = code
        self.msg = msg
        self.status_code = status_code


def project_http_exception_handler(
    request: Request,
    exc: ProjectException,
):
    return JSONResponse(
        status_code=exc.status_code,
        content=ResponseModelDTO(
            code=exc.code,
            msg=exc.msg,
        ).dict(exclude_none=True),
    )


# some global case of exception
Global_E422 = ProjectException(
    code="NOT_OK_422",
    msg="RequestValidationError",
    status_code=422,
)


class ExceptionResponseModel(ResponseModelDTO):
    """
    Trong trường hợp, validate input fail, trả về detail lỗi
    """

    detail: Optional[list] = Field(default=None)


def value_error_exception_handler(request: Request, exc: RequestValidationError):
    """
    pydantic validate request
    """
    return JSONResponse(
        status_code=Global_E422.status_code,
        content=ExceptionResponseModel(
            code=Global_E422.code,
            msg=Global_E422.msg,
            detail=exc.errors(),
        ).dict(exclude_none=True),
    )

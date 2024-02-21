from typing import Any, Optional

import ujson
from pydantic import BaseModel, ConfigDict, Field
from starlette.responses import JSONResponse


class ResponseModelDTO(BaseModel):
    """
    DTO for response.

    Form chung cho mọi response API của dịch vụ
    """

    code: str
    msg: str
    data: Optional[Any] = Field(default=None)

    model_config = ConfigDict(from_attributes=True)


# define some unique case of schema response
SUCCESS_RESP = ResponseModelDTO(code="OK_200", msg="success")


class ProjectJSONResponse(JSONResponse):
    """
    Custom response.

    :return: class json when success.
    """

    def render(self, content: Any) -> bytes:
        """
        Render.

        :param content: incoming response.
        :return: json response.
        """
        return ujson.dumps(
            ResponseModelDTO(
                code=SUCCESS_RESP.code,
                msg=SUCCESS_RESP.msg,
                data=content,
            ).dict(exclude_none=True),
            ensure_ascii=False,
        ).encode("utf-8")


# swagger define for router in FastAPI
base_responses = {
    422: {"model": ResponseModelDTO},
}

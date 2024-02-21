from pydantic import BaseModel

from fastapi_sample.web.api.base_response import ResponseModelDTO


class Message(BaseModel):
    """Simple message model."""

    message: str


class ResponseMsg(ResponseModelDTO):
    data: Message

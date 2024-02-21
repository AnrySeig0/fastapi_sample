from fastapi import APIRouter

from fastapi_sample.web.api.base_response import base_responses
from fastapi_sample.web.api.echo.exception import ECHO_ERROR_01
from fastapi_sample.web.api.echo.schema import Message, ResponseMsg

router = APIRouter(responses={200: {"model": ResponseMsg}, **base_responses})


@router.post("/")
async def send_echo_message(
    incoming_message: Message,
) -> Message:
    """
    Sends echo back to user.

    :param incoming_message: incoming message.
    :returns: message same as the incoming.
    """
    return incoming_message


@router.post("/error", responses={200: {"model": ResponseMsg}})
async def send_echo_message():
    """
    raise Error
    """
    raise ECHO_ERROR_01


@router.post(
    "/error_invalid_input",
    responses={200: {"model": ResponseMsg}},
)
async def send_echo_message(incoming_message: Message):
    """
    raise Error
    """
    raise ECHO_ERROR_01

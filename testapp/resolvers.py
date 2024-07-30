import random
import requests
import testapp.models
from asgiref.sync import sync_to_async
from .types import *
from gqlauth.core.constants import Messages
from gqlauth.jwt.types_ import (
    ObtainJSONWebTokenInput,
    ObtainJSONWebTokenType,
    RefreshTokenType,
    RevokeRefreshTokenType,
    TokenType,
    VerifyTokenInput,
    VerifyTokenType,
)


@sync_to_async
def me_sync() -> CustomUser:
    return testapp.models.CustomUser.objects.get(id=1)


async def me() -> CustomUser:
    return await me_sync()

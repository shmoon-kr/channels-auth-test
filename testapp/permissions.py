import typing
from asgiref.sync import sync_to_async
from strawberry.permission import BasePermission
from strawberry.types import Info
from gqlauth.core.utils import get_user


class IsAuthenticated(BasePermission):
    message = "Unauthorized"

    @sync_to_async
    # This method can also be async!
    def has_permission(self, source: typing.Any, info: Info, **kwargs) -> bool:
        user = get_user(info)
        return user.is_authenticated

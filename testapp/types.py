import strawberry_django
from typing import Optional
from strawberry import auto
from django.contrib.auth import get_user_model


@strawberry_django.type(get_user_model())
class CustomUser:
    id: auto
    email: auto

import strawberry
from gqlauth.user.queries import UserQueries
from gqlauth.user import arg_mutations as mutations
from gqlauth.core.middlewares import JwtSchema
from .types import *
from .resolvers import *
from .permissions import *


@strawberry.type
class Query(UserQueries):
    me: CustomUser = strawberry.field(resolver=me, permission_classes=[IsAuthenticated],)
    me_sync: CustomUser = strawberry.field(resolver=me_sync, permission_classes=[IsAuthenticated],)


@strawberry.type
class Mutation:

    # include what-ever mutations you want.
    verify_token = mutations.VerifyToken.field
    update_account = mutations.UpdateAccount.field
    archive_account = mutations.ArchiveAccount.field
    delete_account = mutations.DeleteAccount.field
    password_change = mutations.PasswordChange.field
    #swap_emails = mutations.SwapEmails.field
    #captcha = Captcha.field
    token_auth = mutations.ObtainJSONWebToken.field
    register = mutations.Register.field
    verify_account = mutations.VerifyAccount.field
    resend_activation_email = mutations.ResendActivationEmail.field
    send_password_reset_email = mutations.SendPasswordResetEmail.field
    password_reset = mutations.PasswordReset.field
    password_set = mutations.PasswordSet.field
    refresh_token = mutations.RefreshToken.field
    revoke_token = mutations.RevokeToken.field
    #verify_secondary_email = mutations.VerifySecondaryEmail.field


schema = strawberry.Schema(query=Query, mutation=Mutation)
arg_schema = JwtSchema(query=Query, mutation=Mutation, subscription=None)

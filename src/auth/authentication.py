from fastapi_users.authentication import AuthenticationBackend, BearerTransport, JWTStrategy

from config import settings


SECRET = settings.auth.secret_key

bearer_transport = BearerTransport(tokenUrl=settings.auth.token_url)


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(
        secret=SECRET,
        lifetime_seconds=settings.auth.lifetime_seconds_access
    )


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

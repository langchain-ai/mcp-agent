import hmac
import os

from langgraph_sdk import Auth

auth = Auth()

def _get_app_secret() -> str:
    """Get the app secret from the environment.

    This is sufficient for a very simple authentication system that contains
    a single "user" with a single secret key.
    """
    secret = os.environ.get("APP_SECRET")
    if not secret:
        raise ValueError("APP_SECRET environment variable is required.")
    if secret != secret.strip():
        raise ValueError("APP_SECRET cannot have leading or trailing whitespace.")
    return secret


APP_SECRET = _get_app_secret()

@auth.authenticate
async def authenticate(authorization: str) -> Auth.types.MinimalUserDict:
    # Expecting a header like: "Bearer <token>"
    # if not authorization or not authorization.startswith("Bearer "):
    #     raise Auth.exceptions.HTTPException(status_code=401, detail="Missing or invalid Authorization header")

    # token = authorization.removeprefix("Bearer ").strip()

    # # Validate the token using HMAC constant-time comparison
    # if not hmac.compare_digest(token, APP_SECRET):
    #     raise Auth.exceptions.HTTPException(status_code=401, detail="Invalid token")

    return {
        "identity": "authenticated-user",
    }

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
    # Validate credentials (e.g., API key, JWT token)
    if not authorization or not hmac.compare_digest(authorization, APP_SECRET):
        raise Auth.exceptions.HTTPException(status_code=401, detail="Unauthorized")

    # Return user info - only identity and is_authenticated are required
    # Add any additional fields you need for authorization
    return {
        "identity": "authenticated-user",
    }



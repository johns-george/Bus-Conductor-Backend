from google.oauth2 import id_token
from google.auth.transport import requests
from sqlalchemy.orm import Session

GOOGLE_CLIENT_ID = "your-google-client-id"

def verify_google_token(token: str,db: Session):
    try:
        idinfo = id_token.verify_oauth2_token(
            token,
            requests.Request(),
            GOOGLE_CLIENT_ID
        )
        return idinfo
    except Exception:
        return None
from datetime import datetime, timedelta
from http.client import HTTPException
from jose import JWTError, jwt

SECRET_KEY = ""   # change in prod
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def create_tokens(username: str):
    access_token = create_access_token(
        {"sub": username},
        expires_delta=timedelta(minutes=5)
    )

    refresh_token = create_access_token(
        {"sub": username, "type": "refresh"},
        expires_delta=timedelta(days=7)
    )

    return access_token, refresh_token

def create_access_token(data: dict,expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
from sqlalchemy.orm import Session
from src.models.user import User
from src.schemas.signup import SignUpRequest
from src.utility import hash_password, verify_password
from src.utility.auth_utility import create_tokens, decode_access_token
from src.utility.google_auth import verify_google_token

def google_login(token: str, db: Session):
    google_user = verify_google_token(token)

    if not google_user:
        return {"message": "Invalid Google token"}

    email = google_user.get("email")
    name = google_user.get("name")

    # Check if user exists
    user = db.query(User).filter(User.email == email).first()

    # Create user if not exists
    if not user:
        user = User(
            username=email,   # or generate username
            email=email,
            password=None     # no password for Google users
        )
        db.add(user)
        db.commit()
        db.refresh(user)

    # Create YOUR JWT
    access_token, refresh_token = create_tokens(user.username)
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }

def signup(signup_request: SignUpRequest,db: Session):
    user_data = signup_request.dict()
    existing_user = db.query(User).filter(
        User.username == user_data["username"]
    ).first()

    if existing_user:
        return {"message": "Username already exists"}
    
    user_data["password"] = hash_password(user_data["password"])
    new_user = User(**user_data)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    access_token, refresh_token = create_tokens(user.username)
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }

def signin(username: str, password: str, db: Session):
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.password):
        return {"message": "Invalid username or password"}

    access_token, refresh_token = create_tokens(user.username)
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }
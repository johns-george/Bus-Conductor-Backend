from sqlalchemy.orm import Session
from src.models.user import User
from src.schemas.signup import SignUpRequest
from src.utility import hash_password, verify_password
from src.utility.auth_utility import create_access_token, decode_access_token

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
    return {"message": "Sign-up successful"}

def signin(username: str, password: str, db: Session):
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.password):
        return {"message": "Invalid username or password"}

    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.schemas.signup import SignUpRequest
from src.services import auth_service
from src.database import get_db
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import HTTPException
from src.utility.auth_utility import create_access_token, decode_access_token

router=APIRouter(prefix="/auth")

@router.post("/google-login")
def google_login(token: str, db: Session = Depends(get_db)):
    return auth_service.google_login(token, db)

@router.post("/sign-in")
def sign_in(form_data: OAuth2PasswordRequestForm = Depends(),db: Session = Depends(get_db)):
    return auth_service.signin(form_data.username, form_data.password, db)
   

@router.post("/sign-up")
def sign_up(sign_up_request: SignUpRequest,db: Session = Depends(get_db)):
    return auth_service.signup(sign_up_request, db)


@router.post("/refresh")
def refresh_token(refresh_token: str):
    payload = decode_access_token(refresh_token)

    if not payload or payload.get("type") != "refresh":
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    username = payload.get("sub")

    new_access_token = create_access_token({"sub": username})

    return {"access_token": new_access_token}
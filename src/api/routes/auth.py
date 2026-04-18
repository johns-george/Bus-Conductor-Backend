from fastapi import APIRouter
from src.schemas.signup import SignUpRequest
from src.services import auth_service

router=APIRouter(prefix="/auth")

@router.post("/sign-in")
def sign_in(username: str, password: str):
    auth_service.signin(username, password)
    return {"message": "Sign-in successful"}

@router.post("/sign-up")
def sign_up(sign_up_request: SignUpRequest):
    auth_service.signup(sign_up_request)
    return {"message": "Sign-up successful"}
from fastapi import APIRouter, status
from ..schemas.authentication import LoginIn
from ..security import sign_jwt
from ..views.authentication import LoginOut

router = APIRouter(prefix="/authentication")


@router.post("/login", status_code=status.HTTP_202_ACCEPTED, response_model=LoginOut)
async def login(input: LoginIn):
    return sign_jwt(user_id=input.user_id)

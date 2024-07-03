from datetime import timedelta, datetime
from typing import Annotated 
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status
from app.database import SessionLocal
from app.models import Users
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
# from fastapi.security import Auth2PasswordRequestForm, Auth2PasswordBearer
from jose import jwt, JWTError
from pydantic import BaseModel
from sqlalchemy.orm import Session
  # Assuming you have a schema for user creation


router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

SECRET_KEY='e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
ALGORITHM='HS256'

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')
# oauth2_bearer = Auth2PasswordRequestBearer(tokenUrl='auth/token')



class CreateUserRequest(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token :str
    token_type : str


def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(db:db_dependency,
                        create_user_request:CreateUserRequest):
    create_user_model= Users(
        username=create_user_request.username,
        password=bcrypt_context.hash(create_user_request.password),
    )
    db.add(create_user_model)
    db.commit()
    db.refresh(create_user_model)  # Optional: Refresh the model to get updated values
    return {'message': 'User created successfully'} 

# @router.post("/", status_code=status.HTTP_201_CREATED)
# async def create_user(create_user_request: CreateUserRequest, db: Session = Depends(get_db)):
#     hashed_password = bcrypt_context.hash(create_user_request.password)
#     new_user = Users(username=create_user_request.username, hashed_password=hashed_password)
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return {'message': 'User created successfully'}

   






    # return{"message": "User created successfully"}

@router.post("/token", response_model=Token)
async def login_for_access_token(from_data: Annotated[OAuth2PasswordRequestForm, Depends()],
                                db: db_dependency):
    user = authenticate_user(from_data.username, from_data.password,db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                              detail='Could not validate user.')
    token= create_access_token(user.username, user.id, timedelta(minutes=20))

    return {'access_token': token, 'token_type':'bearer'}





def authenticate_user(username: str, password: str, db):
    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.password):
        return False
    return user

def create_access_token(username:str,user_id: int, expires_delta: timedelta):
    encode = {'sub': username, 'id':user_id}
    expires = datetime.utcnow() + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)



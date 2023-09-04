from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
router = APIRouter()

oauth2 = OAuth2PasswordBearer(tokenUrl ="login")

class User(BaseModel):
    username : str
    full_name:str
    email : str
    disabled : bool

class UserDB(User):
    password:str


users_db = {
    "manupe" : {
        "username" : "manupe",
        "full_name" : "manuel pena",
        "email" : "pena@gmail.com",
        "disabled" : False,
        "password" : "123456",
    }
}

def search_user_db(username:str):
    if username in users_db:
        return UserDB(**users_db[username])

def search_user(username:str):
    if username in users_db:
        return User(**users_db[username])



async def current_user(token:str = Depends(oauth2)):
    user = search_user(token)
    if not user :
        raise HTTPException(404,"Incorrecto", headers={"WWW-Autenticate":"Bearer"})
    if user.disabled:
        raise HTTPException(404,"usuario inactivo")
    
    return user

@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=400, detail="usuario incorrecto")
    
    user = search_user_db(form.username)
    if not form.password == user.password:
        raise HTTPException(status_code=400, detail="contraseña incorrecta")

    return{"access_token": user.username , "token_type":"bearer"}

    
@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user 



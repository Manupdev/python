from fastapi import APIRouter ,Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta

router = APIRouter()


ALGORITHM = "H5256"
ACCESS_TOKEN_DURATION = 1
SECRET = "201d573bd7d1344d3a3bfce1550b69102fd11be3db6d379508b6cccc58ea230b"

oauth2 = OAuth2PasswordBearer(tokenUrl="login")


crypt = CryptContext(schemes=["bcrypt"])


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
        "password" : "$2a$12$lVCuJ3AKmtFTKDASzxOFE.6SGc4CS1sjnQ1lT8E1iQItXV6ffkese",
    }
}


def search_user_db(username:str):
    if username in users_db:
        return UserDB(**users_db[username])


def search_user(username:str):
    if username in users_db:
        return User(**users_db[username])



async def auth_user(token:str = Depends(oauth2)):
    
    exception =HTTPException(
        status_code=401,
        detail="Credenciales de autenticación inválidas",
        headers={"WWW-Authenticate": "Bearer"})


    try:
        

        username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
        if username is None:
            raise exception
        

    except JWTError:
        raise exception
    
    return search_user(username)



async def current_user(user:User = Depends(oauth2)):
    
    if user.disabled:
        raise HTTPException(404,"usuario inactivo")
    
    return user


@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=400, detail="usuario incorrecto")
    
    user = search_user_db(form.username)

    if not crypt.verify(form.password, user.password):
        raise HTTPException(404,"contraseña incorrecta")
    
    access_token = {"sub" : user.username,
                    "exp":datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)}

    return{"access_token": jwt.encode(access_token, SECRET,algorithm=ALGORITHM) , "token_type":"bearer"}


@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user 

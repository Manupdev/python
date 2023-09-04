from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from db.models.user import User
from db.client import db_client
from db.schemas.user import user_schema, users_schema

router = APIRouter(prefix="/userdb",tags=["userdb"],responses=(404,"no encontrado"))


#Entidad json
class User(BaseModel):
    id : int
    name : str
    apellido : str

users_list = []





@router.get ("/", response_model=list(User))

async def users():
    return users_schema(db_client.local.users.find())


@router.get ("/{id}")
async def user(id:int):
    users = filter(lambda user : user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return "Error"
    


@router.get ("/")
async def user(id:int):
    users = filter(lambda user : user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return "Error"
    


@router.post("/",status_code=201, response_model=User)
async def user(user : User):
    if type(search_user_by_name(user.email)) == User:
        raise HTTPException(204,"ya existe")
    user_dict = dict(user)    
    del user_dict["id"]

    id = db_client.local.users.insert_one(user_dict).inserted_id
    
    new_user = user_schema (db_client.local.users.find_one({"_id":id}))

    return User(**new_user) 

    
def search_user_by_name(field:str, key:str):
    users = filter(lambda user:user.id == id, users_list)
    try:
        user = db_client.local.users.find_one({field:key})
        return User(**user_schema(user))
    except:
        return ("error")

#put cambio de usuario entero
#patch, cambio de alguna parte del usuario

@router.put("/")
async def user(user: User):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
            return user
    if not found:
        return ( "no se actualizo")
    


@router.delete("/{id}")
async def user(id:int):
    found = False
    for index, delete_user in enumerate(users_list):
        if delete_user.id == id:
            del users_list[index]
            found=True

    if not found:
        return "No se elimino"
from fastapi import FastAPI
from routers import products, basic_auth_users, jwt_auth_users,users_db
from fastapi.staticfiles import StaticFiles
app = FastAPI()

#routers
app.include_router(products.router)
app.include_router(users_db.router)
app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)


app.mount("/static", StaticFiles(directory="static"),name="static")

@app.get("/")
async def root():
    
    return "hola fastapi"

@app.get("/url")
async def url():
    return("url_curso: ")

#inicia el server: uvicorn main:app --reload


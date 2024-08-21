from fastapi import FastAPI, status, Depends, HTTPException
import uvicorn
from app import models
from app.database import engine, SessionLocal
from typing import Annotated,Optional
from sqlalchemy.orm import Session
from app.auth import db_dependency, router
from app import book,cart,order
from fastapi.middleware.cors import CORSMiddleware
import bcrypt




app = FastAPI()
# app.include_router(auth.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this as needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



models.Base.metadata.create_all(bind=engine)
app.include_router(router)
app.include_router(book.router)
app.include_router(cart.router)
app.include_router(order.router)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", status_code=status.HTTP_200_OK)
async def read_root(user: Optional[str] = None, db: Session = Depends(get_db)):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed")
       
    print(bcrypt.__version__)

    return {"User": user}
    
if __name__ == "__main__":
    #   uvicorn.run(app)
     uvicorn.run(app,host="0.0.0.0",port=5450)























#.....................................................................................
# testing code
 


# from fastapi import FastAPI
# from typing import Optional
# from pydantic import BaseModel
# import uvicorn

# # from routes.index import user
# # from models.index import metadata # Import metadata, not users
# # from database import engine, Base, SessionLocal

# class PackageIn(BaseModel):
#     name : str
#     number: str
#     describtion: Optional[str]=None


# class Package(BaseModel):
#     name : str
#     number: str
#     describtion: Optional[str]=None

# app= FastAPI()

# @app.get('/')
# async def hello_world():
#     return {'Hello' : 'World'}


# @app.post("/package/", response_model=Package)
# async def make_package(package: Package):
#     return package

# @app.post("/package/{priority}")
# async def make_package(priority:int,package: Package, value: bool):
#         return {"priority":priority, **package.dict(), "value":value}

#......................................................................................

#old codes

# from fastapi.middleware.cors import CORSMiddleware
# from fastapi import HTTPException

# app = FastAPI()
# CORS (Cross-Origin Resource Sharing) middleware if needed
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


# app.include_router(user, prefix="/user", tags=["user"])

# from models.user import users

# @app.on_event("startup")
# def startup():
#     Base.metadata.create_all(bind=engine)
# Check database connection on startup

# @app.on_event("startup")
# def startup_event():
#     print("Application starting up...")

# @app.on_event("shutdown")
# def shutdown_event():
#     print("Application shutting down...")

# @app.get("/")
# async def root():
#      return {"message": "Hello World"}

# @app.get("/favicon.ico")
# async def get_favicon():
#     raise HTTPException(status_code=404)

# metadata.create_all(bind=engine)  # Create tables before running the app

# if __name__ == "__main__":
#      uvicorn.run(app)
    #  metadata.create_all(bind=engine)
    #   uvicorn.run(app,host="0.0.0.0",port=8080)

    
    
    
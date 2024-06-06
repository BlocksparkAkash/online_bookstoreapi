from fastapi import APIRouter, HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select
from database import conn
from models.user import users
from models.book import books
from models.cart import cart
from models.order import order
from schemas.index import User
from typing import List
user = APIRouter()

# @user.get("/",response_model=List[User])
# async def read_data():
#     try:
#         result = conn.execute(select([users])).fetchall()
#         return [User.from_orm(row) for row in result]
#     except SQLAlchemyError as e:
#         raise HTTPException(status_code=500, detail=str(e))

    # try:
    #     result = conn.execute(users.select()).fetchall()
    #     return result
    # except SQLAlchemyError as e:
    #     raise HTTPException(status_code=500, detail=str(e))


    #new code :

@user.get("/", response_model=List[User])
async def read_data():
    try:
        query = select(users)
        result = conn.execute(query).fetchall()
        return [User.from_orm(row) for row in result]
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

@user.get("/{id}", response_model=User)
async def read_data(id: int):
    try:
        query = select(users).where(users.c.id == id)
        result = conn.execute(query).fetchone()
        if not result:
            raise HTTPException(status_code=404, detail="User not found")
        return User.from_orm(result)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

# @user.get("/{id}")
# async def read_data(id: int):
#     try:
#         result = conn.execute(users.select().where(users.c.id == id)).fetchall()
#         if not result:
#             raise HTTPException(status_code=404, detail="User not found")
#         return result
#     except SQLAlchemyError as e:
#         raise HTTPException(status_code=500, detail=str(e))

@user.post("/register")
async def write_data(user: User):
    try:
        conn.execute(users.insert().values(
            name=user.name,
            email=user.email,
            password=user.password
        ))
        return conn.execute(users.select()).fetchall()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

@user.put("/{id}")
async def update_data(id: int, user: User):
    try:
        result = conn.execute(users.update().values(
            name=user.name,
            email=user.email,
            password=user.password
        ).where(users.c.id == id))
        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail="User not found")
        return conn.execute(users.select()).fetchall()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

@user.delete("/{id}")
async def delete_data(id: int):
    try:
        result = conn.execute(users.delete().where(users.c.id == id))
        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail="User not found")
        return conn.execute(users.select()).fetchall()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

# from fastapi import APIRouter,Depends, HTTPException
# from sqlalchemy.exc import SQLAlchemyError
# from sqlalchemy.orm import Session
# from sqlalchemy import select
# from database import SessionLocal, engine
# from models.user import users
# from models.book import books
# from models.cart import cart
# from models.order import order
# from schemas.index import User
# from typing import List

# user = APIRouter()

#   # Import the SQLAlchemy model
# router = APIRouter()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# @user.post("/user/register")
# def register_user(username: str, db: Session = Depends(get_db)):
#     # Example endpoint for registering a user
#     new_user = User(username=username)
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# @user.get("/", response_model=List[User])
# async def read_users():
#     try:
#         query = select(users)
#         result = SessionLocal().execute(query).fetchall()
#         return [User.from_orm(row) for row in result]
#     except SQLAlchemyError as e:
#         raise HTTPException(status_code=500, detail=str(e))

# @user.get("/{id}", response_model=User)
# async def read_user(id: int):
#     try:
#         query = select(users).where(users.c.id == id)
#         result = SessionLocal().execute(query).fetchone()
#         if not result:
#             raise HTTPException(status_code=404, detail="User not found")
#         return User.from_orm(result)
#     except SQLAlchemyError as e:
#         raise HTTPException(status_code=500, detail=str(e))





#11111111111111111111111111111111111111111111111111111111111111
# @user.post("/register")
# async def register():
#      return {"message": "Hello World"}

# # @user.post("/register", response_model=User)
# # async def register_user(user: User):
# #     try:
# #         query = select(users).where(users.c.username == user.username)
# #         existing_user = SessionLocal().execute(query).fetchone()
# #         if existing_user:
# #             raise HTTPException(status_code=400, detail="Username already registered")

# #         # Insert new user into database
# #         query = users.insert().values(
# #             username=user.username,
# #             password=user.password  # Ensure to hash the password before inserting in production
# #         )
# #         SessionLocal().execute(query)
# #         return user

# #     except SQLAlchemyError as e:
# #         raise HTTPException(status_code=500, detail=str(e))



# #11111111111111111111111111111111111111111111111111111111111












# # Additional routes for update and delete if needed



# # @user.get("/",response_model=List[User])
# # async def read_data():
# #     try:
# #         result = conn.execute(select([users])).fetchall()
# #         return [User.from_orm(row) for row in result]
# #     except SQLAlchemyError as e:
# #         raise HTTPException(status_code=500, detail=str(e))

# #     try:
# #         result = conn.execute(users.select()).fetchall()
# #         return result
# #     except SQLAlchemyError as e:
# #         raise HTTPException(status_code=500, detail=str(e))


# # #     #new code :

# # # @user.get("/", response_model=List[User])
# # # async def read_data():
# # #     try:
# # #         query = select(users)
# # #         result = conn.execute(query).fetchall()
# # #         return [User.from_orm(row) for row in result]
# # #     except SQLAlchemyError as e:
# # #         raise HTTPException(status_code=500, detail=str(e))

# # @user.get("/{id}", response_model=User)
# # async def read_data(id: int):
# #     try:
# #         query = select(users).where(users.c.id == id)
# #         result = conn.execute(query).fetchone()
# #         if not result:
# #             raise HTTPException(status_code=404, detail="User not found")
# #         return User.from_orm(result)
# #     except SQLAlchemyError as e:
# #         raise HTTPException(status_code=500, detail=str(e))

# # @user.get("/{id}")
# # async def read_data(id: int):
# #     try:
# #         result = conn.execute(users.select().where(users.c.id == id)).fetchall()
# #         if not result:
# #             raise HTTPException(status_code=404, detail="User not found")
# #         return result
# #     except SQLAlchemyError as e:
# #         raise HTTPException(status_code=500, detail=str(e))

# # @user.post("/register")
# # async def write_data(user: User):
# #     try:
# #         conn.execute(users.insert().values(
# #             name=user.name,
# #             email=user.email,
# #             password=user.password
# #         ))
# #         return conn.execute(users.select()).fetchall()
# #     except SQLAlchemyError as e:
# #         raise HTTPException(status_code=500, detail=str(e))

# # @user.put("/{id}")
# # async def update_data(id: int, user: User):
# #     try:
# #         result = conn.execute(users.update().values(
# #             name=user.name,
# #             email=user.email,
# #             password=user.password
# #         ).where(users.c.id == id))
# #         if result.rowcount == 0:
# #             raise HTTPException(status_code=404, detail="User not found")
# #         return conn.execute(users.select()).fetchall()
# #     except SQLAlchemyError as e:
# #         raise HTTPException(status_code=500, detail=str(e))

# # @user.delete("/{id}")
# # async def delete_data(id: int):
# #     try:
# #         result = conn.execute(users.delete().where(users.c.id == id))
# #         if result.rowcount == 0:
# #             raise HTTPException(status_code=404, detail="User not found")
# #         return conn.execute(users.select()).fetchall()
# #     except SQLAlchemyError as e:
# #         raise HTTPException(status_code=500, detail=str(e))


# # #new codes 

# # # routes/user.py
# # from fastapi import APIRouter, HTTPException
# # from sqlalchemy.exc import SQLAlchemyError
# # from sqlalchemy import select
# # from database import conn
# # from models.user import users
# # from schemas.user import UserCreate  # Import UserCreate from schemas.user

# # user = APIRouter()


# # # @user.post("/register", response_model=UserCreate)
# # # async def register_user(user: UserCreate):
# # #     try:
# # #         # Check if the username already exists
# # #         query = select(users).where(users.c.username == user.username)
# # #         existing_user = await conn.execute(query)
# # #         print(existing_user)
# # #         if existing_user.fetchone():
# # #             raise HTTPException(status_code=400, detail="Username already registered")

# # #         # Insert new user into database
# # #         query = users.insert().values(
# # #             username=user.username,
# # #             password=user.password  # Ensure to hash the password before inserting in production
# # #         )
# # #         await conn.execute(query)

# # #         return user

# # #     except SQLAlchemyError as e:
# # #         raise HTTPException(status_code=500, detail=str(e))


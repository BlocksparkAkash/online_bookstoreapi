from fastapi import FastAPI
# from fastapi import HTTPException
import uvicorn
from routes.index import user
from models.index import metadata # Import metadata, not users
from database import engine  # Import the engine object

app = FastAPI()

app.include_router(user)
# from models.user import users

@app.get("/")
async def root():
     return {"message": "Hello World"}

# @app.get("/favicon.ico")
# async def get_favicon():
#     raise HTTPException(status_code=404)

metadata.create_all(bind=engine)  # Create tables before running the app

if __name__ == "__main__":
    uvicorn.run(app)
    # metadata.create_all(bind=engine)
    #uvicorn.run(app,host="0.0.0.0",port=8080)
    
    
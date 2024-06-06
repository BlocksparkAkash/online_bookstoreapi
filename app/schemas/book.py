from pydantic import BaseModel

class BookSchema(BaseModel):
    title: str
    author: str
    price: float
    quantity_available: int

    class Config:
        orm_mode = True
        from_attributes = True 

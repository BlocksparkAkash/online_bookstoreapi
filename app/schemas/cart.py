from pydantic import BaseModel

class CartItemSchema(BaseModel):
    book_id: int
    quantity: int

    class Config:
        orm_mode = True
        from_attributes = True 

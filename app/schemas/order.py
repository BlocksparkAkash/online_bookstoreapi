from pydantic import BaseModel


class OrderSchema(BaseModel):
    user_id: int
    total_price: float
    status: str

    class Config:
        orm_mode = True
        from_attributes = True 

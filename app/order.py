from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime,JSON
from datetime import datetime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from typing import List,Union
from starlette import status
from app.auth import oauth2_bearer, get_current_user
from app.models import Users


class Orders(Base):
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    total_price = Column(Float, nullable=False)
    status = Column(String, default='pending')
    created_at = Column(DateTime, default=datetime.utcnow)
    

    user = relationship('Users', back_populates='orders')


router = APIRouter(
    prefix='/orders',
    tags=['orders']
)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class OrderItemCreate(BaseModel):
    book_id: int
    quantity: int

class OrderCreateRequest(BaseModel):
    total_price: float
    items: List[OrderItemCreate]

class OrderItem(BaseModel):
    id: int
    user_id: int
    total_price: float
    status: str
    created_at: datetime
    

    class Config:
        orm_mode = True

class OrderResponse(BaseModel):
    items: List[OrderItem]
    message: Union[str, None] = None

    class Config:
        orm_mode = True


# API endpoints
@router.get("/", response_model=OrderResponse)
def get_orders(db: Session = Depends(get_db), current_user: Users = Depends(get_current_user)):
    orders = db.query(Orders).filter(Orders.user_id == current_user.id).all()
    if not orders:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No orders found")
    
    order_items_pydantic = [
        OrderItem(
            id=order.id,
            user_id=order.user_id,
            total_price=order.total_price,
            status=order.status,
            created_at=order.created_at
        ) for order in orders
    ]
    
    return OrderResponse(items=order_items_pydantic)

@router.post("/", response_model=OrderResponse)
def create_order(
    request: OrderCreateRequest,
    db: Session = Depends(get_db),
    current_user: Users = Depends(get_current_user)
):
    new_order = Orders(
        user_id=current_user.id,
        total_price=request.total_price,
        status='pending',
        created_at=datetime.utcnow()
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    
    order_item = OrderItem(
        id=new_order.id,
        user_id=new_order.user_id,
        total_price=new_order.total_price,
        status=new_order.status,
        created_at=new_order.created_at,
    )
    
    return OrderResponse(items=[order_item], message="Order placed successfully")
    
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from pydantic import BaseModel
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import List,Union
from starlette import status
from app.auth import oauth2_bearer, get_current_user
from app.models import Users 




class Cart(Base):
    __tablename__ = 'cart'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    book_id = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

router = APIRouter(
    prefix='/cart',
    tags=['cart']
)

# Dependency to get DB session
def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()

class CartItem(BaseModel):
    id: int
    user_id: int
    book_id: int
    quantity: int
    created_at: datetime

    class Config:
        orm_mode = True


class CartResponse(BaseModel):
    items: List[CartItem]
    message: Union[str, None] = None

    class Config:
        orm_mode = True

#test code 

@router.get("/", response_model=CartResponse)
def get_cart(db: Session = Depends(get_db), current_user: Users = Depends(get_current_user)):
    cart_items = db.query(Cart).filter(Cart.user_id == current_user.id).all()
    if not cart_items:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cart is empty")

    # Convert database models to Pydantic models
    cart_items_pydantic: List[CartItem] = [
        CartItem(
            id=item.id,
            user_id=item.user_id,
            book_id=item.book_id,
            quantity=item.quantity,
            created_at=item.created_at
        ) for item in cart_items
    ]
    
    return CartResponse(items=cart_items_pydantic)

class CartAddRequest(BaseModel):
    book_id: int
    quantity: int

@router.post("/", response_model=CartItem)
def add_to_cart(request: CartAddRequest, db: Session = Depends(get_db), current_user: Users = Depends(get_current_user)):
    cart_item = db.query(Cart).filter(Cart.user_id == current_user.id, Cart.book_id == request.book_id).first()
    if cart_item:
        cart_item.quantity += request.quantity
        db.commit()
        db.refresh(cart_item)
    else:
        new_cart_item = Cart(
            user_id=current_user.id,
            book_id=request.book_id,
            quantity=request.quantity,
            created_at=datetime.utcnow()
        )
        db.add(new_cart_item)
        db.commit()
        db.refresh(new_cart_item)
        cart_item = new_cart_item
    return cart_item

class CartUpdateRequest(BaseModel):
    book_id: int
    quantity: int

@router.put("/update", response_model=CartItem)
def update_cart_item(request: CartUpdateRequest, db: Session = Depends(get_db), current_user: Users = Depends(get_current_user)):
    cart_item = db.query(Cart).filter(Cart.user_id == current_user.id, Cart.book_id == request.book_id).first()
    if not cart_item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found in the cart")

    cart_item.quantity = request.quantity
    db.commit()
    db.refresh(cart_item)
    return cart_item
    
@router.delete("/remove/{book_id}", response_model=CartResponse)
def remove_cart_item(book_id: int, db: Session = Depends(get_db), current_user: Users = Depends(get_current_user)):
    cart_item = db.query(Cart).filter(Cart.user_id == current_user.id, Cart.book_id == book_id).first()
    if not cart_item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found in the cart")

    db.delete(cart_item)
    db.commit()
    return {"detail": "Item removed from the cart"}
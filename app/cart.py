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
from app.book import DBBook




class Cart(Base):
    __tablename__ = 'cart'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False,unique=True)
    book_id = Column(Integer, ForeignKey('books.id'),nullable=False, unique=True)
    quantity = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationship to the Book model
    book = relationship("DBBook", backref="cart_items")

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
    book_title: str
    author_name: str
    price: float
    created_at: datetime

    class Config:
        orm_mode = True


class CartResponse(BaseModel):
    items: List[CartItem]
    message: Union[str, None] = None

    class Config:
        orm_mode = True

#test code 

@router.get("/fetch", response_model=CartResponse)
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
            book_title=item.book.title,  # Access the title from the Book model
            author_name=item.book.author,  # Access the author name
            price=item.book.price,  # Access the price
            quantity=item.quantity,
            created_at=item.created_at
        ) for item in cart_items
    ]
    
    return CartResponse(items=cart_items_pydantic)

class CartAddRequest(BaseModel):
    book_id: int
    quantity: int
# Add book to the cart
class CartAddRequest(BaseModel):
    title: str
    quantity: int

@router.post("/addtocart", response_model=CartItem)
def add_to_cart(request: CartAddRequest, db: Session = Depends(get_db), current_user: Users = Depends(get_current_user)):
    book = db.query(DBBook).filter(DBBook.title == request.title).first()
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

    cart_item = db.query(Cart).filter(Cart.user_id == current_user.id, Cart.book_id == book.id).first()
    if cart_item:
        cart_item.quantity += request.quantity
        db.commit()
        db.refresh(cart_item)
    else:
        new_cart_item = Cart(
            user_id=current_user.id,
            book_id=book.id,
            quantity=request.quantity,
            created_at=datetime.utcnow()
        )
        db.add(new_cart_item)
        db.commit()
        db.refresh(new_cart_item)
        cart_item = new_cart_item

    # Convert to Pydantic model for response
    cart_item_pydantic = CartItem(
        id=cart_item.id,
        user_id=cart_item.user_id,
        book_id=cart_item.book_id,
        book_title=cart_item.book.title,
        author_name=cart_item.book.author,
        price=cart_item.book.price,
        quantity=cart_item.quantity,
        created_at=cart_item.created_at
    )
    
    return cart_item_pydantic


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
    # details = "Item removed from the cart"
    return {"detail": "Item removed from the cart"}
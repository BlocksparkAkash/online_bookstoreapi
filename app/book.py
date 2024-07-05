from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal, Base
from sqlalchemy import Column, Integer, String, Float
from pydantic import BaseModel
from typing import List

router = APIRouter(
    prefix='/book',
    tags=['book']
)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Book(BaseModel):
    title: str
    author: str
    price: float
    quantity_available: int

class BookResponse(BaseModel):
    message: str
    book: Book

# Pydantic model for request body (POST)
class BookCreate(BaseModel):
    title: str
    author: str
    price: float
    quantity_available: int


class BookUpdate(BaseModel):
    title: str
    author: str
    price: float
    quantity_available: int

# SQLAlchemy model for database representation
class DBBook(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    quantity_available = Column(Integer, nullable=False)

# POST endpoint to create a new book
@router.post("/", response_model=BookCreate)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    db_book = DBBook(
        title=book.title,
        author=book.author,
        price=book.price,
        quantity_available=book.quantity_available
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

# GET endpoint to retrieve all books (example)
@router.get("/books", response_model=List[str])
def get_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Retrieve a list of book titles from the bookstore.

    Parameters:
    - skip (int): Number of records to skip (default: 0).
    - limit (int): Maximum number of records to return (default: 10).

    Returns:
    - List[str]: List of book titles retrieved from the database.
    """
    books = db.query(DBBook.title).offset(skip).limit(limit).all()
    return [title for (title,) in books]

# Additional CRUD endpoints can be added similarly (GET by ID, PUT, DELETE)

@router.get("/{book_id}", response_model=BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    """
    Retrieve details of a specific book.

    Parameters:
    - book_id (int): ID of the book to retrieve.

    Returns:
    - BookCreate: Details of the specific book retrieved from the database.
    """
    book = db.query(DBBook).filter(DBBook.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    # return book
    response = {
        "message": "Book retrieved successfully",
        "book": {
            "title": book.title,
            "author": book.author,
            "price": book.price,
            "quantity_available": book.quantity_available
        }
    }
    return response



@router.put("/books/{book_id}", response_model=BookResponse)
def update_book(book_id: int, book_update: BookUpdate, db: Session = Depends(get_db)):
    """
    Update details of a specific book.

    Parameters:
    - book_id (int): ID of the book to update.
    - book_update (BookUpdate): Updated details of the book.

    Returns:
    - BookResponse: Details of the updated book.
    """
    book = db.query(DBBook).filter(DBBook.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    # Update the book details
    book.title = book_update.title
    book.author = book_update.author
    book.price = book_update.price
    book.quantity_available = book_update.quantity_available

    db.commit()
    db.refresh(book)

    response = {
        "message": "Book updated successfully",
        "book": {
            "title": book.title,
            "author": book.author,
            "price": book.price,
            "quantity_available": book.quantity_available
        }
    }
    return response






# DELETE endpoint to delete a specific book
@router.delete("/{book_id}", response_model=BookResponse)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    """
    Delete a specific book.

    Parameters:
    - book_id (int): ID of the book to delete.

    Returns:
    - BookResponse: Confirmation message with details of the deleted book.
    """
    book = db.query(DBBook).filter(DBBook.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    db.delete(book)
    db.commit()

    response = {
        "message": "Book deleted successfully",
        "book": {
            "title": book.title,
            "author": book.author,
            "price": book.price,
            "quantity_available": book.quantity_available
        }
    }
    return response
from sqlalchemy import Table, Column, Integer, String, Float, DateTime
from .index import metadata

books = Table(
    'books',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String(255)),
    Column('author', String(255)),
    Column('price', Float),
    Column('quantity_available', Integer),
    Column('created_at', DateTime)
)

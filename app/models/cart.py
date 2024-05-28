from sqlalchemy import Table, Column, Integer, ForeignKey, DateTime
from .index import metadata

cart = Table(
    'cart',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('book_id', Integer, ForeignKey('books.id')),
    Column('quantity', Integer),
    Column('created_at', DateTime)
)

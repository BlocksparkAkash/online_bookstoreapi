from sqlalchemy import Table, Column, Integer, ForeignKey, DateTime, Float, String
from .index import metadata

order = Table(
    'order',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('total_price', Float),
    Column('status', String(50)),
    Column('created_at', DateTime)
)

from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String,DateTime
from .index import metadata  # Relative import

# Define the 'users' table here

users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('username', String(50), unique=True),
    Column('email', String(100), unique=True),
    Column('password', String(100)),
    Column('created_at', DateTime)
)

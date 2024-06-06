from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# from sqlalchemy.exc import OperationalError

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:1234@localhost:3306/online_bookstore"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
meta = MetaData() 
conn = engine.connect()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()



# insert_query = """
# INSERT INTO users (name, email, password)
# VALUES
# ('Alice', 'alice@example.com', 'hashed_password_1'),
# ('Bob', 'bob@example.com', 'hashed_password_2'),
# ('Charlie', 'charlie@example.com', 'hashed_password_3'),
# ('David', 'david@example.com', 'hashed_password_4'),
# ('Emma', 'emma@example.com', 'hashed_password_5');
# """

# # Execute the SQL query
# with engine.connect() as connection:
#     connection.execute(insert_query)

# print("Sample user data inserted into the 'users' table.")
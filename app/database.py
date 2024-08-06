from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base



SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:1234@192.168.0.108:3306/online_bookstore"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()



try:
    # Try to connect
    with engine.connect() as connection:
        print("Connection successful!")
        # Optionally, perform database operations here
except Exception as e:
    print(f"Connection failed: {e}")





# from sqlalchemy import create_engine, MetaData
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.sql import text

# from sqlalchemy.exc import OperationalError


# engine = create_engine(SQLALCHEMY_DATABASE_URL)
# meta = MetaData() 
# conn = engine.connect()

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

# engine = create_engine(SQLALCHEMY_DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()
# meta = MetaData()


# wsl --set-default-version 2
# wsl --set-version Ubuntu-22.04 2
# wsl -l -v




# def test_database_connection():
#     try:
#         db = SessionLocal()
#         db.execute(text("SELECT 1"))
#         print("Database connection successful!")
#     except Exception as e:
#         print(f"Database connection error: {str(e)}")
#     finally:
#         db.close()

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
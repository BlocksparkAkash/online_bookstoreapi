# Online Bookstore API

## Project Description
This project aims to develop an API for an online bookstore using FastAPI, SQLAlchemy, and MySQL. The API will facilitate user authentication, book management, cart operations, and order placement. 

## Features
1. **User Authentication:**
   - Users can register for an account with a username, email, and password.
   - Registered users can log in using their credentials to obtain a JWT token for authentication.
2. **Book Operations:**
   - CRUD operations for managing books in the database.
   - Each book has attributes such as title, author, price, and quantity available.
3. **Cart Management:**
   - Authenticated users can add books to their shopping cart.
   - Users can view their current cart contents, update it, and remove items.
4. **Order Placement:**
   - Authenticated users can place orders for items in their cart.
   - Upon placing an order, the inventory quantity of each book is updated accordingly.
   - Orders include details such as the user, books ordered, total price, and order status.

## Endpoints
1. `/register`: POST endpoint for user registration.
2. `/login`: POST endpoint for user login and token generation.
3. `/books`:
   - GET: Retrieve a list of all books.
   - POST: Add a new book to the bookstore.
4. `/books/<book_id>`:
   - GET: Retrieve details of a specific book.
   - PUT: Update details of a specific book.
   - DELETE: Delete a specific book.
5. `/cart`:
   - GET: Retrieve the current user's shopping cart contents.
   - POST: Add a book to the user's shopping cart.
   - PUT: Update the quantity of a book in the user's shopping cart.
   - DELETE: Remove a book from the user's shopping cart.
6. `/orders`:
   - GET: Retrieve a list of all orders placed by the user.
   - POST: Place a new order.

## Database Schema
1. **User Table:**
   - id (Primary Key): Unique identifier for the user.
   - username: Username chosen by the user (unique).
   - email: Email address of the user (unique).
   - password: Hashed password of the user.
   - created_at: Timestamp indicating when the user account was created.
2. **Book Table:**
   - id (Primary Key): Unique identifier for the book.
   - title: Title of the book.
   - author: Author of the book.
   - price: Price of the book.
   - quantity_available: Number of copies available in the inventory.
   - created_at: Timestamp indicating when the book entry was added.
3. **Cart Table:**
   - id (Primary Key): Unique identifier for the cart item.
   - user_id (Foreign Key): Identifier of the user who owns the cart item.
   - book_id (Foreign Key): Identifier of the book in the cart.
   - quantity: Quantity of the book in the cart.
   - created_at: Timestamp indicating when the cart item was added.
4. **Order Table:**
   - id (Primary Key): Unique identifier for the order.
   - user_id (Foreign Key): Identifier of the user who placed the order.
   - total_price: Total price of the order.
   - status: Status of the order (e.g., pending, completed).
   - created_at: Timestamp indicating when the order was placed.

## Project Deliverables
- Complete source code of the FastAPI with necessary files and configurations.
- Postman collection for testing the API endpoints.
- Thorough testing to ensure reliability and functionality.
- Code uploaded to a repository (e.g., GitHub) for version control and collaboration.

# WorkFlow 
- create virtual environment`python -m venv venv`
- activate virtual environment `.\venv\Scripts\activate`
- add dependecy (if you install some new) `pip freeze > requirements.txt`
- install dependencies `pip install -r requirements.txt`
- run server `python main.py`"# online_bookstoreapi" 

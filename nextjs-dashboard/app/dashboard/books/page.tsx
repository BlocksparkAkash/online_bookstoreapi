// import BookListPage from '../books/BookListPage'; // Correct import path

// // Hardcoded data
// const books = [
//   { title: 'Book 1', image: '/books/book1.jpg' },
//   { title: 'Book 2', image: '/books/book2.jpg' },
//   { title: 'Book 3', image: '/books/book3.jpg' },
// ];

// const BookPage = () => {
//   return <BookListPage books={books} />;
// };

// export default BookPage;
import React from 'react';
import BookListPage from '../books/BookListPage';

const BookPage = () => {
  return <BookListPage />;
};

export default BookPage;

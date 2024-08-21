"use client";

import { useState, useEffect } from 'react';
import axios from 'axios';
import styles from './booklist.module.css';

interface Book {
  title: string; // Changed to reflect the actual data structure
  image?: string; // Optional image field
}

const BookListPage = () => {
  const [books, setBooks] = useState<string[]>([]); // Update state to handle array of strings
  const [authToken, setAuthToken] = useState<string>('');

  useEffect(() => {
    const token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyMjUiLCJpZCI6MywiZXhwIjoyMjY0MjM0NTk4fQ.ekc6EA50dj6-5sdgbtCTe51mjLfk6zO45pa88krdIKw'; // Replace with your actual method of retrieving the token
    setAuthToken(token);

    const fetchBooks = async () => {
      try {
        const response = await axios.get('http://192.168.1.5:5450/book/books', {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });
        setBooks(response.data); // Expecting an array of book titles
      } catch (error) {
        console.error('Error fetching books:', error);
      }
    };

    fetchBooks();
  }, [authToken]);

  const handleAddToCart = async (bookTitle: string) => {
    try {
      const response = await axios.post('http://192.168.1.5:5450/cart/addtocart',
        {
          title: bookTitle,
          quantity: 1,
        },
        {
          headers: {
            Authorization: `Bearer ${authToken}`,
          },
        }
      );

      console.log(`Added book titled "${bookTitle}" to cart`, response.data);
    } catch (error) {
      if (axios.isAxiosError(error)) {
        console.error('Error adding to cart:', error.response?.data || error.message);
      } else {
        console.error('Unexpected error:', error);
      }
    }
  };

  return (
    <div className={styles.bookListContainer}>
      <h1>Book List</h1>
      
      <div className={styles.bookGrid}>
        {books.map((bookTitle, index) => (
          <div key={index} className={styles.bookBox}>
            <img 
              src='https://via.placeholder.com/150' // Placeholder URL
              alt={bookTitle}
              className={styles.bookImage} 
            />
            <div className={styles.bookTitle}>{bookTitle}</div>
            <button 
              className={styles.addToCartButton} 
              onClick={() => handleAddToCart(bookTitle)}
            >
              Add to Cart
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};

export default BookListPage;

// "use client";

// import { useState, useEffect } from 'react';
// import axios from 'axios';
// import styles from './booklist.module.css'; // Ensure the path is correct

// interface Book {
//   title: string;
//   image: string;
// }

// const BookListPage = () => {
//   const [books, setBooks] = useState<Book[]>([]);

//   // Fetch books from the API
//   useEffect(() => {
//     const fetchBooks = async () => {
//       try {
//         const response = await axios.get('http://192.168.1.8:5446/book/books');
//         setBooks(response.data); // Assuming the API returns an array of books
//         console.log(response.data)
//       } catch (error) {
//         console.error('Error fetching books:', error);
//       }
//     };

//     fetchBooks();
//   }, []);

//   // Function to handle "Add to Cart" button click
//   const handleAddToCart = async (bookTitle: string) => {
//     try {
//       const response = await axios.post('http://192.168.1.147:5446/cart/addtocart', {
//         title: bookTitle,
//         quantity: 1, // Example quantity
//       });

//       console.log(`Added ${bookTitle} to cart`, response.data);
//     } catch (error) {
//       console.error('Error adding to cart:', error);
//     }
//   };

//   return (
//     <div className={styles.bookListContainer}>
//       <h1>Book List</h1>
//       <div className={styles.bookGrid}>
//         {books.map((book, index) => (
//           <div key={index} className={styles.bookBox}>
//             <img src={book.image} alt={book.title} className={styles.bookImage} />
//             <div className={styles.bookTitle}>{book.title}</div>
//             <button 
//               className={styles.addToCartButton} 
//               onClick={() => handleAddToCart(book.title)}
//             >
//               Add to Cart
//             </button>
//           </div>
//         ))}
//       </div>
//     </div>
//   );
// };

// export default BookListPage;



// "use client"; // Indicates that this component should be rendered on the client-side

// import styles from './booklist.module.css'; // Ensure the path is correct

// interface BookListPageProps {
//   books: { title: string; image: string }[];
// }

// const BookListPage = ({ books }: BookListPageProps) => {
//   // Function to handle "Add to Cart" button click
//   const handleAddToCart = (bookTitle: string) => {
//     console.log(`Added ${bookTitle} to cart`);
//     // Implement cart logic here, e.g., call API or update state
//   };

//   return (
//     <div className={styles.bookListContainer}>
//       <h1>Book List</h1>
//       <div className={styles.bookGrid}>
//         {books.map((book, index) => (
//           <div key={index} className={styles.bookBox}>
//             <img src={book.image} alt={book.title} className={styles.bookImage} />
//             <div className={styles.bookTitle}>{book.title}</div>
            
//             <button 
//               className={styles.addToCartButton} 
//               onClick={() => handleAddToCart(book.title)}
//             >Add to Cart
//             </button>
            
//           </div>
//         ))}
//       </div>
//     </div>
//   );
// };

// export default BookListPage;

// //working code 

// // import styles from './booklist.module.css'; // Ensure the path is correct

// // interface BookListPageProps {
// //   books: string[];
// // }

// // const BookListPage = ({ books }: BookListPageProps) => {
// //   return (
// //     <div className={styles.bookListContainer}>
// //       <h1 className={styles.heading}>Book List</h1>
// //       <ul className={styles.list}>
// //         {books.map((book, index) => (
// //           <li key={index} className={styles.listItem}>
// //             {book}
// //           </li>
// //         ))}
// //       </ul>
// //     </div>
// //   );
// // };

// // export default BookListPage;

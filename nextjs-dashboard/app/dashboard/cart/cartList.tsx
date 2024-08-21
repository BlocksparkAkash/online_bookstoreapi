import React from 'react';
import styles from './cart.module.css';

interface CartItem {
  id: number;
  book_id: number;
  quantity: number;
  book_title: string;
  price: number;
}

interface CartListProps {
  cartItems: CartItem[];
}

const CartList: React.FC<CartListProps> = ({ cartItems }) => {
  const calculateTotal = () =>
    cartItems.reduce((acc, item) => acc + item.quantity * item.price, 0);

  return (
    <div className={styles.container}>
      <h2 className={styles.heading}>Your Cart</h2>
      {cartItems.length === 0 ? (
        <p className={styles.emptyMessage}>Your cart is empty.</p>
      ) : (
        <>
          <ul className={styles.cartList}>
            {cartItems.map((item) => (
              <li key={item.id} className={styles.cartItem}>
                <div className={styles.itemDetails}>
                  <span className={styles.bookTitle}>{item.book_title}</span>
                  
                  <span className={styles.bookPrice}>Bookprice : ${item.price.toFixed(2)}</span><br></br>
                  <span className={styles.bookQuantity}>Qty: {item.quantity}</span> 
                </div>
                <div className={styles.itemTotal}>
                  <span>Total: ${(item.quantity * item.price).toFixed(2)}</span>
                </div>
              </li>
            ))}
          </ul>
          <div className={styles.cartSummary}>
            <span className={styles.totalLabel}>Total Amount:</span>
            <span className={styles.totalAmount}>${calculateTotal().toFixed(2)}</span>
          </div>
        </>
      )}
    </div>
  );
};

export default CartList;

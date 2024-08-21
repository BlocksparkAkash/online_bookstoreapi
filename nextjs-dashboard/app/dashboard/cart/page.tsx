import React from 'react';
import axios from 'axios';
import CartList from '../cart/cartList';
// import AddToCartButton from '../cart/AddToCartButton';

interface CartItem {
  id: number;
  book_id: number;
  quantity: number;
}

const CartPage = async () => {
  let cartItems: CartItem[] = [];
  const token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyMjUiLCJpZCI6MywiZXhwIjoyMjYzNTU0NTQzfQ.3ZqNIgDMAeYCRJu0Un1NzHiUPXuWUJ2t4gppMcEZNsk'; // Replace with actual token or retrieve from context or local storage

  try {
    const response = await axios.get('http://192.168.1.5:5450/cart/fetch', {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    cartItems = response.data.items;
     console.log(cartItems)
  } catch (err) {
    console.error('Error fetching cart items:', err);
  }

  return (
    <div>
      <h1>Shopping Cart</h1>
      <CartList cartItems={cartItems} />
      {/* <AddToCartButton bookId={1} /> Replace 1 with the actual book ID */}
    </div>
  );
};

export default CartPage;

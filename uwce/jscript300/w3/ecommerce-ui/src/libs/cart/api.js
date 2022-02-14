const saveToLocalStorage = (cart) => {
  localStorage.setItem('cart', JSON.stringify(cart));
}

const getFromLocalStorage = () => {
  const emptyCart = { items: [] };
  const cart = JSON.parse(localStorage.getItem('cart'));
  return cart || emptyCart;
}

// saveToLocalStorage({
//   items: [
//     { productId: 'Centrally-located Manhattan studio', quantity: 3 },
//   ]
// });

// console.log('cart', getFromLocalStorage());

export const fetch = async () => getFromLocalStorage();

export const addToCart = async (productId, quantity = 1) => {
  const cart = await fetch();
  const exists = cart.items.findIndex(item => item.productId === productId) > -1;

  if(exists) {
    console.log('Item already exists');
  }

  const newItem = { productId, quantity };
  const newCart = {
    ...cart,
    items: [
      ...cart.items,
      newItem,
    ],
  };

  saveToLocalStorage(newCart);

  return newCart;
}

// addToCart('Denver apartment outside Union Station', 5);

// console.log('cart', getFromLocalStorage());
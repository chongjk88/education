import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import { Provider } from 'react-redux';
import App from './App';
import configureStore from './state/store';
import registerServiceWorker from './registerServiceWorker';
// import { addToCart } from './state/cart/actions';

// import './libs/cart/api';
// import * as productApi from './libs/product/api';
// import { fetchProducts } from './state/product/actions';

// productApi.fetchAll()
 // .then((products) => console.log('products', products));

// console.log(store.getState());
// store.dispatch(fetchProducts());

const store = configureStore({  });

// store.dispatch(addToCart('Quaint 3-bedroom home in Gamla stan', 6));

ReactDOM.render(
  <Provider store={store}>
    <App />
  </Provider>, 
  document.getElementById('root')
);

registerServiceWorker();

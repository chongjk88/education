import React, { Component } from 'react';
import { connect } from 'react-redux';
import { fetchProducts } from './state/product/actions';
import { fetchCart, addToCart } from './state/cart/actions';

import ProductGrid from './components/ProductGrid';
import CartTable from './components/CartTable';

import logo from './logo.svg';
import './App.css';

// import airbnbs from './data/airbnbs.json';
// import Data from './data/Data.js';

import 'font-awesome/css/font-awesome.min.css';

class App extends Component {
  componentWillMount() {
    this.props.fetchProducts();
    this.props.fetchCart();
  }

  addToCart = (product) => {
    this.props.addToCart(product.title, 1);
    // console.log('product', product);
  }

  render() {
    const {
      isProductsLoading,
      products,
      cart,
    } = this.props;

    if(isProductsLoading) {
      return <h2><i className="fa fa-spinner fa-spin"></i></h2>
    }

    // console.log('cart', cart)

    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to Airbnb</h1>
        </header>
        {/* {products.map(product => <h3>{product.title}</h3>)} */}
        <div>
          <h2><i className="fa fa-shopping-cart"></i> Shopping Cart:</h2>
          <CartTable
            cart={cart}
          />
        </div>
        <div className="listingWrapper">
          {/* {airbnbs.map((article, idx) => {
            return <Data key={idx} article={article} />;
          })} */}

          {/* <ProductGrid products={products} /> */}
          
          <ProductGrid
            products={products}
            addToCart={this.addToCart}
          />
        </div>
      </div>
    );
  }
}

const getProductById = (products, productId) => products.find(p => p.title === productId);

const populateCartItems = (cart, products) => ({
  ...cart,
  items: cart.items.map(item => ({
    ...item,
    product: getProductById(products, item.productId),
  }))
})

const mapStateToProps = (state) => ({
  isProductsLoading: state.product.isLoading,
  products: state.product.products,
  cart: populateCartItems(state.cart.cart, state.product.products),
});

const mapDispatchToProps = {
  fetchProducts,
  fetchCart,
  addToCart,
}

export default connect(mapStateToProps, mapDispatchToProps)(App);

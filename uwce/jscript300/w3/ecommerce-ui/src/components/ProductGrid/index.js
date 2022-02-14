import React from 'react';
import styled from 'styled-components';

import PropTypes from 'prop-types';
import '../../data/Data.css';

const Wrapper = styled.div``;

const ProductGrid = ({ products, addToCart }) => (
  <Wrapper>
    {products.map(product => (
      <div className="cardWrapper">
        <div className="houseImgWrapper">
          <img className="houseImg" src={product.image} alt="Card" />
          <p className="housePrice">Price: ${product.payment.cost}</p>
        </div>
        <div className="houseInfoWrapper">
          <h2>{product.title}</h2>
          <p>Type: {product.houseType}</p>
          <p>Location: {product.location.city}, {product.location.country}</p>
          
          <p>Cancellation: {product.payment.description !== "" && product.payment.description}{product.payment.description === "" && "n/a" }</p>
          <p>Host: {product.host.name} {product.host.isSuperhost === true && <i className="fa fa-star"></i> } | Score: {product.rating.stars}/5 | Reviews: {product.rating.reviews}</p>
          <div className="addCartButton">
            <button onClick={() => addToCart(product)}>Add to cart <i className="fa fa-cart-plus"></i></button> 
          </div>
        </div>
      </div>
    ))}
  </Wrapper>
);

ProductGrid.propTypes = {
  products: PropTypes.arrayOf(PropTypes.shape({
    image: PropTypes.string,
    houseType: PropTypes.string,
    title: PropTypes.string,
    city: PropTypes.string,
    country: PropTypes.string,
    cost: PropTypes.number,
    description: PropTypes.string,
    starts: PropTypes.string,
    numberofreviews: PropTypes.number,
    host: PropTypes.string,
    issuperhost: PropTypes.bool,
  })).isRequired,
  addToCart: PropTypes.func.isRequired,
};


export default ProductGrid;
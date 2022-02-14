import React, { Component } from 'react';
import './Data.css';
import PropTypes from 'prop-types';
import 'font-awesome/css/font-awesome.min.css';

class Data extends Component {
  render() {
    // console.log(this.props.article);
    const {
      title,
      houseType,
      image,
      location,
      payment,
      host,
      rating
    } = this.props.article;
    return (
      <div className="cardWrapper">
        <div className="houseImgWrapper">
          <img className="houseImg" src={image} alt="Card" />
          <p className="housePrice">Price: ${payment.cost}</p>
        </div>
        <div className="houseInfoWrapper">
          <h2>{title}</h2>
          <p>Type: {houseType}</p>
          <p>Location: {location.city}, {location.country}</p>
          
          <p>Cancellation: {payment.description !== "" && payment.description}{payment.description === "" && "n/a" }</p>
          <p>Host: {host.name} {host.isSuperhost === true && <i className="fa fa-star"></i> } | Score: {rating.stars}/5 | Reviews: {rating.reviews}</p>
          <div className="addCartButton">
            <button value={this.props.id} onClick={this.props.addRental}>Add to cart <i className="fa fa-cart-plus"></i></button> 
          </div>
        </div>
      </div>
    );
  }
}

Data.propTypes = {
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
  handleClick: PropTypes.func,
}

export default Data;
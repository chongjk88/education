import React, { Component } from 'react';
import './Card.css';
import Moment from '../node_modules/moment';
import FontAwesomeIcon from '@fortawesome/react-fontawesome';

class Card extends Component {
  render() {
    // console.log(this.props.article);
    const {
      title,
      description,
      image,
      link,
      author,
      postedDate,
      minutesToRead,
      hasAudioAvailable,
      memberPreview
    } = this.props.article;
    
    return (
      <div className="cardWrapper cardWrapper2">
      <a href={link}></a>
        <div className="cardImgWrapper cardImgWrapper2">
          <img className="cardImg cardImg2" src={image} alt="Card"  />
        </div>
        <div className="cardInfoWrapper cardInfoWrapper2">
          {hasAudioAvailable === true && <div className="cardIcon cardAudio"><FontAwesomeIcon icon={["fas", "volume-up"]}/> Audio available</div> }
          {memberPreview === true && hasAudioAvailable === false && <div className="cardIcon cardMember1"><FontAwesomeIcon icon={["fas", "star"]}/> Member preview</div> }
          {memberPreview === true && hasAudioAvailable === true && <div className="cardIcon cardMember2"><FontAwesomeIcon icon={["fas", "star"]}/></div> }
          <h2>{title}</h2>
          <p>{description}</p>
          <div className="cardAuthorWrapper cardAuthorWrapper2">
            {author.isMediumMember === true && <div className="isMember"></div> }
            <div className="cardAuthorImgWrapper cardAuthorImgWrapper2">
              <img className="cardAuthorImg cardAuthorImg2" src={author.image} alt="Card" />
            </div>
            <div className="cardAuthorNameWrapper cardAuthorNameWrapper2">
              <p className="cardAuthorName cardAuthorName2">{author.name}</p>
              <span className="cardAuthorDate cardAuthorDate2">{Moment(postedDate).format('MMM D')} · {minutesToRead} min read</span>
              <FontAwesomeIcon icon={["far", "bookmark"]} className="bookmark bookmark2"/>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default Card;
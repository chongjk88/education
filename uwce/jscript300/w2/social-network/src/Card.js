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
      <div className="cardWrapper">
        <a href={link}></a>
        <div className="cardImgWrapper">
          <img className="cardImg" src={image} alt="Card" />
        </div>
        <div className="cardInfoWrapper">
          {hasAudioAvailable === true && <div className="cardIcon cardAudio"><FontAwesomeIcon icon={["fas", "volume-up"]}/> Audio available</div> }
          {memberPreview === true && hasAudioAvailable === false && <div className="cardIcon cardMember1"><FontAwesomeIcon icon={["fas", "star"]}/> Member preview</div> }
          {memberPreview === true && hasAudioAvailable === true && <div className="cardIcon cardMember2"><FontAwesomeIcon icon={["fas", "star"]}/></div> }
          <h2>{title}</h2>
          <p>{description}</p>
          <div className="cardAuthorWrapper">
              {author.isMediumMember === true && <div className="isMember"></div> }
            <div className="cardAuthorImgWrapper">
              <img className="cardAuthorImg" src={author.image} alt="Card" />
            </div>
            <div className="cardAuthorNameWrapper">
              <p className="cardAuthorName">{author.name}</p>
              <span className="cardAuthorDate">{Moment(postedDate).format('MMM D')} · {minutesToRead} min read</span>
              <FontAwesomeIcon icon={["far", "bookmark"]} className="bookmark"/>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default Card;
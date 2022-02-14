import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Card from './Card';
import Card2 from './Card2';
import fontawesome from '@fortawesome/fontawesome'
import FontAwesomeIcon from '@fortawesome/react-fontawesome';
import { faBookmark } from '@fortawesome/fontawesome-free-regular';
import { faStar, faVolumeDown } from '@fortawesome/fontawesome-free-solid'

import yourArticles from './your-articles.json';
import missedArticles from './missed-articles.json';
console.log(yourArticles);

class App extends Component {
  render() {
    return (
      <div className="App">
        <div className="header header1">
          <h1>For You</h1>
        </div>
        {yourArticles.map((article, idx) => {
          return <Card key={idx} article={article} />;
        })}
        
        <div className="header header2">
          <h1>In case you missed it</h1>
        </div>
        {missedArticles.map((article, idx) => {
          return <Card2 key={idx} article={article} />;
        })}
      </div>
    );
  }
}

export default App;

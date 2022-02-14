import React, { Component } from 'react';
// import logo from './logo.svg';
import './App.css';
import logo from './Star_Wars_logo.png';

import { 
  BrowserRouter, Route, Link
} from 'react-router-dom';

const About = () => <p>This is a Star Wars film app</p>;

class FilmDetail extends Component {
  constructor(props) {
    super(props);
    this.state = {
      film: {}
    };
  }

  componentDidMount() {
    const filmId = this.props.match.params.filmId;
    fetch(`https://swapi.co/api/people/${filmId}/`)
      .then(response => response.json())
      .then(data => {
        console.log(data);
        console.log(filmId);
        this.setState((prevState, props) => {
          return { film: data };
        });
      });
    // make API call here and update state
  }

  render() {
    const { 
      name,
      height,
      hair_color,
      eye_color,
      gender
     } = this.state.film;
    // const title = this.state.film.title;
    // const opening_crawl = this.state.film.opening_crawl
    return (
      <div className="charDetailWrapper">
        <h2><b>Name:</b> {name}</h2>
        <p><b>Height:</b> {height}</p>
        <p><b>Hair color:</b> {hair_color}</p>
        <p><b>Eye color:</b> {eye_color}</p>
        <p><b>Gender:</b> {gender}</p>
        <Link to="/">Close</Link>
      </div>
    )
  }
}

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      films: []
    };
  }

  componentDidMount() {
    fetch('https://swapi.co/api/people')
      .then(response => response.json())
      .then(data => {
        this.setState((prevState, props) => {
          return {
            films: data.results
          };
        });
      })
      .catch(error => console.log(error));
    }
    
  render() {
    // console.log('state', this.state);
    return (
      <div className="App">
        <img src={logo} alt="logo" className="logo" />
        <div className="background">
          {this.state.films.map(film => 
            <div className="charWrapper">
              <p className="charName">{film.name}&nbsp;</p>
              <a className="charLink" href={`/people/${film.url.substring(28, 32)}`}>Link</a>
            </div>
          )}
        </div>
        <BrowserRouter>
          <div>
            <Route path="/about" component={About} />
            <Route path="/people/:filmId" component={FilmDetail} />
          </div>
        </BrowserRouter>
      </div>
    );
  }
}

export default App;
// import logo from './logo.svg';
import React from "react";
import {
  // BrowserRouter as Router,
  Route,
  Switch
} from 'react-router-dom';


import Header from './components/Header';
import Main from './components/Main';
import MoviesView from './components/MoviesView';
import ActorsView from './components/ActorsView';
import NewActor from './components/NewActor';
import NewMovie from './components/NewMovie';
import EditActor from './components/EditActor';
import EditMovie from './components/EditMovie';
import './App.css';


class App extends React.Component {
  render() {
    return (
      <div className="App">
        <div className="d-flex h-100 text-center text-white bg-dark body">
          <div className="cover-container d-flex w-100 h-100 flex-column">
            <Header/>
            <Switch>
              <Route exact path="/" component={Main} />
              <Route path="/movies" component={MoviesView} />
              <Route path="/actors" component={ActorsView} />
              <Route path="/add-actor" component={NewActor} />
              <Route path="/add-movie" component={NewMovie} />
              <Route path="/edit-actor/:id" component={EditActor} />
              <Route path="/edit-movie/:id" component={EditMovie} />
            </Switch>

          </div>
        </div>
      </div>
    );
  }
}

export default App;

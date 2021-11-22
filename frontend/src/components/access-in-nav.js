import React from "react";
import { Link } from 'react-router-dom';
import LogoutButton from "./logout-button";

class AccessInNav extends React.Component {
  render() {
    return (
      <div>
        <header className="bg-white">
          <Link to="/"><h3 className="float-md-start nav-link text-dark">Castr</h3></Link>
          <nav className="nav nav-masthead justify-content-center float-md-end">
            <Link to="/movies"><h4 className="nav-link text-dark fw-bold">Movies</h4></Link>
            <Link to="/actors"><h4 className="nav-link text-dark fw-bold">Actors</h4></Link>
            <LogoutButton />
          </nav>
        </header>
      </div>
    );
  }
}

export default AccessInNav;

import React from "react";
import LoginButton from "./login-button";
import SignupButton from "./signup-button";

class AccessOutNav extends React.Component {
  render() {
    return (
      <header>
        <h3 className="float-md-start nav-link">Castr</h3>
        <nav className="nav nav-masthead justify-content-center float-md-end">
          <SignupButton />
          <LoginButton />
        </nav>
      </header>
    );
  }
}

export default AccessOutNav

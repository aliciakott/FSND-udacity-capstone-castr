import React from "react";
import LoginButton from "./login-button";
import SignupButton from "./signup-button";

class AccessOutNav extends React.Component {
  render() {
    return (
      <header>
        <div className="mb-auto">
          <h3 className="float-md-start">Castr</h3>
          <nav className="nav nav-masthead justify-content-center float-md-end">
            <SignupButton />
            <LoginButton />
          </nav>
        </div>
      </header>
    );
  }
}

export default AccessOutNav

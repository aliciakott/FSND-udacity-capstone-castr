import React from "react";
import './Main.css';

class Main extends React.Component {
  render() {
    return(
      <div className="cover-container">
        <main className="row align-items-center px-5 m-0">
          <h6 className="my-auto">The purpose of this project is to demonstrate proficiency in a number of skills relating to full-stack web development.
          These include database ORM's, RESTful API's, authorization, and deployment of apps.
          Please review the README file to learn more about the different ways you can test this app, at varying degrees of access.
          </h6>
        </main>
        <footer className="mt-auto"></footer>
      </div>
    );
  }
}

export default Main;

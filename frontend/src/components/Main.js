import React from "react";
import User from "./User";

class Main extends React.Component {
  state = {
    executiveLogin: 'executive_producer@agency.fsnd',
    executivePW: 'WIOEBFV9734IUAPEBF984HGT*',
    directorLogin: 'casting_director@agency.fsnd',
    directorPW: 'jnfvbiuew98ejkvoidfdvzioo9e9e!',
    assistantLogin: 'casting_assistant@agency.fsnd',
    assistantPW: 'diebpgbiapsgnoag98!'
  }

  copyToClipboard = (passcode) => {
    navigator.clipboard.writeText(passcode);
  }


  render() {
    const { executiveLogin, executivePW, directorLogin, directorPW, assistantLogin, assistantPW } = this.state;

    return(
      <div className="cover-container">
        <main className="d-flex flex-column align-items-center bg-white">
          <section>
            <div className="row mh-50">
              <div className="col-xs-12 col-sm-12 col-md-6 empty"></div>
              <div className="col xs-12 col-sm-12 col-md-6 p-5 bg-dark">
                <h1 className="mt-5 mb-1">Welcome to Castr</h1>
                <h6 className="mt-1 mb-5">The purpose of this project is to demonstrate proficiency in a number of skills relating to full-stack web development.
                These include database ORM's, RESTful API's, authorization through Auth0, and deployment. 
                Explore the app with the login information below. More information about cloning, running, and testing Castr locally can be found in the README.
                </h6>
              </div>
            </div>
          </section>
          <section>
            <div className="container mw-100 mx-0 mb-auto bg-white text-dark">
              <div className="row px-1 justify-content-center">
                <User
                  title="Executive Producer"
                  login={executiveLogin}
                  pw={executivePW}
                  copyToClipboard={this.copyToClipboard}
                  can="add, edit, & delete actors or movies."
                />
                <User
                  title="Casting Director"
                  login={directorLogin}
                  pw={directorPW}
                  copyToClipboard={this.copyToClipboard}
                  can="add, edit, or delete actors, and edit movies."
                  cannot="add or delete movies."
                />
                <User
                  title="Casting Assistant"
                  login={assistantLogin}
                  pw={assistantPW}
                  copyToClipboard={this.copyToClipboard}
                  can="view actors & movies only."
                  cannot="add, edit, & delete actors or movies."
                />
              </div>
            </div>
          </section>
        </main>
      </div>
    );
  }
}

export default Main;

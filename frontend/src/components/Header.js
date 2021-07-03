import React, { Component } from 'react';
import { withAuth0 } from "@auth0/auth0-react";
import AccessInNav from "./access-in-nav";
import AccessOutNav from "./access-out-nav";

class Header extends Component {  
  render() {
    const { isAuthenticated } = this.props.auth0;

    return isAuthenticated ? <AccessInNav /> : <AccessOutNav />;
  }
}

export default withAuth0(Header);

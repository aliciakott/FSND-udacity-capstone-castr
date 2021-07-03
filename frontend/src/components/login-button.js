import React from "react";
import { withAuth0 } from "@auth0/auth0-react";

class LoginButton extends React.Component {
    render() {
        const { loginWithRedirect } = this.props.auth0;
        return (
            <h4 className="nav-link text-white" onClick={() => loginWithRedirect()}>
                Log In
            </h4>
        );
    }
}

export default withAuth0(LoginButton);

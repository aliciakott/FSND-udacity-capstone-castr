import React from "react";
import { withAuth0 } from "@auth0/auth0-react";

class SignupButton extends React.Component {
    render() {
        const { loginWithRedirect } = this.props.auth0;
        return (
            <h4 className="nav-link text-white"
                onClick={() => loginWithRedirect({
                    screen_hint: "signup",})}>
                    Sign Up
            </h4>
        );
    }
}

export default withAuth0(SignupButton);

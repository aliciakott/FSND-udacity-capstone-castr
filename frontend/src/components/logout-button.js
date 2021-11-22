import React from "react";
import { withAuth0 } from "@auth0/auth0-react";

class LogoutButton extends React.Component {
    render() {
        const { logout } = this.props.auth0;
        return (
            <h4 className="nav-link text-dark" onClick={() => logout({
                returnTo: window.location.origin,
            })}>Log Out</h4>
        );
    }
}

export default withAuth0(LogoutButton);

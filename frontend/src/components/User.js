import React from "react";

class User extends React.Component {
    render() {
        const { title, login, pw, can, cannot } = this.props;
        return (
            <div className="col-xs-12 col-sm-6 col-md-6 col-lg-4 p-5">
                <h4>{title}</h4>
                <div className="input-group pb-2">
                  <input class="form-control" type="text" placeholder={login} readonly/>
                  <span className="input-group-btn">
                    <button className="btn btn-light" title="Copy user name to clipboard" onClick={() => this.props.copyToClipboard(this.props.login)}>copy</button>
                  </span>
                </div>
                <div className="input-group pb-2">
                  <input class="form-control" type="text" placeholder={pw} readonly/>
                  <span className="input-group-btn">
                    <button className="btn btn-light" title="Copy password to clipboard" onClick={() => this.props.copyToClipboard(this.props.pw)}>copy</button>
                  </span>
                </div>
                <h6>
                    {can && <span><span className="text-success fw-bold">Can</span> {can}</span>}
                    {cannot && <span><span className="text-danger fw-bold"> Cannot</span> {cannot}</span>}
                </h6>
              </div>
        );
    }
}

export default User;
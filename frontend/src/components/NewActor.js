import React from "react";
import { withAuth0 } from "@auth0/auth0-react";
import $ from 'jquery';

class NewActor extends React.Component {
  state = {
    name: "",
    age: null,
    gender: ""
  }

  postNewActor = async (event) => {
    event.preventDefault();
    const { getAccessTokenSilently } = this.props.auth0;
    const token = await getAccessTokenSilently();

    $.ajax({
      url: '/actors',
      type: "POST",
      headers: { Authorization: `Bearer ${token}`, },
      dataType: 'json',
      contentType: 'application/json',
      data: JSON.stringify({
        name: this.state.name,
        age: this.state.age,
        gender: this.state.gender
      }),
      success: (result) => {
        this.redirect_uri('/actors');
      },
      error: (error) => {
        alert('Unable to add actor to our database. Please check your permissions, or try your request again.')
        return;
      }
    })
  }

  redirect_uri = (path) => {
    window.location.href = window.location.origin + path;
  }

  handleChange = (event) => {
    this.setState({[event.target.name]: event.target.value})
  }

  render() {
    return (
      <form className="" onSubmit={this.postNewActor}>
        <div className="form-group">
          <label for="actor-name">
            Name
            <input type="text" className="form-control" id="actor-name" name="name" onChange={this.handleChange} required/>
          </label>
        </div>
        <div className="form-group">
          <label for="gender">
            Gender
            <input type="text" className="form-control" id="gender" name="gender" onChange={this.handleChange} required/>
          </label>
        </div>
        <div className="form-group">
          <label for="actor-age">
            Age
            <input type="number" className="form-control" id="actor-age" name="age" min="0" max="100" onChange={this.handleChange} required/>
          </label>
        </div>
        <div className="form-group">
          <input type="submit" className="btn btn-lg btn-light fw-bold border-white bg-white mt-3" value="Submit" />
        </div>
      </form>
    );
  }
}

export default withAuth0(NewActor);

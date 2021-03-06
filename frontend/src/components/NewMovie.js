import React from "react";
import { withAuth0 } from "@auth0/auth0-react";
import $ from 'jquery';

class NewMovie extends React.Component {
  state = {
    title: "",
    release_date: null
  }

  postNewMovie = async (event) => {
    event.preventDefault();
    const { getAccessTokenSilently } = this.props.auth0;
    const token = await getAccessTokenSilently();

    $.ajax({
      url: '/movies',
      type: "POST",
      headers: { Authorization: `Bearer ${token}`, },
      dataType: 'json',
      contentType: 'application/json',
      data: JSON.stringify({
        title: this.state.title,
        release_date: this.state.release_date
      }),
      success: (result) => {
        this.redirect_uri('/movies');
      },
      error: (error) => {
        alert('Unable to add movie to our database. Please check your permissions, or try your request again.')
        return;
      }
    })
  }

  redirect_uri = (path) => {
    this.props.history.push(path);
  }

  handleChange = (event) => {
    this.setState({[event.target.name]: event.target.value})
  }

  render() {

    return (
      <form className="m-auto" onSubmit={this.postNewMovie}>
        <div className="form-group">
          <label for="movie-title">
            Title
            <input type="text" className="form-control" id="movie-title" name="title" onChange={this.handleChange} required/>
          </label>
        </div>
        <div className="form-group">
          <label for="release-date">
            Release Date
            <input type="date" className="form-control" id="release-date" name="release_date" placeholder="2021-07-02" onChange={this.handleChange} required/>
          </label>
        </div>
        <input type="submit" className="btn btn-lg btn-light fw-bold border-white bg-white mt-3" value="Submit" />
      </form>
    );
  }
}

export default withAuth0(NewMovie);

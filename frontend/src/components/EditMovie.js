import React from "react";
import { withAuth0 } from "@auth0/auth0-react";
import $ from 'jquery';

class EditMovie extends React.Component {
  state = {
    title: "",
    release_date: null,
    id: null
  }

  componentDidMount() {
    this.getSelectedMovie()
  }

  getSelectedMovie = async () => {
    const { id } = this.props.match.params;
    const { getAccessTokenSilently } = this.props.auth0;
    const token = await getAccessTokenSilently();

    $.ajax({
      url: `/movies/${id}`,
      type: "GET",
      headers: { Authorization: `Bearer ${token}`, },
      success: (result) => {
        this.setState({
          title: result.movie.title,
          release_date: result.movie.release_date,
          id: result.movie.id
        })
        return;
      },
      error: (error) => {
        alert('Unable to find that movie. Please try again later.')
        return;
      }
    })
  }

  updateSelectedMovie = async (event) => {
    event.preventDefault();
    const id = this.state.id;
    const { getAccessTokenSilently } = this.props.auth0;
    const token = await getAccessTokenSilently();


    $.ajax({
      url: `/movies/${id}`,
      type: "PATCH",
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
        alert('Unable to update this movie. Please check your permissions, or try again later.')
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
    const { title, release_date } = this.state;
    release_date = release_date.toLocaleString("en-CA");

    return (
      <form className="" onSubmit={(e) => this.updateSelectedMovie(e)}>
        <div className="form-group">
          <label for="title">
            Title
            <input type="text" className="form-control" id="title" name="title" value={title} onChange={this.handleChange} required/>
          </label>
        </div>
        <div className="form-group">
          <label for="release_date">
            Release Date
            <input type="date" className="form-control" id="release_date" name="release_date" value={release_date} onChange={this.handleChange} required/>
          </label>
        </div>
        <div className="form-group">
          <input type="submit" className="btn btn-lg btn-light fw-bold border-white bg-white mt-3" value="Submit" />
        </div>
      </form>
    );
  }
}

export default withAuth0(EditMovie);

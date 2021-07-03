import React from "react";
import { Link } from "react-router-dom";
import { withAuth0 } from "@auth0/auth0-react";
import $ from 'jquery';
import Movie from "./Movie";

class MoviesView extends React.Component {
  state = {
    movies: []
  }

  componentDidMount() {
    this.getMovies();
  }

  getMovies = async () => {
    const { getAccessTokenSilently } = this.props.auth0;
    const token = await getAccessTokenSilently();

    $.ajax({
      url: 'http://localhost:5000/movies',
      type: "GET",
      headers: { Authorization: `Bearer ${token}`, },
      success: (result) => {
        this.setState({
          movies: result.movies
        })
        return;
      },
      error: (error) => {
        alert('Unable to load movies. Please try your request again')
        return;
      }
    })
  }

  deleteMovie = async (id) => {
    const { getAccessTokenSilently } = this.props.auth0;
    const token = await getAccessTokenSilently();

    $.ajax({
      url: `http://localhost:5000/movies/${id}`,
      type: "DELETE",
      headers: { Authorization: `Bearer ${token}`, },
      success: (result) => {
        this.setState({
          movies: result.movies
        })
        return;
      },
      error: (error) => {
        alert('Unable to process delete request. Please check your permissions, or try again later')
        return;
      }
    })
  }

  render() {
    return (
      <div>
        <div>
        {this.state.movies.map((movie) => (
            <Movie
              key={movie.id}
              id={movie.id}
              title={movie.title}
              release_date={movie.release_date}
              deleteMovie={this.deleteMovie}
            />
          ))}
        </div>
        <div>
          <Link to="/add-movie"><i className="las la-plus"></i></Link>
        </div>
      </div>
    );
  }
}

export default withAuth0(MoviesView);

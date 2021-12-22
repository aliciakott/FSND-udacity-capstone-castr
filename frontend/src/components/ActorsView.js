import React from "react";
import $ from 'jquery';
import { Link } from "react-router-dom";
import { withAuth0 } from "@auth0/auth0-react";
import Actor from "./Actor";

class ActorsView extends React.Component {
  state = {
    actors: []
  }

  componentDidMount() {
    this.getActors();
  }

  getActors = async () => {
    const { getAccessTokenSilently } = this.props.auth0;
    const token = await getAccessTokenSilently();

    $.ajax({
      url: '/actors',
      type: "GET",
      headers: { Authorization: `Bearer ${token}`, },
      success: (result) => {
        this.setState({
          actors: result.actors
        })
        return;
      },
      error: (error) => {
        alert('Unable to load actors. Please try your request again')
        return;
      }
    })
  }

  deleteActor = async (id) => {
    const { getAccessTokenSilently } = this.props.auth0;
    const token = await getAccessTokenSilently();

    $.ajax({
      url: `/actors/${id}`,
      type: "DELETE",
      headers: { Authorization: `Bearer ${token}`, },
      success: (result) => {
        this.setState({
          actors: result.actors
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
      <div className="d-flex flex-column">
        <div className="container">
          <div className="row justify-content-center">
            {this.state.actors.map((actor) => (
              <Actor
                id={actor.id}
                name={actor.name}
                age={actor.age}
                gender={actor.gender}
                deleteActor={this.deleteActor}
              />
            ))}
          </div>
        </div>
        <div className="my-5">
          <Link to="/add-actor"><i className="las la-plus text-white"></i></Link>
        </div>
      </div>
    );
  }
}

export default withAuth0(ActorsView);

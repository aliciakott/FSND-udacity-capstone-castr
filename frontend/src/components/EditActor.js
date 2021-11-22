import React from "react";
import { withAuth0 } from "@auth0/auth0-react";
import $ from 'jquery';

class EditActor extends React.Component {
  state = {
    name: "",
    gender: "",
    age: null,
    id: null
  }

  componentDidMount() {
    this.getSelectedActor()
  }

  getSelectedActor = async () => {
    const { id } = this.props.match.params;
    const { getAccessTokenSilently } = this.props.auth0;
    const token = await getAccessTokenSilently();

    $.ajax({
      url: `/actors/${id}`,
      type: "GET",
      headers: { Authorization: `Bearer ${token}`, },
      success: (result) => {
        this.setState({
          name: result.actor.name,
          gender: result.actor.gender,
          age: result.actor.age,
          id: result.actor.id
        })
        return;
      },
      error: (error) => {
        alert('Unable to find that actor. Please try again later.')
        return;
      }
    })
  }

  updateSelectedActor = async (event) => {
    event.preventDefault();
    const id = this.state.id;
    const { getAccessTokenSilently } = this.props.auth0;
    const token = await getAccessTokenSilently();


    $.ajax({
      url: `/actors/${id}`,
      type: "PATCH",
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
        alert('Unable to update this actor. Please check your permissions, or try again later.')
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
    const { name, age, gender } = this.state;

    return (
      <form className="" onSubmit={(e) => this.updateSelectedActor(e)}>
        <div className="form-group">
          <label for="actor-name">
            Name
            <input type="text" className="form-control" id="actor-name" name="name" value={name} onChange={this.handleChange} required/>
          </label>
        </div>
        <div className="form-group">
          <label for="gender">
            Gender
            <input type="text" className="form-control" id="gender" name="gender" value={gender} onChange={this.handleChange} required/>
          </label>
        </div>
        <div className="form-group">
          <label for="actor-age">
            Age
            <input type="number" className="form-control" id="actor-age" name="age" value={age} min="0" max="100" onChange={this.handleChange} required/>
          </label>
        </div>
        <div className="form-group">
          <input type="submit" className="btn btn-lg btn-light fw-bold border-white bg-white mt-3" value="Submit" />
        </div>
      </form>
    );
  }
}

export default withAuth0(EditActor);

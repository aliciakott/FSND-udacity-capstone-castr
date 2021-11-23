import React from "react";
import { Link } from "react-router-dom";

class Actor extends React.Component {
  render() {
    const { id, name, age, gender } = this.props;
    return (
      <div className="col-xs-12 col-sm-6 col-md-3 py-5 px-auto">
        <div className=""><h1>{name}</h1></div>
        <div className="d-flex flex-row justify-content-center">
          <div className="p-1"><h6>{age}</h6></div>
          <div className="p-1"><h6>{gender}</h6></div>
        </div>
        <div className="d-flex flex-row justify-content-center">
          <div className="p-1"><Link to={`edit-actor/${id}`}><i className="las la-edit text-white"></i></Link></div>
          <div className="p-1"><i className="las la-trash text-white" onClick={() => this.props.deleteActor(this.props.id)}></i></div>
        </div>
      </div>
    );
  }
}

export default Actor;

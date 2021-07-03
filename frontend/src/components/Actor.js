import React from "react";
import { Link } from "react-router-dom";

class Actor extends React.Component {
  render() {
    const { id, name, age, gender } = this.props;
    return (
      <div>
        <div className="">{name}</div>
        <div className="">{age}</div>
        <div className="">{gender}</div>
        <div className=""><Link to={`edit-actor/${id}`}><i className="las la-edit"></i></Link>
        </div>
        <div className=""><i className="las la-trash" onClick={() => this.props.deleteActor(this.props.id)}></i></div>
      </div>
    );
  }
}

export default Actor;

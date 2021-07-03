import React from "react";
import { Link } from "react-router-dom";

class Movie extends React.Component {
  render() {
    const { id, title, release_date } = this.props;
    return (
      <div>
        <div className="">{title}</div>
        <div className="">{release_date}</div>
        <div className=""><Link to={`edit-movie/${id}`}><i className="las la-edit"></i></Link></div>
        <div className=""><i className="las la-trash" onClick={() => this.props.deleteMovie(this.props.id)}></i></div>
      </div>
    );
  }
}

export default Movie;

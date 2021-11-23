import React from "react";
import { Link } from "react-router-dom";

class Movie extends React.Component {
  render() {
    const { id, title, release_date } = this.props;
    return (
      <div className="col-xs-12 col-sm-6 col-md-4 py-5 px-auto">
        <div className=""><h1>{title}</h1></div>
        <div className=""><h6>Relase Date:<br/>{release_date}</h6></div>
        <div className="d-flex flex-row justify-content-center">
          <div className="p-1"><Link to={`edit-movie/${id}`}><i className="las la-edit text-white"></i></Link></div>
          <div className="p-1"><i className="las la-trash text-white" onClick={() => this.props.deleteMovie(this.props.id)}></i></div>
        </div>
      </div>
    );
  }
}

export default Movie;

import os
from flask import Flask, request, abort, jsonify, send_from_directory, redirect
from flask_cors import CORS

from database.models import Movie, Actor, setup_db
from auth.auth import AuthError, requires_auth

def return_all(option):
    if option == "movies":
        results = Movie.query.all()

    if option == "actors":
        results = Actor.query.all()

    return [result.format() for result in results]

def return_one_or_none(option, id):
    if option == "movie":
        result = Movie.query.filter(Movie.id==id).one_or_none()

    if option == "actor":
        result = Actor.query.filter(Actor.id==id).one_or_none()

    if result is None:
        abort(404)

    return result

def create_app(test_config=None):
    app = Flask(__name__, static_folder='frontend/build', static_url_path='')
    # COMMENT OUT setup_db(app) DURING TESTING ONLY!!!
    setup_db(app)

    CORS(app)
    @app.after_request
    def after_request(response):
      response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization, true')
      response.headers.add('Access-Control-Allow-Methods', 'GET, PATCH, POST, DELETE, OPTIONS')

      return response


# //ENDPOINTS//

# GET REQUESTS

    @app.route('/')
    def serve():
        return send_from_directory(app.static_folder, 'index.html')

    @app.route('/movies')
    @requires_auth('get:movies')
    def get_movies():
        try:
            movies = return_all("movies")
            return jsonify({
                'success': True,
                'movies': movies
            })
        except:
            abort(400)

        return app

    @app.route('/actors')
    @requires_auth('get:actors')
    def get_actor():
        try:
            actors = return_all("actors")
            return jsonify({
                'success': True,
                'actors': actors
            })
        except:
            abort(400)

        return app

    @app.route('/movies/<int:movie_id>', methods=['GET'])
    @requires_auth('get:movies')
    def get_movie_by_id(movie_id):
        target_movie = return_one_or_none("movie", movie_id)
        return jsonify({
            'success': True,
            'movie': target_movie.format()
        })

    @app.route('/actors/<int:actor_id>', methods=['GET'])
    @requires_auth('get:actors')
    def get_actor_by_id(actor_id):
        target_actor = return_one_or_none("actor", actor_id)
        return jsonify({
            'success': True,
            'actor': target_actor.format()
        })

# CREATE (post)
    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def create_new_movie():
        body = request.get_json()
        title = body.get('title', None)
        release_date = body.get('release_date', None)

        new_movie = Movie(title=title, release_date=release_date)
        new_movie.insert()

        movies = return_all("movies")
        return jsonify({
            'success': True,
            'movies': movies
        })

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def create_new_actor():
        body = request.get_json()
        name = body.get('name', None)
        age = body.get('age', None)
        gender = body.get('gender', None)

        new_actor = Actor(name=name, age=age, gender=gender)
        new_actor.insert()

        actors = return_all("actors")
        return jsonify({
            'success': True,
            'actors': actors
        })

# UPDATE (patch)
    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def update_movie(movie_id):
        body = request.get_json()
        title = body.get('title', None)
        release_date = body.get('release_date', None)

        target_movie = return_one_or_none("movie", movie_id)

        if title is not None:
            target_movie.title = title
        if release_date is not None:
            target_movie.release_date = release_date

        target_movie.update()
        return jsonify({
            'success': True,
            'movie': target_movie.format()
        })

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def update_actor(actor_id):
        body = request.get_json()
        name = body.get('name', None)
        age = body.get('age', None)
        gender = body.get('gender', None)

        target_actor = return_one_or_none("actor", actor_id)

        if name is not None:
            target_actor.name = name
        if age is not None:
            target_actor.age = age
        if gender is not None:
            target_actor.gender = gender

        target_actor.update()
        return jsonify({
            'success': True,
            'actor': target_actor.format()
        })

# DELETE (delete)
    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(movie_id):
        target_movie = return_one_or_none("movie", movie_id)
        target_movie.delete()

        movies = return_all("movies")
        return jsonify({
            'success': True,
            'deleted': movie_id,
            'movies': movies
        })

    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(actor_id):
        target_actor = return_one_or_none("actor", actor_id)
        target_actor.delete()

        actors = return_all("actors")
        return jsonify({
            'success': True,
            'deleted': actor_id,
            'actors': actors
        })

# //ERROR HANDLING//
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
                        "success": False,
                        "error": 422,
                        "message": "Unprocessable request."
                        }), 422

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
                        "success": False,
                        "error": 404,
                        "message": "Resource not found."
                        }), 404

    @app.errorhandler(400)
    def invalid_request(error):
        return jsonify({
                        "success": False,
                        "error": 400,
                        "message": "Request format is invalid."
                        }), 400

    @app.errorhandler(AuthError)
    def auth_error_handler(exception):
        return jsonify({
            "success": False,
            "error": exception.status_code,
            "message": exception.error
        }), exception.status_code

    return app

app = create_app()
if __name__=='__main__':
    app.run()

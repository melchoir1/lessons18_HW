from flask import request
from flask_restx import Namespace, Resource
from implemented import movie_service, movie_schema, movies_schema

"""Шаг 7. Допишем код views с использованием сервисов"""
movie_ns = Namespace('movies')

@movie_ns.route('/')
class MoviesView(Resource):

    def get(self):
        data = {
            'director_id' : request.args.get('director_id'),
            'genre_id' : request.args.get('genre_id'),
            'year' : request.args.get('year')
            }
        all_movie = movie_service.filters(data)
        return movies_schema.dump(all_movie), 200

    def post(self):
        data = request.json
        new_movie = movie_service.add_movie(data)
        return '', 201,  {'location': f'/movies/{new_movie.id}'}

@movie_ns.route('/<int:mid>')
class MovieView(Resource):

    def get(self, mid):
        movie = movie_service.get_film(mid)
        return movie_schema.dump(movie), 200

    def put(self, mid):
        data = request.json
        data['id'] = mid
        movie_schema.update(data)
        return 'Update', 204

    def delete(self, mid):
        data = request.json
        data['id'] = mid
        movie_schema.delete_film(data)
        return 'Delete', 204
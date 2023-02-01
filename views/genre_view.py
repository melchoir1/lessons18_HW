from flask_restx import Namespace, Resource
from implemented import genre_service, genre_schema, genres_schema

"""Шаг 7. Допишем код views с использованием сервисов"""
genre_ns = Namespace('genres')

@genre_ns.route('/')
class GenresView(Resource):

    def get(self):
        genre_all_view = genre_service.genre_all()
        return genres_schema.dump(genre_all_view)

@genre_ns.route('/<int:gid>')
class GenreView(Resource):

    def get(self, gid):
        genre_id_view = genre_service.genre_id()
        return genre_schema.dump(genre_id_view)
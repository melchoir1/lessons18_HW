from flask_restx import Namespace, Resource
from implemented import director_service, director_schema, directors_schema

"""Шаг 7. Допишем код views с использованием сервисов"""
director_ns = Namespace('directors')

@director_ns.route('/')
class DirectorsView(Resource):

    def get(self):
        director_all = director_service.director_all()
        return directors_schema.dump(director_all), 200

@director_ns.route('/<int:did>')
class DirectorView(Resource):

    def get(self, did):
        director_id = director_service.director_id(did)
        return director_schema.dump(director_id)
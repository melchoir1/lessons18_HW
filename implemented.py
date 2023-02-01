# файл для создания DAO и сервисов чтобы импортировать их везде

# book_dao = BookDAO(db.session)
# book_service = BookService(dao=book_dao)
#
# review_dao = ReviewDAO(db.session)
# review_service = ReviewService(dao=review_dao)


from .dao.movie_dao import MovieDAO
from .dao.genre_dao import GenreDAO
from .dao.director_dao import DirectorDAO

from .service.movie_service import MovieService
from .service.genre_service import GenreService
from .service.director_service import DirectorService

from .dao.model.movie import MovieSchema
from .dao.model.genre import GenreSchema
from .dao.model.director import DirectorSchema

from setup_db import db

director_dao = DirectorDAO(db.session)
director_service = DirectorService(db.session)

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(db.session)

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

movie_dao = MovieDAO(db.session)
movie_service = MovieService(db.session)

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)
from .model.movie import Movie
# Шаг 5. Пишем DAO
class MovieDAO:
    def __init__(self, session):
        self.session = session
# Получить все фильмы
    def get_film_all(self):
        all_movie = self.session.query(Movie).all()
        return all_movie
# Получить фильм по id
    def get_film_id(self, mid):
        film_id = self.session.query(Movie).get(mid)
        return film_id
# Получить фильмы режиссера по id
    def get_director_id(self, did):
        #director_id = self.session.query(Movie).filter(Movie.director_id == did).all()
        query = self.session.query(Movie)
        query = query.filter(Movie.director_id == did)
        director_id = query.all()
        return director_id
# Получить фильмы по жанру по id
    def get_genre_id(self, gid):
        #genre_id = self.session.query(Movie).filter(Movie.genre_id == gid).all()
        query = self.session.query(Movie)
        query = query.filter(Movie.genre_id == gid)
        genre_id = query.all()
        return genre_id
# Получить фильмы по году по id
    def get_film_id(self, yid):
        #year_id = self.session.query(Movie).filter(Movie.year == yid).all()
        query = self.session.query(Movie)
        query = query.filter(Movie.year == yid)
        year_id = query.all()
        return year_id
# Создать фильм
    def create(self, data):
        new_movie = Movie(**data)
        self.session.add(new_movie)
        self.session.commit()
        return new_movie
# Изменить информацию о фильме
    def update(self, movie):
        self.session.add(movie)
        self.session.commit()
# Удалить фильм
    def delete(self, movie):
        self.session.delete(movie)
        self.session.commit()

from dao.movie_dao import MovieDAO

# Шаг 6. Напишем сервисы
class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao
# Добавление фильма
    def add_film(self, data):
        new_film = self.dao.create(data)
        return new_film
# Получение фильма
    def get_film(self, mid):
        get_film = self.dao.get_film_id(mid)
        return get_film
# Получение всех фильмов
    def get_film_all(self):
        film_all = self.dao.get_film_all()
        return film_all
# Изменение фильма
    def update_film(self, data):
        mid = data.get('id')
        movie = self.get_film_id(mid)

        movie.title = data.get('title')
        movie.description = data.get('description')
        movie.trailer = data.get('trailer')
        movie.year = data.get('year')
        movie.rating = data.get('rating')
        movie.genre_id = data.get('genre_id')
        movie.director_id = data.get('director_id')

        return self.dao.update(movie)
# Фильтрация фильма по разным полям
    def filter_film(self, data):
        if data.get('genre_id') is not None:
            return self.dao.get_genre_id(data.get('genre_id'))
        elif data.get('director_id') is not None:
            return self.dao.get_director_id(data.get('director_id'))
        elif data.get('year') is not None:
            return self.dao.get_film_id(data.get('year'))
        else:
            return self.dao.get_film_all()
# Удаление фильма
    def delete_film(self, mid):
        movie = self.get_film_id(mid)
        self.dao.delete(movie)


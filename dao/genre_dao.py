from .model.genre import Genre
# Шаг 5. Пишем DAO
class GenreDAO:
    def __init__(self, session):
        self.session = session
# Получить все жанры
    def get_genre_all(self):
        all_genre = self.session.query(Genre).all()
        return all_genre
# Получить жанры по id
    def get_genre_id(self, gid):
        genre_id = self.session.query(gid)
        return genre_id
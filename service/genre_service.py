from dao.genre_dao import GenreDAO

# Шаг 6. Напишем сервисы
class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao
# Получение всех
    def genre_all(self):
        genre_all = self.dao.get_genre_all()
        return genre_all
# Получение по id
    def genre_id(self, gid):
        genre_id = self.dao.get_genre_id(gid)
        return genre_id

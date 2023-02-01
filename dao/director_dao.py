from .model.director import Director
# Шаг 5. Пишем DAO
class DirectorDAO:
    def __init__(self, session):
        self.session = session
# Получить всех режиссеров
    def get_director_all(self):
        all_director  = self.session.query(Director).all()
        return all_director
# Получить режиссеров по id
    def get_director_id(self, did):
        director_id = self.session.query(Director).all(did)
        return director_id
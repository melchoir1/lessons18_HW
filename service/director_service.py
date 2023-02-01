from dao.director_dao import DirectorDAO

# Шаг 6. Напишем сервисы
class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao
#  Получение всех
    def director_all(self):
        director_all = self.dao.get_director_all()
        return director_all
# Получение по id
    def director_id(self, did):
        director_id = self.dao.get_director_id(did)
        return director_id

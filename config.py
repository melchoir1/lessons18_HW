# Это файл конфигурации приложения, здесь может хранится путь к бд, ключ шифрования, что-то еще.
# Чтобы добавить новую настройку, допишите ее в класс.

# Пример

# class Config(object):
#     DEBUG = True
#     SECRET_HERE = '249y823r9v8238r9u'


class Config(object):
    DEBUG = True
    SECRET_HERE = 'TEST'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///movies.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
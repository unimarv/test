# код написан для того чтобы брать токен брался автоматически, без копирования каждый раз. Нужен будет только менять в response - "cats"(как логин) и "а"(как пароль)
import login
from classes import Login

def ttoken():
    responsea = login.post_login(Login('admin', 'admin@mail.ru', 'a'))
    response = login.post_login(Login('dogs', 'dogs@mail.ru', 'aSdqqw!0'))
    token = response[1]['token']
    tokena = responsea[1]['token']
    return tokena, token



# код написан для того чтобы брать токен брался автоматически, без копирования каждый раз. Нужен будет только менять в response - "cats"(как логин) и "а"(как пароль)
from classes import Login

def ttoken():
    responsea = login.post_login(Login('admin', 'a'))
    response = login.post_login(Login('dogs', 'a'))
    token = response[1]['token']
    tokena = responsea[1]['token']
    return tokena, token
print(ttoken())


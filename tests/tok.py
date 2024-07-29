# код создан для того чтобы брать токен брался автоматически, без копирования каждый раз. Нужен будет только менять в response - "cats"(как логин) и "а"(как пароль)
import login
from classes import Login

def ttoken():
    response = login.post_login(Login('cats', 'a'))
    token = response[1]['token']
    return token

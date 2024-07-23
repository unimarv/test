import login
from classes import Login

def ttoken():
    response = login.post_login(Login('cats', 'a'))
    token = response[1]['token']
    return token

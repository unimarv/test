
import requests
from classes import Login, Update_Login
from typing import *

base_url = "http://192.168.32.142:8989"

def post_login(login: Login) -> Tuple[int, Any]:
    response = requests.post(f'{base_url}/login', data=login.to_json())
    return response.status_code, response.json()

login = Login(username='admin', password='a')
status_code, response_json = post_login(login)
print(response_json['token'])

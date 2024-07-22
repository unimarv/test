import requests
from classes import Login, Update_Login
from typing import *

base_url = "http://192.168.32.142:8989"


# POST

#token=" eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjE2NDI2MjAsImlhdCI6MTcyMTYzOTAyMCwiaXNBZG1pbiI6ImZhbHNlIiwiaXNzIjoibnJ0Yl9icGxhX3NlcnZlciIsInN1YiI6IjAyYzEyNGQ4LTAyOTYtNDQxNy1iMDc2LWY0MjNhYTNkOWQ2MCJ9.1kLTKgQUR8r4LyOOmTorIsaDSRcy5Sa9ToZkZnoUa3pLKY2I70oDVTZkEEfEsn7EiszjsVvKNGlBmBbpntRUI7qa4lT4EF3E5sdBO1QIuqfQKBCRTUIdOo33BQLMgqG1psLVQHxSSe7GEhc7PAfS6L8m1wdgwm0X7hR-JEXC3Tx6BWBT4mRPJyYcp9MboOpRt0mSZuiB1vY4HHNXt76C5ufQYTb5TDQ-A458AOPszFAgCpUrHHBs0g4CAWQ6rUriqPdrLNqy_HkxaDbm1FYt7XhnE2gFC7EPN8yYPTap18OKNpy-pf8el5dupKIVpMBhhG_0czvptESYeQ3LQnf0wg"
# headers = {'Authorization': f'Bearer {token}'}

def choose(function):
    if function == post_login:
        login = Login.from_dict({"login": "admin", "password": "a"})  #admin a
        return login
    elif function == put_login:
        update_login = Update_Login.from_dict({"login": "a", "email": "a"})
        return update_login


def post_login(login: Login) -> Tuple[int, Any]:
    response = requests.post(f'{base_url}/login', data=login.to_json())
    return response.status_code, response.json()


def delete_login() -> Any:
    response = requests.delete(f"{base_url}/login")
    return response.json()


def put_login(update_login) -> Tuple[int, Any]:
    response = requests.put(base_url + '/login', data=update_login.to_json())
    return response.status_code, response.json()


if __name__ == 'main':
    login = choose(post_login)
    print(post_login(login))

    update_login = choose(put_login)
    print(put_login(update_login))

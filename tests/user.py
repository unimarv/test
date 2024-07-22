import requests
from classes import User, Update_User, New_Password
from typing import *
from token import *

base_url = "http://192.168.32.142:8989"

token="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjE2NTk4MjQsImlhdCI6MTcyMTY1NjIyNCwiaXNBZG1pbiI6ImZhbHNlIiwiaXNzIjoibnJ0Yl9icGxhX3NlcnZlciIsInN1YiI6IjY2ZGE2ODE2LWM2MmYtNDZlNC1hMThlLTg2ZmM1N2RiNzkxNyJ9.VlkfBhwj4Er2rIkU9zlzEhG4wmSoQxrVs_ObuGVNBqliKKp3EBIqX8qqU5-3M4kqkKBgXn-92r3c12UutvrodjBIZdCGCydNzOIKbFaHNk_N02t2Z859fiPlnGKB2T5f_9qd_pZTOhOmQn9BkD8BAXW_zwbm1g5jDk2mRCf3fTLa6OwFnZRWKGeitB65PDMQM0pU7ogcd3BeUjYRD1LyJyb6ABvfPXJZTOe6WDEpqLEwAfPYiVwxCYPsJgjksJ5FlhjauDxsiGJPYyKnL6eYexQ9NRsiQZsHy3u_hwIbRcD1eb4UpmQ0EyF0MzqPW0-uiaJYe-ok5X2oZwi3rmh9rQ"
headers = {'Authorization': f'Bearer {token}'}

def post_user(user) -> Tuple[int, Any]:
	response = requests.post(f'{base_url}/user', data=user.to_json(), headers=headers)
	return response.status_code, response.json()


def get_user(qkey, qvalue) -> Any:
	paylod = {qkey: qvalue}
	response = requests.get(f"{base_url}/user", params=paylod, headers=headers)
	return response.status_code, response.json()


def get_all_users() -> Any:
	response = requests.get(f'{base_url}/user', headers=headers)
	return response.json()


def put_user(qkey, qvalue, update_user) -> Any:
	paylodp = {qkey: qvalue}
	response = requests.put(base_url + '/user', data=update_user.to_json(), params=paylodp, headers=headers)
	return response.json()


def put_change_password_user(qkey, qvalue, npassword) -> Any:
	paylodc = {qkey: qvalue}
	response = requests.put(f"{base_url}/user", data=npassword.to_json(), params=paylodc, headers=headers)
	return response.json()


def get_delete_user(qkey, qvalue) -> Any:
	paylodd = {qkey: qvalue}
	response = requests.delete(f"{base_url}/user", params=paylodd, headers=headers)
	return response.json()

def choose_user(function) -> Any:
	if function == post_user:
		user = User.from_dict({"company": "fkjhgdfkgh", "email":"fghfjkfg@fdgh.ru", "login": "dkghfdkfjhgdkfgh",
							   "password": "ghdfgkjdfhg", "rank": "dgjkdfhgkj"})
		return user
	elif function == put_user:
		update_user = Update_User.from_dict(
			{"company": "dfghdfjhg", "email": "fjhg@fhg.ru", "login": "jfdhgdjfkhg", "rank": "fjhgkdjfh"})
		return update_user
	elif function == put_change_password_user:
		npassword = New_Password.from_dict({"old_password":"dlfghjdghj", "password": "dfjgdjfhg"})
		return npassword


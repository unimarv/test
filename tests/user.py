import requests
from classes import User, Update_User, New_Password
from typing import *
from tok import *

base_url = "http://192.168.32.142:9898"
token = ttoken()[1]
headers = {'Authorization': f'Bearer {token}'}

def post_user(user, headers) -> Tuple[int, Any]:
	response = requests.post(f'{base_url}/user', data=user.to_json(), headers=headers)
	return response.json(), response.status_code


def get_user(qkey, qvalue, headers) -> Tuple[Any, int]:
	paylod = {qkey: qvalue}
	response = requests.get(f"{base_url}/user", params=paylod, headers=headers)
	return response.json(), response.status_code


def get_all_users(headers) -> Any:
	response = requests.get(f'{base_url}/user', headers=headers)
	return response.json(), response.status_code


def put_user(qkey, qvalue, update_user, headers) -> Tuple[Any, int]:
	paylodp = {qkey: qvalue}
	response = requests.put(base_url + '/user', data=update_user.to_json(), params=paylodp, headers=headers)
	return response.json(), response.status_code


def put_change_password_user(qkey, qvalue, npassword, headers) -> Tuple[Any, int]:
	paylodc = {qkey: qvalue}
	response = requests.put(f"{base_url}/user", data=npassword.to_json(), params=paylodc, headers=headers)
	return response.json(), response.status_code


def get_delete_user(qkey, qvalue, headers) -> Tuple[Any, int]:
	paylodd = {qkey: qvalue}
	response = requests.delete(f"{base_url}/user", params=paylodd, headers=headers)
	return response.json(), response.status_code

def choose_user(function) -> Tuple[Any, int]:
	if function == post_user:
		user = User.from_dict({"company": "fkjhgdfkgh", "email":"fghfjkfg@fdgh.ru", "login": "cats",
							   "password": "QWEqwe!1", "rank": "dgjkdfhgkj"})
		return user
	elif function == put_user:
		update_user = Update_User.from_dict(
			{"company": "dfghdfjhg", "email": "fjhg@fhg.ru", "login": "jfdhgdjfkhg", "rank": "fjhgkdjfh"})
		return update_user
	elif function == put_change_password_user:
		npassword = New_Password.from_dict({"old_password":"dlfghjdghj", "password": "dfjgdjfhg"})
		return npassword

# user = User.from_dict({"company": "fkjhgdfkgh", "email":"fghfjkfg@fdgh.ru", "login": "cats",
# 							   "password": "QWEqwe!1", "rank": "dgjkdfhgkj"})
# userr = post_user(user, headers)
# print(userr)

import requests
from classes import User, Update_User, New_Password
from typing import *
from tok import *

base_url = "http://192.168.32.142:9898"
token = ttoken()
headers = {'Authorization': f'Bearer {token}'}

def post_user(user) -> Tuple[int, Any]:
	response = requests.post(f'{base_url}/user', data=user.to_json(), headers=headers)
	return response.json()


def get_user(qkey, qvalue) -> Any:
	paylod = {qkey: qvalue}
	response = requests.get(f"{base_url}/user", params=paylod, headers=headers)
	return response.json()


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
		user = User.from_dict({"company": "fkjhgdfkgh", "email":"fghfjkfg@fdgh.ru", "login": "admin",
							   "password": "a", "rank": "dgjkdfhgkj"})
		return user
	elif function == put_user:
		update_user = Update_User.from_dict(
			{"company": "dfghdfjhg", "email": "fjhg@fhg.ru", "login": "jfdhgdjfkhg", "rank": "fjhgkdjfh"})
		return update_user
	elif function == put_change_password_user:
		npassword = New_Password.from_dict({"old_password":"dlfghjdghj", "password": "dfjgdjfhg"})
		return npassword


# user = get_user("login", "admin")
# print(user)

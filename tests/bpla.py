import requests
from typing import *
from classes import Bpla, Update_Bpla
from tok import *

base_url = "http://192.168.32.142:9898"

token = ttoken()[1]
headers = {'Authorization': f'Bearer {token}'}

def post_bpla(bpla, headers) -> Tuple[int, Any]:
	response = requests.post(f'{base_url}/bpla',  data=bpla.to_json(), headers=headers)
	return response.status_code, response.json()

def delete_bpla(qkey, qvalue, headers) -> Tuple[int, Any]:
	payloadd = {qkey: qvalue}
	response = requests.delete(f"{base_url}/bpla", params=payloadd, headers=headers)
	return response.status_code, response.json()

def put_bpla(qkey, qvalue, update_bpla, headers) -> Tuple[int, Any]:
	payloadp = {qkey: qvalue}
	response = requests.put(base_url + '/bpla', data=update_bpla.to_json(), params=payloadp, headers=headers)
	return response.status_code, response.json()

def get_bpla(qkey, qvalue, headers) -> Tuple[int, Any]:
	paylaod = {qkey: qvalue}
	response = requests.get(f"{base_url}/bpla", params=paylaod, headers=headers)
	return response.status_code, response.json()

def choose_bpla(function) -> Tuple[int, Any]:
	if function == post_bpla:
		bpla = Bpla.from_dict({"bort_number":'ldfjhg', "encryption_key":'fdgh', "model":'gfkdfghdflghru', "modem_id":'dfkghdfg', "type": 23, "user_id":'dcf85b21-e71b-4256-848d-05041b896b7b'})
		return bpla

	elif function == put_bpla:
		update_bpla = Update_Bpla.from_dict({"encryption_key": "dghdfkg", "modem_id": "flhgkjdfhg"})
		return update_bpla

#
# bpla = choose_bpla(get_bpla)
# print(get_bpla(bpla))

import requests
from typing import *
from classes import Bpla, Update_Bpla

base_url = "http://192.168.32.142:8989"

token="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjE2NTk4MjQsImlhdCI6MTcyMTY1NjIyNCwiaXNBZG1pbiI6ImZhbHNlIiwiaXNzIjoibnJ0Yl9icGxhX3NlcnZlciIsInN1YiI6IjY2ZGE2ODE2LWM2MmYtNDZlNC1hMThlLTg2ZmM1N2RiNzkxNyJ9.VlkfBhwj4Er2rIkU9zlzEhG4wmSoQxrVs_ObuGVNBqliKKp3EBIqX8qqU5-3M4kqkKBgXn-92r3c12UutvrodjBIZdCGCydNzOIKbFaHNk_N02t2Z859fiPlnGKB2T5f_9qd_pZTOhOmQn9BkD8BAXW_zwbm1g5jDk2mRCf3fTLa6OwFnZRWKGeitB65PDMQM0pU7ogcd3BeUjYRD1LyJyb6ABvfPXJZTOe6WDEpqLEwAfPYiVwxCYPsJgjksJ5FlhjauDxsiGJPYyKnL6eYexQ9NRsiQZsHy3u_hwIbRcD1eb4UpmQ0EyF0MzqPW0-uiaJYe-ok5X2oZwi3rmh9rQ"
headers = {'Authorization': f'Bearer {token}'}

def post_bpla(bpla) -> Tuple[int, Any]:
	response = requests.post(f'{base_url}/bpla',  data=bpla.to_json())
	return response.status_code, response.json()

def delete_bpla(qkey, qvalue) -> Any:
	payloadd = {qkey: qvalue}
	response = requests.delete(f"{base_url}/bpla", params=payloadd)
	return response.json()

def put_bpla(qkey, qvalue, update_bpla) -> Any:
	payloadp = {qkey: qvalue}
	response = requests.put(base_url + '/bpla', data=update_bpla.to_json(), params=payloadp)
	return response.json()

def get_bpla(qkey, qvalue) -> Any:
	paylaod = {qkey: qvalue}
	response = requests.get(f"{base_url}/bpla", params=paylaod)
	return response.json()

def choose_bpla(function) -> Any:
	if function == post_bpla:
		bpla = Bpla.from_dict({"bort_number": "hfgkjdfhgk", "encryption_key": "dgfdkjhgkdjhfg", "model": "dkfgdkjfghdfkg",
							   "modem_id": "dfhgkjdfhg", "type": "23", "user_id": "dlghfdkjhgdfg"})
		return bpla

	elif function == put_bpla:
		update_bpla = Update_Bpla.from_dict({"encryption_key": "dghdfkg", "modem_id": "flhgkjdfhg"})
		return update_bpla


bpla = choose_bpla(post_bpla)
print(post_bpla(bpla))

update_bpla = choose_bpla(put_bpla)
print(put_bpla(update_bpla))

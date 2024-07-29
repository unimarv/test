import requests
from classes import Flight
from typing import *
from tok import *
# POST
base_url = "http://192.168.32.142:9898"

flight = Flight.from_dict({"bpla_id": "fjkhgdkfjhg", "waypoints": [{"latitude": 12, "longitude": 14, "altitude": 14, "airspeed": 10.2, "groundspeed": 13.2, "distance": 11.2, "heading": 1,
																	   "param1": 25.6, "param2": 75.9, "param3": 23.4, "param":25.1, "svp_id": "fhgjfkhg", "can_switch_svp": True, "switched_svp": True, "svp_new_id": "kgjhkfdgj", "unix_timestmp": 2}]})

token = ttoken()
headers = {'Authorization': f'Bearer {token}'}
def post_flight(flight) -> Tuple[int, Any]: # функция размещения полётного задания
	response = requests.post(f'{base_url}/flight', data=flight.to_json(), headers=headers)
	return response.status_code, response.json()

def delete_flight(qkey, qvalue) -> Any: # удаление полётного задания
	payloadd = {qkey: qvalue}
	response = requests.delete(f"{base_url}/flight", params=payloadd, headers=headers)
	return response.json()


def put_flight(qkey, qvalue) -> Any: # выполнение полётного задания 
	payloadp = {qkey: qvalue}
	response = requests.put(base_url + '/flight', params=payloadp, headers=headers)
	return response.json()


def get_flight(qkey, qvalue) -> Any: # получение полётного задания 
	paylaod = {qkey: qvalue}
	response = requests.get(f"{base_url}/flight", params=paylaod, headers=headers)
	return response.json()

import requests
from classes import Flight
from typing import *

# POST
base_url = "http://192.168.32.142:8989"

flight = Flight.from_dict({"bpla_id": "fjkhgdkfjhg", "waypoints": [{"latitude": 12, "longitude": 14, "altitude": 14, "airspeed": 10.2, "groundspeed": 13.2, "distance": 11.2, "heading": 1,
																	   "param1": 25.6, "param2": 75.9, "param3": 23.4, "param":25.1, "svp_id": "fhgjfkhg", "can_switch_svp": True, "switched_svp": True, "svp_new_id": "kgjhkfdgj", "unix_timestmp": 2}]})

token="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjE2NTUwNzMsImlhdCI6MTcyMTY1MTQ3MywiaXNBZG1pbiI6ImZhbHNlIiwiaXNzIjoibnJ0Yl9icGxhX3NlcnZlciIsInN1YiI6IjAyYzEyNGQ4LTAyOTYtNDQxNy1iMDc2LWY0MjNhYTNkOWQ2MCJ9.ZTXpHssxWx2mEhJLtNGVQzt_6VyZF9BPLgxq49ukToAVzEryUQRYm2JV9caYO3fIvVDfhAKMtdv2fsdEXyeUTN5UUSiqH7rdFJ-iczGjU0wJx7roF-wDHjIfPJUZvCHKQU3AG9F8lghMi51Vb9oLFWLTewTpD0EVr-aoXBYk7ML_Ua0hy_Dnf45p6GoQwLjqZrDkCsJUIogQ0T9wtq2SFLqWhcU1iGd1TM41-4RrSZhnZfRlRsfx4ncJDU1mCrSEsVG7LKwjJ9vvB_IohdJLlRNgithY9nqC9n3Y33raR-J1kJHHsw_Zaaa-d4zIzTuhEQ03BGxgkaXq2GLAVkHiDA"
headers = {'Authorization': f'Bearer {token}'}
def post_flight(flight) -> Tuple[int, Any]:
	response = requests.post(f'{base_url}/flight', data=flight.to_json(), headers=headers)
	return response.status_code, response.json()

def delete_flight(qkey, qvalue) -> Any:
	payloadd = {qkey: qvalue}
	response = requests.delete(f"{base_url}/flight", params=payloadd, headers=headers)
	return response.json()


def put_flight(qkey, qvalue) -> Any:
	payloadp = {qkey: qvalue}
	response = requests.put(base_url + '/flight', params=payloadp, headers=headers)
	return response.json()


def get_flight(qkey, qvalue) -> Any:
	paylaod = {qkey: qvalue}
	response = requests.get(f"{base_url}/flight", params=paylaod, headers=headers)
	return response.json()

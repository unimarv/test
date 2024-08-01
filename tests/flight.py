import requests
from classes import Flight
from typing import *
from tok import *

# POST
base_url = "http://192.168.32.142:9898"

flight = Flight.from_dict({"bpla_id": "f395bce2-be36-4343-a752-f28d082fc1f0", "waypoints": [
    {"latitude": 12, "longitude": 14, "altitude": 14, "airspeed": 10.2, "groundspeed": 13.2, "distance": 11.2,
     "heading": 1,
     "param1": 25.6, "param2": 75.9, "param3": 23.4, "param": 25.1, "svp_id": "fadc262d-75ef-4921-83ee-6437734bf929", "can_switch_svp": True,
     "switched_svp": True, "svp_new_id": "141506d5-cc3e-4220-9d4c-00d23ccdce11", "unix_timestmp": 2}]})

token = ttoken()[0]
headers = {'Authorization': f'Bearer {token}'}


def post_flight(flight, headers) -> Tuple[int, Any]:
    response = requests.post(f'{base_url}/flight', data=flight.to_json(), headers=headers)
    return response.status_code, response.json()


def delete_flight(qkey, qvalue, headers) -> Any:
    payloadd = {qkey: qvalue}
    response = requests.delete(f"{base_url}/flight", params=payloadd, headers=headers)
    return response.status_code, response.json()


def put_flight(qkey, qvalue, headers) -> Any:
    payloadp = {qkey: qvalue}
    response = requests.put(base_url + '/flight', params=payloadp, headers=headers)
    return response.status_code, response.json()


def get_flight(qkey, qvalue, headers) -> Any:
    paylaod = {qkey: qvalue}
    response = requests.get(f"{base_url}/flight", params=paylaod, headers=headers)
    return response.status_code, response.json()

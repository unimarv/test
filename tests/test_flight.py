import pytest
from classes import Waypoints, Flight
from flight import *
from tok import *

status = 'status'
bpla_id_figures = "f395bce2-be36-4343-a752-f28d082fc1f0"
mission_id_name = "mission_id"
modem_id_name = "modem_id"

svp_id = "fadc262d-75ef-4921-83ee-6437734bf929"
non_token_admin = ttoken()[0]
mission_id = ""
modem_id = "1db55e6d-7251-437c-b3d4-87d0a4d3f06e"

@pytest.fixture
def waypoints():
    return Waypoints(latitude=123, longitude=456, altitude=789, airspeed=10.5, groundspeed=20.5, distance=30.5, heading=45, param1=1.2, param2=3.4, param3=5.6, param=7.8, svp_id=svp_id, can_switch_svp=True, switched_svp=False, svp_new_id="141506d5-cc3e-4220-9d4c-00d23ccdce11", unix_timestmp=1643723400)

@pytest.fixture
def flight(waypoints):
    return Flight(bpla_id=bpla_id_figures, waypoints=[waypoints])


def test_post_flight_unauthorized(flight, waypoints):
    status_code, response = post_flight(flight, headers=None)
    assert status_code == 401
    assert response == {status:"Требуется авторизация"}


def test_post_flight_real_request(waypoints, flight): # размещение полетного задания
    headers = {'Authorization': f'Bearer {non_token_admin}'}
    status_code, response = post_flight(flight, headers=headers)
    assert status_code == 201
    assert response == {
            "mission_id": response["mission_id"],
            status: 'Полетное задание зарегестрировано'}
    global mission_id
    mission_id = response['mission_id']


def test_get_flight_unauthorized(flight, waypoints): # начать полётное задание
    global mission_id
    status_code, response = get_flight(mission_id_name, mission_id, headers=None)
    assert status_code == 401
    assert response == {status: "Требуется авторизация"}

def test_get_flight_real_request(flight, waypoints): # получить полётное задание
    global mission_id
    headers = {'Authorization': f'Bearer {non_token_admin}'}
    status_code, response = get_flight(mission_id_name, mission_id, headers=headers)
    assert status_code == 200
    assert response == {"bpla_id": flight.bpla_id,
                        "waypoints": [{'airspeed': waypoints.airspeed,
                                        'altitude': waypoints.altitude,
                                        'can_switch_svp': waypoints.can_switch_svp,
                                        'distance': waypoints.distance,
                                        'groundspeed': waypoints.groundspeed,
                                        'heading': waypoints.heading,
                                        'latitude': waypoints.latitude,
                                        'longitude': waypoints.longitude,
                                        'svp_id': waypoints.svp_id,
                                        'switched_svp': waypoints.switched_svp,
                                        'unix_timestmp': waypoints.unix_timestmp}]}


def test_put_flight_unauthorized(flight, waypoints): # начать полётное задание
    global mission_id
    status_code, response = put_flight(modem_id_name, modem_id, headers=None)
    assert status_code == 401
    assert response == {status: "Требуется авторизация"}


def test_put_flight_real_request(flight, waypoints): # начать полётное задание
    global mission_id
    headers = {'Authorization': f'Bearer {non_token_admin}'}
    status_code, response = put_flight(modem_id_name, modem_id, headers=headers)
    assert status_code == 200
    assert response == {status: 'Подключение к БВС установлено'}


def test_delete_flight_unauthorized(flight, waypoints):
    status_code, response = delete_flight(mission_id_name, flight.bpla_id, headers=None)
    assert status_code == 401
    assert response == {status: "Требуется авторизация"}

def test_delete_flight_real_request(waypoints, flight): # удаление полётного задания
    global mission_id
    headers = {'Authorization': f'Bearer {non_token_admin}'}
    status_code, response = delete_flight(mission_id_name, mission_id, headers=headers)
    assert status_code == 200
    assert response == {status: 'Полетное задание удалено'}

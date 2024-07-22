import pytest
from classes import Waypoints, Flight
from flight import *
from unittest.mock import patch
from dataclasses import asdict
from operator import *

@pytest.fixture
def waypoints():
    return Waypoints(latitude=123, longitude=456, altitude=789, airspeed=10.5, groundspeed=20.5, distance=30.5, heading=45, param1=1.2, param2=3.4, param3=5.6, param=7.8, svp_id="3ed0c33b-c5a4-4cc1-ac1a-370637c2e443", can_switch_svp=True, switched_svp=False, svp_new_id="edce7400-a359-4866-9477-e324091d2d3a", unix_timestmp=1643723400)

@pytest.fixture
def flight(waypoints):
    return Flight(bpla_id="0f6eb538-84b6-4819-a0ed-95645aa5bd1a", waypoints=[waypoints])

@patch('requests.post')
def test_post_flight_success(mock_post, flight):
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {'status': 'Требуется авторизация'}
    status_code, response = post_flight(flight)
    assert status_code == 200
    assert response == {'status': 'Требуется авторизация'}
    mock_post.assert_called_once_with(f'{base_url}/flight', data=flight.to_json(), headers=headers)

@patch('requests.post')
def test_post_flight_failure(mock_post, flight):
    mock_post.return_value.status_code = 401
    mock_post.return_value.json.return_value = {'status': 'Требуется авторизация'}
    status_code, response = post_flight(flight)
    assert status_code == 401
    assert response == {'status': 'Требуется авторизация'}
    mock_post.assert_called_once_with(f'{base_url}/flight', data=flight.to_json(), headers=headers)


def test_post_flight_real_request():
    waypoints = Waypoints(latitude=123, longitude=456, altitude=789, airspeed=10.5, groundspeed=20.5, distance=30.5, heading=45, param1=1.2, param2=3.4, param3=5.6, param=7.8, svp_id="fadc262d-75ef-4921-83ee-6437734bf929", can_switch_svp=True, switched_svp=False, svp_new_id="cca0ae0c-75b7-4cff-add4-9bc4be509d02", unix_timestmp=1643723400)
    flight = Flight(bpla_id="0f6eb538-84b6-4819-a0ed-95645aa5bd1a", waypoints=[waypoints])
    status_code, response = post_flight(flight)
    mission_id = response["mission_id"]
    assert status_code == 201
    assert response['status'] == 'Полетное задание зарегестрировано'
    assert mission_id != ""
    # assert list(map(itemgetter(0), response.items()))[0] == 'mission_id'

@patch('requests.delete')
def test_delete_flight_success(mock_delete, waypoints):
    mock_delete.return_value.status_code = 200
    mock_delete.return_value.json.return_value = {'message': 'Flight deleted successfully'}
    flight = Flight(bpla_id='some_id', waypoints=[waypoints])
    response = delete_flight("bpla_id", flight.bpla_id)
    assert response == {'message': 'Flight deleted successfully'}
    mock_delete.assert_called_once_with(f'{base_url}/flight', params={"bpla_id": "some_id"}, headers=headers)

@patch('requests.delete')
def test_delete_flight_failure(mock_delete, waypoints):
    mock_delete.return_value.status_code = 404
    mock_delete.return_value.json.return_value = {'error': 'flight not found'}
    flight = Flight(bpla_id='some_id', waypoints=[waypoints])
    response = delete_flight("bpla_id", flight.bpla_id)
    assert response == {'error': 'flight not found'}
    mock_delete.assert_called_once_with(f'{base_url}/flight', params={"bpla_id": "some_id"}, headers=headers)

def test_delete_flight_real_request(waypoints):
    flight = Flight(bpla_id='some_id', waypoints=[waypoints])
    response = delete_flight("bpla_id", flight.bpla_id)
    assert response == {'status': 'Некорректный запрос'}

@patch('requests.put')
def test_put_flight_success(mock_put, flight, waypoints):
    mock_put.return_value.status_code = 200
    mock_put.return_value.json.return_value = {'message': 'Flight updated successfully'}
    flight = Flight(bpla_id='some_id', waypoints=[waypoints])
    response = put_flight("bpla_id", flight.bpla_id)
    assert response == {'message': 'Flight updated successfully'}
    mock_put.assert_called_once_with(f'{base_url}/flight', params={"bpla_id": "some_id"}, headers=headers)

@patch('requests.put')
def test_put_flight_failure(mock_put, flight, waypoints):
    mock_put.return_value.status_code = 404
    mock_put.return_value.json.return_value = {'error': 'flight not found'}
    flight = Flight(bpla_id='some_id', waypoints=[waypoints])
    response = put_flight("bpla_id", flight.bpla_id)
    assert response == {'error': 'flight not found'}
    mock_put.assert_called_once_with(f'{base_url}/flight', params={"bpla_id": "some_id"}, headers=headers)

def test_put_flight_real_request(flight, waypoints):
    flight = Flight(bpla_id='some_id', waypoints=[waypoints])
    response = put_flight("bpla_id", flight.bpla_id)
    assert response == {'status': 'Некорректный запрос'}

@patch('requests.get')
def test_get_flight_success(mock_get, flight, waypoints):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {'bpla_id': 'bpla_id', 'waypoints': [asdict(flight.waypoints[0])]}
    flight = Flight(bpla_id='some_id', waypoints=[waypoints])
    response = get_flight("bpla_id", flight.bpla_id)
    assert response == {'bpla_id': 'bpla_id', 'waypoints': [asdict(flight.waypoints[0])]}
    mock_get.assert_called_once_with(f'{base_url}/flight', params={"bpla_id": "some_id"}, headers=headers)

@patch('requests.get')
def test_get_flight_failure(mock_get, flight, waypoints):
    mock_get.return_value.status_code =404
    mock_get.return_value.json.return_value = {'error': 'flight not found'}
    flight = Flight(bpla_id='some_id', waypoints=[waypoints])
    response = get_flight("bpla_id", flight.bpla_id)
    assert response == {'error': 'flight not found'}
    mock_get.assert_called_once_with(f'{base_url}/flight', params={"bpla_id": "some_id"}, headers=headers)

def test_get_flight_real_request(flight, waypoints):
    flight = Flight(bpla_id='some_id', waypoints=[waypoints])
    response = get_flight("bpla_id", flight.bpla_id)
    assert response == {'status': 'Некорректный запрос'}

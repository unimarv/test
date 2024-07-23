import pytest
from classes import Waypoints, Flight
from flight import *


status = 'status'
bpla_id_figures = "0f6eb538-84b6-4819-a0ed-95645aa5bd1a"
bpla_id_name = "bpla_id"
uncorrect = 'Некорректный запрос'

@pytest.fixture
def waypoints():
    return Waypoints(latitude=123, longitude=456, altitude=789, airspeed=10.5, groundspeed=20.5, distance=30.5, heading=45, param1=1.2, param2=3.4, param3=5.6, param=7.8, svp_id="3ed0c33b-c5a4-4cc1-ac1a-370637c2e443", can_switch_svp=True, switched_svp=False, svp_new_id="edce7400-a359-4866-9477-e324091d2d3a", unix_timestmp=1643723400)

@pytest.fixture
def flight(waypoints):
    return Flight(bpla_id=bpla_id_figures, waypoints=[waypoints])

def test_post_flight_real_request(waypoints, flight):
    status_code, response = post_flight(flight)
    if status_code == 201:
        assert response == {
            "mission_id": response["mission_id"],
            status: 'Полетное задание зарегестрировано'}
    elif status_code == 400:
        assert response == {status: uncorrect}


def test_delete_flight_real_request(waypoints, flight):
    response = delete_flight(bpla_id_name, flight.bpla_id)
    assert response == {status: uncorrect}


def test_put_flight_real_request(flight, waypoints):
    response = put_flight(bpla_id_name, flight.bpla_id)
    assert response == {status: uncorrect}


def test_get_flight_real_request(flight, waypoints):
    response = get_flight(bpla_id_name, flight.bpla_id)
    assert response == {status: uncorrect}

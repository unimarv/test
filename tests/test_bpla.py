import pytest
from classes import Bpla, Update_Bpla
from bpla import base_url, post_bpla, put_bpla, delete_bpla, get_bpla
from unittest.mock import patch
from dataclasses import asdict


@pytest.fixture
def bpla():
    return Bpla(bort_number='ldfjhg', encryption_key='fdgh', model='gfkdfghdflghru', modem_id='dfkghdfg', type='23', user_id='lfghjdfg')
@pytest.fixture
def update_bpla():
    return Update_Bpla(encryption_key='dhfgsd', modem_id='fgdfgdg')

@patch('requests.post')
def test_post_bpla_success(mock_post, bpla):
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {'status': 'Вход успешен'}
    status_code, response = post_bpla(bpla)
    assert status_code == 200
    assert response == {'status': 'Вход успешен'}
    mock_post.assert_called_once_with(f'{base_url}/bpla', data=bpla.to_json())

@patch('requests.post')
def test_post_bpla_failure(mock_post, bpla):
    mock_post.return_value.status_code = 401
    mock_post.return_value.json.return_value = {'error': 'invalid credentials'}
    status_code, response = post_bpla(bpla)
    assert status_code == 401
    assert response == {'error': 'invalid credentials'}
    mock_post.assert_called_once_with(f'{base_url}/bpla', data=bpla.to_json())

def test_post_bpla_real_request():
    bpla = Bpla(bort_number='ldfjhg', encryption_key='fdgh', model='gfkdfghdflghru', modem_id='dfkghdfg', type='23', user_id='lfghjdfg')
    status_code, response = post_bpla(bpla)
    assert status_code == 200
    assert response == {'status': 'Вход успешен'}


def test_get_bpla(base_url, bpla):
    response = get_bpla("user_id", bpla["user_id"])
    assert response["bort_number"] == bpla["bort_number"]
    assert response["encryption_key"] == bpla["encryption_key"]
    assert response["model"] == bpla["model"]
    assert response["modem_id"] == bpla["modem_id"]
    assert response["type"] == bpla["type"]


@patch('requests.delete')
def test_delete_bpla_success(mock_delete):
    mock_delete.return_value.status_code = 200
    mock_delete.return_value.json.return_value = {'status': 'Успешно вышли из системы'}
    response = delete_bpla()
    assert response == {'status': 'Успешно вышли из системы'}
    mock_delete.assert_called_once_with(f'{base_url}/bpla')

@patch('requests.delete')
def test_delete_bpla_failure(mock_delete):
    mock_delete.return_value.status_code = 404
    mock_delete.return_value.json.return_value = {'status': 'Пользователь не найден'}
    response = delete_bpla()
    assert response == {'status': 'Пользователь не найден'}
    mock_delete.assert_called_once_with(f'{base_url}/bpla')

def test_delete_bpla_real_request():
    response = delete_bpla()
    assert response == {'status': 'Успешно вышли из системы'}



@patch('requests.put')
def test_put_bpla_success(mock_put, update_bpla):
    mock_put.return_value.status_code = 200
    mock_put.return_value.json.return_value = {'message': 'success'}
    response = put_bpla(update_bpla)
    assert response == {'message': 'success'}
    mock_put.assert_called_once_with(f'{base_url}/bpla', data=asdict(update_bpla))

@patch('requests.put')
def test_put_bpla_failure(mock_put, update_user):
    mock_put.return_value.status_code = 404
    mock_put.return_value.json.return_value = {'error': 'not found'}
    response = put_bpla(update_bpla)
    assert response == {'error': 'not found'}
    mock_put.assert_called_once_with(f'{base_url}/bpla', data=asdict(update_user))

def test_put_bpla_real_request(update_bpla):
    response = put_bpla(update_bpla)
    assert response == {'message': 'success'}


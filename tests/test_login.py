import pytest
from dataclasses import asdict
from classes import Login, Update_Login
from login import post_login, base_url, delete_login, put_login
from unittest.mock import patch


@pytest.fixture
def login():
    return Login(login='a', password='a')

@pytest.fixture
def update_login():
    return Update_Login(login='dhfgsd', email='slfflkgjs@gfgf.ru')



@patch('requests.post')
def test_post_login_success(mock_post, login):
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {'status': 'Вход успешен'}
    status_code, response = post_login(login)
    assert status_code == 200
    assert response == {'status': 'Вход успешен'}
    mock_post.assert_called_once_with(f'{base_url}/login', data=login.to_json())

@patch('requests.post')
def test_post_login_failure(mock_post, login):
    mock_post.return_value.status_code = 401
    mock_post.return_value.json.return_value = {'error': 'invalid credentials'}
    status_code, response = post_login(login)
    assert status_code == 401
    assert response == {'error': 'invalid credentials'}
    mock_post.assert_called_once_with(f'{base_url}/login', data=login.to_json())

def test_post_login_real_request():
    login = Login(login='a', password='a')
    status_code, response = post_login(login)
    assert status_code == 200
    assert response == {'status': 'Вход успешен'}


@patch('requests.delete')
def test_delete_login_success(mock_delete):
    mock_delete.return_value.status_code = 200
    mock_delete.return_value.json.return_value = {'status': 'Успешно вышли из системы'}
    response = delete_login()
    assert response == {'status': 'Успешно вышли из системы'}
    mock_delete.assert_called_once_with(f'{base_url}/login')

@patch('requests.delete')
def test_delete_login_failure(mock_delete):
    mock_delete.return_value.status_code = 404
    mock_delete.return_value.json.return_value = {'status': 'Пользователь не найден'}
    response = delete_login()
    assert response == {'status': 'Пользователь не найден'}
    mock_delete.assert_called_once_with(f'{base_url}/login')

def test_delete_login_real_request():
    response = delete_login()
    assert response == {'status': 'Успешно вышли из системы'}


@patch('requests.put')
def test_put_login_success(mock_put, update_login):
    mock_put.return_value.status_code = 200
    mock_put.return_value.json.return_value = {'message': 'success'}
    response = put_login(update_login)
    assert response == {'message': 'success'}
    mock_put.assert_called_once_with(f'{base_url}/login', data=asdict(update_login))

@patch('requests.put')
def test_put_login_failure(mock_put, update_login):
    mock_put.return_value.status_code = 404
    mock_put.return_value.json.return_value = {'error': 'not found'}
    response = put_login(update_login)
    assert response == {'error': 'not found'}
    mock_put.assert_called_once_with(f'{base_url}/login', data=asdict(update_login))

def test_put_login_real_request(update_login):
    response = put_login(update_login)
    assert response == {'message': 'success'}

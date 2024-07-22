import pytest
from classes import User, Update_User, New_Password
from user import base_url, post_user, get_delete_user, get_user, get_all_users, put_user, put_change_password_user, headers, token
from unittest.mock import patch
from dataclasses import asdict
import requests
from operator import *


@pytest.fixture
def user():
    return User(company='asd', login='dogs', email='admin@mail.ru', password='a', rank='asd')

@pytest.fixture
def update_user():
    return Update_User(company='dhfgsd', login='admin', email='fgyhdfkgh@fg.ru', rank='fkhg')

@pytest.fixture
def new_password():
    return New_Password(old_password="a", password="fjhfdhhjdfghjk")

@patch('requests.post')
def test_post_user_success(mock_post, user):
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {'status': 'Вход успешен'}
    status_code, response = post_user(user)
    assert status_code == 200
    assert response == {'status': 'Вход успешен'}
    mock_post.assert_called_once_with(f'{base_url}/user', data=user.to_json(), headers=headers)

@patch('requests.post')
def test_post_user_failure(mock_post, user):
    mock_post.return_value.status_code = 401
    mock_post.return_value.json.return_value = {'error': 'invalid credentials'}
    status_code, response = post_user(user)
    assert status_code == 401
    assert response == {'error': 'invalid credentials'}
    mock_post.assert_called_once_with(f'{base_url}/user', data=user.to_json(), headers=headers)

def test_post_user_real_request():
    user = User(company='asd', login='dogs', email='gfkdfgh@dflgh.ru', password='dfkghdfg', rank='lfghjdfg')
    status_code, response = post_user(user)
    assert response == {'status': 'Пароль должен быть как минимум из 8 символов,\nсодержать строчную и заглавную букву,\nцифру, а так же спецсимвол'}


def test_get_user(user):
    status_code, response = get_user("login", user.login)
    assert status_code == 200
    assert list(response.keys())[0] == 'company'
    assert response["company"] == user.company
    assert response["login"] == user.login
    assert response["email"] == user.email
    assert response["rank"] == user.rank


def test_get_all_users():
    response = get_all_users()
    if 'status' in response:
        assert response['status'] == 'Недостаточно прав'
    else:
        assert isinstance(response, list)



@patch('requests.delete')
def test_delete_user_success(mock_delete, user):
    mock_delete.return_value.status_code = 200
    mock_delete.return_value.json.return_value = {'status': 'Успешно вышли из системы'}
    # user = User(company='ldfjhg', login='somelogin', email='gfkdfgh@dflgh.ru', password='dfkghdfg', rank='lfghjdfg')
    response = get_delete_user("login", user.login)
    assert response == {'status': 'Успешно вышли из системы'}
    mock_delete.assert_called_once_with(f'{base_url}/user', params={"login": "dogs"}, headers=headers)

@patch('requests.delete')
def test_delete_user_failure(mock_delete, user):
    mock_delete.return_value.status_code = 404
    mock_delete.return_value.json.return_value = {'status': 'Пользователь не найден'}
    # user = User(company='ldfjhg', login='somelogin', email='gfkdfgh@dflgh.ru', password='dfkghdfg', rank='lfghjdfg')
    response = get_delete_user("login", user.login)
    assert response == {'status': 'Пользователь не найден'}
    mock_delete.assert_called_once_with(f'{base_url}/user', params={"login": "dogs"}, headers=headers)

def test_delete_user_real_request(user):
    # user = User(company='ldfjhg', login='somelogin', email='gfkdfgh@dflgh.ru', password='dfkghdfg', rank='lfghjdfg')
    response = get_delete_user("login", user.login)
    assert response == {'status': 'Недостаточно прав'}


@patch('requests.put')
def test_put_user_success(mock_put, update_user):
    mock_put.return_value.status_code = 200
    mock_put.return_value.json.return_value = {'message': 'success'}
    # update_user = Update_User(company='dhfgsd', login='fgdfgdg', email='fgyhdfkgh@fg.ru', rank='fkhg')
    response = put_user("login", update_user.login, update_user)
    assert response == {'message': 'success'}
    mock_put.assert_called_once_with(f'{base_url}/user', data=asdict(update_user), params={"login": "admin"}, headers=headers)

@patch('requests.put')
def test_put_user_failure(mock_put, update_user):
    mock_put.return_value.status_code = 404
    mock_put.return_value.json.return_value = {'error': 'not found'}
    response = put_user("login", update_user.login, update_user)
    assert response == {'error': 'not found'}
    mock_put.assert_called_once_with(f'{base_url}/user', data=asdict(update_user), params={"login": "admin"}, headers=headers)

def test_put_user_real_request(update_user):
    response = put_user("login", update_user.login, update_user)
    assert response == {'status': 'Некорректный запрос'}


def test_put_change_password_user(user, new_password):
    response = put_change_password_user("login", user.login, new_password)
    assert list(map(itemgetter(0), response.items()))[0] == 'status'
    assert response["status"] == 'Пароль должен быть как минимум из 8 символов,\nсодержать строчную и заглавную букву,\nцифру, а так же спецсимвол'

def test_put_change_password_user_invalid_old_password(user, new_password):
    new_password.old_password = "a"
    with pytest.raises(requests.exceptions.HTTPError):
        put_change_password_user("login", user.login, new_password)
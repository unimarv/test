import pytest
from classes import Login, Update_Login
from login import post_login, delete_login, put_login


@pytest.fixture
def login():
    return Login(login='cats', password='a')

@pytest.fixture
def update_login():
    return Update_Login(login='dhfgsd', email='slfflkgjs@gfgf.ru')


def test_post_login_real_request(login):
    status_code, response = post_login(login)
    assert status_code == 200
    assert response == {
        'status': 'Вход успешен',
        'token': response['token'],
        'userData': {'company': response['userData']['company'],
                     'email': response['userData']['email'],
                     'isAdmin': response['userData']['isAdmin'],
                     'login': login.login,
                     'rank': response['userData']['rank'],
                     'user_id': response['userData']['user_id']
                     }
        }


def test_delete_login_real_request():
    response = delete_login()
    assert response == {'status': 'Успешно вышли из системы'}


def test_put_login_real_request(update_login):
    status_code, response = put_login(update_login)
    assert status_code, response == (404, {'message': 'success'})

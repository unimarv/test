import pytest
from classes import Login, Update_Login
from login import post_login, delete_login, put_login


login_input = "input"
password_input = "password"
email_input = "email@mail.ru"

@pytest.fixture
def login(): # функция, которая берёт ключи из класса Login и присваивает им значения
    return Login(login='dogs', email='dogs@mail.ru', password='aSdqqw!0')

@pytest.fixture
def update_login(): # функция, которая берёт ключи из класса Update_Login и присваивает им значения
    return Update_Login(login='dhfgsd', email='slfflkgjs@gfgf.ru')

def test_post_login_not_found(login):
    login.login = login_input
    login.email = email_input
    status_code, response = post_login(login)
    assert status_code == 404
    assert response == {'status': 'Пользователь не найден'}

def test_post_login_wrong_password(login):
    login.password = password_input
    status_code, response = post_login(login)
    assert status_code == 400
    assert response == {'status': "Не удалось войти"}

def test_post_login_real_request(login): # функция, которая проверяет вход пользователя и получает данные о нём
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


# def test_post_login_unconfirmed_email(login):
#     llogin = login.login
#     status_code, response = post_login(login)
#     print(f"Response: {response}")
#     print(f"Status Code: {status_code}")
#     assert status_code == 403
#     assert response == {'status': 'Подтвердите регистрацию аккаунта по указанному адресу электронной почты'}

def test_delete_login_real_request(): # функция выхода/удаления пользователя
    response = delete_login()
    assert response == {'status': 'Успешно вышли из системы'}


def test_put_login_real_request(update_login): # восстановление аккаунта пользователя по логину
    update_login.login = "login_input"
    status_code, response = put_login(update_login)
    assert status_code == 404
    assert response == {'status': "Пользователь не найден"}

import pytest
from classes import User, Update_User, New_Password
from user import post_user, get_delete_user, get_user, get_all_users, put_user, put_change_password_user
from operator import *

status = 'status'
login = 'login'

passmess = 'Пароль должен быть как минимум из 8 символов,\n'\
           'содержать строчную и заглавную букву,\n'\
           'цифру, а так же спецсимвол'

notenough = 'Недостаточно прав'
uncorrect = 'Некорректный запрос'

auth_type = "login"
auth_value = "user_login"
invalid = "invalid_old_password"
short = "short"
@pytest.fixture
def user(): # функция, которая берёт ключи из класса User и присваивает им значения
    return User(company='aw', login='cats', email='can@mail.ru', password='f', rank='asd')

@pytest.fixture
def update_user(): # функция, которая берёт ключи из класса Update_User и присваивает им значения
    return Update_User(company='dhfgsd', login='mice', email='fgyhdfkgh@fg.ru', rank='fkhg')

@pytest.fixture
def new_password(): # функция, которая берёт ключи из класса New_Password и присваивает им значения
    return New_Password(old_password="f", password="j")


def test_post_user_real_request(user): # запрос на регистрацию, данные менять в функции user
    response = post_user(user)
    assert response == {status: passmess}


def test_get_user(user): #получение данных пользователя
    response = get_user(login, user.login)
    if status in response:
        assert response == {status: notenough}
    else:
        assert response == {
            'company': user.company,
            'email': user.email,
            'isAdmin': response['isAdmin'],
            'login': user.login,
            'rank': user.rank,
            'user_id': response['user_id']
        }


def test_get_all_users(): #получение данных всех пользователей
    response = get_all_users()
    if status in response:
        assert response == {status: notenough}
    else:
        assert list(response)


def test_delete_user_real_request(user): #удаление пользователя
    response = get_delete_user(login, user.login)
    assert response == {status: notenough}


def test_put_user_real_request(update_user): #обновление данных о пользователе
    response = put_user(login, update_user.login, update_user)
    assert response == {status: uncorrect}


def test_put_change_password_user_success(user, new_password): #успешное изменение пароля пользователя
    response = put_change_password_user(login, user.login, new_password)
    assert list(map(itemgetter(0), response.items()))[0] == status
    assert response == {status: passmess}

def test_put_change_password_user_invalid_old_password(new_password): #изменения пароля с неверным старым паролем
    new_password.old_password = invalid
    response = put_change_password_user(auth_type, auth_value, new_password)
    assert response == {status: passmess}

def test_put_change_password_user_invalid_new_password(new_password): #проверка что измененный пароль слишком короткий
    new_password.password = short
    response = put_change_password_user(auth_type, auth_value, new_password)
    assert response == {status: passmess}

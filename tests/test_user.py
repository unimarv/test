import pytest
from classes import User, Update_User, New_Password
from user import post_user, get_delete_user, get_user, get_all_users, put_user, put_change_password_user, headers
from tok import *
from operator import *

status = 'status'
login = 'login'
statuscode = 'status_code'


notenough = 'Недостаточно прав'
uncorrect = 'Некорректный запрос'
needauthorization = "Требуется авторизация"
success = 'Вход выполнен успешно'
notfound = 'Пользователь не найден'


invalid = "aSdqqw@3"
short = "short"
incorrect = "aa"
updatepassword = "aSdqqw!0"

tokenad = ttoken()[0]
non_token_admin = ttoken()[1]


@pytest.fixture
def user(): # функция, которая берёт ключи из класса User и присваивает им значения
    return User(company='asd', login='asdogs', email='asdogs@mail.ru', password='aSdqqw!0', rank='asd')

@pytest.fixture
def update_user(): # функция, которая берёт ключи из класса Update_User и присваивает им значения
    return Update_User(company='dhfgsd', login='catss', email='fgyhdfkgh@fg.ru', rank='fkhg')

@pytest.fixture
def new_password(): # функция, которая берёт ключи из класса New_Password и присваивает им значения
    return New_Password(old_password="aSdqqw!0", password="aSdqqw!20")

@pytest.fixture
def old_password(): # функция, которая берёт ключи из класса New_Password и присваивает им значения
    return New_Password(old_password="aSdqqw!20", password="aSdqqw!0")



def test_post_user_short_login(user):  # логин должен быть длиннее 4х символов
    headers = {'Authorization': f'Bearer {non_token_admin}'}
    user.login = 'cat'
    response, status_code = post_user(user, headers=headers)
    assert status_code == 400
    assert response == {status: 'Логин должен быть длиннее 4х символов,\nможет содержать только _,\nрусские и латинские буквы'}

def test_post_user_invalid_email(user):  # неправильный адрес электронной почты
    user.email = 'canmail.ru'
    response, status_code = post_user(user, headers=headers)
    assert status_code == 400
    assert response == {status: 'Неправильный адрес электронной почты'}

def test_post_user_invalid_password(user):  # неправильный пароль
    headers = {'Authorization': f'Bearer {non_token_admin}'}
    user.password = '1234567'
    response, status_code = post_user(user, headers=headers)
    assert status_code == 400
    assert response == {'status': 'Пароль должен быть как минимум из 8\n'
           'символов, содержать строчную и заглавную\n'
           'букву, цифру, а так же спецсимвол'}

def test_post_user_empty_rank(user):  # неправильное название должности (пустое)
    user.rank = ''
    response, status_code = post_user(user, headers=headers)
    assert status_code == 400
    assert response == {status: 'Неправильное название должности'}

def test_post_user_empty_company(user):  # неправильное название компании (пустое)
    user.company = ''
    response, status_code = post_user(user, headers=headers)
    assert status_code == 400
    assert response == {status: 'Неправильное название компании'}

def test_post_user_existing_login(user):  # пользователь с таким именем уже существует
    usert_t = user
    usert_t.email ="dasdasdasd@asdasd.asd"
    usert_t.login = 'dogs'
    response, status_code = post_user(usert_t, headers=headers)
    assert status_code == 400
    assert response == {status:'Пользователь с таким именем\nуже существует'}

def test_post_user_existing_email(user):  # пользователь с такой электронной почтой уже существует
    usert_t = user
    usert_t.login = 'jskadfajdbs'
    usert_t.email = 'dogs@mail.ru'
    response, status_code = post_user(usert_t, headers=headers)
    assert status_code == 400
    assert response == {status: 'Пользователь с такой электронной\nпочтой уже существует'}

def test_post_user_real_request(user): # запрос на регистрацию, данные менять в функции user
    response, status_code = post_user(user, headers=headers)
    print(f"Response: {response}")
    print(f"Status Code: {status_code}")
    assert status_code == 200
    assert response == {status: 'Email с инструкциями для завершения\nрегистрации отправлен на указанную почту'}

def test_unauth_get_user(user):
    response, status_code = get_user(login, user.login, headers={'Authorization': None})
    assert status_code == 401
    assert response == {status: needauthorization}

def test_noenough_get_user(user):
    response, status_code = get_user(login, user.login, headers={'Authorization': f'Bearer {non_token_admin}'})
    assert status_code == 403
    assert response == {status: notenough}

def test_get_nonexistent_user(user):
    response, status_code = get_user('login', 'nonexistent_user', headers={'Authorization': f'Bearer {tokenad}'})
    assert status_code == 404
    assert response == {status: "Пользователь не найден"}

def test_get_user(user):  # получение данных пользователя
    response, status_code = get_user('login', user.login, headers={'Authorization': f'Bearer {tokenad}'})
    assert status_code == 200
    assert response == {
            'company': user.company,
            'email': user.email,
            'isAdmin': response.get('isAdmin'),
            'login': user.login,
            'rank': user.rank,
            'user_id': response.get('user_id')
    }


def test_get_all_users_unauthorized():  # требуется токен
    response, status_code = get_all_users(headers={'Authorization': None})
    assert status_code == 401
    assert response == {status: 'Требуется авторизация'}

def test_get_all_users_forbidden_no_admin():  # недостаточно прав (не админ)
    headers = {'Authorization': f'Bearer {non_token_admin}'}
    response, status_code = get_all_users(headers=headers)
    assert status_code == 403
    assert response == {status: 'Недостаточно прав'}

def test_get_all_users_without_admin(): #получение данных всех пользователей#
    headers = {'Authorization': f'Bearer {non_token_admin}'}#
    response, status_code = get_all_users(headers=headers)#
    assert status_code == 403#
    assert response == {status: 'Недостаточно прав'}#

def test_get_all_users(): #получение данных всех пользователей
    headers = {'Authorization': f'Bearer {tokenad}'}
    response, status_code = get_all_users(headers=headers)
    assert status_code == 200
    assert list(response)

# def test_delete_user_unauthorized(user):  # требуется токен
#     response, status_code = get_delete_user(login, user.login, headers={})
#     assert status_code == 401
#     assert response == {status: 'Требуется авторизация'}
#
# def test_delete_user_real_request(user): #удаление пользователя
#     headers = {'Authorization': f'Bearer {non_token_admin}'}
#     response, status_code = get_delete_user(login, user.login, headers=headers)
#     assert status_code == 403
#     assert response == {status: notenough}
#
# def test_delete_user(user): #получение данных всех пользователей
#     headers = {'Authorization': f'Bearer {tokenad}'}
#     response, status_code = get_delete_user(login, user.login, headers=headers)
#     assert status_code == 200
#     assert response == {status: "Пользователь уадлён"}


def test_put_user_unauthorized(update_user):  # требуется токен
    response, status_code = put_user(login, update_user.login, update_user, headers={})
    assert status_code == 401
    assert response == {status: 'Требуется авторизация'}

def test_put_user_forbidden_no_admin(update_user):  # недостаточно прав (не админ)
    headers = {'Authorization': f'Bearer {non_token_admin}'}
    response, status_code = put_user(login, update_user.login, update_user, headers=headers)
    assert status_code == 403
    assert response == {status: 'Недостаточно прав'}

def test_put_user_short_login(update_user):  # логин должен быть длиннее 4х символов
    headers = {'Authorization': f'Bearer {tokenad}'}
    update_user.login = 'catss'
    response, status_code = put_user(login, update_user.login, update_user, headers=headers)
    assert status_code == 400
    assert response == {status: 'Логин должен быть длиннее 4х символов,\nможет содержать только _,\nрусские и латинские буквы'}

def test_put_user_short_login(update_user):  # логин должен быть длиннее 4х символов
    headers = {'Authorization': f'Bearer {non_token_admin}'}
    update_user.login = 'catss'
    response, status_code = put_user(login, update_user.login, update_user, headers=headers)
    assert status_code == 403
    assert response == {status: 'Недостаточно прав'}

def test_put_user_invalid_email(update_user):  # неправильный адрес электронной почты
    headers = {'Authorization': f'Bearer {tokenad}'}
    update_user.email = 'canmail.ru'
    response, status_code = put_user(login, update_user.login, update_user, headers=headers)
    assert status_code == 400
    assert response == {status: 'Неправильный адрес электронной почты'}

def test_put_user_invalid_email(update_user):  # неправильный адрес электронной почты
    headers = {'Authorization': f'Bearer {non_token_admin}'}
    update_user.email = 'canmail.ru'
    response, status_code = put_user(login, update_user.login, update_user, headers=headers)
    assert status_code == 403
    assert response == {status: 'Недостаточно прав'}

def test_put_user_invalid_password(update_user):  # неправильный пароль
    headers = {'Authorization': f'Bearer {tokenad}'}
    update_user.password = '1234567'
    response, status_code = put_user(login, update_user.login, update_user, headers=headers)
    assert status_code == 400
    assert response == {'status': 'Пароль должен быть как минимум из 8\n'
           'символов, содержать строчную и заглавную\n'
           'букву, цифру, а так же спецсимвол'}

def test_put_user_invalid_password(update_user):  # неправильный пароль
    headers = {'Authorization': f'Bearer {non_token_admin}'}
    update_user.password = '1234567'
    response, status_code = put_user(login, update_user.login, update_user, headers=headers)
    assert status_code == 403
    assert response == {status: 'Недостаточно прав'}

def test_put_user_empty_rank(update_user):  # неправильное название должности (пустое)
    headers = {'Authorization': f'Bearer {tokenad}'}
    update_user.rank = ''
    response, status_code = put_user(login, update_user.login, update_user, headers=headers)
    assert status_code == 400
    assert response == {status: 'Неправильное название должности'}

def test_put_user_empty_rank(update_user):  # неправильное название должности (пустое)
    headers = {'Authorization': f'Bearer {non_token_admin}'}
    update_user.rank = ''
    response, status_code = put_user(login, update_user.login, update_user, headers=headers)
    assert status_code == 403
    assert response == {status: 'Недостаточно прав'}

def test_put_user_empty_company(update_user):  # неправильное название компании (пустое)
    headers = {'Authorization': f'Bearer {tokenad}'}
    update_user.company = ''
    response, status_code = put_user(login, update_user.login, update_user, headers=headers)
    assert status_code == 400
    assert response == {status: 'Неправильное название компании'}

def test_put_user_empty_company(update_user):  # неправильное название компании (пустое)
    headers = {'Authorization': f'Bearer {non_token_admin}'}
    update_user.company = ''
    response, status_code = put_user(login, update_user.login, update_user, headers=headers)
    assert status_code == 403
    assert response == {status: 'Недостаточно прав'}

def test_put_user_existing_login(update_user):  # пользователь с таким именем уже существует
    headers = {'Authorization': f'Bearer {tokenad}'}
    update_user.login = "cats"
    response, status_code = put_user(login, update_user.login, update_user, headers=headers)
    assert status_code == 400
    assert response == {status:'Пользователь с таким именем\nуже существует'}

def test_put_user_existing_login(update_user):  # пользователь с таким именем уже существует
    headers = {'Authorization': f'Bearer {non_token_admin}'}
    update_user.login = "cats"
    response, status_code = put_user(login, update_user.login, update_user, headers=headers)
    assert status_code == 403
    assert response == {status: 'Недостаточно прав'}

def test_put_user_existing_email(update_user):  # пользователь с такой электронной почтой уже существует
    headers = {'Authorization': f'Bearer {tokenad}'}
    update_user.email = 'can@mail.ru'
    response, status_code = put_user(login, update_user.login, update_user, headers=headers)
    assert status_code == 400
    assert response == {status: 'Пользователь с такой электронной почтой уже существует'}

def test_put_user_existing_email(update_user):  # пользователь с такой электронной почтой уже существует
    headers = {'Authorization': f'Bearer {non_token_admin}'}
    update_user.email = 'can@mail.ru'
    response, status_code = put_user(login, update_user.login, update_user, headers=headers)
    assert status_code == 403
    assert response == {status: 'Недостаточно прав'}

def test_put_user_real_request(update_user): # запрос на регистрацию, данные менять в функции user
    headers = {'Authorization': f'Bearer {tokenad}'}
    response, status_code = put_user(login, update_user.login, update_user, headers=headers)
    assert status_code == 200
    assert response == {status: success}

def test_put_user_real_request(update_user): # запрос на регистрацию, данные менять в функции user
    headers = {'Authorization': f'Bearer {non_token_admin}'}
    response, status_code = put_user(login, update_user.login, update_user, headers=headers)
    assert status_code == 403
    assert response == {status: 'Недостаточно прав'}

def test_put_change_password_user_unauthorized(user, new_password):  # требуется токен
    response, status_code = put_user(login, user.login, new_password, headers=None)
    assert status_code == 401
    assert response == {status: 'Требуется авторизация'}


def test_put_change_password_user_invalid_old_password(user, new_password): #изменения пароля с неверным старым паролем
    headers = {'Authorization': f'Bearer {tokenad}'}
    new_password.old_password = invalid
    response, status_code = put_change_password_user(login, user.login, new_password, headers=headers)
    assert status_code == 400
    assert response == {status: 'Пароли не совпадают'}

def test_put_change_password_user_invalid_new_password(user, new_password): #проверка что измененный пароль слишком короткий
    headers = {'Authorization': f'Bearer {tokenad}'}
    new_password.password = short
    response, status_code = put_change_password_user(login, user.login, new_password, headers=headers)
    assert status_code == 400
    assert response == {status: 'Пароль должен быть как минимум из 8\n'
           'символов, содержать строчную и заглавную\n'
           'букву, цифру, а так же спецсимвол'}

def test_put_change_password_user_incorrect_new_password(user, new_password): #проверка что новый пароль неверный
    headers = {'Authorization': f'Bearer {tokenad}'}
    new_password.password = incorrect
    response, status_code = put_change_password_user(login, user.login, new_password, headers=headers)
    assert status_code == 400
    assert response == {status: 'Пароль должен быть как минимум из 8\n'
           'символов, содержать строчную и заглавную\n'
           'букву, цифру, а так же спецсимвол'}

def test_put_change_password_user_success(user, new_password, old_password): #успешное изменение пароля пользователя
    headers = {'Authorization': f'Bearer {tokenad}'}
    response, status_code = put_change_password_user(login, user.login, new_password, headers=headers)
    assert status_code == 200
    assert response == {status: 'Пользователь обновлен'}
    put_change_password_user(login, user.login, old_password, headers=headers)
    assert status_code == 200
    assert response == {status: 'Пользователь обновлен'}

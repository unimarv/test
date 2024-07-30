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
    return User(company='aw', login='dogs', email='can@mail.ru', password='a', rank='asd')

@pytest.fixture
def update_user(): # функция, которая берёт ключи из класса Update_User и присваивает им значения
    return Update_User(company='dhfgsd', login='catss', email='fgyhdfkgh@fg.ru', rank='fkhg')

@pytest.fixture
def new_password(): # функция, которая берёт ключи из класса New_Password и присваивает им значения
    return New_Password(old_password="f", password="j")

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
    usert_t.email ="asdasdasdasd@asdasd.asd"
    usert_t.login = 'cats'
    response, status_code = post_user(usert_t, headers=headers)
    assert status_code == 400
    assert response == {status:'Пользователь с таким именем\nуже существует'}

def test_post_user_existing_email(user):  # пользователь с такой электронной почтой уже существует
    usert_t = user
    usert_t.login = 'jskadfajdbs'
    usert_t.email = 'can@mail.ru'
    response, status_code = post_user(usert_t, headers=headers)
    assert status_code == 400
    assert response == {status: 'Пользователь с такой электронной\nпочтой уже существует'}

def test_post_user_real_request(user): # запрос на регистрацию, данные менять в функции user
    response, status_code = post_user(user, headers=headers)
def test_post_login_real_request(login): # функция, которая проверяет вход пользователя и получает данные о нём
    status_code, response = post_login(login)
    assert status_code == 200
    assert response == {status: success}

# def test_unauth_get_user(user):
#     response, status_code = get_user(login, user.login, headers={'Authorization': None})
#     assert status_code == 401
#     assert response == {status: needauthorization}
#
# def test_noenough_get_user(user):
#     response, status_code = get_user(login, user.login, headers = {'Authorization': f'Bearer {non_token_admin}'})
#     assert status_code == 403
#     assert response == {status: notenough}
#
# def test_get_nonexistent_user(user):
#     headers = {'Authorization': f'Bearer {tokenad}'}
#     response, status_code = get_user('login', 'nonexistent_user', headers)
#     assert status_code == 404
#     assert response == {status: "Пользователь не найден"}
#
# def test_get_user(user):  # получение данных пользователя
#     # user = User(company='aw', login='cats', email='can@mail.ru', password='f', rank='asd')
#     headers = {'Authorization': f'Bearer {tokenad}'}
#     response, status_code = get_user('login', user.login, headers)
#     assert status_code == 200
#     assert response == {
#             'company': user.company,
#             'email': user.email,
#             'isAdmin': response.get('isAdmin'),
#             'login': user.login,
#             'rank': user.rank,
#             'user_id': response.get('user_id')
#     }
#
#
# def test_get_all_users_unauthorized():  # требуется токен
#     response, status_code = get_all_users(headers={})
#     assert status_code == 401
#     assert response == {status: 'Требуется авторизация'}
#
# def test_get_all_users_forbidden_no_admin():  # недостаточно прав (не админ)
#     headers = {'Authorization': f'Bearer {non_token_admin}'}
#     response, status_code = get_all_users(headers=headers)
#     assert status_code == 403
#     assert response == {status: 'Недостаточно прав'}
#
# def test_get_all_users(): #получение данных всех пользователей
#     headers = {'Authorization': f'Bearer {tokenad}'}
#     response, status_code = get_all_users(headers=headers)
#     assert status_code == 200
#     assert list(response)
#
# def test_delete_user_unauthorized(user):  # требуется токен
#     response, status_code = get_delete_user(login, user.login, headers={})
#     assert status_code == 401
#     assert response == {status: 'Требуется авторизация'}
#
# def test_delete_user_real_request(user): #удаление пользователя
#     headers['Authorization'] = 'Bearer non-admin-token'
#     response, status_code = get_delete_user(login, user.login, headers=headers)
#     assert status_code == 403
#     assert response == {status: notenough}
#
# def test_delete_user(user): #получение данных всех пользователей
#     global isadmin
#     headers = {'Authorization': f'Bearer {token}'} if token else {}
#     response, status_code = get_delete_user(login, user.login, headers=headers)
#     assert status_code == 200 if isadmin else 403
#     assert response == {status: "Пользователь уадлён"}
#
#
# def test_put_user_unauthorized(update_user):  # требуется токен
#     response, status_code = put_user(login, update_user.login, update_user, headers={})
#     assert status_code == 401
#     assert response == {status: 'Требуется авторизация'}
#
# def test_put_user_forbidden_no_admin(update_user):  # недостаточно прав (не админ)
#     headers['Authorization'] = 'Bearer non-admin-token'
#     response, status_code = put_user(login, update_user.login, update_user, headers=headers)
#     assert status_code == 403
#     assert response == {status: 'Недостаточно прав'}
#
# def test_put_user_short_login(update_user):  # логин должен быть длиннее 4х символов
#     update_user.login = 'catss'
#     response, status_code = put_user(login, update_user.login, update_user, headers=headers)
#     assert status_code == 400 if isadmin else 403
#     assert response == {status: 'Логин должен быть длиннее 4х символов,\nможет содержать только _,\nрусские и латинские буквы'} if isadmin else {status: 'Недостаточно прав'}
#
# def test_put_user_invalid_email(update_user):  # неправильный адрес электронной почты
#     update_user.email = 'canmail.ru'
#     response, status_code = put_user(login, update_user.login, update_user, headers=headers)
#     assert status_code == 400 if isadmin else 403
#     assert response == {status: 'Неправильный адрес электронной почты'} if isadmin else {status: 'Недостаточно прав'}
#
# def test_put_user_invalid_password(update_user):  # неправильный пароль
#     update_user.password = '1234567'
#     response, status_code = put_user(login, update_user.login, update_user, headers=headers)
#     assert status_code == 400
#     assert response == {'status': 'Пароль должен быть как минимум из 8\n'
#            'символов, содержать строчную и заглавную\n'
#            'букву, цифру, а так же спецсимвол'}
#
# def test_put_user_empty_rank(update_user):  # неправильное название должности (пустое)
#     update_user.rank = ''
#     response, status_code = put_user(login, update_user.login, update_user, headers=headers)
#     assert status_code == 400
#     assert response == {status: 'Неправильное название должности'}
#
# def test_put_user_empty_company(update_user):  # неправильное название компании (пустое)
#     update_user.company = ''
#     response, status_code = put_user(login, update_user.login, update_user, headers=headers)
#     assert status_code == 400
#     assert response == {status: 'Неправильное название компании'}
#
# def test_put_user_existing_login(update_user):  # пользователь с таким именем уже существует
#     update_user.login = "cats"
#     response, status_code = put_user(login, update_user.login, update_user, headers=headers)
#     assert status_code == 400
#     assert response == {status:'Пользователь с таким именем\nуже существует'}
#
# def test_put_user_existing_email(update_user):  # пользователь с такой электронной почтой уже существует
#     update_user.email = 'can@mail.ru'
#     response, status_code = put_user(login, update_user.login, update_user, headers=headers)
#     assert status_code == 400
#     assert response == {status: 'Пользователь с такой электронной почтой уже существует'}
#
# def test_put_user_real_request(update_user): # запрос на регистрацию, данные менять в функции user
#     response, status_code = put_user(login, update_user.login, update_user, headers=headers)
#     assert status_code == 200
#     assert response == {status: success}
# #
# def test_put_change_password_user_success(user, new_password): #успешное изменение пароля пользователя
#     response = put_change_password_user(login, user.login, new_password)
#     assert list(map(itemgetter(0), response.items()))[0] == status
#     assert response == {status: passmess}
#
# def test_put_change_password_user_invalid_old_password(new_password): #изменения пароля с неверным старым паролем
#     new_password.old_password = invalid
#     response = put_change_password_user(auth_type, auth_value, new_password)
#     assert response == {status: passmess}
#
# def test_put_change_password_user_invalid_new_password(new_password): #проверка что измененный пароль слишком короткий
#     new_password.password = short
#     response = put_change_password_user(auth_type, auth_value, new_password)
#     assert response == {status: passmess}

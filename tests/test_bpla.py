import pytest
from classes import Bpla, Update_Bpla
from bpla import post_bpla, put_bpla, delete_bpla, get_bpla
from tok import *
from typing import *

bpla_id_name = 'bpla_id'
bpla_name = 'bpla'
bplas_name = 'bplas'
user_id_name = 'user_id'

_bpla_id = ''
bpla_id = ''
unknown_user_id_input = "02c124d8-0296-4417-b076-f423aa3d9d68"
unknown_bpla_id = "d464d4b1-dfa9-43eb-9e57-2800e24119fb"
status = 'status'

non_token_admin = ttoken()[1]
@pytest.fixture
def bpla(): # функция, которая берёт ключи из класса Bpla
    return Bpla(bort_number='qwerty', encryption_key='1234', model='qaz', modem_id='qsx', type=11, user_id='02c124d8-0296-4417-b076-f423aa3d9d60')
@pytest.fixture
def update_bpla(): # функция, которая берёт ключи из класса Update_Bpla
    return Update_Bpla(encryption_key='dhfgsd', modem_id='fgdfgdg')

def test_post_bpla_unauthorized(bpla) -> Tuple[Any, Any]:
    status_code, response = post_bpla(bpla, headers=None)
    assert status_code == 401
    assert response == {status: "Требуется авторизация"}

def test_post_bpla_real_request(bpla) -> Tuple[Any, Any]: # регистрация БПЛА
    headers = {'Authorization': f'Bearer {non_token_admin}'}
    status_code, response = post_bpla(bpla, headers=headers)
    print(f"Response: {response},Status Code: {status_code}")
    assert response == {
        'bpla': {
            'bort_number': bpla.bort_number,
            'bpla_id': response[bpla_name][bpla_id_name],
            'encryption_key': bpla.encryption_key,
            'model': bpla.model,
            'modem_id': bpla.modem_id,
            'type': bpla.type
        },
        status: 'Новый БПЛА зарегестрирован'
    }
    global _bpla_id
    _bpla_id = response[bpla_name][bpla_id_name]

def test_get_bpla_unauthorized(bpla) -> Tuple[Any, Any]:
    status_code, response = get_bpla(user_id_name, bpla.user_id, headers=None)
    assert status_code == 401
    assert response == {status:"Требуется авторизация"}

def test_get_bpla_not_found(bpla) -> Tuple[Any, Any]:
    headers = {'Authorization': f'Bearer {non_token_admin}'}
    status_code, response = get_bpla(user_id_name, unknown_user_id_input, headers=headers)
    print(f"Response: {response},Status Code: {status_code}")
    assert status_code == 404
    assert response == {status: "БПЛА не найден"}

def test_get_bpla(bpla) -> Tuple[Any, Any]: # функция получения данных БПЛА пользователя
    global bpla_id
    headers = {'Authorization': f'Bearer {non_token_admin}'}
    status_code, response = get_bpla(user_id_name, bpla.user_id, headers=headers)
    bpla_id = response[bplas_name][0][bpla_id_name]
    print(f"Response: {response},Status Code: {status_code}")
    assert response == {
        'bplas': [{
            'bort_number': bpla.bort_number,
            'bpla_id': bpla_id,
            'encryption_key': bpla.encryption_key,
            'model': bpla.model,
            'modem_id': bpla.modem_id,
            'type': bpla.type,
            #'missions': response['bplas'][0]['missions']
        },]
    }

def test_put_bpla_unauthorized(update_bpla, bpla) -> Tuple[Any, Any]:
    global _bpla_id
    status_code, response = put_bpla("bpla_id", _bpla_id, update_bpla, headers=None)
    assert status_code == 401
    assert response == {status:"Требуется авторизация"}

def test_put_bpla_not_found(update_bpla) -> Tuple[Any, Any]:
    global _bpla_id
    headers = {'Authorization': f'Bearer {non_token_admin}'}
    status_code, response = put_bpla(bpla_id_name, unknown_bpla_id, update_bpla, headers=headers)
    print(f"Response: {response},Status Code: {status_code}")
    assert status_code == 400
    assert response == {status: "Некорректный запрос"}


def test_put_bpla_real_request(update_bpla, bpla) -> Tuple[Any, Any]: # функция для обновления БПЛА
    global _bpla_id
    headers = {'Authorization': f'Bearer {non_token_admin}'}
    status_code, response = put_bpla(bpla_id_name, _bpla_id, update_bpla, headers=headers)
    print(f"Response: {response},Status Code: {status_code}")
    assert status_code == 200
    assert response == {
        'bpla': {
            'bort_number': bpla.bort_number,
            'bpla_id': _bpla_id,
            'encryption_key': update_bpla.encryption_key,
            'model': bpla.model,
            'modem_id': update_bpla.modem_id,
            'type': bpla.type
            },
        status: 'БПЛА обновлен'
        }

def test_delete_bpla_unauthorized(bpla) -> Tuple[Any, Any]:
    status_code, response = delete_bpla(bpla_id_name, bpla_id, headers=None)
    assert status_code == 401
    assert response == {status: "Требуется авторизация"}

def test_delete_bpla_real_request(bpla) -> Tuple[Any, Any]:  # функция удаления БПЛА
    global bpla_id
    headers = {'Authorization': f'Bearer {non_token_admin}'}
    status_code, response = delete_bpla(bpla_id_name, bpla_id, headers=headers)
    print(f"Response: {response},Status Code: {status_code}")
    assert status_code == 200
    assert response == {status: 'БПЛА удален'}

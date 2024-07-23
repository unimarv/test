import pytest
from classes import Bpla, Update_Bpla
from bpla import post_bpla, put_bpla, delete_bpla, get_bpla


bpla_id_name = 'bpla_id'
bpla_name = 'bpla'
bplas_name = 'bplas'
user_id_name = 'user_id'

_bpla_id = ''
_bpla_id_ = ''

status = 'status'
@pytest.fixture
def bpla(): # функция, которая берёт ключи из класса Bpla
    return Bpla(bort_number='qwerty', encryption_key='1234', model='qaz', modem_id='qsx', type=11, user_id='dcf85b21-e71b-4256-848d-05041b896b7b')
@pytest.fixture
def update_bpla(): # функция, которая берёт ключи из класса Update_Bpla
    return Update_Bpla(encryption_key='dhfgsd', modem_id='fgdfgdg')


def test_post_bpla_real_request(bpla): # регистрация БПЛА
    response = post_bpla(bpla)
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
    global _bpla_id_
    _bpla_id_ = response[bpla_name][bpla_id_name]




def test_get_bpla(bpla): # функция получения данных БПЛА пользователя
    response = get_bpla(user_id_name, bpla.user_id)
    bpla_id = response[bplas_name][0][bpla_id_name]
    assert response == {
        'bplas': [{
            'bort_number': bpla.bort_number,
            'bpla_id': bpla_id,
            'encryption_key': bpla.encryption_key,
            'model': bpla.model,
            'modem_id': bpla.modem_id,
            'type': bpla.type,
            'missions': response[bplas_name][0]['missions']
        },]
    }
    global _bpla_id
    _bpla_id = response[bplas_name][0][bpla_id_name]



def test_delete_bpla_real_request(bpla): # функция удаления БПЛА
    global _bpla_id
    status_code, response = delete_bpla(bpla_id_name, _bpla_id)
    if status_code != 200:
        assert response == {status: 'Некорректный запрос'}
    else:
        assert response == {status: 'БПЛА удален'}


def test_put_bpla_real_request(update_bpla, bpla): # функция для обновления БПЛА
    global _bpla_id_
    status_code, response = put_bpla("bpla_id", _bpla_id, update_bpla)
    if status_code != 200:
        assert response == {status: 'Некорректный запрос'}
    else:
        assert response == {
            'bpla': {
                'bort_number': bpla.bort_number,
                'bpla_id': _bpla_id_,
                'encryption_key': update_bpla.encryption_key,
                'model': bpla.model,
                'modem_id': update_bpla.modem_id,
                'type': bpla.type

            },
            status: 'БПЛА обновлен'
        }

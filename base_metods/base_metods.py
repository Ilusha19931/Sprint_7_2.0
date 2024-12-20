import string
import random

import pytest
import requests
from data import URL, payload_first, payload_second, URL_COURIER, URL_LOGIN


def create_courier_for_test():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    return payload

@pytest.fixture
def delete_courier():
    payload = create_courier_for_test()
    login = payload["login"]
    password = payload["password"]
    id_courier = get_courier_id(login, password)
    yield
    response = requests.delete(f'{URL}{URL_COURIER}/{id_courier}')
    return response

def get_courier_id(login, password):
    payload = {
        "login": login,
        "password": password
    }
    response = requests.post(f'{URL}{URL_LOGIN}', data=payload)
    if response.status_code == 200:
        return response.json()['id']
    else:
        return 0

def  create_concrete_courier():
    payload = {
        "login": "login",
        "password": "password",
        "firstName": "first_name"
    }

    return payload

def login_concrete_courier():
        payload = {
            "login": "login",
            "password": "password"
        }
        response = requests.post(f'{URL}{URL_LOGIN}', data=payload)
        return response


def login_get_id_courier(login, password):
    payload = {
        "login": login,
        "password": password
    }
    response = requests.post(f'{URL}{URL_LOGIN}', data=payload)
    if response.status_code == 200:
        return response.json()['id']
    else:
        return 0


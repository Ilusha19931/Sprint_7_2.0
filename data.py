URL = 'http://qa-scooter.praktikum-services.ru/api/v1'
URL_COURIER = '/courier'
URL_LOGIN = '/courier/login'
URL_ORDER = '/orders'

payload_first = {
    "login": "Identycal_login",
    "password": "qwer1234",
    "firstName": "Ivaan"
}

payload_second = {
    "login": "Identycal_login",
    "password": "1234qwer",
    "firstName": "Denil"
}

colors = ['"BLACK"',
          '"GREY"',
          '"BLACK", "GREY"',
         None
         ]

orderEndpoints = ['orders?courierId=335921',
          'orders?courierId=335921&nearestStation=["1", "2"]',
         'orders?limit=10&page=0&nearestStation=["110"]'
         ]

color = None
order = {
    "firstName": "Ilyusha",
    "lastName": "Ivanov",
    "address": "Kostroma.45",
    "metroStation": 3,
    "phone": "+7 999 888 44 22",
    "rentTime": 5,
    "deliveryDate": "2020-07-07",
    "comment": "Vchera",
    "color": [color]
}
class Text:

    text_error_2_courier = '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'
    text_correct = '{"ok":true}'
    text_no_needed_field_register = '{"code":400,"message":"Недостаточно данных для создания учетной записи"}'
    text_no_needed_field_login = '{"code":400,"message":"Недостаточно данных для входа"}'
    text_not_found_login = '{"code":404,"message":"Учетная запись не найдена"}'
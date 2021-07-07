import requests
import random


class ApiDataMock:

    response = requests.get(
        'https://my.api.mockaroo.com/create_account_form_selenium_seleniumacademy_platzi.json?key=cbb86130')
    data = response.json()

    i = random.randint(0, 99)

    first_name = data[i]['first_name']
    middle_name = data[i]['middle_name']
    last_name = data[i]['last_name']
    email_address = data[i]['email_address']
    password = data[i]['password']
    print(password)
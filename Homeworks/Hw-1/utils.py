import requests
import random
from faker import Faker


def show_requirements():
    with open('requirements.txt', encoding="utf8") as f:
        file = f.read()
    return file


def show_generate_users(count= 10):
    fake = Faker()
    users_list = ''
    for _ in range(count):
        user_name = fake.name().split()[0]
        if len(user_name) < 5:
            continue
        else:
            users_list += f'Имя: {user_name}, почта: {user_name.lower() + str(random.randint(0, 100)) + "@gmail.com"}'
    return users_list


def show_mean():
    pass


def show_space():
    return str(requests.get('http://api.open-notify.org/astros.json').json()['number'])


print(show_generate_users())
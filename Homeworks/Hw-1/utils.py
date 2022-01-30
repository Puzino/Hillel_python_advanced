import requests
from faker import Faker

def show_requirements():
    with open('requirements.txt', encoding="utf8") as f:
        file = f.read()
    return file


def show_generate_users(count=100):
    fake = Faker()
    for _ in range(count):
        print(fake.name(), fake.)


def show_mean():
    pass


def show_space():
    return str(requests.get('http://api.open-notify.org/astros.json').json()['number'])

show_generate_users(10)
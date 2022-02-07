import string
import random

def generate_password(password_length: int = 10) -> str:
    """
    generate random string with 10 chars
    """
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    password = ''
    for _ in range(password_length):
        password += random.choice(chars)
    return password

def inches_to_cm(value: float, decimal_point=2) -> float:
    '''

    '''
    return round(value * 2.54, decimal_point)


def mean():
    height = 175
    weight = 65
    # return height, weight
    return {
        'height': height,
        'weight': weight,
    }
    return f'Avg height is: {height}. Avg weight is: {weight}.'

'''
open('.txt')

with open() as file:
   file.read()
'''
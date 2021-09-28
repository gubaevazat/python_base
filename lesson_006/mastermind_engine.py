import random

_hidden_number = None


def make_number():
    global _hidden_number
    while True:
        _hidden_number = str(random.randint(1000, 1999))
        if check_number(_hidden_number):
            break


def check_user_number(user_number):
    number_dict = {'bulls': 0, 'cows': 0}
    for i, user_num in enumerate(user_number):
        if _hidden_number.find(user_num) == i:
            number_dict['bulls'] += 1
        elif _hidden_number.find(user_num) != -1:
            number_dict['cows'] += 1
    return number_dict


def check_number(number):
    return len(number) == 4 and len(set(number)) == len(number)


def is_gameover(user_number):
    return user_number == _hidden_number



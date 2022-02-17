# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.
from random import randint

ENLIGHTENMENT_CARMA_LEVEL = 777


class IamGodError(Exception):

    def __init__(self, message='Я бог!'):
        self.message = message
        super().__init__(self.message)


class DrunkError(Exception):

    def __init__(self, message='Я пьян!'):
        self.message = message
        super().__init__(self.message)


class CarCrashError(Exception):

    def __init__(self, message='Я разбил машину'):
        self.message = message
        super().__init__(self.message)


class GluttonyError(Exception):

    def __init__(self, message='Я объелся!'):
        self.message = message
        super().__init__(self.message)


class DepressionError(Exception):

    def __init__(self, message='Я в депрессии!'):
        self.message = message
        super().__init__(self.message)


class SuicideError(Exception):

    def __init__(self, message='Я самоубийца!'):
        self.message = message
        super().__init__(self.message)


def one_day():
    dice = randint(1, 13)
    if dice == 1:
        raise my_errors[randint(0, 5)]
    else:
        return randint(1, 7)


my_errors = [IamGodError, DrunkError, CarCrashError, GluttonyError, DepressionError, SuicideError]

carma = 0
while True:
    try:
        carma += one_day()
    except (IamGodError, DrunkError, CarCrashError, GluttonyError, DepressionError, SuicideError) as exc:
        print(f'Что то пошло не так - {exc}')
    if carma >= ENLIGHTENMENT_CARMA_LEVEL:
        break



# https://goo.gl/JnsDqu

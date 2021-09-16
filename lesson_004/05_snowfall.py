# -*- coding: utf-8 -*-
import random

import simple_draw as sd


# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20


# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()


sd.resolution = (1200, 600)
y = 500

snowflakes = []

while True:
    snowflakes.append({'x': random.randint(0, 1200), 'y': y, 'length': random.randint(10, 50)})

    sd.start_drawing()
    for snowflake in snowflakes:
        point = sd.get_point(snowflake['x'], snowflake['y'])
        sd.snowflake(center=point, length=snowflake['length'], color=sd.COLOR_WHITE)
    sd.finish_drawing()
    sd.sleep(0.2)

    sd.start_drawing()
    new_snowflakes = []
    old_snowflakes = []
    for snowflake in snowflakes:
        point = sd.get_point(snowflake['x'], snowflake['y'])
        sd.snowflake(center=point, length=snowflake['length'], color=sd.background_color)
        snowflake['x'] += random.randint(-10, 20)
        snowflake['y'] -= 10
        if snowflake['y'] > 40:
            new_snowflakes.append(snowflake)
        else:
            old_snowflakes.append(snowflake)
    for snowflake in old_snowflakes:
        point = sd.get_point(snowflake['x'], snowflake['y'])
        sd.snowflake(center=point, length=snowflake['length'], color=sd.COLOR_WHITE)
    sd.finish_drawing()
    snowflakes = new_snowflakes
    if sd.user_want_exit():
        break

sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg



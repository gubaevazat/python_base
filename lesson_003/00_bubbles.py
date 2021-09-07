# -*- coding: utf-8 -*-
import random
import time

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
point = sd.get_point(300, 300)


# sd.circle(point, 100, width=2)
# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
# TODO здесь ваш код


def bubble(coordinate, radius, step, color = sd.COLOR_YELLOW):
    for _ in range(3):
        sd.circle(coordinate, radius, color=color, width=2)
        radius += step


# bubble(point, 50, 5)
# Нарисовать 10 пузырьков в ряд

# for x in range(100, 1001, 100):
#     point = sd.get_point(x, 300)
#     bubble(point, 50, 5)
# Нарисовать три ряда по 10 пузырьков

# for y in range(200, 401, 100):
#     for x in range(100, 1001, 100):
#         point = sd.get_point(x, y)
#         bubble(point, 50, 5)
# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код
for _ in range(100):
    point = sd.get_point(random.randint(0, 1200), random.randint(0, 600))
    color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    bubble(point, 50, 5, color=color)
    time.sleep(0.02)
sd.pause()

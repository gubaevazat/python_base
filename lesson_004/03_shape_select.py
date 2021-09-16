# -*- coding: utf-8 -*-
import time

import simple_draw as sd


# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg




def figure_draw(point, angle, length, n):
    for _ in range(n):
        vector = sd.get_vector(point, angle, length)
        vector.draw(width=2)
        angle += 360 / n
        point = vector.end_point


figure_select = {0: 'triangle', 1: 'square', 2: 'pentagon', 3: 'hexagon'}

for key, value in figure_select.items():
    print(key, ' : ', value)

while True:
    num = 3
    if 0 <= num <= 3:
        print('Номер:', num)
        break
    else:
        print('Неверный номер')

point = sd.get_point(200, 200)
figure_draw(point, 0, 200, num + 3)

sd.pause()

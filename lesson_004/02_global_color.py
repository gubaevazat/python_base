# -*- coding: utf-8 -*-
import simple_draw as sd


# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

# TODO здесь ваш код


def figure_draw(point, angle, length, n, color):
    for _ in range(n):
        vector = sd.get_vector(point, angle, length)
        vector.draw(width=2, color=color)
        angle += 360 / n
        point = vector.end_point


def triangle(point, angle=0, length=100, color=sd.COLOR_YELLOW):
    figure_draw(point, angle, length, 3, color)


def square(point, angle=0, length=100, color=sd.COLOR_YELLOW):
    figure_draw(point, angle, length, 4, color)


def pentagon(point, angle=0, length=100, color=sd.COLOR_YELLOW):
    figure_draw(point, angle, length, 5, color)


def hexagon(point, angle=0, length=100, color=sd.COLOR_YELLOW):
    figure_draw(point, angle, length, 6, color)


color_list = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
              sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE]
# figure_color = color_list[6]
print('Возможные цвета:')
# for number, color1 in enumerate(color_list):
#     print(number, ' : ', color1)

# while True:
#     number = int(input('Enter number of color'))
#     if number >= 0 and number <= 6:
#         print(number)
#         break
#     else:
#         print('Enter the number again:')
number = 6

color2 = color_list[number]
hexagon(sd.get_point(100, 100), color=color2)
triangle(sd.get_point(400, 450), color=color2)
square(sd.get_point(400, 100), color=color2)
pentagon(sd.get_point(100, 400), color=color2)

sd.pause()

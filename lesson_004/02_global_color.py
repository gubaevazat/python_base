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


def figure_draw(point, angle, length, n):
    for _ in range(n):
        vector = sd.get_vector(point, angle, length)
        vector.draw(width=2)
        angle += 360 / n
        point = vector.end_point


def triangle(point, angle=0, length=100):
    figure_draw(point, angle, length, 3)


def square(point, angle=0, length=100):
    figure_draw(point, angle, length, 4)


def pentagon(point, angle=0, length=100):
    figure_draw(point, angle, length, 5)


def hexagon(point, angle=0, length=100):
    figure_draw(point, angle, length, 6)



hexagon(sd.get_point(100, 100))
triangle(sd.get_point(400, 450))
square(sd.get_point(400, 100))
pentagon(sd.get_point(100, 400))
sd.pause()

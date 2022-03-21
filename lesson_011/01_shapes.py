# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def get_polygon(n):
    def draw(point, angle, length):
        for _ in range(n):
            vector = sd.get_vector(point, angle, length)
            vector.draw(width=2)
            angle += 360 / n
            point = vector.end_point
    return draw


draw_triangle = get_polygon(n=3)
draw_triangle(point=sd.get_point(200, 200), angle=13, length=100)

draw_square = get_polygon(n=4)
draw_square(point=sd.get_point(400, 400), angle=0, length=100)


sd.pause()

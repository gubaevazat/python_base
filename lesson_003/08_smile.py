# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

# TODO здесь ваш код


def smile(x, y, color):
    sd.circle(sd.get_point(x, y), 100, color=color, width=3)
    sd.circle(sd.get_point(x - 40, y + 25), 10, color=color)
    sd.circle(sd.get_point(x + 40, y + 25), 10, color=color)


smile(300, 300, sd.COLOR_YELLOW)

sd.pause()

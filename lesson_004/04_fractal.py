# -*- coding: utf-8 -*-

import simple_draw as sd


# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения



def draw_branches(point, angle, length):
    if length < 4:
        return
    v1 = sd.get_vector(point, angle + sd.random_number(20, 30), length)
    v2 = sd.get_vector(point, angle - sd.random_number(20, 30), length)
    v1.draw()
    v2.draw()
    next_point1 = v1.end_point
    next_point2 = v2.end_point
    next_angle1 = angle + sd.random_number(20, 30)
    next_angle2 = angle - sd.random_number(20, 30)
    next_length = length * 0.75 * sd.random_number(70, 130) / 100
    draw_branches(next_point1, next_angle1, next_length)
    draw_branches(next_point2, next_angle2, next_length)


sd.resolution = (800, 600)
root_point = sd.get_point(400, 100)
draw_branches(point=root_point, angle=90, length=100)

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()

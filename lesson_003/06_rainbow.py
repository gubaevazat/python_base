# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)

# start_y = 50
# end_y = 350
# for color in rainbow_colors:
#     start_point = sd.get_point(50, start_y)
#     end_point = sd.get_point(350, end_y)
#     sd.line(start_point, end_point, color, width=4)
#     start_y += 5
#     end_y += 5


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

point = sd.get_point(300, -50)
radius = 200
for color in rainbow_colors:
    sd.circle(point, radius, color, width=20)
    radius += 20
sd.pause()

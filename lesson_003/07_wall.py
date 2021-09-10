# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
for y in range(0, 601, 50):
    sd.line(sd.get_point(0, y), sd.get_point(600, y), width=2)
    for x in range(y % 100, 601, 100):
        sd.line(sd.get_point(x, y), sd.get_point(x, y + 50), width=2)
sd.pause()

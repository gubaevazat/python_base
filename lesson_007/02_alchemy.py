# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())


def converter(element_one, element_two):
    if (isinstance(element_one, Water) and isinstance(element_two, Air)) or \
            (isinstance(element_two, Water) and isinstance(element_one, Air)):
        return Storm()
    elif (isinstance(element_one, Water) and isinstance(element_two, Fire)) or \
            (isinstance(element_two, Water) and isinstance(element_one, Fire)):
        return Steam()
    elif (isinstance(element_one, Water) and isinstance(element_two, Earth)) or \
            (isinstance(element_two, Water) and isinstance(element_one, Earth)):
        return Dirt()
    elif (isinstance(element_one, Air) and isinstance(element_two, Fire)) or \
            (isinstance(element_two, Air) and isinstance(element_one, Fire)):
        return Lightning()
    elif (isinstance(element_one, Air) and isinstance(element_two, Earth)) or \
            (isinstance(element_two, Air) and isinstance(element_one, Earth)):
        return Dust()
    elif (isinstance(element_one, Earth) and isinstance(element_two, Fire)) or \
            (isinstance(element_two, Earth) and isinstance(element_one, Fire)):
        return Lava()


class Water:
    def __add__(self, other):
        return converter(self, other)

    def __str__(self):
        return __class__.__name__


class Air:
    def __add__(self, other):
        return converter(self, other)

    def __str__(self):
        return __class__.__name__


class Fire:
    def __add__(self, other):
        return converter(self, other)

    def __str__(self):
        return __class__.__name__


class Earth:
    def __add__(self, other):
        return converter(self, other)

    def __str__(self):
        return __class__.__name__


class Steam:
    def __str__(self):
        return __class__.__name__


class Storm:
    def __str__(self):
        return __class__.__name__


class Dirt:
    def __str__(self):
        return __class__.__name__


class Lightning:
    def __str__(self):
        return __class__.__name__


class Dust:
    def __str__(self):
        return __class__.__name__


class Lava:
    def __str__(self):
        return __class__.__name__


print(Water() + Air())
print(Air() + Earth())
print(Water(), '+', Air(), '=', Water() + Air())
print(Fire(), '+', Air(), '=', Fire() + Air())
# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.

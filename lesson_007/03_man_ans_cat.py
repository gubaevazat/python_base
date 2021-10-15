# -*- coding: utf-8 -*-

from random import randint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.


class Cat:

    def __init__(self):
        self.fullness = 50
        self.house = None

    def sleep(self):
        print('Я кот и я сплю')
        self.fullness -= 10

    def eat(self):
        print('Я кот и я ем')
        self.house.food -= 10
        self.fullness += 20

    def tears_wallpaper(self):
        print('Я кот и деру обои')
        self.fullness -= 10
        self.house.dirt += 5

    def act(self):
        if self.fullness < 0:
            print('Я кот, я умер...')
        dice = randint(1, 6)
        if self.fullness <= 0:
            self.eat()
        elif dice == 1:
            self.eat()
        elif 2 <= dice <= 3:
            self.tears_wallpaper()
        elif 4 <= dice <=6:
            self.sleep()

    def __str__(self):
        return 'Я кот моя сытость {}, живу в {}'.format(self.fullness, self.house)


class Man:

    def __init__(self, house):
        self.house = house
        self.money = 50
        self.fullness = 50

    def pick_up_cat(self, cat):
        print('Подобрал кота')
        cat.house = self.house

    def buy_cat_food(self):
        print('Купил еды')
        self.house.food += 50
        self.money -= 50

    def clean_house(self):
        print('Убрался в доме')
        self.house.dirt -= 100
        self.fullness -= 20

    def work(self):
        print('Поработал')
        self.money += 150

    def eat(self):
        print('поел')
        self.house.food -= 20
        self.fullness += 20

    def act(self):
        if self.fullness < 0:
            print('Я человек и я умер....')
        if self.fullness <= 20:
            self.eat()
        if self.money <= 0:
            self.work()
        if self.house.food <= 0:
            self.buy_cat_food()
        if self.house.dirt >= 100:
            self.clean_house()


class House:

    def __init__(self):
        self.food = 0
        self.dirt = 0

    def __str__(self):
        return 'доме, продуктов осталось {}, грязи {}'.format(self.food, self.dirt)


my_cat = Cat()
print(my_cat)
man = Man(House())
man.pick_up_cat(my_cat)
print(my_cat)
for i in range(1, 366):
    print('================ day ', i, ' =====================')
    man.act()
    my_cat.act()
    print(my_cat)
# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)

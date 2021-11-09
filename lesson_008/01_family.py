# -*- coding: utf-8 -*-
import random

from termcolor import cprint
from random import randint

######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    money = 100
    eat = 50
    dirt = 0
    eat_for_cat = 30
    all_money = 0
    all_eat = 0
    all_coat = 0

    def __str__(self):
        return 'В доме денег - {}, еды - {}, грязи - {}'\
            .format(House.money, House.eat, House.dirt)


class Human:

    def __init__(self):
        self.fullness = 30
        self.happiness = 100

    def eat(self):
        amount_of_food = random.randint(10, 30)
        self.fullness += amount_of_food
        House.eat -= amount_of_food
        House.all_eat += amount_of_food

    def petting_cat(self):
        self.happiness += 5
        return 'гладит кота'

    def __str__(self):
        return 'сытость - {}, счастье - {}'.format(self.fullness, self.happiness)

    def act(self):
        if House.dirt > 90:
            self.happiness -= 10
        if self.fullness < 0:
            return 'умер от голода'
        elif self.happiness < 10:
            return 'умер от депрессии'


class Husband(Human):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return '{} '.format(self.name) + super().__str__()

    def eat(self):
        super().eat()
        print('{} поел(а)'.format(self.name))

    def work(self):
        House.money += 150
        House.all_money += 150
        self.fullness -= 10
        print('{} поработал'.format(self.name))

    def gaming(self):
        self.happiness += 20
        self.fullness -= 10
        print('{} поиграл в WoT, хорошо))'.format(self.name))

    def act(self):

        # self.happiness -= 50
        if self.fullness <= 10:
            self.eat()
        elif self.happiness <= 10:
            self.gaming()
        elif House.money <= 400:
            self.work()
        elif random.randint(0, 4) == 4:
            self.petting_cat()
        if super().act() is not None:
            print('{} '.format(self.name) + super().act())


class Wife(Human):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return '{} '.format(self.name) + super().__str__()

    def eat(self):
        super().eat()
        print('{} поел(а)'.format(self.name))

    def shopping(self):
        House.eat += 50
        House.money -= 50
        self.fullness -= 10
        print('{} купила продукты'.format(self.name))

    def buy_eat_cat(self):
        House.eat_for_cat += 10
        House.money -= 10
        self.fullness -= 10
        print('{} купила еду коту'.format(self.name))

    def buy_fur_coat(self):
        House.money -= 350
        self.happiness += 60
        self.fullness -= 10
        House.all_coat += 1
        print('{} купила шубу, я счастлива!!!'.format(self.name))

    def clean_house(self):
        House.dirt -= 100
        self.fullness -= 10
        print('{} убралась в доме'.format(self.name))

    def act(self):
        if super().act() is not None:
            print('{} '.format(self.name) + super().act())
        # self.fullness -= 5
        if self.fullness <= 10:
            self.eat()
        elif self.happiness <= 10:
            self.buy_fur_coat()
        elif House.eat <= 30:
            self.shopping()
        elif House.eat_for_cat <= 5:
            self.buy_eat_cat()
        elif House.dirt >= 100:
            self.clean_house()
        elif random.randint(0, 4) == 4:
            self.petting_cat()


######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat:

    def __init__(self, name):
        self.fullness = 30
        self.name = name

    def eat(self):
        amount_of_food = random.randint(5, 10)
        self.fullness += amount_of_food * 2
        House.eat_for_cat -= amount_of_food

    def sleep(self):
        print('{} спит'.format(self.name))
        self.fullness -= 10

    def soil(self):
        print('{} дерет обои'.format(self.name))
        House.dirt += 5
        self.fullness -= 10

    def __str__(self):
        return '{}, сытость - {}'.format(self.name, self.fullness)

    def act(self):
        if self.fullness < 0:
            print('{} - умер от голода'.format(self.name))
        if self.fullness <= 10:
            self.eat()
        elif random.randint(0, 1):
            self.sleep()
        else:
            self.soil()


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child(Human):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return '{} '.format(self.name) + super().__str__()

    def eat(self):
        amount_of_food = random.randint(5, 10)
        self.fullness += amount_of_food
        House.eat -= amount_of_food

    def sleep(self):
        print('{} - поспал'.format(self.name))
        self.fullness -= 5

    def act(self):
        if super().act() is not None:
            print('{} '.format(self.name) + super().act())
        if self.fullness <= 5:
            self.eat()
        else:
            self.sleep()


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
kolya = Child(name='Коля')
murzik = Cat(name='Мурзик')

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    kolya.act()
    murzik.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(kolya, color='cyan')
    cprint(murzik, color='cyan')
#

# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')


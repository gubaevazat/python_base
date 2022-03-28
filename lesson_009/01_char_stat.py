# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# TODO здесь ваш код
import zipfile


class CharStat:

    def __init__(self, file_name):
        self.stat = {}
        self.file_name = file_name

    def unzip(self):
        zip_file = zipfile.ZipFile(self.file_name, 'r')
        zip_file.extract(zip_file.namelist()[0])
        self.file_name = zip_file.namelist()[0]

    def counting(self):
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        if char in self.stat:
                            self.stat[char] += 1
                        else:
                            self.stat[char] = 1

    def sort_descending_stat(self, key=1, reverse=True):
        sorted_tuples = sorted(self.stat.items(), key=lambda x: x[key], reverse=reverse)
        self.stat = dict(sorted_tuples)

    def sort_ascending_stat(self):
        self.sort_descending_stat(key=1, reverse=False)

    def sort_ascending_alphabet(self):
        self.sort_descending_stat(key=0, reverse=False)

    def sort_descending_alphabet(self):
        self.sort_descending_stat(key=0, reverse=True)

    def print_stat(self):
        print('+---------+---------+')
        print('|  буква  | частота |')
        print('+---------+---------+')
        sum_alpha = 0
        for key, value in self.stat.items():
            print('|    {}    |  {:6d} |'.format(key, value))
            sum_alpha += value
        print('+---------+---------+')
        print(f'|  ИТОГО  | {sum_alpha} |')
        print('+---------+---------+')


char_stat = CharStat('./python_snippets/voyna-i-mir.txt.zip')
char_stat.unzip()
char_stat.counting()
char_stat.sort_descending_alphabet()
char_stat.print_stat()
# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828

# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# TODO здесь ваш код
from datetime import date, datetime


class LogParserMinute:

    def __init__(self, file_name):
        self.stat = {}
        self.file_name = file_name

    def collect(self):
        with open(self.file_name, 'r', encoding='cp1251') as file_read, \
                open('events_NOK.txt', 'w', encoding='cp1251') as file_write:

            for line in file_read:
                log_line = line.replace('[', '').replace(']', '').split()
                if log_line[2] == 'NOK':
                    date_time_current = datetime.strptime(log_line[0] + ' ' + log_line[1], '%Y-%m-%d %H:%M:%S.%f')
                    date_time_current = self.sort(date_time_current)
                    # print(date_time_current)
                    count = 1
                    break

            for line in file_read:
                log_line = line.replace('[', '').replace(']', '').split()
                if log_line[2] == 'NOK':
                    date_time_next = datetime.strptime(log_line[0] + ' ' + log_line[1], '%Y-%m-%d %H:%M:%S.%f')
                    date_time_next = self.sort(date_time_next)
                    # print(date_time_next)
                    if date_time_current == date_time_next:
                        count += 1
                    else:
                        line = '[' + self.format_write(date_time_current) + '] ' + str(count) + '\n'
                        file_write.write(line)
                        date_time_current = date_time_next
                        count = 1

    @staticmethod
    def sort(date_time):
        return date_time.replace(second=0, microsecond=0)

    @staticmethod
    def format_write(date_time):
        return date_time.strftime('%Y-%m-%d %H:%M')


class LogParserHour(LogParserMinute):

    @staticmethod
    def sort(date_time):
        return date_time.replace(minute=0, second=0, microsecond=0)


class LogParserDay(LogParserMinute):

    @staticmethod
    def sort(date_time):
        return date_time.replace(hour=0, minute=0, second=0, microsecond=0)

    @staticmethod
    def format_write(date_time):
        return date_time.strftime('%Y-%m-%d')


parser = LogParserDay('events.txt')
parser.collect()
# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828

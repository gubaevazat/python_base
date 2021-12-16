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


class LogParser:

    def __init__(self, file_name):
        self.stat = {}
        self.file_name = file_name

    def collect(self):
        with open(self.file_name, 'r', encoding='cp1251') as file_read, \
                open('events_NOK.txt', 'w', encoding='cp1251') as file_write:
            date_time_current = None
            count = 0
            for line in file_read:
                log_line = line.replace('[', '').replace(']', '').split()
                date_time_next = datetime.strptime(log_line[0] + ' ' + log_line[1], '%Y-%m-%d %H:%M:%S.%f')
                date_time_next = date_time_next.replace(second=0, microsecond=0)
                if log_line[2] == 'NOK':
                    if date_time_current == date_time_next:
                        count += 1
                    else:
                        if count != 0:
                            line = '[' + date_time_next.strftime('%Y-%m-%d %H:%M') + '] ' + str(count) + '\n'
                            file_write.write(line)
                        date_time_current = date_time_next
                        count = 0


parser = LogParser('events.txt')
parser.collect()
# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828

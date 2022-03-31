# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234

from datetime import datetime


class LogParserMinute:

    def __init__(self, file_name, event):
        self.file_name = file_name
        self.event = event

    def __iter__(self):
        self.file_read = open(self.file_name, 'r', encoding='cp1251')
        for line in self.file_read:
            time, event = self.convert(line)
            if event == self.event:
                self.time_current, self.event_current = time, event
                return self

    def __next__(self):
        count = 0
        if self.event_current == self.event:
            count = 1
        while True:
            line = self.file_read.readline()
            if not line:
                self.file_read.close()
                raise StopIteration
            time, event = self.convert(line)
            # print('current', self.time_current, self.event_current)
            # print(time, event)
            if time == self.time_current:
                if event == self.event:
                    count += 1
                self.event_current = event
            else:
                if count == 0:
                    self.time_current, self.event_current = time, event
                else:
                    time_return = self.time_current
                    self.time_current, self.event_current = time, event
                    return time_return, count

    @staticmethod
    def convert(line):
        log_line = line.replace('[', '').replace(']', '').split()
        date_time = datetime.strptime(log_line[0] + ' ' + log_line[1], '%Y-%m-%d %H:%M:%S.%f')
        date_time = date_time.replace(second=0, microsecond=0)
        event = log_line[2]
        return date_time, event


grouped_events = LogParserMinute('events.txt', 'NOK')
for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')



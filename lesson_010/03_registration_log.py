# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.

# TODO здесь ваш код

class NotNameError(Exception):

    def __init__(self, message='Поле имени должно содержать только буквы!'):
        self.message = message
        super().__init__(self.message)


class NotMailError(Exception):

    def __init__(self, message='Email не содержит @ или .'):
        self.message = message
        super().__init__(self.message)


with open('registrations.txt', 'r', encoding='utf8') as registration_file, \
     open('registrations_good.log', 'w', encoding='utf8') as registration_good, \
     open('registration_bad.log', 'w', encoding='utf8') as registration_bad:
    for line_number, line in enumerate(registration_file):
        try:
            name, email, age = line.split()
            if not name.isalpha():
                raise NotNameError
            if not ('@' in email) and ('.' in email):
                raise NotMailError
            if 99 < int(age) < 10:
                raise ValueError('Возраст меньше десяти или больше 99!')
            registration_good.write(line)
        except (ValueError, NotNameError, NotMailError) as exc:
            registration_bad.write(line)
            registration_bad.write(str(exc) + '\n')

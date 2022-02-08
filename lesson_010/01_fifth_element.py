# -*- coding: utf-8 -*-

# Умножить константу BRUCE_WILLIS на пятый элемент строки, введенный пользователем

BRUCE_WILLIS = 42
leeloo = None
try:
    input_data = input('Если хочешь что-нибудь сделать, сделай это сам: ')
    leeloo = int(input_data[4])
except (ValueError, IndexError) as exc:
    print(f'что-то пошло не так - {exc}, параметры - {exc.args} ')
except BaseException as exc:
    print(f'что-то пошло не так - {exc}, параметры - {exc.args} ')

try:
    result = BRUCE_WILLIS * leeloo
    print(leeloo)
    print(f"- Leeloo Dallas! Multi-pass № {result}!")
except BaseException as exc:
    print(f'что-то пошло не так - {exc}, параметры - {exc.args} ')



# Ообернуть код и обработать исключительные ситуации для произвольных входных параметров
# - ValueError - невозможно преобразовать к числу
# - IndexError - выход за границы списка
# - остальные исключения
# для каждого типа исключений написать на консоль соотв. сообщение





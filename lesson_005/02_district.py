# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

# TODO здесь ваш код

from district.soviet_street.house1 import room1 as sov_h1_r1
from district.soviet_street.house1 import room2 as sov_h1_r2
from district.soviet_street.house2 import room1 as sov_h2_r1
from district.soviet_street.house2 import room2 as sov_h2_r2

from district.central_street.house1 import room1 as cen_h1_r1
from district.central_street.house1 import room2 as cen_h1_r2
from district.central_street.house2 import room1 as cen_h2_r1
from district.central_street.house2 import room2 as cen_h2_r2

all_folks = sov_h1_r1.folks + sov_h1_r2.folks + sov_h2_r1.folks + sov_h2_r2.folks + \
            cen_h1_r1.folks + cen_h1_r2.folks + cen_h2_r1.folks + cen_h2_r2.folks
print('На районе живут', ','.join(all_folks))




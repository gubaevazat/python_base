# -*- coding: utf-8 -*-

import os
import shutil
import time
import zipfile


# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# TODO здесь ваш код


class FilesArrange:

    def __init__(self, filename):
        self.file_name = filename

    def unzip(self):
        with zipfile.ZipFile(self.file_name, 'r') as zip_file:
            zip_file.extractall('icons')
        self.file_name = 'icons'

    def collect(self):
        # os.makedirs('icons_by_year', exist_ok=True)
        for dir_path, dir_names, file_names in os.walk(self.file_name):
            for file in file_names:
                full_file_path = os.path.join(dir_path, file)
                secs = os.path.getmtime(full_file_path)
                file_time = time.gmtime(secs)
                print(file, dir_path, file_time.tm_year, file_time.tm_mon)
                new_dir = os.path.join('icons_by_year', str(file_time.tm_year), str(file_time.tm_mon))
                # print(new_dir)
                if os.path.isdir(new_dir):
                    shutil.copy2(full_file_path, new_dir)
                else:
                    os.makedirs(new_dir)
                    shutil.copy2(full_file_path, new_dir)





ar = FilesArrange('icons')
# ar.unzip()
print(ar.file_name)
ar.collect()



# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828

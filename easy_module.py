__author__ = 'Мишин Егор Олегович'
# Модуль для работы hw05_normal.py

from os import mkdir, rmdir, listdir, getcwd


def create_dir(name_dir):       # создаем папки в директории
    mkdir(name_dir)


def delete_dir(name_dir):       # удаляем папки в директори
    rmdir(name_dir)


def list_dir():
    print('Ваша текущая директория %s' % getcwd())          # текущая дериктория
    print('Её содержимое:')
    print(listdir(getcwd()))


def file_copy(source, destination):                 # копируем файл откуда и куда
    from shutil import copyfile
    copyfile(source, destination)
    print('Копия успешно сделана')


def change_dir(dir_name):                       # меняем директорию  (более правильно наверное реализовано в hard)
    from os import chdir
    chdir(dir_name)

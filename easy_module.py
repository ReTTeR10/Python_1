__author__ = 'Мишин Егор Олегович'
# Модуль для работы hw05_normal.py

from os import mkdir, rmdir


def create_dir(name_dir):       # создаем папки в директории
    mkdir(name_dir)


def delete_dir(name_dir):       # удаляем папки в директори
    rmdir(name_dir)


def list_dir(dir_name):
    from os import listdir, path
    dir_list = []
    for i in listdir(dir_name):
        if path.isdir(i):
            dir_list.append(i)
    print('\n Список папок в текущей директории: ', dir_list)


def file_copy(source, destination):
    from shutil import copyfile
    copyfile(source, destination)
    print('Копия успешно сделана')


def change_dir(dir_name):
    from os import chdir
    chdir(dir_name)
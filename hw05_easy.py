from os.path import isdir

__author__ = 'Мишин Егор Олегович'
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
print('Задача 1: создание/удаление папок')

from os import mkdir, rmdir, listdir

def create_dir(name_dir):       # создаем папки в директории
    mkdir(name_dir)

def delete_dir(name_dir):       # удаляем папки в директори
    rmdir(name_dir)

ans = input('Создать папки? y/n\n')
if ans == 'y':
    for i in range(9):
        create_dir('dir_' + str(i+1))
else:
    pass

print('\n Папки в текущей директории: ', listdir(), '\n')

ans1 = input('Удалить папки dir_1 : dir_9? y/n\n')

if ans1 == 'y':
    for i in range(9):
        delete_dir('dir_'+str(i+1))
else:
    pass

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
print('\n Задача 2 - список папок')

def list_dir():
    from os import listdir, path, getcwd
    dir_list = []
    for i in listdir(getcwd()):
        if path.isdir(i):
            dir_list.append(i)
    print('\n Список папок в текущей директории: ', dir_list)

list_dir()



# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

print('\n Задача 3 - Копия исполняемого файла')

def file_copy():
    from shutil import copyfile
    from sys import argv
    copyfile(argv[0],(argv[0].split('.')[0]) + '_copy.' + argv[0].split('.')[1])

file_copy()
print('Копия успешно сделана')
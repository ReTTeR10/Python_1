__author__ = 'Мишин Егор Олегович'
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
print('Задача 1: создание/удаление папок')

import os

def create_dir(name_dir):       # создаем папки в директории
    os.mkdir(name_dir)

def delete_dir(name_dir):       # удаляем папки в директори
    os.rmdir(name_dir)

ans = input('Создать папки? y/n\n')
if ans == 'y':
    for i in range(9):
        create_dir('dir_' + str(i))
else:
    pass

print('\n Папки в текущей директории: ', os.listdir(), '\n')

ans1 = input('Удалить папки dir_1 : dir_9? y/n\n')

if ans1 == 'y':
    for i in range(9):
        delete_dir('dir_'+str(i))
else:
    pass

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

#def listdir():
   # os.list.dir()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
#путь откуда вызвал и присваиваешь новый
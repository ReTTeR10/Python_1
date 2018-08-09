__author__ = 'Мишин Егор Олегович'
# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# В этой программе добавил изменение цвета шрифта для ответа. Например при зпередачи аргумента ping ответ pong должен
# стать зеленым. Однако при тестировании на другом компьютере текст не покрасился


import os
import sys

print('sys.argv = ', sys.argv)

homepath = os.path.abspath(sys.argv[0]).split(sys.argv[0])[0]


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp - <file_name.extention> - копировать файл")
    print("rm - <file_name.extention> - удалить файл")
    print("cd - <dir_name> - переход в указанную папку")
    print("ls - Полный путь к текущей директории")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print('pong')


def cp():
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    from shutil import copyfile
    copyfile(file_name, (file_name.split('.')[0]) + '_copy.' + file_name.split('.')[1])
    print("Файл скопирован")


def rm():
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    from os import remove
    if input('\n Вы уверены!? YES/NO\n') == 'YES':
        remove(file_name)
        print('Удалено')
    else:
        print("Файл не удален")


def changedir():
    if not dir_name:
        print("Необходимо указать имя папки вторым параметром")
        return
    from os import chdir
    f = open(os.path.join(homepath, 'settings.txt'), 'w')
    chdir(dir_name)
    f.write(os.getcwd())
    print("Вы перешли в директорию:", os.getcwd())
    f.close()

def fullpath():
    print('Полный путь к текущей директории:', os.getcwd())



do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": cp,
    "rm": rm,
    "cd": changedir,
    "ls": fullpath
}


try:
    if sys.argv[1]:
        if os.path.isfile('settings.txt'):
            f = open('settings.txt', 'r')
            os.chdir(f.read())
            f.close()
            print("Текущая папка из settings.txt:", os.getcwd())
    else:
        pass
except IndexError:
    dir_name = None


print('\n')

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    file_name = sys.argv[2]  # второй параметр может указывать на файл, поэтому используем argv[2]
except IndexError:
    file_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
else:
    print('\n Укажите параметры!')
    print_help()

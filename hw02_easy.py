
__author__ = 'Мишин Егор Олегович'
# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruits = ['яблоко', 'банан', 'киви', 'арбуз']                   #задаем список фруктов
i = 0                                                           #создаем счетчик
for fruit in fruits:                                            #цикл в списке
    print('{}.'.format(i+1), '{0:>10}'.format(fruit))           #печатаем форматированный список
    i += 1                                                      #увеличичваем счетчик


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.



first_list = [14, 2, 15, 9, 29, 35, 40, 39, 59, 100]
second_list = [6, 18, 9, 93, 40, 35, 97, 79]

print("1ый список: ", first_list)
print("2ой список: ", second_list)
for num in set(first_list) & set(second_list):
    first_list.remove(num)
print("Результат :", first_list)


# import random
#
#
# def rand_int():
#     num = int(random.uniform(1, 20))   # Возможные цифры в списках( на данный момент от 1 до 20)
#     return num
#
#
#
# ans = ''
# while ans != 'n':
#     first_list = []
#     second_list = []
#     first_list_len = int(input('Введите длину 1-го списка: '))
#     second_list_len = int(input('Введите длину 2-го списка: '))
#
#
#     while first_list_len != 0:
#         first_list = first_list + [rand_int()]
#         first_list_len -= 1
#
#     while second_list_len != 0:
#         second_list = second_list + [rand_int()]
#         second_list_len -= 1
#     print('Первый список из случайных чисел: ', first_list)
#     print('Второй список из случайных чисел: ', second_list)
#
#     if set(first_list) & set(second_list):
#         print("Одинаковые числа есть")
#         for num in set(first_list) & set(second_list):
#             first_list.remove(num)
#         print('\nПервый список после удаления элементов, \nвходящих во второй: ', first_list)
#         print('Второй список: ', second_list)
#         ans = input('Повторить? y/n')
#     else:
#         print("Одинаковых чисел нет")
#         ans = input('Повторить? y/n')




# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

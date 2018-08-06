__author__ = 'Мишин Егор Олегович'

# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
print('\n Задача 1 - генератор квадрата эл-ов исходного списка\n')
import random


my_list = [random.randint(-10,10) for _ in range(10)]
my_list1 = [elem**2 for elem in my_list]
print('Список 1: ', my_list, '\nСписок 2: ', my_list1)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

print('\n Задание №2 - фрукты')

fruits1 = [fruit for fruit in ['banana', 'coconut', 'apple', 'orange']]
fruits2 = [fruit for fruit in ['kiwi', 'banana', 'mango', 'blackberry', 'watermelon', 'orange']]

print(fruits1)
print(fruits2)
fruits3 = [fruit for fruit in fruits1 if fruit in fruits2]
print('\n В обоих списках присутствуют: ', fruits3)




# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

import random
print('\n Задание 3 - произвольные числа')

#num = [random.randint(-100, 100) for _ in range(10)]
num = [l for l in [3.3, 21, 10, 4, -4, 0, -2.1, 2.3, 2.4]]

print('\n Исходный список: ', num)
answer1 = [i for i in num if i % 3 == 0]
answer2 = [i for i in num if i > 0]
answer3 = [i for i in num if i % 4 != 0]

print('\n', answer1, '\n', answer2, '\n', answer3)

print(3.3 % 3 == 0)



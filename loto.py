__author__ = 'Мишин Егор Олегович'

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11      
      16 49    55 88    77    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""



import random
from sys import exit


def sort_to_max(origin_list, start, end):    # сортируем по возрастанию значения в карточке
    for i in range(end, start, -1):
        for j in range(start, i):
            if origin_list[j] > origin_list[j + 1]:
                origin_list[j], origin_list[j + 1] = origin_list[j + 1], origin_list[j]


class Cards:
    def __init__(self):
        self.row_count = 3
        self.column_count = 9
        self.number_in_row_count = 5
        self.numbers = random.sample(range(1, 91), 15)
        self.kegs_count = 15
        self.distribution_row = list()
        for i in range(self.row_count):
            sort_to_max(self.numbers, self.number_in_row_count * i, self.number_in_row_count * (i + 1) - 1)
            self.distribution_row += random.sample(range(self.column_count), self.number_in_row_count)

    def __str__(self):
        card = ''
        num_index = 0
        for row in range(self.row_count):
            for col in range(self.column_count):
                if col in self.distribution_row[self.number_in_row_count * row: self.number_in_row_count * (row + 1)]:
                    card += ' ' * (2 - len(str(self.numbers[num_index]))) + str(self.numbers[num_index]) + ' '
                    num_index += 1
                else:
                    card += ' ' * 3
            card += '\n'
        return card

    def delete_number(self, keg):
        i = self.numbers.index(keg)
        self.numbers[i] = '-'
        self.kegs_count -= 1
        return True


if input("\nКак насчет партейки в Лото? y/n\n") == 'y':
    player_card = Cards()
    computer_card = Cards()
    kegs = random.sample(range(1, 91), 90)
    step = 0
    ans = ''
    while player_card.kegs_count > 0 and computer_card.kegs_count > 0:
        if ans == 'q':
             print('Жаль, пока!')
             exit()
        print('Tекущий номер |{}| (осталось {})'.format(kegs[step], 90 - step - 1))
        print('------ Ваша карточка -----')
        print(player_card)
        print('-- Карточка компьютера ---')
        print(computer_card)
        ans = input('Зачеркнуть цифру? (y/n/q): ')
        try:
            concurrence = player_card.delete_number(kegs[step])
        except ValueError:
            concurrence = False
        try:
            computer_card.delete_number(kegs[step])
        except ValueError:
            pass
        if (ans == 'y' and not concurrence) or (ans == 'n' and concurrence):
            print('Ошибка! Вы проиграли!')
            ans = 'q'
            exit()
        print()
        step += 1
    if player_card.kegs_count == 0:
        print('Вы выиграли!')
    elif computer_card.kegs_count == 0:
        print('Вы проиграли!')
    elif player_card.kegs_count == 0 and computer_card.kegs_count == 0:
        print('Ничья!')
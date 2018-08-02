__author__ = 'Мишин Егор Олегович'
# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.
print('\n Задача 1 - округление')


def my_round(number, ndigits):

   b=str(number).split('.')
   d=b[1]                     #вся дробная часть
   try:
       c=int((b[1])[ndigits:])            #лишняя часть дробной части
   except Exception:
       return number
   k = (len(str(d))-ndigits if len(str(d))-ndigits > 0 else 1)
   z='1'+'0'*k    #число по которому мы смотрим в какую сторону будет округление
   if (int(z)-c) >= c:
       itog = b[0]+ '.' + (b[1])[:ndigits]
   else:
       if len(str(int((b[1])[:ndigits]) + 1)) == ndigits:
           itog = float(b[0] + '.' + str(int((b[1])[:ndigits])+1))  #доп проверка на случай увеличения целой части числа
       else:
           itog = float(str(int(b[0])+1) + '.0')
   return itog

print(my_round(5.000006, 4) , round(5.000006, 4))
print(my_round(2.1999967, 5), round(2.1999967, 5))
print(my_round(2.9999967, 5), round(2.9999967, 5))


# print(my_round(2.1234567, 5))
#print(my_round(2.1999967, 5))
#print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить
print('\n Задача №2 - счастливый билетик')


def lucky_ticket(ticket_number):
    ticket_number = str(ticket_number)  # преобразуем число в строку
    sum1 = 0
    sum2 = 0

    if len(ticket_number) != 6:         # проверяем количество цифр
        ticket_number = 'Неверное число, должно быть шестизначное'
        return ticket_number            # Однако, если число начинается с 0, то программа работает некорректно
                                        # уже не успел попроавить эту особенность...
    for i in ticket_number[:3]:         # ищем сумму первых 3х цифр
        sum1 += int(i)
    for i in ticket_number[3:]:
        sum2 += int(i)

    if sum1 == sum2:
        ticket_number = 'Поздравляю! Билет счастливый'
    else:
        ticket_number = 'Не повезло =('

    return ticket_number


print('\n')
print(lucky_ticket(123456))
print(lucky_ticket(12321))
print(lucky_ticket(436751))

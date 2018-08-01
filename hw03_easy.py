# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

#a = []

def my_round(number, ndigits):
    pass
#     a.append([[number].index('.')])
# ##    b = str([number])
#     print(b, type(b), '.' in b)
# o = 0
    # for i in b[b.index('.')+1:]:
#     #     if ndigits < len(b):
#     #         for k in b[-1:b.index('.'+ndigits)]:
#     #             if int(k) > 4:
#     #                 if o != 0:
#     #
#     #                 o += 1
##i = -1
##while i !=


     #   else:
      #      0
  ##      a.append(i)



    # print(a)
#    for i in a[:]:
#         pass
#     print(type(a))
#     pass


# print(my_round(2.1234567, 5))
#print(my_round(2.1999967, 5))
#print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    ticket_number = str(ticket_number)  # преобразуем число в строку
    sum1 = 0
    sum2 = 0

    if len(ticket_number) != 6:         # проверяем количество цифр
        ticket_number = 'Неверное число, должно быть шестизначное'
        return ticket_number

    for i in ticket_number[:3]:         # ищем сумму первых 3х цифр
        sum1 += int(i)
    for i in ticket_number[3:]:
        sum2 += int(i)

    if sum1 == sum2:
        ticket_number = 'Поздравляю! Билет счастливый'
    else:
        ticket_number = 'Не повезло =('

    return ticket_number



print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))

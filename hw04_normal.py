__author__ = 'Мишин Егор Олегович'
# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.
print('\n Задача № 1 - Верхний регистр')

import re

line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO'\
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK'\
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn'\
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa'\
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete'\
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ'\
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb'\
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC'\
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB'\
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT'\
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu'\
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB'\
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa'\
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ'\
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'

print('\n Вариант с re: ', re.findall('[A-Z]*([a-z]+)[A-Z]', line))    # ищем совпадения по шаблону


i = 0
alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'                                     # строка с алфавитом из заглавных букв
l = ''
while i != len(line)-1:
    if line[i] in alp:
        #l += line[i] + ','
        while line[i] in alp:
            i += 1
        l += ','
    else:
        l += line[i]
        i+=1
print('\n Вариант без re: ', l)









# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.
print('\n Задача № 2 - 2 в нижнем и 2 в верхнем')

import re
line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm'\
       'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV'\
       'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA'\
       'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV'\
       'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW'\
       'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC'\
       'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR'\
       'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm'\
       'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn'\
       'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS'\
       'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf'\
       'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH'\
       'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN'\
       'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ'\
       'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'

print('\n Вариант с re: ', re.findall('[a-z]{2}([A-Z]+)[A-Z]{2}', line_2))
i = 2
alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alp1 = str.lower(alp)
l = ''
while i != len(line_2)-2:
    if line_2[i] in alp:
        if line_2[i-2] in alp1 and line_2[i-1] in alp1:
            l += ','
            while line_2[i+1] in alp and line_2[i+2] in alp:
                l += line_2[i]
                i += 1
        else:
            i += 1
        i += 1
    else:
        i += 1

    # if line_2[i] in alp:
    #     if line_2[i-1] and line_2[-2] in alp1:
    #         if line_2[i+1] and line_2[i+2] in alp:
    #
    #     #l += line[i] + ','
    #             l += line_2[i]
    #             i += 1
    #         else:
    #             i += 1
    #
    #     else:
    #         i += 1
    #     l += ','
    # else:
    #     l += line_2[i]
    #     i+=1
print('\n Вариант без re: ', l)


# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.
import random
import os

print('\n Задача № 3 - 2500')

z = 'C:\Projects\git\python'
path = os.path.join(z, str('number.txt'))
f = open(path, 'a', encoding = 'UTF-8')
num1 = ''
num = [random.randint(0, 9) for _ in range(2500)]
for i in num:
    num1 += str(i)
f.write(num1+'\n')
print(num, '\n', len(num))
f.close()


# num1 = [1, 2, 4, 4, 4, 2, 1, 0, 2, 2, 2, 2, 5, 7, 3, 2, 5, 1] - тестовый список для проверки

f = open(path, 'r', encoding = 'UTF-8')
v = f.read()
max = []
pret = []
i = 0
l = 1
while i != len(v)-1:
#while i != len(num1)-1:
    pret = [v[i]]
    while v[i] == v[i+1]:
        pret.append(v[i])
        i += 1
    if len(pret) > len(max):
        max = pret.copy()
        pret = []
    else:
        pass
    i += 1
    pret = []
print('максимальная последовательность: ', max)

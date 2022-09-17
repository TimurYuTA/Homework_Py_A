# Задача 1.
# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# a = input('\nВведите число: ')
# d = input('\nЗадайте точность от 10^(-1) до 10^(-10): ')
# list_a = a.split('.')
# count_a = 0
# count_d = 0
# for i in d.split('.')[1]: count_d += 1
# if float(a) % 1 != 0:
#     for i in a.split('.')[1]: count_a += 1
# if count_a > count_d: print(f'\n{a[:count_d - count_a]}\n')
# elif count_a < count_d:
#     for i in range(count_d - count_a): a = a + '0'
#     print(f'\n{a}\n')
# else: print(f'\n{a}\n')



# Задача 2.
# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# n = int(input('\nВведите натуральное число N: '))
# list_n = []
# i = 2
# while n > 1:
#     if n % i == 0:
#         list_n.append(i)
#         n = n / i 
#     else: i += 1
# print(f'\nСписок простых множителей вашего числа  -> {list_n}\n')



# Задача 3.
# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов 
# исходной последовательности.

# n = int(input('\nЗадайте количество чисел в последовательности: '))
# list_in = [int(input(f'Введите {i + 1}-е число: ')) for i in range(n)]
# list_out = []
# i = 0
# while i < n:
#     if list_in[i] in list_out: i += 1
#     else: 
#         list_out.append(list_in[i])
#         i += 1
# print(f'\n{list_in} -> {list_out}\n')



# Задача 4.
# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


# from random import randint


# k = int(input('\nВведите натуральную степень k: '))
# list_m = []
# for i in range(0, k + 1):
#     number = randint(0, 100)
#     if number != 0:
#         if number == 1:
#             if i == 0: list_m.insert(0, str(number))
#             elif i == 1: list_m.insert(0, 'x')
#             else: list_m.insert(0, 'x^' + str(i))
#         else:
#             if i == 0: list_m.insert(0, str(number))
#             elif i == 1: list_m.insert(0, str(number) + '*x')
#             else: list_m.insert(0, str(number) + '*x^' + str(i))
# str_m = ' + '.join(list_m) + ' = 0'
# with open('4-4.txt', 'w') as f: f.write(str_m)
# print(f'\n{str_m}\n')



# Задача 5.
# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, 
# содержащий сумму многочленов.

# from random import randint


# # Создаём два файла, в каждый из которых создаем и записываем многочлен
# for j in range(2):
#     k = int(input('\nВведите натуральную степень k: '))
#     list_m = []
#     for i in range(0, k + 1):
#         number = randint(0, 100)
#         if number != 0:
#             if number == 1:
#                 if i == 0: list_m.insert(0, str(number))
#                 elif i == 1: list_m.insert(0, 'x')
#                 else: list_m.insert(0, 'x^' + str(i))
#             else:
#                 if i == 0: list_m.insert(0, str(number))
#                 elif i == 1: list_m.insert(0, str(number) + '*x')
#                 else: list_m.insert(0, str(number) + '*x^' + str(i))
#     str_m = ' + '.join(list_m) + ' = 0'
#     with open(f'4-5-{j + 1}.txt', 'w') as file: file.write(str_m)

# # Считываем два файла, разделяем и записываем многочлены в списки 
# with open('4-5-1.txt', 'r') as file_1: list_1 = file_1.read()[:-4].split(' + ')
# with open('4-5-2.txt', 'r') as file_2: list_2 = file_2.read()[:-4].split(' + ')

# # Находим максимальную степень многочленов
# power = max(int(list_1[0].split('x^')[1]), int(list_2[0].split('x^')[1]))

# # Создаём список, и записываем туда сумму многочленов где степень >= 2
# list_sum = []
# i = 0
# while i < (power - 1):
#     if int(list_1[0].split('x^')[1]) == int(list_2[0].split('x^')[1]):
#         if '*x^' in list_1[0] and '*x^' in list_2[0]:
#             list_sum.append(str(int(list_1[0].split('*x^')[0]) + int(list_2[0].split('*x^')[0])) + '*x^' + str(int(list_1[0].split('*x^')[1])))
#         elif '*x^' in list_1[0] and 'x^' in list_2[0]:
#             list_sum.append(str(int(list_1[0].split('*x^')[0]) + 1) + '*x^' + str(int(list_1[0].split('*x^')[1])))
#         elif 'x^' in list_1[0] and '*x^' in list_2[0]:
#             list_sum.append(str(int(list_2[0].split('*x^')[0]) + 1) + '*x^' + str(int(list_1[0].split('*x^')[1])))
#         else: list_sum.append(str(2) + '*x^' + str(int(list_1[0].split('*x^')[1])))
#         list_1.pop(0)
#         list_2.pop(0)
#     else:
#         if int(list_1[0].split('x^')[1]) > int(list_2[0].split('x^')[1]): 
#             list_sum.append(list_1[0])
#             list_1.pop(0)
#         else: 
#             list_sum.append(list_2[0])
#             list_2.pop(0)
#     i += 1

# # Записываем сумму многочленов где степень = 1
# if '*x' in list_1[0] and '*x' in list_2[0]:
#     list_sum.append(str(int(list_1[0].split('*x')[0]) + int(list_2[0].split('*x')[0])) + '*x')
#     list_1.pop(0)
#     list_2.pop(0)
# elif '*x' in list_1[0] and 'x' in list_2[0]:
#     list_sum.append(str(int(list_1[0].split('*x')[0]) + 1) + '*x')
#     list_1.pop(0)
#     list_2.pop(0)
# elif 'x' in list_1[0] and '*x' in list_2[0]:
#     list_sum.append(str(int(list_2[0].split('*x')[0]) + 1) + '*x')
#     list_1.pop(0)
#     list_2.pop(0)
# elif 'x' in list_1[0] and 'x' in list_2[0]:
#     list_sum.append(str(2) + '*x')
#     list_1.pop(0)
#     list_2.pop(0)
# elif 'x' in list_1[0] and 'x' not in list_2[0]:
#     list_sum.append(list_1[0])
#     list_1.pop(0)
# elif 'x' not in list_1[0] and 'x' in list_2[0]:
#     list_sum.append(list_2[0])
#     list_2.pop(0)

# # Записываем сумму многочленов где нет "х"
# list_sum.append(str(int(list_1[0]) + int(list_2[0])))

# # Записываем полученный многочлен в файл и выводим в консоль
# str_sum = ' + '.join(list_sum) + ' = 0'
# with open('4-5-SUM.txt', 'w') as file_sum: file_sum.write(str_sum)
# print(f'\n{str_sum}\n')

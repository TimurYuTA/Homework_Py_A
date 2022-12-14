# Задача 1.
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# summ = 0
# for i in input('\nВведите вещественное число: ').translate({ord(i): None for i in ',.'}): summ = summ + int(i)
# print(f'\nСумма цифр введённого числа -> {summ}\n')



# Задача 2.
# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# n = int(input('\nВведите число N: '))
# while n < 1:
#     n = int(input('Введите целое число N >= 1 : '))
# product_n = [1]
# if n == 1:
#     print(f'\nНабор произведений чисел от 1 до {n} -> {product_n}\n')
# else:
#     for i in range(1, n):
#         product_n.append(product_n[i - 1]*(i + 1))
#     print(f'\nНабор произведений чисел от 1 до {n} -> {product_n}\n')



# Задача 3.
# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# n = int(input('\nВведите количество элементов в списке: '))
# list_n = []
# sum_n = 0
# for i in range(1, n + 1):
#     list_n.append(round((1 + 1 / i) ** i, 2))
#     sum_n = sum_n + list_n[i-1]
# print(f'\n{list_n} -> {sum_n}\n')



# Задача 4.
# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

# from random import randint


# n = int(input('\nВведите количество элементов в списке: '))
# list_n = []
# for i in range(n):
#     list_n.append(randint(-n, n))
# with open('file.txt', 'r') as file:
#     print(f'\n{list_n}\n\nПроизведение элементов -> {list_n[int(file.readline())] * list_n[int(file.readline(2))]}\n')



# Задача 5.
# Реализуйте алгоритм перемешивания списка.

# from random import randint


# list_in = [1, 2, 3, 4, 5]
# list_index = []
# list_out = []
# for i in range(len(list_in)):
#     j = randint(0, len(list_in) - 1)
#     while j in list_index:
#             j = randint(0, len(list_in) - 1)
#     else:
#         list_index.append(j)
#         list_out.append(list_in[j])
# print(f'\n{list_in} -> {list_out}\n')

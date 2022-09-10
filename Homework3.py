# Задача 1.
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# list_in = []
# list_odd = []
# sum_odd = 0
# for i in range(int(input('\nВведите количество элементов в списке: '))):
#     list_in.append(int(input('Введите значение элемента: ')))
#     if i == 1 or i % 2 != 0:
#         sum_odd += list_in[i]
#         list_odd.append(list_in[i])
# print(f'\n{list_in} -> на нечётных позициях элементы {list_odd}, ответ: {sum_odd}\n')



# Задача 2.
# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# n = int(input('\nВведите количество элементов в списке: '))
# list_in = []
# list_out = []
# for i in range(n):
#     list_in.append(int(input('Введите значение элемента: ')))
# for i in range(round(n / 2 + 0.1)):
#     list_out.append(list_in[i] * list_in[n - 1 - i])
# print(f'\n{list_in} => {list_out}\n')



# Задача 3.
# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным 
# и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# n = int(input('\nВведите количество элементов в списке: '))
# list_in = []
# f_max = 0.0
# f_min = 0.0
# for i in range(n):
#     list_in.append(float(input('Введите значение элемента: ')))
#     if list_in[i] % 1 > f_max:
#         f_max = list_in[i] % 1
#     if list_in[i] % 1 < f_min:
#         f_min = list_in[i] % 1
# print(f'\n{list_in} => {str(f_max - f_min)[:4]}\n')



# Задача 4.
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# n = int(input('\nВведите десятичное число: '))
# list_bin = []
# while n / 2 >= 0.5:
#     list_bin.append(int(n % 2))
#     n = (n - n % 2) / 2
# print(f'{list_bin} -> {str(list_bin)[::-1]}')


n = int(input('\nВведите десятичное число: '))
list_bin = []
while n / 2 >= 0.5:
    list_bin.insert(0, int(n % 2))
    n = (n - n % 2) / 2
print(*list_bin)



# Задача 5.
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
# [Негафибоначчи]

'''
Задача 32: 
Определить индексы элементов массива (списка), 
значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)

Ввод: [-5, 9, 0, 3, -1, -2, 1,
4, -2, 10, 2, 0, -9, 8, 10, -9,
0, -5, -5, 7]
Вывод: [1, 9, 13, 14, 19]
'''

numbers = int(input("Введите количество элементов для начального массива: "))
left_bound = 5
rigth_bound = 15

import random

list_rand = [random.randint(left_bound * (-2), rigth_bound * 2) for i in range(numbers)]
print(f'Начальный список: {list_rand}')

result = [i for i in range(numbers) if left_bound <= list_rand[i] <= rigth_bound]
print(f'Список индексов: {result}')
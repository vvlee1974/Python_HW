'''Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.'''

number = int(input("Введите число N: "))
a = 2
k = 0

for n  in range(number):
    n = a ** k
    if n < number:
        print(f'2 в степени {k} = {n}')
    else:
        break
    k = k + 1
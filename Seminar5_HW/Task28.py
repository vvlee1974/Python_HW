''' Задача 28: 
Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
Из всех арифметических операций допускаются только +1 и -1. 
Также нельзя использовать циклы.

*Пример:*

2 2
    4 
'''
def sum(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    
    if a >= b:
        return sum(a + 1, b - 1)
    return sum(a - 1, b + 1)
    
        
a = int(input("Введите число А: "))
b = int(input("Введите число В: "))

if a >= 0 and b >= 0:
    print(f'Сумма чисел {a} + {b} = {sum(a, b)}')
else:
    print("Введите положительное число ")
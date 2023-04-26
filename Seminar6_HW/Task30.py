''' Задача 30:  
Заполните массив элементами арифметической прогрессии. 
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.

Пример:
Ввод: 7 2 5

Вывод: 7 9 11 13 15
'''
first_number = int(input("Введите первое число: "))
dif = int(input("Введите разность: "))
numbers = int(input("Введите количество элементов: "))

list = []
for i in range(numbers):
    list.append(first_number + (numbers - 1) * dif)
    numbers -= 1
print(f'Результат: {sorted(list)}')


''' Вариант 2'''
# number = input("Введите три числа через пробел: ")
# list1 = list(map(int, number.split()))

# list2 = []
# for i in range(list1[0], list1[0] + list1[2] * list1[1], list1[1]):
#     list2.append(i) 
#     #print(i)

# print(f" Результат: {sorted(list2)}")
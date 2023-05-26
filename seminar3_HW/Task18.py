'''Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*
5
1 2 3 4 5
6
-> 5'''

len_list = int(input("Введите количество элементов в списке: "))
number = int(input("Введите число: "))
min = 0
tmp = 0
 
rand_list=[]
import random

for i in range(len_list):
    rand_list.append(random.randint(1,len_list))
    
    if rand_list[i] < number:
        tmp = rand_list[i]
        if tmp > min:
            min = tmp

print(*rand_list)
print(f'Ближайшее наименьшее число: {min}')
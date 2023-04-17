'''Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
1 2 3 4 5
3
-> 1'''

len_list = int(input("Введите количество элементов в списке: "))
number = int(input("Введите искомое число: "))
count = 0

import random
 
rand_list=[]

for i in range(len_list):
    rand_list.append(random.randint(1,len_list))
    if rand_list[i] == number:
        count += 1
        
print(*rand_list)
print(f'В списке число {number} повторяется {count} раз(а)')
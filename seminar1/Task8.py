'''Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

*Пример:*

3 2 4 -> yes
3 2 1 -> no'''

n = int(input("Введите число для n: "))
m = int(input("Введите число для m: "))
k = int(input("Введите число для k: "))

sum = n * m

if k < sum and (k % n == 0 or k % m == 0):
    if (n < m and k <= sum - n) or (n > m and k <= sum - m) or (n == m and k <= sum - n):
        print("yes")
else:
    print("no")
'''
Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, 
что Петя и Сережа сделали одинаковое количество журавликов, 
а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

*Пример:*

6 -> 1  4  1
24 -> 4  16  4
60 -> 10  40  10
'''

n = int(input("Введите общее количество бумажных журавликов: "))

if n % 6 == 0:
    p = n // 6
    s = p
    k = n - s * 2
    print(f"Петя: {p}, Катя: {k}, Серёжа: {s}")
else:
    print("Введённое число не соответствует условию задачи. Повторите ввод")


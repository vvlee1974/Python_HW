''' Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

*Пример:*

**Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
    **Вывод:** Парам пам-пам '''

poem = "Пам-па-рам рАм-па-раМ тра-Ля-ля" 

alphabet = ['-', "а", "б", 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
vowel_letters = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']


def rhythm_poem(poem):
    p = list(map(list, poem.lower().split()))
    #print(p)
    f = lambda x: sum(1 for i in x if i in vowel_letters)
    tmp = f(p[0])
    f2 = lambda x: sum(1 for i in x if i not in alphabet)
    tmp2 = 0
    
    if all([f(i) == tmp for i in p]) and all([f2(i) == tmp2 for i in p]):
        return "Парам пам пам"
    return "Пам парам"
            
print(rhythm_poem(poem))
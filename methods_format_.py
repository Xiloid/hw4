"""
    1. Если в строке больше символов в нижнем регистре - вывести все в нижнем,
        если больше в верхнем - вывести все в верхнем,
        если поровну - вывести в противоположных регистрах.
    2. Если в строке каждое слово начинается с заглавной буквы, тогда
        добавить в начало строки 'done. '.
        Иначе заменить первые 5 элементов строки на 'draft: '.
    (можно использовать метод replace и/или конкатенацию строк + срезы)
    3. Если длина строки больше 20, то обрезать лишние символы до 20.
        Иначе дополнить строку символами '@' до длины 20.
    (можно использовать метод ljust либо конкатенацию и дублирование (+ и *))
    После выполнения кажого пункта выводить результат типа:
        1. Исходная строка: "some string".
        Результат: "some edited string".
    (Использовать форматирование строк f либо метод format)
"""
flag = flag2 = 0
low_char = big_char = i = 0
string = input('Введите строку: ')
for i in string:                                                    # ПЕРВЫЙ ПУНКТ ЗАДАНИЯ
    if str.isupper(i):
        big_char += 1
    elif str.islower(i):
        low_char += 1
if big_char > low_char:
    print('Больше заглавных: ', string.upper())
elif big_char < low_char:
    print('Больше строчных: ', string.lower())
else:
    print('Заглавных и строчных поровну:', string.swapcase())
for i in string:                                                     # ВТОРОЙ ПУНКТ ЗАДАНИЯ
    if i != ' ' and flag == 0:
        flag = 1
        if i.islower():
            flag2 = 1
    else:
        if i == ' ':
            flag = 0
if flag2 == 0:
    print('DONE.', string)
else:
    repl = string[0:4]
    print(string.replace(repl, 'DRAFT: '))
long = len(string)                                                  # ТРЕТИЙ ПУНКТ ЗАДАНИЯ
if long > 20:
    string = string[:20]
    print('Обрезанная строка до 20 символов: ', string)
else:
    print('Дополненная строка до 20 символов:', string.ljust(20, '@'))

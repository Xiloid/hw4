"""
    Вводится строка.
    1. Вывести количество слов в введенной строке.
    2. Вывести самое длинное слово и его длину.
"""
count = flag = numlet = ind = big = 0
string = input('Введите строку: ')
for i in range(len(string)):
    if string[i] != ' ' and flag == 0:
        count += 1
        flag = 1
    else:
        if string[i] == ' ':
            flag = 0
    if string[i] != ' ':
        numlet += 1
    else:
        if numlet > big:
            big = numlet
            ind = i - numlet
        numlet = 0
if numlet > big:
    m = numlet
    ind = i - numlet + 1
print(f'В строке слов: {count}')
print(f'Самое длинное слово: "{string[ind:ind + big]}" и в этом слове {big} букв')

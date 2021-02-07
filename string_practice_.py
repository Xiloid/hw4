string = 'Lorem, Ipsum, is, simply, dummy, text, of, the, printing, industry.'
# 1. Изменить строку таким образом, чтоб вместо ', ' был пробел ' '
#    Результат: 'Lorem Ipsum is simply dummy text of the printing industry.'
new_string = string.replace(',', '')
print('1) Строка без запятых:', new_string)
# 2. Найти индекс самой последней буквы 's' в строке.
#    Результат: 53
print('2) Индекс последней буквы S в строке:', new_string.rfind('s'))
# 3. Найти количество букв 'i' в строке (регистр не имеет значения).
#    Результат: 6
little = new_string.count('i')
big = new_string.count('I')
print(f'3) {little + big} заглавных + строчных букв')
# 4. Найти и вывести срез строки.
#    Результат: 'simply dummy text'
#    (используйте методы find или index для получения индексов)
# s = input('Введите начало среза: ')
# n = input('Введите конец среза: ')
s = 'simply'
n = 'text'
l = new_string.find(s)
l2 = new_string.rfind(n) + len(n)
print('4) Обрезок строки:', new_string[l:l2])
# 5. Продублируйте первую половину строки 3 раза и склейте с второй половиной
#    и выведите на экран.
#    Результат: 'Lorem Ipsum is simply dummy tLorem Ipsum is simply dummy tLorem Ipsum is simply dummy text of the printing industry.'
cutted = len(new_string) // 2
cutted_start = new_string[0:cutted]
cutted_end = new_string[cutted:len(new_string)]
new_string2 = cutted_start * 3 + cutted_end
print('5) Продублированная и склеенная строка:', new_string2)






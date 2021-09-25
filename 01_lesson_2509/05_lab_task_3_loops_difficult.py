'''Задаче должно быть все равно: A < B or B < A'''
summary = 0
a = int(input('Введите а: '))
b = int(input('Введите b: '))

if a < b:
    for number in range(a, b + 1, 1):  # последовательность от а до б включительно
        summary += number  # инкрементировать (увеличить с присваиванием) summary
else:
    for number in range(a, b - 1, -1):  # последовательность от а до б включительно
        summary += number  # инкрементировать (увеличить с присваиванием) summary

print(f'Сумма всех чисел от {a} до {b} = {summary}')

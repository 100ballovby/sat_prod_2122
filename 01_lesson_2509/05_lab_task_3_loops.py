summary = 0
a = int(input('Введите а: '))
b = int(input('Введите b: '))

for number in range(a, b + 1):  # последовательность от а до б включительно
    summary += number  # инкрементировать (увеличить с присваиванием) summary

print(f'Сумма всех чисел от {a} до {b} = {summary}')

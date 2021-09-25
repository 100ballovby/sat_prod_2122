from math import sqrt
a = int(input('Введите a: '))
b = int(input('Введите b: '))

print(f'Среднее геометрическое: {sqrt(a * b)}')
print(f'Среднее гармоническое: {(2 * a * b) / (a + b)}')
print(f'Среднее квадратичное: {sqrt((a ** 2 + b ** 2) / 2)}')

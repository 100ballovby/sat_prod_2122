'''
range(5) -> 0, 1, 2, 3, 4
range(7, 11) -> 7, 8, 9, 10
range(1, 11, 2) -> 1, 3, 5, 7, 9
'''

num1 = int(input('Для какого числа? '))
num2 = int(input('До какого числа? '))

for i in range(1, num2 + 1):
    # от num1 до num2 включительно делать:
    print(f'{num1} * {i} = {num1 * i}')



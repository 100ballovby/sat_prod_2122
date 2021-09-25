'''Среди чисел 1, 5, 10, 16, 23, ... найти первое число, большее n.
Условный оператор не использовать. Решить задачу используя циклическую
конструкцию while.'''

step = 4  # шаг смены последовательности
n = int(input('Введите число: '))  # число, с которым сравниваем
i = 1  # управляющая переменная

while i < n:  # когда n станет больше, цикл остановится. Условного оператора нет, но условие есть
    print(i)  # выводим числа
    i += step  # увеличиваем управляющую переменную цикла на шаг
    step += 1  # шаг увеличиваем на 1

print(f'Число большее {n} - {i}')



'''
try:
    do_smth()
except:
    do_another()
else:
    do_else()
finally:
    do_finnally()

Types of exceptions:
ImportError - ошибка импорта библиотеки/модуля
IndexError - неправильное обращение к индексу
KeyError - неправильное обращение к ключу словаря
NameError - обращение к переменной, которой нет
TypeError - неправильный тип данных
ValueError - функция не получает аргумент правильного типа
ZeroDivisionError - деление на 0
ArithmeticError - ошибка вычислений
OSError - ошибки, возникающие при работе с ОС компьютера
'''
divider = int(input('Введите число: '))

try:  # попробуй сделать это:
    print(235 / divider)
except ZeroDivisionError:  # если произошло деление на 0
    print('На 0 делить нельзя!')

print('hello')



divider = input('Введите число: ')

try:  # попробуй сделать это:
    divider = int(divider)
    print(235 / divider)
except ZeroDivisionError:  # если произошло деление на 0
    print('На 0 делить нельзя!')
except ValueError:
    print('Вы ввели не число!')
except:
    print('Все плохо! Зови сисадмина!')
print('hello')
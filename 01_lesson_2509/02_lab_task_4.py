'''
2π * r^2 + 2π * r * h
'''
from math import pi

radius = float(input('Радиус круга: '))
height = float(input('Высота цилиндра: '))

s = (2 * pi * (radius ** 2)) + (2 * pi * radius * height)
print(f'Площадь цилиндра: {round(s, 4)} см^2')
# round(obj, n) - округлить число obj до n знаков после запятой

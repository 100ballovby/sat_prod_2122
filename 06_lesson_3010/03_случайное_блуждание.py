import random as r
import matplotlib.pyplot as plt

points = 5000  # количество точек в блуждании
x_val = [0]  # список координат для каждой точки
y_val = [0]  # список координат для каждой точки

while len(x_val) < points:
    x_direction = r.choice([1, -1])
    x_distance = r.choice(range(5))
    x_step = x_distance * x_direction

    y_direction = r.choice([1, -1])
    y_distance = r.choice(range(5))
    y_step = y_distance * y_direction

    if x_step == y_step == 0:  # игнорирую нулевое перемещение
        continue  # пропуск итерации цикла

    # вычисление следующих значений х и у
    next_x = x_val[-1] + x_step  # последняя координата точки + шаг
    next_y = y_val[-1] + y_step  # последняя координата точки + шаг

    # записываю координаты
    x_val.append(next_x)
    y_val.append(next_y)

plt.scatter(x_val, y_val, s=5)
plt.show()

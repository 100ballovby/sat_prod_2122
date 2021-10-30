import random as r
import matplotlib.pyplot as plt

points = 100000
x_val = [0]
y_val = [0]

while len(x_val) < points:
    x_direction = r.choice([1, -1])
    x_distance = r.choice(range(5))
    x_step = x_distance * x_direction

    y_direction = r.choice([1, -1])
    y_distance = r.choice(range(5))
    y_step = y_distance * y_direction

    if x_step == y_step == 0:
        continue
    next_x = x_val[-1] + x_step
    next_y = x_val[-1] + y_step

    x_val.append(next_x)
    y_val.append(next_y)

plt.scatter(x_val, y_val, s=5)
plt.show()
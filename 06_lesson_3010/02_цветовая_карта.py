import matplotlib.pyplot as plt

x_axis = list(range(1, 1001))  # список чисел от 1 до 1000
y_axis = [i ** 2 for i in x_axis]  # квадраты списка чисел от 1 до 1000

x_axis_2 = [i for i in range(2000, 1125, -1)] + [j for j in range(1000, 750, -2)]
print(len(x_axis_2))
plt.scatter(x_axis, y_axis, c=y_axis, cmap=plt.cm.inferno,
            edgecolors='none', s=40)
plt.scatter(x_axis_2, y_axis, c=y_axis,
            cmap=plt.cm.GnBu, edgecolors='none', s=40)
plt.show()


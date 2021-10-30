import matplotlib.pyplot as plt

transistors = []
intel_4004 = 2300
for i in range(30):
    transistors.append(intel_4004)
    intel_4004 *= 2  # intel_4004 = intel_4004 * 2
print(transistors)
years = range(1971, 2001)

plt.plot(years, transistors, linewidth=5)  # построить график с шириной линии 5
plt.title('Количество транзисторов на процессорах с 1971 года',
          fontsize=24)  # название диаграммы
plt.xlabel('Года', fontsize=14)
plt.ylabel('Транзисторы', fontsize=14)

# управляю размером шрифта на осях графика
plt.tick_params(axis='both', labelsize=14)
plt.show()  # показать

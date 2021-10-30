import matplotlib.pyplot as plt

transistors = []
intel_4004 = 2300
for i in range(30):
    transistors.append(intel_4004)
    intel_4004 *= 2  # intel_4004 = intel_4004 * 2
print(transistors)
plt.plot(transistors)  # построить график
plt.show()  # показать

import random as r

rlist = [r.randint(1, 100) for i in range(20)]

print(rlist)
summary = 0
for number in rlist:  # для каждого числа в списке
    # summary = summary + number
    summary += number  # прибавлять число из списка к переменной
print(summary)  # получается сумма всех чисел


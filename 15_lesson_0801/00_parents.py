def parent(num):
    def child_1():  # датчик
        return 'Printing from the first child function'

    def child_2():  # мотор
        return 'Printing from the second child function'

    if num == 1:
        return child_1
    else:
        return child_2


d = parent(1)
m = parent(2)

print(parent)
print(d())
print(m())



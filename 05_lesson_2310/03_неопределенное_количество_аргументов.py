def star_arg(*x) -> tuple:
    print(type(x))
    return x

print(star_arg(4, 5, 6, 7))


def middle_mark(*students) -> float:
    length = len(students)  # количество баллов
    summ = 0  # сумма баллов
    for mark in students:  # перебираю каждую оценку
        summ += mark  # считаю сумму баллов
    return summ / length  # нахожу среднюю


print(middle_mark(7, 8, 4, 5, 3, 5, 6, 8))

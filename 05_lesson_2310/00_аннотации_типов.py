def sqrt(n: int) -> float:  # параметр n
    """
    Функция считает квадратный корень
    :param n: число, передаваемое пользователем
    :return: float - квадратный корень числа n
    """
    n **= 0.5  # local
    return n
# global

print(sqrt(56))  # аргумент n



z = 3.14927563
print(round(z))  # 3
print(round(z, 4))  # 3.1493


def my_plus(a: int, b: int, c: int = 0) -> int:
        return a + b + c


print(my_plus(5, 6))  # 11
print(my_plus(5, 6, 3))  # 14
print(my_plus(c=3, a=15, b=7))

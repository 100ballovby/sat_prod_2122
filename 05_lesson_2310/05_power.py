def power(a: int, n: int) -> int:
    b = a
    for i in range(n - 1):
        b *= a
    return b


print(power(0, 0))




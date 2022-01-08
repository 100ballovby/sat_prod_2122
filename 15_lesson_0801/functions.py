def factorial(n):
    if n <= 1:
        return n
    else:
        return n * factorial(n - 1)


if __name__ == '__main__':  # если вызывается ИМЕННО ЭТОТ ФАЙЛ
    for i in range(1, 10):
        print(factorial(i))


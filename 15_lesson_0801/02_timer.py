import time


def timer(func):
    """Print the runtime of the decorated function"""
    def wrapper(*args):
        start = time.perf_counter()  # точка начала работы
        value = func(*args)  # вызываю функцию и сохраняю результат работы в переменной
        end = time.perf_counter()  # точка окончания работы
        run_time = end - start  # замеряю разницу
        print(f'Finished {func.__name__}! in {run_time:.4f} seconds')
        return value
    return wrapper


def slow_down(func):
    """Sleep 1 second before calling the function"""
    def wrapper_slow(*args):
        time.sleep(1)  # ничего не делать 1 секунду
        return func(*args)
    return wrapper_slow


@slow_down
def countdown(number):
    if number < 1:
        print('Ффффсё!')
    else:
        print(number)
        countdown(number - 1)


countdown(7)

@timer
def waste_some_time(iters: int):
    for i in range(iters):
        sum([i ** 3 for i in range(1000)])


waste_some_time(1)
waste_some_time(10000)

def my_decorator(f):
    def wrapper(*args):
        print('Do smth before')
        f(*args)
        print('Do smth after')
    return wrapper


@my_decorator
def say_hello(name):
    print(f'Hello {name}')


say_hello()




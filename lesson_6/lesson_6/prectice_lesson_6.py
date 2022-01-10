

def decorator(func):
    def wrapper(*args, **kwargs):
        print('я сделал')
        res = func(*args, **kwargs)
        return res

    return wrapper


@decorator
def summ(a, b):
    return a - b


test = summ(2, 5)

print(test)


def some_func():
    a = 2
    b = 4
    print(a + b)
    print(f'{some_func.__name__}')


some_func()


def log(func):
    print(f'Функция {func.__name__} отработала')

    def wrapper(*args, **kwargs):
        res = func(*args)
        return res

    return wrapper


@log
def calc(a, b):
    return a + b


calc(2, 4)

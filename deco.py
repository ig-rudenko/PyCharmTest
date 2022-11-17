import time


def timer(function):
    print('Зашли в timer')

    def wrapper(*args, **kwargs):
        """Декоратор"""

        print('Начало декоратора')
        start: float = time.time()

        result = function(*args, **kwargs)

        end: float = time.time()

        return result

    print("Передали в функцию wrapper", function.__name__)
    return wrapper


@timer
def factorial(n):
    if n == 0:
        return 1
    x = 1
    for i in range(1, n + 1):
        x *= i
    return x


factorial(900)

factorial(30000)

factorial(40000)

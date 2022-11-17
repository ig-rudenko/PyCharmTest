import time


# Декоратор
def timer(function):
    print('Зашли в timer')

    def wrapper(*args, **kwargs):
        """Декоратор"""

        print('Начало декоратора')
        start: float = time.time()

        result = function(*args, **kwargs)  # Вызов функции <<<<<<<<<<<<<<<<<<<<<

        end: float = time.time()
        print(
            "Время выполнения функции",
            function.__name__,
            f"args = {args}",
            end - start
        )

        return result  # Результат!!!!

    print("Передали в функцию wrapper", function.__name__)
    return wrapper


@timer  # factorial = timer(factorial)
def factorial(n):
    if n == 0:
        return 1
    x = 1
    for i in range(1, n + 1):
        x *= i
    return x


@timer
def factorial_rec(n):
    if n == 0:
        return 1
    return n * factorial_rec(n - 1)


factorial(900)

factorial(30000)

factorial(40000)

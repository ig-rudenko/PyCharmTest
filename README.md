# PyCharmTest

Писать, что это такое

```python
import time

def timer(function):
    print('Зашли в timer')

    def wrapper(*args, **kwargs):
        """Декоратор"""

        print('Начало декоратора')
        start: float = time.time()

        result = function(*args, **kwargs)

        end: float = time.time()

        print(f"Время выполнения функции {function.__name__} -> {end - start} сек")

        return result

    print("Передали в функцию wrapper", function.__name__)
    return wrapper

```

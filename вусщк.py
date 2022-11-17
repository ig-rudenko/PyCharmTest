import time


def calc1():
    s = 1
    for i in range(1, 20000):
        s *= i
    return s


def calc2():
    s = 1
    for i in range(1, 30000):
        s *= i
    return s


def calc3():
    s = 1
    for i in range(1, 40000):
        s *= i
    return s


start: float = time.time()
print(start)
# Выполняем что-то
calc1()  # <----------------------------------------- <<<<
# Смотрим, сколько сейчас времени
end: float = time.time()
print("Время выполнения функции calc1", end - start)

start: float = time.time()
# Выполняем что-то
calc2()  # <----------------------------------------- <<<<
# Смотрим, сколько сейчас времени
end: float = time.time()
print("Время выполнения функции calc2", end - start)

start: float = time.time()
# Выполняем что-то
calc3()  # <----------------------------------------- <<<<
# Смотрим, сколько сейчас времени
end: float = time.time()
print("Время выполнения функции calc3", end - start)

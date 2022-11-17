# Функция реверса матрицы
def rv_matrix(mn):
    for row in mn:
        row.reverse()
    return mn.reverse()


matrix = [
    [0, 1, 2, 3, 4],
    [10, 11, 12, 13, 14],
    [20, 21, 2232, 23, 24],
    [30, 31, 32, 33, 34],
    [40, 41, 42, 43, 44]
]

rv_matrix(matrix)


# Функция определения самого большого элемента в матрице
def len_matrix(mn):
    l = 0
    for row in mn:
        for number in row:
            if number > l:
                l = int(number)
    return l


len_matrix(matrix)

for row in matrix:
    for number in row:
        if 10 <= number < 100:
            print(number, end=' ')
        elif number < 10:
            print(number, end='   ')
        else:
            print(number, end=' ')
    print()

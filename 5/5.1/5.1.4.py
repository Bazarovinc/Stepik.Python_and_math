"""Функция, возвращающая массив только с четными элементыми из массива слуайных чисел."""


def even_values(L):
    new_L = []
    for elem in L:
        if elem % 2 == 0:
            new_L.append(elem)
    return new_L


def even_values_1(L):
    return [elem for elem in L if elem % 2 == 0]

print(even_values([1, 2, 3, 4, 5, 6, 7, 8]))
print(even_values_1([1, 2, 3, 4, 5, 6, 7, 8]))

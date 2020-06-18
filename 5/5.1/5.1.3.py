"""Функция, возвращающая числа массива с четным индексом."""


def even_indeces(L):
    new_L = []
    for i in range(len(L)):
        if i % 2 == 0:
            new_L.append(L[i])
    return new_L


def even_indeces_1(L):
    return L[::2]

print(even_indeces([1, 2, 3, 4, 5 , 7]))
print(even_indeces_1([1, 2, 3, 4, 5 , 7]))
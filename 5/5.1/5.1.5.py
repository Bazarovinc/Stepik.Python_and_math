"""Функция, возвращающая развернутый массив элементов"""


def last_to_first(L):
    return L[::-1]

def last_to_first_1(L):
    new_L = L[:]
    new_L.reverse()
    return new_L

print(last_to_first([1, 2, 3, 4, 5, 6, 7]))
print(last_to_first_1([1, 2, 3, 4, 5, 6, 7]))

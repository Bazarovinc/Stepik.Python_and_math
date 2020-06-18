"""Функция, которая возвращает список общих элементов двух массивов"""


def common(L1, L2):
    new_L = []
    for elem in L1:
        if elem in L2:
            new_L.append(elem)
    return new_L


def common_1(L1, L2):
    return list(set(L1) & set(L2))


L1 = [10, 1031, 3312, 3, 1, 13, 52, 2, 0]
L2 = [11, 101, 312, 313, 1, 13, 52, 2, 0]
print(common(L1, L2))
print(common_1(L1, L2))
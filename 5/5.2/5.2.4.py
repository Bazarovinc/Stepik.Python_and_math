def func(elem):
    for e in elem:
        return e


def list_pull(L):
    new_L = []
    for elem in L:
        while True:
            if type(elem[0]) is not list:
                break
            else:
                elem = func(elem)
        if len(elem) != 0:
            for e in elem:
                new_L.append(e)
    return new_L


print(list_pull([['one'], [343, 2], [[9, 9, 9], [[666, 666], [[[[42]]]]]]]))

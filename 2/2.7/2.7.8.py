def convert(L):
    l = []
    for n in L:
        l.append(int(n))
    return l

def maxld(L):
    L = convert(L)
    return L.index(max(L))

print(maxld([1, 2, '42', '3', '4', '5', 6, 13]))
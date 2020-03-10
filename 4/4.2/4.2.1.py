def luka(L0, L1, n):
    Luka = []
    Luka.append(L0)
    Luka.append(L1)
    if n > 1:
        i = 1
        while i != n + 1:
            Luka.append(Luka[-1] + Luka[-2])
            Luka = Luka[-2:]
            i += 1
        return Luka[-1]
    else:
        return Luka[n]


print(luka(0, 9, 5))

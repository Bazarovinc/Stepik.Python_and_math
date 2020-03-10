from decimal import *
getcontext().prec = 50

def luka(L0, L1, n):
    Luka = []
    Luka.append(L0)
    Luka.append(L1)
    if n > 1:
        i = 1
        while i != n:
            Luka.append(Luka[-1] + Luka[-2])
            Luka = Luka[-2:]
            i += 1
        return Decimal(Luka[-1]) / Decimal(Luka[-2])

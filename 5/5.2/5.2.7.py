def front_back(a, b):
    a1, a2, b1, b2, s = '', '', '', '', ''
    if len(a) % 2 != 0:
        a1 = a[:((len(a) // 2) + 1)]
        a2 = a[((len(a) // 2) + 1):]
    else:
        a1 = a[:(len(a) // 2)]
        a2 = a[(len(a) // 2):]
    if len(b) % 2 != 0:
        b1 = b[:((len(b) // 2) + 1)]
        b2 = b[((len(b) // 2) + 1):]
    else:
        b1 = b[:(len(b) // 2)]
        b2 = b[(len(b) // 2):]
    s = a1 + b1 + a2 + b2
    return s


print(front_back('abcde', 'xy1'))

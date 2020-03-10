alphabet = 'ABCDEFGHIJKLMNOPQRSUVWXYZ'

def base_10(n, base):
    s = ''
    while n > 0:
        if base > 10 and n % base >= 10:
            s += alphabet[(n % base) - 10]
        else:
            s += str(n % base)
        n //= base
    return s[::-1]


def convert_to_10(n, base, to_base):
    n1 = 0
    size = len(n) - 1
    for i in n:
        if i in alphabet:
            n_a = int(alphabet.find(i) + 10)
            n1 += n_a * pow(base, size)
        else:
            n1 += int(i) * pow(base, size)
        size -= 1
    return base_10(n1, to_base)


def convert(n, to_base=10, from_base=10):
    if from_base == 10:
        return base_10(int(n), to_base)
    else:
        return convert_to_10(n, from_base, to_base)


print(convert('GHJJEN13424KH4', to_base=10, from_base=36))

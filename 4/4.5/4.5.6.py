import random


def disc_generator(alphabet):
    al = []
    for a in alphabet:
        al += a
    #random.seed(version=2)
    random.shuffle(al)
    alphabet = ''
    for a in al:
        alphabet += a
    return alphabet


def discs_generator(n, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    discs = []
    for i in range(n):
        discs.append(disc_generator(alphabet))
    return discs


def jefferson_encryption(text, discs, step, reverse=False):
    zcaesar = ''
    i = 0
    if reverse:
        step = -step
    for x in text.upper():
        alphabet = discs[i]
        if x in alphabet:
            zcaesar += alphabet[(alphabet.find(x) + step) % len(alphabet)]
            if i + 1 < len(discs):
                i += 1
            else:
                i = 0
    return zcaesar


discs = discs_generator(6)
print(jefferson_encryption("Some encripted text", discs, 4))
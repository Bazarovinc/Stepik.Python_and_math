import random

def disc_generator(alphabet):
    al = []
    for a in alphabet:
        al += a
    random.seed(a=42, version=2)
    random.shuffle(al)
    alphabet = ''
    for a in al:
        alphabet += a
    return alphabet

print(disc_generator("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
def caesar(text, key, alfabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    zcaesar = ''
    for x in text.upper():
        if x in alfabet:
            zcaesar += alfabet[(alfabet.find(x) + key) % len(alfabet)]
    return zcaesar


def bruteforce(text, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    key = -1
    while abs(key) != len(alphabet):
        print(caesar(text, key, alphabet))
        key -= 1


print(bruteforce("BQQMF"))
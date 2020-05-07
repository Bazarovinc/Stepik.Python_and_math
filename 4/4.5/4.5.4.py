def numerics(n):
    nums = []
    while n > 0:
        nums.append(n % 10)
        n //= 10
    nums.reverse()
    return nums


def jarriquez_encryption(text, key, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ', reverse=False):
    key = numerics(key)
    if reverse:
        for i in range(len(key)):
            key[i] = -key[i]
    i = 0
    zcaesar = ''
    for x in text.upper():
        if x in alphabet:
            zcaesar += alphabet[(alphabet.find(x) + key[i]) % len(alphabet)]
            if i + 1 < len(key):
                i += 1
            else:
                i = 0
    return zcaesar


print(jarriquez_encryption("У СУДЬИ ЖАРРИКЕСА ПРОНИЦАТЕЛЬНЫЙ УМ", 423, alphabet="АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ", reverse=True))
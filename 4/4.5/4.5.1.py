def caesar(text, key):
    alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    zcaesar = ''
    for x in text.upper():
        if x in alfabet:
            zcaesar += alfabet[(alfabet.find(x) + key) % len(alfabet)]
    return zcaesar


s = caesar("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG", 100)
print(s)
s = caesar(s, -100)
print(s)

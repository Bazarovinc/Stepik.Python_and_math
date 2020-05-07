def caesar(text, key, alfabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    zcaesar = ''
    for x in text.upper():
        if x in alfabet:
            zcaesar += alfabet[(alfabet.find(x) + key) % len(alfabet)]
    return zcaesar
def rotor(symbol, n, reverse=False):
    rotors = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
              1: 'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
              2: 'AJDKSIRUXBLHWTMCQGZNPYFVOE',
              3: 'BDFHJLCPRTXVZNYEIWGAKMUSQO',
              4: 'ESOVPZJAYQUIRHXLNFTGKDCMWB',
              5: 'VZBRGITYUPSDNHLXAWMJQOFECK',
              6: 'JPGVOUMFYQBENHZRDKASXLICTW',
              7: 'NZJHGRCXMYSWBOUFAIVLPEKQDT',
              8: 'FKQHTLXOCBJSPDZRAMEWNIUYGV',
              'beta': 'LEYJVCNIXWPBQMDRTAKZGFUHOS',
              'gamma': 'FSOKANUERHMBTIYCWLQPZXVGJD'
              }
    symbol = symbol.upper()
    if reverse == False:
        if symbol in rotors[0]:
            return rotors[n][rotors[0].find(symbol)]
    elif reverse:
        if symbol in rotors[n]:
            return rotors[0][rotors[n].find(symbol)]


def reflector(symbol, n):
    refB = ['AY', 'BR', 'CU', 'DH', 'EQ', 'FS', 'GL', 'IP', 'JX', 'KN', 'MO', 'TZ', 'VW']
    symbol = symbol.upper()
    if n > 0:
        for s in refB:
            if symbol in s:
                index = s.find(symbol) - 1
                return s[index]
    return symbol


def enigma(text, ref, rot1, rot2, rot3):
    rotors = [rot3, rot2, rot1]
    new_text = ''
    for s in text:
        symb = s
        if symb in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or symb in 'qwertyuiopasdfghjklzxcvbnm':
            for rot in rotors:
                symb = rotor(symb, rot)
            symb = reflector(symb, ref)
            rotors.reverse()
            for rot in rotors:
                symb = rotor(symb, rot, reverse=True)
            new_text += symb
            rotors.reverse()
    return new_text

print(enigma('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 1, 1, 2, 3))

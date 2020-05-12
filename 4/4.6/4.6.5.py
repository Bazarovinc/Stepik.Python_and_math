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
move_next = {
    1: 'R',
    2: 'F',
    3: 'W',
    4: 'K',
    5: 'A',
    6: 'AN',
    7: 'AN',
    8: 'AN'
}
refB = ['AY', 'BR', 'CU', 'DH', 'EQ', 'FS', 'GL', 'IP', 'JX', 'KN', 'MO', 'TZ', 'VW']

def rotor(symbol, n, reverse=False):
    symbol = symbol.upper()
    if reverse == False:
        if symbol in rotors[0]:
            return rotors[n][rotors[0].find(symbol)]
    elif reverse:
        if symbol in rotors[n]:
            return rotors[0][rotors[n].find(symbol)]


def reflector(symbol, n):
    symbol = symbol.upper()
    if n > 0:
        for s in refB:
            if symbol in s:
                index = s.find(symbol) - 1
                return s[index]
    return symbol


def enigma(text, ref, rot1, shift1, rot2, shift2, rot3, shift3):
    alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rotors = [rot3, rot2, rot1]
    shifts = [shift3, shift2, shift1]
    new_text = ''
    for s in text:
        symb = s
        if symb in alfabet or symb in 'qwertyuiopasdfghjklzxcvbnm':
            symb = symb.upper()
            new_symb = False
            for i in range(len(rotors)):
                if i == 0:
                    shifts[i] += 1
                if i == 0 and alfabet[(0 + shifts[i]) % len(alfabet)] in move_next[rotors[i]]:
                    shifts[i + 1] += 1
                    new_symb = True
                elif i == 1 and alfabet[(0 + shifts[i] + 1) % len(alfabet)] in move_next[rotors[i]]\
                        and new_symb == False:
                    shifts[i] += 1
                    shifts[i + 1] += 1
                symb = alfabet[(alfabet.find(symb) + shifts[i]) % len(alfabet)]
                symb = rotor(symb, rotors[i])
                symb = alfabet[(alfabet.find(symb) - shifts[i]) % len(alfabet)]
            symb = reflector(symb, ref)
            rotors.reverse()
            shifts.reverse()
            for i in range(len(rotors)):
                symb = alfabet[(alfabet.find(symb) + shifts[i]) % len(alfabet)]
                symb = rotor(symb, rotors[i], reverse=True)
                symb = alfabet[(alfabet.find(symb) - shifts[i]) % len(alfabet)]
            new_text += symb
            rotors.reverse()
            shifts.reverse()
    return new_text

if 'BGDMBTZUONCIZMORCPNVLGOVLMURTNZNDROPETXLPLYCMIBICXITUCM' == enigma('AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA', 1, 2, 3, 2, 3, 2, 3):
    print('OK\n', 'BGDMBTZUONCIZMORCPNVLGOVLMURTNZNDROPETXLPLYCMIBICXITUCM')

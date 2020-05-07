def kidds_encryption(text, reverse=False):
    chifr = ['8;4‡)*56(1†092:3?¶-.',
             'ethosnairfdlmbyguvcp']
    new_text = ''
    for t in text.lower():
        if t in chifr[1] and reverse == False:
            new_text += chifr[0][chifr[1].find(t)]
        elif t in chifr[0] and reverse:
            new_text += chifr[1][chifr[0].find(t)]
    return new_text

print(kidds_encryption("XxL ,L, LxX"))
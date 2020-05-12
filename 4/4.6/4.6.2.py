def reflector(symbol, n):
    refB = ['AY', 'BR', 'CU', 'DH', 'EQ', 'FS', 'GL', 'IP', 'JX', 'KN', 'MO', 'TZ', 'VW']
    symbol = symbol.upper()
    if n > 0:
        for s in refB:
            if symbol in s:
                index = s.find(symbol) - 1
                return s[index]
    return symbol

print(reflector('y', 1))
def translate(n, b=2):
    s = []
    while n > 0:
        s.append(n % b)
        n //= b
    s.reverse()
    line = ''
    for i in s:
        line += str(i)
    return (int(line))


print(translate(19, 7))
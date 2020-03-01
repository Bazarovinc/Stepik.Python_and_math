def fix_start(s):
    c = s[0]
    s = s.replace(c, "*")
    s = s.replace(s[0], c, 1)
    return s


s = input()
print(fix_start(s))

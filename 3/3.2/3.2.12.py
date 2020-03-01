def both_ends(s):
    if len(s) < 2:
        return ""
    else:
        return s[:2] + s[-2:]


s = input()
print(both_ends(s))

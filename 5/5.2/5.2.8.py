def mimic_dict(string):
    L = string.split()
    d = {}
    for i in range(len(L)):
        if i == 0:
            d[''] = [L[i]]
            d[L[i]] = []
        else:
            if L[i] not in d and i != len(L) - 1:
                d[L[i]] = []
            if L[i - 1] in d:
                d[L[i - 1]].append(L[i])
    return d

print(mimic_dict("a cat and a dog a fly"))

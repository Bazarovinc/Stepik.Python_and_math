def kaprekar_step(L):
    min_1 = sorted(L)
    max_1 = sorted(L, reverse=1)
    n_min = 0
    for i in min_1:
        n_min = n_min * 10 + i
    n_max = 0
    for i in max_1:
        n_max = n_max * 10 + i
    return n_max - n_min

print(kaprekar_step([2, 7, 1, 8]))
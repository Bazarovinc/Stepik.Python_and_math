def even_indeces(L):
    new_list = []
    for i in range(len(L)):
        if i % 2 == 0:
            new_list.append(L[i])
    return new_list

print(even_indeces([2, 1, 13, 19, 0, 1]))
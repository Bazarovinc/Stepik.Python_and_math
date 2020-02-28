def counter(T):
    all_diff_num = []
    for line in T:
       dif = []
       line = line.lower()
       dif.append(line[0])
       for i in range(len(line)):
           for j in range(len(line)):
               if line[i] != line[j] and line[i] not in dif:
                   dif.append(line[i])
       all_diff_num.append(len(dif))
    max_str = max(all_diff_num)
    num_of_max = all_diff_num.count(max_str)
    if num_of_max > 1:
        indexs = []
        indexs.append(all_diff_num.index(max_str))
        i = 0
        while len(indexs) != num_of_max:
            indexs.append(all_diff_num.index(max_str, indexs[i] + 1))
            i += 1
        max_len = len(T[indexs[0]])
        for i in range(len(indexs)):
            if len(T[indexs[i]]) > max_len:
                max_len = len(T[indexs[i]])
        return max_len
    elif num_of_max == 1:
        return len(T[all_diff_num.index(max_str)])


print(counter(('Aa', 'ab', 'AaAa', 'AaAaAa', 'ABBA')))
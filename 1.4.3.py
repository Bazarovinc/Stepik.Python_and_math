import math

L = [1, 2, 6]

for i in range(1, len(L)):
    if math.fabs(L[i] - L[i - 1]) == 1:
        index = i - 1
        break
print(index)
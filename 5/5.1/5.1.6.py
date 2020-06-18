"""Найти все числа от 0 до 100, которые делятся на 5, но не делятся на 3"""

counter = 0
for i in range(0, 101, 5):
    if i % 3 != 0:
        counter += i
print(counter)
L = [i for i in range(0, 101, 5) if i % 3 != 0]
print(L)
res = sum(L)
print(res)
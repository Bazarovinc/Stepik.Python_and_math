import math as m

a = int(input())
b = int(input())
c = int(input())
p = (a + b + c) / 2
s = m.sqrt(p * (p - a) * (p - b) * (p - c))
print(p)
print(s)
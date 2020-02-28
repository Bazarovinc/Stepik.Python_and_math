import math as m

a = float(input())
s = 3 * m.pow(a, 2) * m.sqrt(5 * (5 + 2 * m.sqrt(5)))
v = (pow(a, 3) * (15 + 7 * m.sqrt(5))) / 4
print(round(s, 2))
print(round(v, 2))

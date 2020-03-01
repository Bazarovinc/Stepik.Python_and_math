f_n = input()
with open(f_n, 'r', encoding="utf-8") as f_o:
    lines = f_o.readlines()
print(lines[-2])

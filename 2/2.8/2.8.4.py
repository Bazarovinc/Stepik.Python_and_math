sheet = 'sheet.txt'
mean = 'mean'
with open(sheet, 'r', encoding="utf-8") as f_o:
    lines = f_o.readlines()
res = 0
num = 0
for line in lines:
    line = line.rstrip()
    line_1 = line.split()
    if line_1[-1] == '(экзамен)' or line_1[-1] == '(автомат)':
        res += int(line_1[-2])
        num += 1
with open(mean, 'r', encoding="utf-8") as f_o:
    mean_r = f_o.readline()
n = float(mean_r)
if num != 0:
    mid = res / num
else:
    mid = 0
if mid == n:
    print("OK")
else:
    print("ERROR")

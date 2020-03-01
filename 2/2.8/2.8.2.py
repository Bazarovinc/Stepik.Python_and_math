f_n = input()
with open(f_n, 'r', encoding="utf-8") as f_o:
    lines = f_o.readlines()
nums = []
for line in lines:
    nums.append(int(line))
print(sum(nums))

lines = []
lines = input().split()
lines.reverse()
for i in range(len(lines)):
    if i == len(lines) - 1:
        print(lines[i])
    else:
        print(lines[i], end="-$-")

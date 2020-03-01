lines = input().split()
size = len(lines)
if size == 3:
    print(lines[1], end=' ')
    print(lines[2], end=' ')
    print(lines[1])
elif size > 3:
    print(lines[1], end=' ')
    print(lines[2], end=' ')
    print(lines[size - 2])

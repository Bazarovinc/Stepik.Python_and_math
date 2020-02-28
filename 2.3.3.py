lines = input().split('&')
printed = []
for line in lines:
    if line not in printed:
        print(line, end=' ')
        printed.append(line)

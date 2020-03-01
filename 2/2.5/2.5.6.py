s = input()
if s == 'int':
    a = int(input())
    b = int(input())
    if a == 0 and b == 0:
        print("Empty Ints")
    else:
        print(a + b)
elif s == 'str':
    n_s = input()
    if n_s == '':
        print("Empty String")
    else:
        print(n_s)
elif s == 'list':
    l = input().split()
    if len(l) == 0:
        print("Empty List")
    else:
        print(l[-1])
else:
    print("Unknown type")

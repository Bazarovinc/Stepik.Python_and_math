def numerics(n):
    nums = []
    while n > 0:
        nums.append(n % 10)
        n //= 10
    return nums

def kaprekar_check(n):
    L = numerics(n)
    if len(L) < 3 or len(L) == 5 or len(L) > 6:
        return False
    if L.count(L[0]) == len(L):
        return False
    if n == 100 or n == 1000 or n == 100000:
        return False
    return True

print(kaprekar_check())
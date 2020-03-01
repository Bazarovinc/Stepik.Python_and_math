def numerics(n):
    nums = []
    while n > 0:
        nums.append(n % 10)
        n //= 10
    return nums

print(numerics(100))
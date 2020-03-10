def numerics(n):
    nums = []
    while n > 0:
        nums.append(n % 10)
        n //= 10
    nums.reverse()
    return nums


def made_n(nums):
    res = 0
    for n in nums:
        res = res * 10 + n
    return res


def for_2(n, nums):
    n1 = made_n(nums[:1])
    n2 = made_n(nums[1:])
    if n1 + n2 == n and n1 != 0 and n2 != 0:
        return True, n1, n2
    return False, 0, 0


def for_more_2(n, nums):
    mid = 0
    size = len(nums)
    while mid - 1 != size:
        n1 = made_n(nums[:mid])
        n2 = made_n(nums[mid:])
        if n1 + n2 == n and n1 != 0 and n2 != 0:
            return True, n1, n2
        mid += 1
    return False, 0, 0


def kaprekar(n):
    mult = n ** 2
    nums = numerics(mult)
    if len(nums) == 2:
        res, n1, n2 = for_2(n, nums)
    else:
        res, n1, n2 = for_more_2(n, nums)
    if res:
        print(True)
        print(str(n) + "**2 = " + str(mult))
        print(str(n1) + " + " + str(n2) + " = " + str(n))
    else:
        print(False)
        print(str(n) + "**2 = " + str(mult))

kaprekar()
"""Функция нахождения простого числа"""


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def is_prime_1(n):
    for i in range(2, int(n ** 0,5) + 1):
        if n % i == 0:
            return False
    return True


n = input()
print(is_prime(n))
print(is_prime_1(n))
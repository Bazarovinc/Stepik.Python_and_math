def factorial (n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def sf(n):
    if n == 0:
        return 1
    else:
        return sf(n - 1) * factorial(n)

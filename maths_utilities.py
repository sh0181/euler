def is_prime(n):
    factor = 2
    while factor * factor <= n:
        if n % factor == 0:
            return False
        factor = factor + 1
    return True

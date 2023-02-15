# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
# 600851475143/2 = 300425737571.5

from maths_utilities import is_prime


def largest_prime_factor(n):
    for i in range(int(n / 2), 2, -1):
        if n % i == 0 and is_prime(i):
            # I've now found all the factors - this part works
            return i


print(largest_prime_factor(600851475143))

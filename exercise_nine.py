# a^2 + b^2 = c^2     a+b+c = 1000      3^2 + 4^2 = 9+16 = 25 = 5^2

import math

def is_int(input):
    return input-int(input)==0

for a in range (1,1000):
    for b in range (1,1000):
        k = a**2 + b**2
        c = math.sqrt(k)

        if is_int(c) and a+b+c==1000:
        # if isinstance(j, int) == True:
        # these are not working because the type is float regardless of decimal places
        # I need some way to say 'if c is whole number then proceed'
            product = a*b*c
            print(a)
            print(b)
            print(c)
            print(product)



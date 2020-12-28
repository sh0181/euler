# Make Sequence

fib1 = 1
fib2 = 1
fibc = 1
total = 0
#fibc = fib1 + fib2
#fib2 = fib1
#fib1 = fibc


def is_even(number):
    return number % 2 == 0

while fibc <= 4000000:
    fibc = fib1 + fib2
    fib2 = fib1
    fib1 = fibc
    print(fibc)
    if is_even(fibc):
        total = total + fibc
     #   total += fibc
    #print(total)

print(total)


# Check if Even



# Add to Total



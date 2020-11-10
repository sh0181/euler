
total = 0


def is_multiple_of_three_or_five(number):
    return number % 3 == 0 or number % 5 == 0


for i in range(1, 1000):
    if is_multiple_of_three_or_five(i):
        total += i
print(total)

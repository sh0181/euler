
total = 0


def multiply_by_2(input):
    return input * 2


def is_multiple_of_three_or_five(cake):
    return cake % 3 == 0 or cake % 5 == 0

# for = i is my counter, count from 1 to 1000 and do this with it
for i in range(1, 1000):
    if is_multiple_of_three_or_five(i):
        total += i
print(total)

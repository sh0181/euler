
def is_palindrome(digits):
    head = 0
    tail = len(digits) - 1
    while head <= tail:
        if digits[head] != digits[tail]:
            return False
        head = head + 1
        tail = tail - 1
    return True


# def is_palindrome(number):
#     # if number[2] == number[3]:
#     #     return True
#     # else:
#     #     return False
#     return number[2] == number[3] and number[1] == number[4] and number[0] == number[5]


def is_three_digits(k):
    return len(k) == 3


for i in range(998001, 99999, -1):
    number = i
    number = str(number)
    # number[1]
    # int(number[1])
    if is_palindrome(number):
        # return (num_is_pal)
        # print(num_is_pal)
        for j in range(999, 99, -1):
            if i % j == 0:
                k = i / j
                Fac2 = int(k)
                Fac2 = str(Fac2)
                if is_three_digits(Fac2):
                    print(number)
                    print(j)
                    print(Fac2)
                    exit(0)
            # I want to pass this on to another function to see if that factor has 3 digits

# number = 9876543210 #declaring and assigning
# number = str(number) #converting
# Then get the index, 0 = 1, 4 = 3 in index notation, use int() to turn it back into a number

# print(int(number[3])) #printing the int format of the string "number"'s index of 3 or '6'

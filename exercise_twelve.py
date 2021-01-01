# triangle number n is the sum of 1 to n.
# test each triangle number to find factors
# once I find one with 5 factors, print it

def count_factors(n):
    factors = 0
    for j in range(1, int(n / 2 + 1)):
        if n % j == 0:
            factors = factors + 1
    return factors


tri_num = 1
i = 1

while count_factors(tri_num) < 500:
    i = i + 1
    tri_num = tri_num + i

print(tri_num)
#
# tri_num = 1
# i = 0
# while i < 30:
#     for j in range (1,tri_num+1):
#         if tri_num % j == 0:
#             # print(str(j) + 'is a factor of ' + str(tri_num))
#             #
#     i = i+1
#     tri_num = tri_num + i
#     if tri_num > 10:
#         exit(0)




longest_length = 0
longest_length_i = 0
for i in range(2,1000001):
    n = i
    print(n)
    length = 1
    while n > 1:
        if n%2 == 0:
            n = n/2
        else:
            n = 3*n + 1
        length = length + 1
        print(n, length)
    if length > longest_length:
        longest_length = length
        longest_length_i = i


print(longest_length, longest_length_i)
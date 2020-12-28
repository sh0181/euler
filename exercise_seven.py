# if i % j == 0: #this means it has a factor and isn't a prime number

pn = 0
i=1

while pn != 10001:
    i = i + 1
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            # then it has a factor so is not a prime number - I'm not interested
            is_prime = False
            break
    if is_prime:
        pn=pn+1
print(i)
        # break
    # if pn==3:
    # print(i)
# need a way to exit once I've found a number it divides by
# need a way to include 2 in the count

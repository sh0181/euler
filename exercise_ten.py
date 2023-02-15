# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

#it's a prime number if it only divides by itself and 1
#take i, divide it by all numbers. If any of them have a zero remainder then ditch the i

sum = 0

for i in range (3,2000001):
        for j in range(2, i+1):
            if i % j == 0: #if i divides by j with no remainder then j is a factor so i isn't prime
                break
            if j==i-1:
                sum = sum + i
        if i==2000000:
            print(sum)
                #this works except I have to add 2 because I don't know how to include it above


#The sum of the squares of the first ten natural numbers is 385
#The square of the sum of the first ten natural numbers is 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

###Sum of squares of first natural numbers
square = 0
sum_square = 0

for i in range (1,101):
    square = i**2
    #print (i)
    #print(square)
    sum_square = sum_square + square
    if i==100:
        print (sum_square)


###Square of sum of first natural numbers
sum = 0
square_sum = 0

for i in range (1,101):
    sum = sum + i
    if i==100:
        square_sum = sum**2
        print(square_sum)


###Difference between sum of squares and sqaure of sums
diff = square_sum - sum_square
print(diff)

a=2
b=1
a=b
print(a)
print(b)


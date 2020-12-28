number = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450

# = int(k)
#string_number = int(number)
string_number = str(number)
length = len(string_number)
print(length)

multiple_old=0
multiple_temp=0
multiple_new=0

#we have our old multiple, we put it into a temporary state. If the new multiple is larger than the
#temporary one, we don't need the old multiple any more as we know it isn't the largest. So we replace
#the old one with the new one.
#define left as being equal to right


for i in range (0,999):
    multiple_temp = multiple_old
    multiple_new = int(string_number[i]) * int(string_number[i + 1]) * int(string_number[i + 2]) * int(string_number[i + 3]) * int(string_number[i + 4]) * int(string_number[i + 5]) * int(string_number[i + 6]) * int(string_number[i + 7]) * int(string_number[i + 8]) * int(string_number[i + 9]) * int(string_number[i + 10]) * int(string_number[i + 11]) * int(string_number[i + 12])

    if multiple_new > multiple_temp:
        multiple_old=multiple_new
        #print(multiple_old)
    #multiple_new = int(string_number[i]) * int(string_number[i+1]) * int(string_number[i+2]) * int(string_number[i+3])

    #if multiple_new>multiple_old:
        print(multiple_old)
        print(string_number[i])
        print(string_number[i+1])
        print(string_number[i+2])
        print(string_number[i+3])
        print(string_number[i+4])
        print(string_number[i+5])
        print(string_number[i+6])
        print(string_number[i+7])
        print(string_number[i+8])
        print(string_number[i+9])
        print(string_number[i+10])
        print(string_number[i+11])
        print(string_number[i+12])


        #sn0=int(string_number[0])
#sn1=int(string_number[1])
#print(string_number[0])
#print(sn0)
#print(string_number[1])
#print(sn1)
#print(multiple)
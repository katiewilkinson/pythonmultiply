#Part 1 of code prints all the odd numbers from 1 to 1000
#Part 2 of code prints all the multiples of 5 from 5 to 1000000



for i in range (1,1001):
    if(i % 2 == 1):
        print i

for i in range(5, 1000001):
    if(i % 5 == 0):
        print i

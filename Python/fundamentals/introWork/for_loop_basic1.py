#Prints all integers between 0 and 150
for x in range(151): 
    print(x)

#Prints multiples of 5 up to 1,000
for x in range(1, 1000, 1):
    if x*5 > 1000:
        break
    print(x*5)

#Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for x in range(1,101):
    if x % 10 == 0:
        print('Coding Dojo')
    elif x % 5 == 0:
        print('Coding')
    else:
        print(x)

#Add odd integers from 0 to 500,000, and print the final sum.
sum = 0

for x in range(500000):
    if x % 2 != 0:
        sum+=x

print(sum)

#Print positive numbers starting at 2018, counting down by fours.
for x in range(2018, 0, -4):
    print(x)

# Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lowNum = 10
highNum = 100
mult = 7
for x in range(lowNum, highNum):
    if x % mult == 0:
        print(x)
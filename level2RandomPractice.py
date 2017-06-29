from random import randint

#FUNCTION

def level2(numlist):
    numSum = 0

    for num in numlist:
        if num %3 == 0 or num %5 == 0: #number is a multiple of 3 or 5
            print(num)
            numSum += num #numSum= numSum + num
    print("Final Sum:")
    print (numSum)
            







#RUNNING CODE
randomlist = []
for x in range(100):
    randnumber = randint(10,99)
    randomlist.append(randnumber)

level2(randomlist)

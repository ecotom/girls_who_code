from random import randint


#FUNCTIONS
def level3(numlist):

    primeSum = 0
    
    #part 1 : iterate through the list
    for num in numlist:


        prime = True

        #part 2: determine if a prime number
        for x in range(2,num):
            if num %x == 0:
                prime = False

        if prime == True:
            print(num)
            primeSum += num


    #part 3 : add to the sum
    print("Final number")
    print (primeSum)

random = []
for x in range(100):
    randnumber = randint(10,99)
    randomlist.append(randnumber)

level3(randomlist)

    

    

from random import randint

def multiple(nums):
    fiveCount = 0

    for number in nums:
        if number %5 == 0:
            fiveCount += 1
    print("There are %d even numbers in this list." %fiveCount)


numlist = []
for x in range(100):
    num = randint(10,99)
    numlist.append(num)

print(numlist)
multiple(numlist)
    

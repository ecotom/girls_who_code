


groceryList=[]

    
while True:
    print(" Do you want to add an item to your list?(y/n)")
    answer = input()
    if (answer == "y"):
        print("What would you like to add?")
        groceryList.append(input())
    elif (answer == "n"):
        print("Your grocery list is ")
        for x in groceryList:
            print (x)
        exit()
    else:
        print("Please type 'y' or 'n'.")
        
    
        
print (groceryList)

##groceryList=["cookies","cake","ice cream","milk","oranges"]
##length = len(groceryList)
##groceryList.append("milk")
##
##for x in groceryList:
##    print(x)

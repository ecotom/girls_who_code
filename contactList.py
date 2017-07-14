##myDict = {}
myDict = {}





addContact = True

while addContact == True:
    print("Would you like to add a contact to your contact list?(y/n)")
    answer = input().lower()
    if (answer == 'y'):
        print ("What is the name?")
        Contact = input().lower()
        print("Would you like to add a number, address, both or neither?")
        answer = input().lower()
        
        if ( answer == 'number'):
            print("What is the number?")
            number = input().lower()
            myDict[Contact] = number
            
        if (answer == ' address'):
            print("What is the address?")
            address = input(). lower()
            myDict[Contact] = address
            
        if (answer == 'both'):
            print("What is the number")
            number = input().lower()
            print("What is the address?")
            address = input(). lower()
            
            myDict[Contact] = []
            myDict[Contact].append(number)
            myDict[Contact].append(address)
            
        elif (answer == 'neither'):
            print("Your conatcts have been saved!")
            addContact = False

        else:
            print("Please type 'number', 'address', 'both', 'neither'.")

    elif (answer == 'n'):
        print("Your contacts have been saved!")
        addWords = False
        

    else:
        print("Please enter 'y' or 'n'")
        exit()

    


##print(myDict)

print("MY CONTACT LIST:")
print()

for item in myDict:
    print("NAME: " + item)
    definition = myDict[item]
    defineType = type(definition)
    
    if (defineType == str):
        print("NUMBER: " + myDict[item])
        
    elif(defineType == list):
        
        for x in number and address:
            print("- " + x)
    print()



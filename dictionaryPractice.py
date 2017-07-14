##myDict = {}
myDict = {"Indispensable": "Absolutely necessary","Boisterous": " Scandalous"}

addWords = True

while addWords == True:
    print("Would you like to add a word to your dictionary?(y/n)")
    answer = input().lower()
    if (answer == 'y'):
        print ("What is the word?")
        word = input().lower()
        print("What is the definition of the word?")
        definition = input().lower()

        myDict[word] = definition


    elif (answer == 'n'):
        print("Your dictionary had been saved!")
        addWords = False

    else:
        print("Please enter 'y' or 'n'")


##print(myDict)

print("MY DICTIONARY:")
print()

for item in myDict:
    print("Word: " + item)
    print("Definition: " + myDict[item])
    print()


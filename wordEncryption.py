realList = []
codeList = []

def yesNO(answer):
    if answer == ("yes"):
        print ("What is the real word?")
        realWord = input()
        realWord = realWord.lower()
        realList.append(realWord)
       # for x in realList:
           # print(x)

        print ("What is the code word?")
        codeWord = input()
        codeWord = codeWord.lower()
        codeList.append(codeWord)
##        for x in codeList:
##            print(x)

        print ("What is the sentence?")
        str = input()
        str = str.lower()
        print (str)
        
            

if answer == "no":
    print (

print("Would you like to create a code word? (Yes/No)")
answer =input()
answer = answer.lower()
print(answer)
yesNO(answer)
print(realList)







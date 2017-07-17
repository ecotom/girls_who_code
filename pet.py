#CLASSES

class Pet:
    def __init__(self,name,age, color):
        self.name = name
        self.age = age
        self.color = color

class Dog(Pet):
    def __init__(self,name,age,color,breed,attitude):
        self.breed = breed
        self.attitude = attitude
        Pet.__init__(self,name,age,color)
        self.adopted = False

    def getName(self):
        return self.name
        
    def speak(self):
        print("Woof!")

    def isAdopted(self):
        return self.adopted

    def setAdopted(self,adopt):
        self.adopted = adopt

    def bio(self):
        print(self.name + " is a " + self.color + " "
              + self.breed + " who is " + self.attitude + " !")
        
#class Cat(Pet):
    


#RUNNING CODE
spot = Dog("Spot","2","Black and White","Terrier","Friendly")
fred = Dog("Fred","1","Brown","BOxer","Sassy")
clifford = Dog ("Clifford","3","Red","Big Red Dog","Nice")
storm = Dog("Storm","2","White","Huskey","Hyper")


dogs = [spot,fred,clifford,storm]

for  each in dogs:
    each.speak()
    print("That's " + each.getName())
    each.bio()
##spot.speak()
##spot.bio()




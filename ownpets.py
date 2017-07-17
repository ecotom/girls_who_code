
#CLASSES
class Pet:
    def __init__(self,name,age,color):
        self.name = name
        self.age = age
        self.color = color

class Dog(Pet):
    def __init__(self,name,age,color,breed,attitude):
        self.breed = breed
        self.attitude = attitude
        Pet.__init__(self,name,age,color)

    def getName(self):
        return self.name

    def speak(self):
        print("Woof!")

    def isAdopted(self):
        return self.adopted

    def setAdopted(self,adopt):
        self.adopted = adopt

    def bio(self):
        print(self.name + " is a " + self.color + " " + self.breed + " who is " + self.attitude + "!")
        

class Dragon(Pet):
    def __init__(self,name,age,color,breed,skill):
        self.breed = breed
        self.skill = skill
        Pet.__init__(self,name,age,color)

    def getName(self):
        return self.name

    def bio(self):
        print(self.name + " is a " + self.color + " " + self.breed + " who can " + self.skill + "!")


class Wolf(Pet):
    def __init__(self,name,age,color,position):
        self.position = position
        Pet.__init__(self,name,age,color)

    def getName(self):
        return self.name

    def bio(self):
        print(self.name + " is a " + self.color + " wolf " + " who is the " + self.position + " of the pack!")

#RUNNING CODE
spot = Dog("Spot","2","Black and White", "Terrier", "Friendly")
fred = Dog("Fred","1","Brown","Boxer","Sassy")
clifford = Dog("Clifford","3", "Red", "Big Red Dog", "Nice")
storm = Dog("Storm","2","White", "Husky", "Hyper")

dogs = [spot, fred, clifford, storm]

toothless = Dragon("Toothless", "1000", "Black", "Nightfury", "strike lightning")

dragons = [toothless]

blaze = Wolf("Blaze", "20", "Gray", "Alpha")

wolf = [blaze]
              
print("Welcome to the Girls Who Code Animal Shelter!")
print("Let me introduce you to our Animals")

for each in dogs:
    each.speak()
    print("Thats " + each.getName())
    each.bio()

for each in dragons:
    print("Thats " + each.getName())
    each.bio()

for each in wolf:
    print("Thats " + each.getName())
    each.bio()


pet.py
Open with Google Docs
Displaying pet.py.

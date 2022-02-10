

class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = 50
        self.health = 100
        is_sleeping = False

    def show_info(self ):
        print(f"\nPet Name: {self.name}\nType: {self.type}\nTricks: {self.tricks}\nEnergy {self.energy}\nHealth: {self.health}\n ")
# implement __init__( name , type , tricks )
# # implement the following methods:
# sleep() - increases the pets energy by 25
    def sleep(self):
        print(f"{self.name} is going to sleep..")
        is_sleeping = True
        self.energy += 25
        is_sleeping = False
        print(f"{self.name} is awake and feeling refreshed!")
        # print(f"Energy is now:{self.energy}")
        return self

# eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        print(f"{self.name} is now eating.")
        self.energy += 5
        self.health += 10
        return self
        
# play() - increases the pet's health by 5
    def play(self):
        print(f"{self.name} loves going on walks!")
        self.health += 5
        return self
# noise() - prints out the pet's sound
    def noise(self):
        print("Bark bark!\n")
        return self

kai = Pet('Kai', 'Doggy', 'Sit')
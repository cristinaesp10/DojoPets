from petclass import Pet

class Ninja:
    def __init__(self, first_name , last_name , treats , pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
        
    def showNinja(self):
        print(f"Ninja Name: {self.first_name}\n")

# implement the following methods:
# walk() - walks the ninja's pet invoking the pet play() method
    def walk(self, pet):
        print(f"{self.first_name} is going on a walk...")
        pet.play()
        return self

# feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self, pet):
        print(f"{self.first_name} is feeding {pet.name}")
        pet.eat()
        return self
# bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self, pet):
        print(f"{self.first_name} is giving {pet.name} a bath!")
        pet.noise()

kai = Pet('Kai', 'Doggy', 'Sit')


chris = Ninja('Chris', 'Manley', 'chicken', 'Kibble', kai )



# chris.walk(kai)
# chris.feed(kai)

# kai.show_info()
chris.showNinja()
chris.bathe(kai)
kai.sleep()
# kai.sleep().eat().play()
kai.show_info()
# kai.noise()
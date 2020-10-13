class Animal():
    def __init__(self, fur):
        self.fur = fur

    def eat(self):
        print("Eating!")

    def report(self):
        print("Animal")


class Dog(Animal): # extend animal

    def __init__(self, fur):
        Animal.__init__(self, fur) # call supper function
        print("Dog created")

    def report(self): # override
        print("I am a Dog")


dog = Dog("Fuzzy")
print(dog.fur)
dog.eat()
dog.report()

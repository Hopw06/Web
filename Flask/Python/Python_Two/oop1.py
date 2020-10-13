mylist = [1, 2, 3]

mylist.append(4)

# everything in python is object
print(type(mylist))

# example object


class Sample():
    pass


x = Sample()

print(type(x))


class Dog():
    # Class object attributes
    gender = "female"

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name


sam = Dog("Huskie", "Sammy")

print(sam.breed)
print(sam.name)
print(sam.gender)

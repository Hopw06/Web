def hello(name="Jose"):
    print("this hello() function just run")

    def greet():
        return "     This is inside the greet()"

    def welcome():
        return "     This is inside the welcome()"

    if name == "Jose":
        return greet
    else:
        return welcome


# fun in python can be return from other function
x = hello("Sammy")
print(x())

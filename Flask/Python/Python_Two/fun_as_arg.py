def hello():
    return "Hi"


def other(func):
    print("Some other code")
    # Asume that func that pass to other function is a function
    print(func())


other(hello)

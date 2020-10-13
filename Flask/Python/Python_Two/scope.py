x = 'outside'


def report():
    x = 'inside'
    return x


print(report())
print(x)

# LEGB rule
# LOCAL
# ENCLOSING
# GLOBAL
# BUILT in

x = "THIS IS GLOBAL LEVEL"


def enclosing():
    #     x = "Enclosing level"

    def inside():
        print(x)
    inside()


enclosing()

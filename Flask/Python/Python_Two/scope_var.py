x = "outside"


def report():
    # Hey grap the global level x variable!
    global x
    # Reassign global variable
    x = 'inside'
    return x


print(report())
print(x)

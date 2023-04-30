# Section 10 - More Functions 3

def mean(*args):  # Allows any number of arguments (like the print function)
    return sum(args) / len(args)


print(mean(1, 3, 4))  # Cannot use keyword arguments with *args parameter

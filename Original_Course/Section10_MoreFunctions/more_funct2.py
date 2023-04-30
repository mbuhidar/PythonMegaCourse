# Section 10 - More Functions 1

def area(a, b=5):  # Parameters
    return a * b


print(area(b=5, a=4)) # Keyword Arguments - position doesn't matter

print(area(a=4)) # b has a default parameter in the function def
# Section 10 - More Functions 4

def mean(**kwargs):  # all arguments to the function must be named using **kwargs
    return kwargs  # returns a dict of keywords and values


print(mean(a=1, b=2, c=3))

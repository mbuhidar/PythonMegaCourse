# Section 10 - String Sorting Exercise

def str_sort(*args):
    return sorted([i.upper() for i in args])


print(str_sort('snow', 'glacier', 'iceberg'))

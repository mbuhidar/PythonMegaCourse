name = input("Enter your name: ")
surname = input('Enter your surname: ')
when = 'today.'
message = "Hello %s %s" %(name, surname) # Python 2 or 3
print(message)
message = f"Hello {name} {surname}.  What's up {when}" # Python 3.6 and later
print(message)

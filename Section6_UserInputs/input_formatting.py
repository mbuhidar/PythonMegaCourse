user_input = input("Enter your name: ")
message = "Hello %s" %user_input # Python 2 or 3
print(message)
message = f'Hello {user_input}' # After Python 3.6
print(message)

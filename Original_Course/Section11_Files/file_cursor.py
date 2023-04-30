# Section 11 - File Cursor

myfile = open("fruits.txt")  # creates a file object
content = myfile.read()  # cursor ends at end of txt file after read method is executed
myfile.close()  # good practice to close files once input is stored in a variable

print(content)
print(content)

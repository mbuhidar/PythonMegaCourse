# Section 11 - File Processing 3

myfile = open("fruits.txt")  # creates a file object
content = myfile.read()  # cursor ends at end of txt file after read method is executed
myfile.close()  # good practice to close files once input is stored in a variable

with open("fruits.txt") as myfile:  # better way to handle creating file objects
    content1 = myfile.read()        # auto closes file when block ends

print(content)
print(content1)

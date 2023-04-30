# Section 11 - Appending to a file

with open("./files/vegetables.txt", "a+") as myfile:  # a+ for  rw append mode
    myfile.write("Okra\n")
    myfile.seek(0)  # Resets cursor to file start
    content = myfile.read()

print(content)

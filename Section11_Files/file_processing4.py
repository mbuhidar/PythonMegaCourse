# Section 11 - File Processing 4 - writing to files

with open("./files/vegetables.txt", "w") as myfile:  # better way to handle creating file objects
    myfile.write("Tomato\nCucumber\nOnion\n")       # auto closes file when block ends
    myfile.write("Garlic\n")

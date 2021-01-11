# Section 11 - File Processing 3

with open("./files/fruits1.txt") as myfile:  # better way to handle creating file objects
    content1 = myfile.read()        # auto closes file when block ends

print(content1)

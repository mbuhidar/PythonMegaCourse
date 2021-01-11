# Section 11 - File Processing 4 - writing to files

with open("./files/vegetables.txt", "w") as myfile:  # better way to handle creating file objects
    myfile.write("Tomato\nCucumber\nOnion\n")       # auto closes file when block ends
    myfile.write("Garlic\n")

"""
    ========= ===============================================================
    Character Meaning
    --------- ---------------------------------------------------------------
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    'U'       universal newline mode (deprecated)
    ========= ===============================================================
    """
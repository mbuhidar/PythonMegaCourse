# Section 12 - Modules

# view modules using sys.builtin_module_names to see Python system modules - written in C

import time
import os

while True:
    if os.path.exists("../Section11_Files/files/vegetables.txt"):
        with open("../Section11_Files/files/vegetables.txt") as file:
            print(file.read())
    else:
        print("File does not exist.")
        break

    time.sleep(10)

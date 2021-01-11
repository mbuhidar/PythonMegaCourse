# Section 12 - Package (or Library) is a module or several modules (pandas is a package or library)

# view modules using sys.builtin_module_names to see Python system modules - written in C

import time
import os
import pandas

while True:
    if os.path.exists("temps_today.csv"):
        data = pandas.read_csv("temps_today.csv")
        print(data.mean()["st1"])
    else:
        print("File does not exist.")
        break

    time.sleep(10)

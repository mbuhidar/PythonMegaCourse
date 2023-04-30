# Section 8 - for loops over dictionaries

student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}

for grades in student_grades.items():
    print(grades) # prints each item as a tuple
    print(f"{grades[0]} has a grade of {grades[1]}.")

print()

for key, value in student_grades.items():
    print("{} has a grade of {}.".format(key, value))

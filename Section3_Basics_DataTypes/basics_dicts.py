# Use dir(list) to see methods for the list function
# Use dir(__builtins__) to see all functions

monday_temperatures = [9.1, 8.8, 7.5]
student_grades = {"Mary": 9.1, "Sim": 8.8, "John": 7.5}

mysum = sum(student_grades.values())
length = len(student_grades)
mean = mysum / length
print(mean)

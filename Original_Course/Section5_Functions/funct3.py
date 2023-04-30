def mean(value):
    # Better way to check type than in funct2.py
    if isinstance(value, list):
        the_mean = sum(value) / len(value)

    elif isinstance(value, dict):
        the_mean = sum(value.values()) / len(value)
    return the_mean

student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}

avg_temps = [54 , 48, 33, 27, 99.9]

print(mean(student_grades))

print(mean(avg_temps))

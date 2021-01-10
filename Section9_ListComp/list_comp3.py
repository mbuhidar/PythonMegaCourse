# Section 9 - List Comprehensions 3

temps = [221, 234, 340, -9999, 230]

"""
new_temps = []
for temp in temps:
    if temp != -9999:
        new_temps.append(temp / 10)
    else:
        new_temps.append(0)
"""

# Same outcome as above using list comprehensions
new_temps = [temp / 10 if temp != -9999 else 0 for temp in temps]

print(new_temps)

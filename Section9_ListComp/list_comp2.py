# Section 9 - List Comprehensions 2

temps = [221, 234, 340, -9999, 230]

"""
new_temps = []
for temp in temps:
    if temp != -9999:
        new_temps.append(temp / 10)
"""

# Same outcome as above using list comprehensions
new_temps = [temp / 10 for temp in temps if temp != -9999]

print(new_temps)

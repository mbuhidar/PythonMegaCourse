# Section 20 - Tkinter GUI

import tkinter as tk

# Create an empty Tkinter window
window = tk.Tk()


def kg_to_g_lb_oz():
    # Get user input value from input box and convert to float
    kg = float(e2_value.get())
    # Convert kg input value to grams, pounds, ounces
    grams = kg * 1000
    pounds = kg * 22.0462
    ounces = kg * 35.274
    t1.delete("1.0", tk.END)  # Deletes content of the text box from start to END
    t1.insert(tk.END, grams)  # Fill in the text box with the variable value
    t2.delete("1.0", tk.END)
    t2.insert(tk.END, pounds)
    t3.delete("1.0", tk.END)
    t3.insert(tk.END, ounces)


# Create a button widget
# The kg_to_g_lb_oz() function is called when the button is pushed
b1 = tk.Button(window, text="Convert", command=kg_to_g_lb_oz)
b1.grid(row=0, column=2)

# Create a label widget with "Kg" as label
e1 = tk.Label(window, text="Kg")
e1.grid(row=0, column=0)

e2_value = tk.StringVar()
e2 = tk.Entry(window, textvariable=e2_value)
e2.grid(row=0, column=1)

# Create three empty text boxes - t1, t2, t3
t1 = tk.Text(window, height=1, width=20)
t1.grid(row=1, column=0)

t2 = tk.Text(window, height=1, width=20)
t2.grid(row=1, column=1)

t3 = tk.Text(window, height=1, width=20)
t3.grid(row=1, column=2)

# Keeps the main window open until user exit
window.mainloop()

# Section 22 - Bookshop Database frontend

import tkinter as tk
from backend_OOP import Database

database = Database("books.db")

class Window():

    def __init__(self, window):

        self.window = window

        self.window.wm_title("Bookstore")

        l1 = tk.Label(self.window, text="Title")
        l1.grid(row=0, column=0)

        l2 = tk.Label(self.window, text="Author")
        l2.grid(row=0, column=2)

        l3 = tk.Label(self.window, text="Year")
        l3.grid(row=1, column=0)

        l4 = tk.Label(self.window, text="ISBN")
        l4.grid(row=1, column=2)

        self.title_text = tk.StringVar()
        self.e1 = tk.Entry(self.window, textvariable=self.title_text)
        self.e1.grid(row=0, column=1)

        self.author_text = tk.StringVar()
        self.e2 = tk.Entry(self.window, textvariable=self.author_text)
        self.e2.grid(row=0, column=3)

        self.year_text = tk.StringVar()
        self.e3 = tk.Entry(self.window, textvariable=self.year_text)
        self.e3.grid(row=1, column=1)

        self.isbn_text = tk.StringVar()
        self.e4 = tk.Entry(self.window, textvariable=self.isbn_text)
        self.e4.grid(row=1, column=3)

        self.list1 = tk.Listbox(self.window, height=6, width=35)
        self.list1.grid(row=2, column=0, rowspan=6, columnspan=2)

        self.sb1 = tk.Scrollbar(self.window)
        self.sb1.grid(row=2, column=2, rowspan=6)

        self.list1.configure(yscrollcommand=self.sb1.set)
        self.sb1.configure(command=self.list1.yview)

        self.list1.bind('<<ListboxSelect>>', self.get_selected_row)

        self.b1 = tk.Button(self.window, text="View all", width=12, command=self.view_command)
        self.b1.grid(row=2, column=3)

        self.b2 = tk.Button(self.window, text="Search entry", width=12, command=self.search_command)
        self.b2.grid(row=3, column=3)

        self.b3 = tk.Button(self.window, text="Add entry", width=12, command=self.add_command)
        self.b3.grid(row=4, column=3)

        self.b4 = tk.Button(self.window, text="Update selected", width=12, command=self.update_command)
        self.b4.grid(row=5, column=3)

        self.b5 = tk.Button(self.window, text="Delete selected", width=12, command=self.delete_command)
        self.b5.grid(row=6, column=3)

        self.b6 = tk.Button(self.window, text="Close", width=12, command=self.window.destroy)
        self.b6.grid(row=7, column=3)


    def view_command(self):
        self.list1.delete(0, tk.END)
        for row in database.view():
            self.list1.insert(tk.END, row)


    def search_command(self):
        self.list1.delete(0, tk.END)
        for row in database.search(self.title_text.get(), self.author_text.get(), 
                                self.year_text.get(), self.isbn_text.get()):
            self.list1.insert(tk.END, row)


    def add_command(self):
        database.insert(self.title_text.get(), self.author_text.get(), self.year_text.get(),
                        self.isbn_text.get())
        self.list1.delete(0, tk.END)
        self.list1.insert(tk.END, (self.title_text.get(), self.author_text.get(), self.year_text.get(),
                    self.isbn_text.get()))


    def delete_command(self):
        database.delete(self.selected_tuple[0])


    def update_command(self):
        database.update(self.selected_tuple[0], self.title_text.get(), self.author_text.get(), 
                        self.year_text.get(), self.isbn_text.get())


    def get_selected_row(self, event):
        global selected_tuple
        try:
            index = self.list1.curselection()[0]
            self.selected_tuple = self.list1.get(index)
            self.e1.delete(0, tk.END)
            self.e1.insert(tk.END, self.selected_tuple[1])
            self.e2.delete(0, tk.END)
            self.e2.insert(tk.END, self.selected_tuple[2])
            self.e3.delete(0, tk.END)
            self.e3.insert(tk.END, self.selected_tuple[3])
            self.e4.delete(0, tk.END)
            self.e4.insert(tk.END, self.selected_tuple[4])
        except IndexError:
            pass



window = tk.Tk()
Window(window)
window.mainloop()

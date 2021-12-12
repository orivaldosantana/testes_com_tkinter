import tkinter as tk

def show_entry_fields():
    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))

master = tk.Tk()
master.geometry('320x100')

tk.Label(master, width=10, text="First Name").grid(row=0)
tk.Label(master, width=10, text="Last Name").grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

tk.Button(master, width=20, text='Quit', command=master.quit).grid(row=2, column=0, sticky=tk.W, pady=4)
tk.Button(master, width=20, text='Show', command=show_entry_fields).grid(row=2, column=1, sticky=tk.W, pady=4)


                                    


tk.mainloop()
import tkinter as tk
from tkinter import messagebox

def greet():
    name = name_entry.get()
    if name:
        greeting = f"Hello, {name}!"
        if check_var.get():
            greeting += " Have a Good Day to You....."
        messagebox.showinfo("Greeting", greeting)
    else:
        messagebox.showwarning("Input Error", "Please enter your name.")

# Create the main window
root = tk.Tk()
root.title("Simple GUI App")
root.geometry("300x300")

# Label
label = tk.Label(root, text="Enter your name:")
label.pack(pady=5)

# Entry
name_entry = tk.Entry(root)
name_entry.pack(pady=5)

# Checkbox
check_var = tk.BooleanVar()
checkbox = tk.Checkbutton(root, text="Add Friendly Message", variable=check_var)

checkbox=tk.Checkbutton(root,text="Yes",variable=check_var)  
checkbox=tk.Checkbutton(root,text="No",variable=check_var)
checkbox.pack(pady=5)

# Button
button = tk.Button(root, text="Greet", command=greet)
button.pack(pady=10)

# Start the GUI event loop
root.mainloop()

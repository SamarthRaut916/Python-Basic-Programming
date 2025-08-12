

import tkinter as tk
import math

# -------------------- Main Window --------------------
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("520x480")
root.config(bg="#282c34")
root.resizable(False, False)

# -------------------- Displays --------------------
history_label = tk.Label(root, text="", anchor="e", bg="#282c34", fg="#888", font=('Arial', 12))
history_label.grid(row=0, column=0, columnspan=6, sticky="we", padx=10)

entry = tk.Entry(root, font=('Arial', 24), bd=0, relief=tk.FLAT, justify='right')
entry.grid(row=1, column=0, columnspan=6, padx=10, pady=(0, 20))
entry.config(bg="#1c1f26", fg="white", insertbackground="white", highlightthickness=2, highlightbackground="#3e4451")

# -------------------- Functions --------------------
def click(symbol):
    entry.insert(tk.END, symbol)

def clear():
    entry.delete(0, tk.END)
    history_label.config(text="")

def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def equal():
    expression = entry.get()
    try:
        # Evaluate using math functions
        result = eval(expression, {"__builtins__": None}, math.__dict__)
        history_label.config(text=expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def on_key(event):
    key = event.char
    if key in '0123456789+-*/().':
        click(key)
    elif key == '\r':  # Enter
        equal()
    elif key == '\x08':  # Backspace
        backspace()

root.bind("<Key>", on_key)

# -------------------- Buttons --------------------
buttons = [
    ('C', '#d19a66', clear),   
    ('⌫', '#d19a66', backspace),
    ('(', '#98c379', lambda: click('(')),
    (')', '#98c379', lambda: click(')')),
    ('%', '#98c379', lambda: click('%')),
    ('/', '#c678dd', lambda: click('/')),
    ('7', '#61afef', lambda: click('7')),
    ('8', '#61afef', lambda: click('8')),
    ('9', '#61afef', lambda: click('9')),
    
    ('*', '#c678dd', lambda: click('*')),
    ('sqrt', '#98c379', lambda: click('sqrt(')),
    ('+', '#e06c75', lambda: click('+')),
    
    ('6', '#61afef', lambda: click('6')),
    ('5', '#61afef', lambda: click('5')),
    ('4', '#61afef', lambda: click('4')),

    ('^', '#c678dd', lambda: click('^')),
    ('.', '#61afef', lambda: click('.')),
    ('-', '#e06c75', lambda: click('-')),    

    ('1', '#61afef', lambda: click('1')),
    ('2', '#61afef', lambda: click('2')),
    ('3', '#61afef', lambda: click('3')),
   
    ('0', '#61afef', lambda: click('0')),
    
    ('=', '#56b6c2', equal)
]

row = 2
col = 0
for (text, color, cmd) in buttons:
    if(text == "="):
                
         btn = tk.Button(root, text=text, width=12, height=2, font=('Arial', 16),
                    bg=color, fg="white", command=cmd, bd=0, relief=tk.FLAT,
                    activebackground="#3e4451", activeforeground="white")
         btn.grid(row=row, column=col, columnspan=2, padx=5, pady=5)


    else:



        btn = tk.Button(root, text=text, width=5, height=2, font=('Arial', 16),
                        bg=color, fg="white", command=cmd, bd=0, relief=tk.FLAT,
                        activebackground="#3e4451", activeforeground="white")
        btn.grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col > 5:
        col = 0
        row += 1

# -------------------- Start --------------------
root.mainloop()

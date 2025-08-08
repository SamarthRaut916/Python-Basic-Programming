import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from matplotlib import pyplot as plt

SAVE_FILE = "tasks.txt"
PREFS_FILE = "prefs.json"

tasks = []
theme = "light"

# ==== Load Preferences ====
def load_preferences():
    global theme
    if os.path.exists(PREFS_FILE):
        with open(PREFS_FILE, "r") as f:
            prefs = json.load(f)
            theme = prefs.get("theme", "light")
    else:
        save_preferences()

def save_preferences():
    with open(PREFS_FILE, "w") as f:
        json.dump({"theme": theme}, f)

# ==== Load/Save Tasks ====
def save_tasks():
    with open(SAVE_FILE, "w") as f:
        for task in tasks:
            f.write(f"{task['text']}||{int(task['done'])}\n")

def load_tasks():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            for line in f:
                text, done = line.strip().split("||")
                tasks.append({'text': text, 'done': bool(int(done))})

# ==== Theme Functions ====
def apply_theme():
    colors = {
        "light": {
            "bg": "#f8f9fa", "fg": "#212529", "accent": "#0d6efd"
        },
        "dark": {
            "bg": "#212529", "fg": "#f8f9fa", "accent": "#0d6efd"
        }
    }

    c = colors[theme]
    root.configure(bg=c["bg"])
    style.configure("TLabel", background=c["bg"], foreground=c["fg"])
    style.configure("TButton", background=c["bg"], foreground=c["fg"])
    style.configure("TFrame", background=c["bg"])
    style.configure("TCheckbutton", background=c["bg"], foreground=c["fg"])
    listbox.config(bg=c["bg"], fg=c["fg"], selectbackground=c["accent"])

def toggle_theme():
    global theme
    theme = "dark" if theme == "light" else "light"
    apply_theme()
    save_preferences()

# ==== Task Logic ====
def add_task():
    task = task_entry.get().strip()
    if task:
        tasks.append({'text': task, 'done': False})
        update_listbox()
        task_entry.delete(0, tk.END)
        save_tasks()

def delete_task():
    selected = listbox.curselection()
    if selected:
        del tasks[selected[0]]
        update_listbox()
        save_tasks()

def toggle_done(event=None):
    selected = listbox.curselection()
    if selected:
        idx = selected[0]
        tasks[idx]['done'] = not tasks[idx]['done']
        update_listbox()
        save_tasks()

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        display = f"✔ {task['text']}" if task['done'] else task['text']
        listbox.insert(tk.END, display)
    update_status()

def update_status():
    total = len(tasks)
    done = len([t for t in tasks if t['done']])
    status_var.set(f"{done}/{total} tasks completed")

# ==== Data Visualization ====
def show_chart():
    done = len([t for t in tasks if t['done']])
    not_done = len(tasks) - done

    if len(tasks) == 0:
        messagebox.showinfo("No Tasks", "Add some tasks to visualize progress.")
        return

    labels = ['Completed', 'Remaining']
    sizes = [done, not_done]
    colors = ['#28a745', '#ffc107']

    plt.figure(figsize=(4, 4))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
    plt.title("Task Completion")
    plt.axis('equal')
    plt.show()

# ==== UI Setup ====
root = tk.Tk()
root.title("🧠 Advanced Todo App")
root.geometry("550x550")

style = ttk.Style(root)

load_preferences()
load_tasks()

# Top frame
top_frame = ttk.Frame(root)
top_frame.pack(pady=15)

task_entry = ttk.Entry(top_frame, width=35)
task_entry.pack(side=tk.LEFT, padx=5)
task_entry.bind("<Return>", lambda e: add_task())

add_btn = ttk.Button(top_frame, text="Add Task", command=add_task)
add_btn.pack(side=tk.LEFT)

# Listbox
list_frame = ttk.Frame(root)
list_frame.pack(padx=15, pady=10)

listbox = tk.Listbox(list_frame, width=50, height=15, font=("Segoe UI", 11), selectbackground="#d0e0ff")
listbox.pack(side=tk.LEFT, fill=tk.BOTH)
listbox.bind("<Double-1>", toggle_done)

scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set)

# Buttons
btn_frame = ttk.Frame(root)
btn_frame.pack(pady=10)

del_btn = ttk.Button(btn_frame, text="🗑 Delete Selected", command=delete_task)
del_btn.pack(side=tk.LEFT, padx=5)

chart_btn = ttk.Button(btn_frame, text="📊 Show Progress", command=show_chart)
chart_btn.pack(side=tk.LEFT, padx=5)

theme_btn = ttk.Button(btn_frame, text="🌓 Toggle Theme", command=toggle_theme)
theme_btn.pack(side=tk.LEFT, padx=5)

# Status
status_var = tk.StringVar()
status_label = ttk.Label(root, textvariable=status_var, font=("Segoe UI", 10))
status_label.pack(pady=10)

# Start App
update_listbox()
apply_theme()
root.mainloop()

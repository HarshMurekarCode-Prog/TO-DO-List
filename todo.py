import tkinter as tk
from tkinter import messagebox

TASK_FILE = "tasks.txt"

# ---------------- Functions ---------------- #

def load_tasks():
    try:
        with open(TASK_FILE, "r") as file:
            for task in file.readlines():
                task_listbox.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass

def save_tasks():
    with open(TASK_FILE, "w") as file:
        tasks = task_listbox.get(0, tk.END)
        for task in tasks:
            file.write(task + "\n")

def add_task():
    task = task_entry.get().strip()

    if task == "":
        messagebox.showwarning("Warning", "Please enter a task.")
        return

    task_listbox.insert(tk.END, task)
    task_entry.delete(0, tk.END)
    save_tasks()

def delete_task():
    try:
        index = task_listbox.curselection()[0]
        task_listbox.delete(index)
        save_tasks()
    except:
        messagebox.showwarning("Warning", "Select a task first.")

def complete_task():
    try:
        index = task_listbox.curselection()[0]
        task = task_listbox.get(index)

        if not task.startswith("✔ "):
            task_listbox.delete(index)
            task_listbox.insert(index, "✔ " + task)

        save_tasks()

    except:
        messagebox.showwarning("Warning", "Select a task.")

# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("To-Do List")
root.geometry("450x550")
root.resizable(False, False)

title = tk.Label(
    root,
    text="My To-Do List",
    font=("Arial", 20, "bold")
)
title.pack(pady=10)

task_entry = tk.Entry(root, font=("Arial", 14))
task_entry.pack(fill="x", padx=20)

add_button = tk.Button(
    root,
    text="Add Task",
    font=("Arial", 12),
    command=add_task,
    bg="#4CAF50",
    fg="white"
)
add_button.pack(fill="x", padx=20, pady=8)

task_listbox = tk.Listbox(
    root,
    font=("Arial", 14),
    height=15
)
task_listbox.pack(fill="both", padx=20, pady=10, expand=True)

complete_button = tk.Button(
    root,
    text="Mark Completed",
    font=("Arial", 12),
    command=complete_task,
    bg="#2196F3",
    fg="white"
)
complete_button.pack(fill="x", padx=20, pady=5)

delete_button = tk.Button(
    root,
    text="Delete Task",
    font=("Arial", 12),
    command=delete_task,
    bg="#f44336",
    fg="white"
)
delete_button.pack(fill="x", padx=20, pady=5)

load_tasks()

root.mainloop()
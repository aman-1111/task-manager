import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
from datetime import datetime

# Database helper functions
def add_task(task, priority, deadline):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (task, priority, deadline) VALUES (?, ?, ?)', (task, priority, deadline))
    conn.commit()
    conn.close()

def get_tasks():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, task, priority, deadline, completed FROM tasks')
    rows = cursor.fetchall()
    conn.close()
    return rows

def mark_completed(task_id):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET completed = 1 WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()

# GUI Application
class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x700")
        self.root.title("Task & Time Management")

        # Frame for input
        frame = tk.Frame(root)
        frame.pack(pady=10)

        tk.Label(frame, text="Task:").grid(row=0, column=0, padx=5)
        self.task_entry = tk.Entry(frame, width=30)
        self.task_entry.grid(row=0, column=1, padx=5)

        tk.Label(frame, text="Priority:").grid(row=0, column=2, padx=5)
        self.priority_combo = ttk.Combobox(frame, values=["High", "Medium", "Low"], width=10)
        self.priority_combo.current(1)
        self.priority_combo.grid(row=0, column=3, padx=5)

        tk.Label(frame, text="Deadline (YYYY-MM-DD):").grid(row=1, column=0, padx=5, pady=5)
        self.deadline_entry = tk.Entry(frame, width=20)
        self.deadline_entry.grid(row=1, column=1, padx=5, pady=5)

        add_btn = tk.Button(frame, text="Add Task", command=self.add_task)
        add_btn.grid(row=1, column=3, padx=5, pady=5)

        # Task Listbox with scrollbar
        self.tasks_listbox = tk.Listbox(root, width=80, height=15)
        self.tasks_listbox.pack(padx=10, pady=10)

        self.tasks_listbox.bind('<Double-Button-1>', self.complete_task)

        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get().strip()
        priority = self.priority_combo.get()
        deadline = self.deadline_entry.get().strip()

        # Simple validation
        if not task:
            messagebox.showwarning("Input Error", "Task cannot be empty.")
            return
        try:
            datetime.strptime(deadline, '%Y-%m-%d')
        except ValueError:
            messagebox.showwarning("Input Error", "Deadline must be in YYYY-MM-DD format.")
            return

        add_task(task, priority, deadline)
        self.task_entry.delete(0, tk.END)
        self.deadline_entry.delete(0, tk.END)
        self.priority_combo.current(1)
        self.load_tasks()

    def load_tasks(self):
        self.tasks_listbox.delete(0, tk.END)
        tasks = get_tasks()
        for t in tasks:
            task_id, task, priority, deadline, completed = t
            status = "✔️" if completed else "❌"
            display_text = f"{task_id}. [{status}] {task} - Priority: {priority}, Deadline: {deadline}"
            self.tasks_listbox.insert(tk.END, display_text)

    def complete_task(self, event):
        selection = self.tasks_listbox.curselection()
        if not selection:
            return
        index = selection[0]
        task_line = self.tasks_listbox.get(index)
        task_id = int(task_line.split('.')[0])
        mark_completed(task_id)
        self.load_tasks()

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()

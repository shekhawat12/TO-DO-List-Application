import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.configure(bg="#f0f0f0")  # Set background color for the main window

        # Task Input Section
        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)
        self.task_entry.configure(bg="#ffffff", fg="#000000")  # White background, black text

        self.category_var = tk.StringVar(value="General")
        self.category_menu = tk.OptionMenu(root, self.category_var, "General", "Work", "Personal")
        self.category_menu.grid(row=0, column=1, padx=10, pady=10)
        self.category_menu.configure(bg="#ffffff", fg="#000000")  # White background, black text

        self.due_date_var = tk.StringVar()
        self.due_date_entry = tk.Entry(root, textvariable=self.due_date_var, width=15)
        self.due_date_entry.grid(row=0, column=2, padx=10, pady=10)
        self.due_date_entry.configure(bg="#ffffff", fg="#000000")  # White background, black text
        self.due_date_var.set(datetime.now().strftime("%Y-%m-%d"))

        self.add_task_button = tk.Button(root, text="Add Task", command=self.add_task, bg="#4caf50", fg="#ffffff")
        self.add_task_button.grid(row=0, column=3, padx=10, pady=10)

        # Task List Section
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=80, height=20)
        self.task_listbox.grid(row=1, column=0, columnspan=4, padx=10, pady=10)
        self.task_listbox.configure(bg="#ffffff", fg="#000000")  # White background, black text

        # Task Action Buttons
        self.delete_task_button = tk.Button(root, text="Delete Task", command=self.delete_task, bg="#f44336", fg="#ffffff")
        self.delete_task_button.grid(row=2, column=0, padx=10, pady=10)

        self.mark_done_button = tk.Button(root, text="Mark Done", command=self.mark_done, bg="#2196f3", fg="#ffffff")
        self.mark_done_button.grid(row=2, column=1, padx=10, pady=10)

        self.show_status_button = tk.Button(root, text="Show Status", command=self.show_status, bg="#ffc107", fg="#000000")
        self.show_status_button.grid(row=2, column=2, padx=10, pady=10)

        # Task Storage
        self.tasks = []

    def add_task(self):
        task_description = self.task_entry.get()
        category = self.category_var.get()
        due_date = self.due_date_var.get()

        if task_description:
            task = {"description": task_description, "category": category, "due_date": due_date, "completed": False}
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task description.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            del self.tasks[selected_index[0]]
            self.update_task_listbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def mark_done(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.tasks[selected_index[0]]['completed'] = True
            self.update_task_listbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

    def show_status(self):
        total_tasks = len(self.tasks)
        completed_tasks = sum(task['completed'] for task in self.tasks)
        messagebox.showinfo("Task Status", f"Total Tasks: {total_tasks}\nCompleted Tasks: {completed_tasks}")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for index, task in enumerate(self.tasks):
            status = "Completed" if task["completed"] else "Pending"
            self.task_listbox.insert(tk.END, f"{index+1}. {task['description']} - {task['category']} - {task['due_date']} - {status}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

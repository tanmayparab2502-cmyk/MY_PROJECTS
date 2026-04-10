import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os


FILE_NAME = "todo_gui_tasks.json"

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("My To-Do List")
        self.root.geometry("400x550")
        self.root.config(bg="#f0f0f0")
        
   
        self.tasks = self.load_tasks()
        
        self.setup_ui()
        self.refresh_listbox()

  
    def load_tasks(self):
        """Loads tracked tasks from the JSON file."""
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, 'r') as file:
                return json.load(file)
        return []

    def save_tasks(self):
        """Saves the current state of tasks to track them permanently."""
        with open(FILE_NAME, 'w') as file:
            json.dump(self.tasks, file, indent=4)

 
    def setup_ui(self):
        """Builds the buttons, listbox, and entry fields."""
     
        title_label = tk.Label(self.root, text="Daily Tasks", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
        title_label.pack(pady=10)


        input_frame = tk.Frame(self.root, bg="#f0f0f0")
        input_frame.pack(pady=5, padx=20, fill=tk.X)

        self.task_entry = tk.Entry(input_frame, font=("Helvetica", 12))
        self.task_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.task_entry.bind("<Return>", lambda event: self.add_task()) 

        add_btn = tk.Button(input_frame, text="Add Task", font=("Helvetica", 10, "bold"), 
                            bg="#4CAF50", fg="white", command=self.add_task)
        add_btn.pack(side=tk.RIGHT)

   
        list_frame = tk.Frame(self.root)
        list_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox = tk.Listbox(list_frame, font=("Helvetica", 12), selectbackground="#a6a6a6",
                                  yscrollcommand=scrollbar.set, activestyle="none")
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.listbox.yview)

        
        btn_frame = tk.Frame(self.root, bg="#f0f0f0")
        btn_frame.pack(pady=10, fill=tk.X)

  
        complete_btn = tk.Button(btn_frame, text="Mark Done / Undone", command=self.toggle_complete)
        complete_btn.pack(side=tk.LEFT, expand=True, padx=5)

        edit_btn = tk.Button(btn_frame, text="Edit Task", command=self.edit_task)
        edit_btn.pack(side=tk.LEFT, expand=True, padx=5)

        delete_btn = tk.Button(btn_frame, text="Delete Task", bg="#f44336", fg="white", command=self.delete_task)
        delete_btn.pack(side=tk.LEFT, expand=True, padx=5)


    def refresh_listbox(self):
        """Clears and repopulates the listbox based on current tracked tasks."""
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✓" if task["done"] else "  "
            display_text = f"[{status}] {task['name']}"
            self.listbox.insert(tk.END, display_text)
            
         
            if task["done"]:
                self.listbox.itemconfig(tk.END, {'fg': 'gray'})
            else:
                self.listbox.itemconfig(tk.END, {'fg': 'black'})

    def add_task(self):
        """Creates a new task."""
        task_name = self.task_entry.get().strip()
        if task_name:
            self.tasks.append({"name": task_name, "done": False})
            self.save_tasks()
            self.refresh_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task name.")

    def toggle_complete(self):
        """Updates a task by marking it done or undone."""
        try:
            selected_index = self.listbox.curselection()[0]
        
            self.tasks[selected_index]["done"] = not self.tasks[selected_index]["done"]
            self.save_tasks()
            self.refresh_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to mark.")

    def edit_task(self):
        """Updates a task's name."""
        try:
            selected_index = self.listbox.curselection()[0]
            current_name = self.tasks[selected_index]["name"]
            
         
            new_name = simpledialog.askstring("Edit Task", "Update task name:", initialvalue=current_name)
            
            if new_name and new_name.strip():
                self.tasks[selected_index]["name"] = new_name.strip()
                self.save_tasks()
                self.refresh_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to edit.")

    def delete_task(self):
        """Deletes a task from the tracker."""
        try:
            selected_index = self.listbox.curselection()[0]
            del self.tasks[selected_index]
            self.save_tasks()
            self.refresh_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

# --- Run the App ---
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

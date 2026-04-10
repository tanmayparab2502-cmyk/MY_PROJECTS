import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = length_var.get()
    

    char_pool = ""
    if upper_var.get():
        char_pool += string.ascii_uppercase
    if lower_var.get():
        char_pool += string.ascii_lowercase
    if digit_var.get():
        char_pool += string.digits
    if symbol_var.get():
        char_pool += string.punctuation
        
   
    if not char_pool:
        messagebox.showwarning("Warning", "Please select at least one character type!")
        return
        

    password = "".join(random.choice(char_pool) for _ in range(length))
    
    
    password_var.set(password)


root = tk.Tk()
root.title("Password Generator")
root.geometry("350x350")
root.config(padx=20, pady=20)


length_var = tk.IntVar(value=12) 
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digit_var = tk.BooleanVar(value=True)
symbol_var = tk.BooleanVar(value=True)
password_var = tk.StringVar()


tk.Label(root, text="Password Length:", font=("Arial", 10, "bold")).pack(anchor="w")
tk.Scale(root, from_=4, to_=64, orient="horizontal", variable=length_var).pack(fill="x")


tk.Label(root, text="Complexity:", font=("Arial", 10, "bold")).pack(anchor="w", pady=(15, 5))
tk.Checkbutton(root, text="Uppercase Letters (A-Z)", variable=upper_var).pack(anchor="w")
tk.Checkbutton(root, text="Lowercase Letters (a-z)", variable=lower_var).pack(anchor="w")
tk.Checkbutton(root, text="Numbers (0-9)", variable=digit_var).pack(anchor="w")
tk.Checkbutton(root, text="Symbols (!@#$)", variable=symbol_var).pack(anchor="w")


tk.Button(root, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white", font=("Arial", 10, "bold")).pack(pady=20)

# 6. Create Output Display Box
tk.Entry(root, textvariable=password_var, font=("Courier", 14), state="readonly", justify="center").pack(fill="x")

# 7. Start the application loop
root.mainloop()

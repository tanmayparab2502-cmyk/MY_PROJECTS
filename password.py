import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = length_var.get()
    
    # Build the character pool based on user selection
    char_pool = ""
    if upper_var.get():
        char_pool += string.ascii_uppercase
    if lower_var.get():
        char_pool += string.ascii_lowercase
    if digit_var.get():
        char_pool += string.digits
    if symbol_var.get():
        char_pool += string.punctuation
        
    # Guard against generating a password with an empty character pool
    if not char_pool:
        messagebox.showwarning("Warning", "Please select at least one character type!")
        return
        
    # Generate the random password
    password = "".join(random.choice(char_pool) for _ in range(length))
    
    # Update the text box on the screen
    password_var.set(password)

# 1. Set up the main application window
root = tk.Tk()
root.title("Password Generator")
root.geometry("350x350")
root.config(padx=20, pady=20)

# 2. Define Variables to store user choices
length_var = tk.IntVar(value=12) # Default length is 12
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digit_var = tk.BooleanVar(value=True)
symbol_var = tk.BooleanVar(value=True)
password_var = tk.StringVar()

# 3. Create the UI Elements (Length Slider)
tk.Label(root, text="Password Length:", font=("Arial", 10, "bold")).pack(anchor="w")
tk.Scale(root, from_=4, to_=64, orient="horizontal", variable=length_var).pack(fill="x")

# 4. Create the UI Elements (Complexity Checkboxes)
tk.Label(root, text="Complexity:", font=("Arial", 10, "bold")).pack(anchor="w", pady=(15, 5))
tk.Checkbutton(root, text="Uppercase Letters (A-Z)", variable=upper_var).pack(anchor="w")
tk.Checkbutton(root, text="Lowercase Letters (a-z)", variable=lower_var).pack(anchor="w")
tk.Checkbutton(root, text="Numbers (0-9)", variable=digit_var).pack(anchor="w")
tk.Checkbutton(root, text="Symbols (!@#$)", variable=symbol_var).pack(anchor="w")

# 5. Create Generate Button
tk.Button(root, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white", font=("Arial", 10, "bold")).pack(pady=20)

# 6. Create Output Display Box
tk.Entry(root, textvariable=password_var, font=("Courier", 14), state="readonly", justify="center").pack(fill="x")

# 7. Start the application loop
root.mainloop()
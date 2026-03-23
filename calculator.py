import tkinter as tk

def click(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + str(value))

def clear():
    display.delete(0, tk.END)

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# Create main window
app = tk.Tk()
app.title("Python Calculator")
app.geometry("320x420")
app.resizable(False, False)

# Display
display = tk.Entry(app, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify="right")
display.pack(fill=tk.BOTH, padx=10, pady=10)

# Button frame
frame = tk.Frame(app)
frame.pack()

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

row = 0
col = 0

for btn in buttons:
    if btn == "=":
        action = calculate
    else:
        action = lambda x=btn: click(x)

    tk.Button(
        frame,
        text=btn,
        width=5,
        height=2,
        font=("Arial", 14),
        command=action
    ).grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col > 3:
        col = 0
        row += 1

# Clear button
tk.Button(
    app,
    text="Clear",
    width=22,
    height=2,
    font=("Arial", 14),
    command=clear
).pack(pady=10)

# Run app
app.mainloop()
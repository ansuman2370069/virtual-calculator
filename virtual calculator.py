import tkinter as tk
from tkinter import messagebox

# Function to update expression in the entry box
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

# Function to evaluate final expression
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except Exception:
        equation.set(" error ")
        expression = ""

# Function to clear the entry box
def clear():
    global expression
    expression = ""
    equation.set("")

# Main program
if __name__ == "__main__":
    # create GUI window
    gui = tk.Tk()
    gui.configure(background="black")
    gui.title("Virtual Calculator")
    gui.geometry("350x450")

    expression = ""
    equation = tk.StringVar()

    # Entry box
    entry_field = tk.Entry(gui, textvariable=equation, font=('Arial', 20, 'bold'), bd=10, insertwidth=2, width=15,
                           borderwidth=4, relief="ridge", justify="right")
    entry_field.grid(row=0, column=0, columnspan=4, pady=20)

    # Button layout
    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ]

    for (text, row, col) in buttons:
        if text == "=":
            action = equalpress
        else:
            action = lambda x=text: press(x)
        tk.Button(gui, text=text, padx=20, pady=20, bd=4, fg="white", bg="gray20",
                  font=('Arial', 15, 'bold'), command=action).grid(row=row, column=col, sticky="nsew")

    # Clear Button
    tk.Button(gui, text='C', padx=20, pady=20, bd=4, fg="white", bg="red",
              font=('Arial', 15, 'bold'), command=clear).grid(row=5, column=0, columnspan=4, sticky="nsew")

    # Run the GUI loop
    gui.mainloop()

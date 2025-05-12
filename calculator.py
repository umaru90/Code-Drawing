import tkinter as tk

# Function to handle button clicks
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

# Function to handle clear button
def clear():
    entry.delete(0, tk.END)

# Function to handle equal button
def calculate():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
window = tk.Tk()
window.title("Calculator")
window.configure(bg="black")

# Create the entry widget
entry = tk.Entry(window, width=15, justify=tk.RIGHT, font=('Arial', 16), bd=0, relief=tk.SUNKEN)
entry.config(highlightbackground="purple", highlightcolor="purple", highlightthickness=2, fg="white", bg="black")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create the number buttons
button_numbers = []
for i in range(9):
    button_numbers.append(tk.Button(window, text=str(i+1), width=5, height=2, font=('Arial', 14),
                                   command=lambda num=i+1: button_click(num), bd=0, relief=tk.RAISED))
    button_numbers[i].config(fg="white", bg="black", activeforeground="white", activebackground="black")
    button_numbers[i].grid(row=1 + (i // 3), column=i % 3, padx=5, pady=5)

# Create the operator buttons
button_plus = tk.Button(window, text="+", width=5, height=2, font=('Arial', 14),
                        command=lambda: button_click("+"), bd=0, relief=tk.RAISED)
button_plus.config(fg="white", bg="black", activeforeground="white", activebackground="black")
button_plus.grid(row=4, column=0, padx=5, pady=5)

button_minus = tk.Button(window, text="-", width=5, height=2, font=('Arial', 14),
                         command=lambda: button_click("-"), bd=0, relief=tk.RAISED)
button_minus.config(fg="white", bg="black", activeforeground="white", activebackground="black")
button_minus.grid(row=4, column=1, padx=5, pady=5)

button_multiply = tk.Button(window, text="*", width=5, height=2, font=('Arial', 14),
                            command=lambda: button_click("*"), bd=0, relief=tk.RAISED)
button_multiply.config(fg="white", bg="black", activeforeground="white", activebackground="black")
button_multiply.grid(row=5, column=0, padx=5, pady=5)

button_divide = tk.Button(window, text="/", width=5, height=2, font=('Arial', 14),
                          command=lambda: button_click("/"), bd=0, relief=tk.RAISED)
button_divide.config(fg="white", bg="black", activeforeground="white", activebackground="black")
button_divide.grid(row=5, column=1, padx=5, pady=5)

button_equal = tk.Button(window, text="=", width=11, height=2, font=('Arial', 14),
                         command=calculate, bd=0, relief=tk.RAISED)
button_equal.config(fg="white", bg="black", activeforeground="white", activebackground="black")
button_equal.grid(row=4, column=2, columnspan=2, padx=5, pady=5)

button_clear = tk.Button(window, text="Clear", width=11, height=2, font=('Arial', 14),
                         command=clear, bd=0, relief=tk.RAISED)
button_clear.config(fg="white", bg="black", activeforeground="white", activebackground="black")
button_clear.grid(row=5, column=2, columnspan=2, padx=5, pady=5)

# Start the main event loop
window.mainloop()

import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)

root = tk.Tk()
root.title("Digital Clock")

window_width = 400  # Adjust the window width as needed
window_height = 200  # Adjust the window height as needed

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))

root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

clock_label = tk.Label(root, font=("Arial", 80), bg="black", fg="white")
clock_label.place(relx=0.5, rely=0.5, anchor="center")

update_time()

root.mainloop()

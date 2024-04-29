import tkinter as tk

def validate_input(new_value):
    if new_value == "":
        return True
    try:
        int(new_value)
        return True
    except ValueError:
        return False

root = tk.Tk()

vcmd = root.register(validate_input)  # Registrar la función de validación

entry = tk.Entry(root, validate="key", validatecommand=(vcmd, "%P"))
entry.pack()

root.mainloop()
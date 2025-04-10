import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Basic GUI window")
root.geometry("300x350")

# Label
label = tk.Label(root, text="This is a label")
label.pack(pady=5)

# Entry Box
entry = tk.Entry(root)
entry.pack(pady=5)

# Button
button = tk.Button(root, text="Click me")
button.pack(pady=5)

# Radio Buttons
radio1 = tk.Radiobutton(root, text="Option 1", value=1)
radio2 = tk.Radiobutton(root, text="Option 2", value=2)
radio1.pack()
radio2.pack()

# Checkbox
checkbox = tk.Checkbutton(root, text="Subscribe to newsletter")
checkbox.pack(pady=5)

# Dropdown menu
options = ["JS", "PY", "C#"]
dropdown_var = tk.StringVar(value=options[0])

dropdown_label = tk.Label(root, text="Choose fav language")
dropdown_label.pack(pady=10)

dropdown = tk.OptionMenu(root, dropdown_var, *options)
dropdown.pack()

# Run the application
root.mainloop()

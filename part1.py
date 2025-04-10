import tkinter as tk

# Create the main window
root=tk.Tk()
root.title("Basic GUI window")
root.geometry("300x350")

# Label
label=tk.Label(root, text="This is a label")
label.pack(pady=10)

# Run the application
root.mainloop()
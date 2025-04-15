import tkinter as tk

root = tk.Tk()
root.title("Exercises")

# E. 1.
heading1 = tk.Label(root, text="1", font=("Arial", 16, "bold"), fg='blue')
heading1.pack(pady=10)

label1 = tk.Label(root, text="Hello, Tkinter!")
label1.pack()

# E. 2.
heading2 = tk.Label(root, text="2", font=("Arial", 16, "bold"), fg='blue')
heading2.pack(pady=10)


def on_click():
    label2.config(text="You clicked me!")


label2 = tk.Label(root, text="Hello")
label2.pack()

button2 = tk.Button(root, text="Click me", command=on_click)
button2.pack()

# E. 3.
heading3 = tk.Label(root, text="3", font=("Arial", 16, "bold"), fg='blue')
heading3.pack(pady=10)


def show_name():
    name3 = entry3.get()
    label3.config(text=f"Hello {name3}!")


entry3 = tk.Entry(root)
entry3.pack()

button3 = tk.Button(root, text="submit", command=show_name)
button3.pack()

label3 = tk.Label(root, text="")
label3.pack()

# E. 4.
heading4 = tk.Label(root, text="4", font=("Arial", 16, "bold"), fg='blue')
heading4.pack(pady=10)


def show_color():
    label4.config(text=f"{color4.get()}")


color4 = tk.StringVar()

red_radio = tk.Radiobutton(
    root, text="Red", variable=color4, value="Red").pack()
green_radio = tk.Radiobutton(
    root, text="Green", variable=color4, value="Green").pack()
blue_radio = tk.Radiobutton(
    root, text="Blue", variable=color4, value="Blue").pack()

button4 = tk.Button(root, text="Submit", command=show_color).pack()
label4 = tk.Label(root, text="")
label4.pack()

# E. 5.
heading5 = tk.Label(root, text="5", font=("Arial", 16, "bold"), fg='blue')
heading5.pack(pady=10)


def subscribe_status():
    text5 = "Subscribed" if is_checked5.get() else "Not Subscribed"
    label5.config(text=text5)


is_checked5 = tk.BooleanVar()

checkbox5 = tk.Checkbutton(root, text="Subscribe",
                           variable=is_checked5, command=subscribe_status)
checkbox5.pack(pady=5)

label5 = tk.Label(root, text="Not Subscribed")
label5.pack()


root.mainloop()

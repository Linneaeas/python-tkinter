import tkinter as tk
from tkinter import messagebox

def on_submit():
    name=entry.get()
    selected_gender=gender_var.get()
    subscribed=subscribe_var.get()
    language=language=language_var.get()

    info=f"Name:{name}\nGender: {selected_gender}\nSubscribed:{subscribed}\nLanguage:{language}"
    messagebox.showinfo("Submittedinfo", info)
    
    
# Main window
root=tk.Tk()
root.title("Robins Demo")
root.geometry("350x350")

# Entry widget
label_name=tk.Label(root, text="Name:")
label_name.pack(pady=5)

entry=tk.Entry(root)
entry.pack()

# Radiobuttons for gender
label_gender=tk.Label(root, text="Gender:")
label_gender.pack(pady=5)

gender_var=tk.StringVar(value="Other")

radio_male=tk.Radiobutton(root, text="Male", variable=gender_var, value="Male")
radio_male.pack()
radio_female=tk.Radiobutton(root, text="Female", variable=gender_var, value="Female")
radio_female.pack()
radio_other=tk.Radiobutton(root, text="Other", variable=gender_var, value="Pther")
radio_other.pack()

# Checkbox
subscribe_var=tk.BooleanVar()
checkbox=tk.Checkbutton(root, text="Subscribe to our newsletter?", variable=subscribe_var)
checkbox.pack(pady=5)

# Dropdown menu
label_language=tk.Label(root, text="Fav language")
label_language.pack(pady=5)

languages=["JS", "PY", "C#", "C++", "Java"]
language_var=tk.StringVar(value=languages[1])

dropdown=tk.OptionMenu(root, language_var, *languages)
dropdown.pack()

# Submit button
submit_button=tk.Button(root, text="Submit", command=on_submit)
submit_button.pack(pady=20)

root.mainloop()
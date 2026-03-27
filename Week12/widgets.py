import tkinter as tk
from tkinter import messagebox, filedialog

root = tk.Tk()
root.title("AI/ML Dashboard")
root.geometry("600x420")
root.config(bg="#f0f8ff")

def open_dataset():
    file = filedialog.askopenfilename()
    if file:
        status.config(text=f"Dataset Loaded: {file.split('/')[-1]}", fg="green")

def show_info():
    messagebox.showinfo("AI Info", "AI helps machines learn patterns from data.")

def show_warning():
    messagebox.showwarning("Warning", "Check your dataset for missing values!")

def show_error():
    messagebox.showerror("Error", "Model failed due to invalid input!")

def select_domain():
    selected = listbox.curselection()
    if selected:
        domain = listbox.get(selected[0])
        status.config(text=f"Selected Domain: {domain}", fg="blue")
    else:
        messagebox.showwarning("Warning", "Please select a domain")

# ---------------- Menu ----------------
menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Load Dataset", command=open_dataset)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

menu_bar.add_cascade(label="File", menu=file_menu)

help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="Info", command=show_info)
help_menu.add_command(label="Warning", command=show_warning)
help_menu.add_command(label="Error", command=show_error)

menu_bar.add_cascade(label="Messages", menu=help_menu)

root.config(menu=menu_bar)

# ---------------- Title ----------------
tk.Label(root, text="AI / ML Control Panel",
         font=("Arial", 16, "bold"),
         bg="#f0f8ff").pack(pady=10)

# ---------------- Listbox Section ----------------
frame = tk.Frame(root)
frame.pack(pady=10)

scroll = tk.Scrollbar(frame)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(frame, height=8, width=30,
                     yscrollcommand=scroll.set)
listbox.pack()

scroll.config(command=listbox.yview)

domains = [
    "Machine Learning", "Deep Learning", "NLP",
    "Computer Vision", "Data Science",
    "Big Data", "AI Ethics", "Robotics"
]

for d in domains:
    listbox.insert(tk.END, d)

# ---------------- Menubutton ----------------
mb = tk.Menubutton(root, text="Quick Actions", bg="lightgray")
mb.menu = tk.Menu(mb, tearoff=0)
mb["menu"] = mb.menu

mb.menu.add_command(label="Load Dataset", command=open_dataset)
mb.menu.add_command(label="Show Info", command=show_info)
mb.menu.add_command(label="Select Domain", command=select_domain)

mb.pack(pady=10)

# ---------------- Buttons ----------------
tk.Button(root, text="Select Domain",
          command=select_domain,
          bg="#4CAF50", fg="white", width=18).pack(pady=5)

tk.Button(root, text="Load Dataset",
          command=open_dataset,
          bg="#2196F3", fg="white", width=18).pack(pady=5)

# ---------------- Status Label ----------------
status = tk.Label(root, text="Status: Ready",
                  bg="#f0f8ff", fg="black", font=("Arial", 11))
status.pack(pady=15)
root.mainloop()
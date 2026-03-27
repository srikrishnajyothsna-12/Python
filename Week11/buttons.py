import tkinter as tk

def show():
    # Get selected hobbies
    hobbies = []
    if var1.get() == 1:
        hobbies.append("Reading")
    if var2.get() == 1:
        hobbies.append("Sports")
    if var3.get() == 1:
        hobbies.append("Music")

    # Get selected gender
    gender = gender_var.get()

    # Display result
    result.config(text=f"Hobbies: {', '.join(hobbies)}\nGender: {gender}")

root = tk.Tk()
root.title("Checkbutton & Radiobutton")
root.geometry("300x300")

# -------------------------------
#  Checkbuttons (Multiple Selection)
# -------------------------------
tk.Label(root, text="Select Hobbies:").pack()

var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()

tk.Checkbutton(root, text="Reading", variable=var1).pack()
tk.Checkbutton(root, text="Sports", variable=var2).pack()
tk.Checkbutton(root, text="Music", variable=var3).pack()

# -------------------------------
#  Radiobuttons (Single Selection)
# -------------------------------
tk.Label(root, text="Select Gender:").pack()

gender_var = tk.StringVar()

tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").pack()
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").pack()

# Button
tk.Button(root, text="Submit", command=show).pack(pady=10)

# Result Label
result = tk.Label(root, text="")
result.pack()

root.mainloop()
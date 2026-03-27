import tkinter as tk

root = tk.Tk()
root.title("Geometry Demo")
root.geometry("500x400")
root.config(bg="white")

# ------------------- PACK -------------------
frame_pack = tk.Frame(root, bg="lavender")
frame_pack.pack(fill="both", expand=True, pady=5)

label1 = tk.Label(frame_pack, text="PACK SECTION", bg="lavender", fg="purple", font=("Helvetica", 14, "bold"))
label1.pack(pady=5)

btn1 = tk.Button(frame_pack, text="One", bg="white")
btn1.pack(side=tk.RIGHT, padx=15, pady=10)

btn2 = tk.Button(frame_pack, text="Two", bg="white")
btn2.pack(side=tk.RIGHT, padx=15, pady=10)

btn3 = tk.Button(frame_pack, text="Three", bg="white")
btn3.pack(side=tk.RIGHT, padx=15, pady=10)

# ------------------- GRID -------------------
frame_grid = tk.Frame(root, bg="lightgray")
frame_grid.pack(fill="both", expand=True, pady=5)

label2 = tk.Label(frame_grid, text="GRID SECTION", bg="lightgray", fg="black", font=("Helvetica", 14, "bold"))
label2.grid(row=0, column=0, columnspan=2, pady=5)

label3 = tk.Label(frame_grid, text="Email:")
label3.grid(row=1, column=0, padx=5, pady=5)

entry1 = tk.Entry(frame_grid)
entry1.grid(row=1, column=1, padx=5, pady=5)

label4 = tk.Label(frame_grid, text="Phone:")
label4.grid(row=2, column=0, padx=5, pady=5)

entry2 = tk.Entry(frame_grid)
entry2.grid(row=2, column=1, padx=5, pady=5)

btn4 = tk.Button(frame_grid, text="Submit", bg="green", fg="white")
btn4.grid(row=3, column=0, columnspan=2, pady=10)

# ------------------- PLACE -------------------
frame_place = tk.Frame(root, bg="peachpuff", height=120)
frame_place.pack(fill="both", expand=True, pady=5)

label5 = tk.Label(frame_place, text="PLACE SECTION", bg="peachpuff", fg="brown", font=("Helvetica", 14, "bold"))
label5.place(x=170, y=10)

btn5 = tk.Button(frame_place, text="Yes", bg="lightgreen")
btn5.place(x=140, y=60)

btn6 = tk.Button(frame_place, text="No", bg="salmon")
btn6.place(x=260, y=60)
root.mainloop()
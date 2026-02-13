import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("VELOCICODE V1")
root.geometry("400x500")
root.configure(bg='#050505')

# Brand Header
header = tk.Label(root, text="V", fg="#00ffcc", bg="#050505", font=("Arial", 70, "bold"))
header.pack(pady=20)

# Script Input Area
editor = tk.Text(root, bg="#111", fg="#00ffcc", font=("Consolas", 10), insertbackground="white")
editor.pack(padx=20, pady=10, fill="both", expand=True)

# Functionality
def attach():
    messagebox.showinfo("Velocicode", "API Successfully Attached")

def run_script():
    # Logic for execution goes here
    print("Executing...")

# Footer Buttons
btn_frame = tk.Frame(root, bg="#050505")
btn_frame.pack(pady=15)

tk.Button(btn_frame, text="ATTACH", command=attach, bg="#00ffcc", fg="black", width=12, font=("Arial", 9, "bold")).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="EXECUTE", command=run_script, bg="#ffffff", fg="black", width=12, font=("Arial", 9, "bold")).grid(row=0, column=1, padx=10)

root.mainloop()
# Update this line in your launcher!
with open("v_core.lua", "r") as f:
    lua_code = f.read()


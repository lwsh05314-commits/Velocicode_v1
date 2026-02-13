import tkinter as tk
from tkinter import messagebox

# Executor Window Setup
root = tk.Tk()
root.title("VELOCICODE EXECUTOR V1")
root.geometry("450x350")
root.configure(bg='#080808')
root.attributes('-topmost', True) # Keeps executor on top of game

# UI Components
title_label = tk.Label(root, text="VELOCICODE", fg="#00ffcc", bg="#080808", font=("Impact", 24))
title_label.pack(pady=5)

# Script Box (Where users paste their code)
script_box = tk.Text(root, bg="#111", fg="#00ffcc", font=("Consolas", 10), insertbackground="white", borderwidth=0)
script_box.pack(padx=10, pady=5, fill="both", expand=True)

# Executor Functions
def attach():
    # Placeholder for the DLL injection logic
    messagebox.showinfo("Velocicode", "Dll Successfully Injected.")

def execute():
    script = script_box.get("1.0", "end-1c")
    if script == "":
        messagebox.showwarning("Warning", "Please enter a script to execute.")
    else:
        print(f"Executing Script: {script[:20]}...")

def clear():
    script_box.delete("1.0", "end")

# Button Bar
btn_frame = tk.Frame(root, bg="#080808")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="EXECUTE", command=execute, bg="#00ffcc", width=10).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="ATTACH", command=attach, bg="#222", fg="white", width=10).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="CLEAR", command=clear, bg="#222", fg="white", width=10).grid(row=0, column=2, padx=5)

root.mainloop()
import os
from pathlib import Path
import ctypes

# This finds the EXACT folder where your script is sitting
BASE_DIR = Path(__file__).parent 

def attach():
    dll_name = "vc_runtime_x64.dll"
    lua_name = "v_core.lua"
    
    # Construct the full paths so it never misses them
    dll_path = BASE_DIR / dll_name
    lua_path = BASE_DIR / lua_name

    if dll_path.exists() and lua_path.exists():
        try:
            # The "Secret Bridge" Injection
            lib = ctypes.WinDLL(str(dll_path))
            with open(lua_path, "r") as f:
                script = f.read()
            
            # This 'adds the stuff' to Roblox
            lib.Execute(script.encode('utf-8')) 
            messagebox.showinfo("Velocicode", "Bypass Injected! 🇧🇪 Stable.")
        except Exception as e:
            messagebox.showerror("Error", f"Injection failed: {e}")
    else:
        messagebox.showerror("404", "Missing vc_runtime_x64.dll or v_core.lua in folder!")
def attach():
    # Use the names we agreed on for the 'stuff'
    dll_file = "vc_runtime_x64.dll" 
    lua_file = "v_core.lua" 
    
    try:
        # This part 'takes' the Roblox app and modifies it
        #  STATUS: ATTEMPTING BYPASS
        import ctypes
        lib = ctypes.WinDLL(f"./{dll_file}")
        
        with open(lua_file, "r") as f:
            lua_content = f.read()
            
        lib.Execute(lua_content.encode('utf-8'))
        messagebox.showinfo("Velocicode", "Successfully added the V-Icon and UI! [🇧🇪]")
        
    except FileNotFoundError:
        messagebox.showerror("Error", "Missing v_core.lua or the DLL. Check your folder!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to modify Roblox: {e}")

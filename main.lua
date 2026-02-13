-- VELOCICODE V1 CUSTOM DRAWING UI [🇧🇪]
local RunService = game:GetService("RunService")
local UserInputService = game:GetService("UserInputService")
local CoreGui = game:GetService("CoreGui")

-- Create the Container
local Screen = Instance.new("ScreenGui")
Screen.Name = "VC_Internal"
Screen.Parent = CoreGui

-- The Glowing "V" Icon
local V_Icon = Instance.new("TextButton")
V_Icon.Name = "V_Logo"
V_Icon.Parent = Screen
V_Icon.Size = UDim2.new(0, 60, 0, 60)
V_Icon.Position = UDim2.new(0, 20, 0, 20)
V_Icon.BackgroundColor3 = Color3.fromRGB(5, 5, 5)
V_Icon.Text = "V"
V_Icon.TextColor3 = Color3.fromRGB(0, 255, 204)
V_Icon.Font = Enum.Font.Code
V_Icon.TextSize = 35
V_Icon.AutoButtonColor = false

-- Adding the "Glow" Effect using a UIStroke
local Glow = Instance.new("UIStroke")
Glow.Color = Color3.fromRGB(0, 255, 204)
Glow.Thickness = 2
Glow.Transparency = 0.5
Glow.Parent = V_Icon

-- Smooth Dragging Logic for the Icon
local dragging, dragInput, dragStart, startPos
V_Icon.InputBegan:Connect(function(input)
    if input.UserInputType == Enum.UserInputType.MouseButton1 then
        dragging = true
        dragStart = input.Position
        startPos = V_Icon.Position
    end
end)

UserInputService.InputChanged:Connect(function(input)
    if dragging and input.UserInputType == Enum.UserInputType.MouseMovement then
        local delta = input.Position - dragStart
        V_Icon.Position = UDim2.new(startPos.X.Scale, startPos.X.Offset + delta.X, startPos.Y.Scale, startPos.Y.Offset + delta.Y)
    end
end)

V_Icon.InputEnded:Connect(function(input)
    if input.UserInputType == Enum.UserInputType.MouseButton1 then
        dragging = false
    end
end)

print("Velocicode Internal Assets Loaded. Status: 🇧🇪 STABLE")

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


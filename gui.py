import os
import subprocess
import tkinter as tk

# Function to start the AI bot
def start_ai():
    output_label.config(text="Starting AI...")
    subprocess.Popen(["python", "main.py"])

# Function to stop the AI bot (closes the process)
def stop_ai():
    output_label.config(text="Stopping AI...")
    os.system("taskkill /f /im python.exe")  # Windows
    os.system("pkill -f main.py")  # Mac/Linux

# Create GUI window
root = tk.Tk()
root.title("Clash Royale AI")
root.geometry("300x200")

# Buttons
start_button = tk.Button(root, text="Start AI", command=start_ai, width=20)
start_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop AI", command=stop_ai, width=20)
stop_button.pack(pady=10)

# Status label
output_label = tk.Label(root, text="AI Status: Idle")
output_label.pack(pady=20)

# Run GUI loop
root.mainloop()

import tkinter as tk
from tkinter import ttk

def create_ui():
    root = tk.Tk()
    root.title("Administration")

    # Title Label
    tk.Label(root, text="Name and Passwords").grid(row=0, column=0, columnspan=4, sticky="w")

    # Server Details
    tk.Label(root, text="Server Name:").grid(row=1, column=0, sticky="e")
    tk.Entry(root).grid(row=1, column=1, sticky="w")

    tk.Label(root, text="Server Password:").grid(row=2, column=0, sticky="e")
    tk.Entry(root, show="*").grid(row=2, column=1, sticky="w")

    tk.Label(root, text="Admin Password:").grid(row=2, column=2, sticky="e")
    tk.Entry(root, show="*").grid(row=2, column=3, sticky="w")

    tk.Label(root, text="Spectator Password:").grid(row=2, column=4, sticky="e")
    tk.Entry(root, show="*").grid(row=2, column=5, sticky="w")

    # Networking
    tk.Label(root, text="Networking").grid(row=3, column=0, columnspan=4, sticky="w")
    
    tk.Label(root, text="Local IP:").grid(row=4, column=0, sticky="e")
    ttk.Combobox(root).grid(row=4, column=1, sticky="w")

    tk.Label(root, text="Server Port:").grid(row=4, column=2, sticky="e")
    tk.Entry(root).grid(row=4, column=3, sticky="w")

    tk.Label(root, text="Query Port:").grid(row=4, column=4, sticky="e")
    tk.Entry(root).grid(row=4, column=5, sticky="w")

    # RCON
    tk.Checkbutton(root, text="Enable RCON").grid(row=5, column=0, sticky="w")
    
    tk.Label(root, text="RCON Port:").grid(row=5, column=1, sticky="e")
    tk.Entry(root).grid(row=5, column=2, sticky="w")
    
    tk.Label(root, text="RCON Server Log Buffer:").grid(row=5, column=3, sticky="e")
    tk.Entry(root).grid(row=5, column=4, sticky="w")

    # Additional Settings
    tk.Label(root, text="Total Conversion ID:").grid(row=6, column=0, sticky="e")
    tk.Entry(root).grid(row=6, column=1, sticky="w")
    
    tk.Label(root, text="Mod IDs:").grid(row=7, column=0, sticky="e")
    tk.Entry(root).grid(row=7, column=1, sticky="w")

    tk.Label(root, text="Autosave Interval:").grid(row=8, column=0, sticky="e")
    tk.Entry(root).grid(row=8, column=1, sticky="w")

    tk.Label(root, text="Message of the Day:").grid(row=9, column=0, sticky="e")
    tk.Entry(root).grid(row=9, column=1, sticky="w")

    # Enable Options
    tk.Checkbutton(root, text="Enable Adminlog").grid(row=10, column=0, sticky="w")
    tk.Checkbutton(root, text="Enable Extinction Event").grid(row=11, column=0, sticky="w")

    root.mainloop()

if __name__ == "__main__":
    create_ui()
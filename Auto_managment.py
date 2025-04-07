"""
Auto_managment.py - Server Automation Control Panel

This module provides a GUI panel for configuring automatic server management tasks including:
- Auto-start on boot (UI implemented, functionality not connected)
- Scheduled shutdowns with optional updates (UI implemented, functionality not connected)
- Auto-backup and auto-update settings (UI implemented, functionality not connected)
- Server restart policies (UI implemented, functionality not connected)

Used in the ARK server management application to automate routine server maintenance tasks.

Note on INI connections:
- Auto-start: Not applicable to server INI files (OS-level functionality)
- Scheduled shutdowns: Not connected to INI files (requires external scheduler)
- Auto-backup: Not connected to INI files (requires external backup system)
- Auto-update: Not connected to INI files (requires Steam CMD integration)
- Server restart: Not connected to INI files (requires process monitoring)
"""

import tkinter as tk
from tkinter import ttk
from scrollable_frame import ScrollableFrameMixin

class AutomaticManagement(ttk.Frame, ScrollableFrameMixin):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_frames()

    def create_frames(self):
        # Create main scrollable container
        self.canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        scrollable_frame = ttk.Frame(self.canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        # Create settings section
        self.create_settings_section(scrollable_frame)
        
        # Pack the scrollable elements
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def create_settings_section(self, parent):
        # Main section frame
        section = ttk.LabelFrame(parent, text="Server Manager Settings", padding="5")
        section.pack(fill="x", padx=5, pady=5)
        
        # Auto-Start checkbox
        ttk.Checkbutton(section, text="Auto-Start server on boot").pack(anchor="w", pady=2)
        
        # First shutdown schedule
        self.create_shutdown_schedule(section, 1)
        
        # Second shutdown schedule
        self.create_shutdown_schedule(section, 2)
        
        # Additional options
        ttk.Checkbutton(section, 
            text="Include server in the Auto-Backup cycle"
        ).pack(anchor="w", pady=2)
        
        ttk.Checkbutton(section, 
            text="Include server in the Auto-Update cycle"
        ).pack(anchor="w", pady=2)
        
        ttk.Checkbutton(section, 
            text="Restart server if shutdown"
        ).pack(anchor="w", pady=2)

    def create_shutdown_schedule(self, parent, schedule_num):
        schedule_frame = ttk.Frame(parent)
        schedule_frame.pack(fill="x", pady=2)
        
        # Shutdown time
        time_frame = ttk.Frame(schedule_frame)
        time_frame.pack(fill="x")
        
        ttk.Checkbutton(time_frame, text="Shutdown server at").pack(side="left")
        time_entry = ttk.Entry(time_frame, width=8)
        time_entry.insert(0, "00:00")
        time_entry.pack(side="left", padx=5)
        
        # Days frame
        days_frame = ttk.Frame(time_frame)
        days_frame.pack(side="left", padx=5)
        
        days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
        for day in days:
            day_frame = ttk.Frame(days_frame)
            day_frame.pack(side="left", padx=2)
            ttk.Label(day_frame, text=day).pack()
            ttk.Checkbutton(day_frame).pack()
        
        # Update and restart options
        ttk.Checkbutton(time_frame, text="perform update").pack(side="left", padx=5)
        ttk.Checkbutton(time_frame, text="then restart").pack(side="left")

def main():
    root = tk.Tk()
    app = AutomaticManagement(root)
    app.pack(fill="both", expand=True)
    root.mainloop()

if __name__ == "__main__":
    main()

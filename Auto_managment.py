import tkinter as tk
from tkinter import ttk

class AutomaticManagement(ttk.Frame):
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
    main()import tkinter as tk
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
        
        # Add scroll functionality from the mixin
        self.add_scroll_functionality(self.canvas)
        
        # Create all sections
        self.create_auto_backup_section(scrollable_frame)
        self.create_auto_update_section(scrollable_frame)
        self.create_auto_start_section(scrollable_frame)
        self.create_auto_shutdown_section(scrollable_frame)
        
        # Pack the scrollable elements
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def create_auto_backup_section(self, parent):
        section = ttk.LabelFrame(parent, text="Automatic Backup", padding="5")
        section.pack(fill="x", padx=5, pady=5)
        
        # Enable Auto-Backup
        backup_frame = ttk.Frame(section)
        backup_frame.pack(fill="x", pady=2)
        ttk.Checkbutton(backup_frame, text="Enable Auto-Backup").pack(side="left")
        ttk.Label(backup_frame, text="Interval:").pack(side="left", padx=5)
        ttk.Entry(backup_frame, width=5).pack(side="left")
        ttk.Label(backup_frame, text="hours").pack(side="left", padx=5)
        
        # Backup retention
        retention_frame = ttk.Frame(section)
        retention_frame.pack(fill="x", pady=2)
        ttk.Label(retention_frame, text="Keep last").pack(side="left")
        ttk.Entry(retention_frame, width=5).pack(side="left", padx=5)
        ttk.Label(retention_frame, text="backups").pack(side="left")
    
    def create_auto_update_section(self, parent):
        section = ttk.LabelFrame(parent, text="Automatic Update", padding="5")
        section.pack(fill="x", padx=5, pady=5)
        
        # Enable Auto-Update
        update_frame = ttk.Frame(section)
        update_frame.pack(fill="x", pady=2)
        ttk.Checkbutton(update_frame, text="Enable Auto-Update").pack(side="left")
        ttk.Label(update_frame, text="Check every:").pack(side="left", padx=5)
        ttk.Entry(update_frame, width=5).pack(side="left")
        ttk.Label(update_frame, text="minutes").pack(side="left", padx=5)
        
        # Update options
        options_frame = ttk.Frame(section)
        options_frame.pack(fill="x", pady=2)
        ttk.Checkbutton(options_frame, text="Update mods automatically").pack(side="left")
        ttk.Checkbutton(options_frame, text="Notify on Discord").pack(side="left", padx=20)
    
    def create_auto_start_section(self, parent):
        section = ttk.LabelFrame(parent, text="Automatic Start", padding="5")
        section.pack(fill="x", padx=5, pady=5)
        
        # Enable Auto-Start
        start_frame = ttk.Frame(section)
        start_frame.pack(fill="x", pady=2)
        ttk.Checkbutton(start_frame, text="Enable Auto-Start").pack(side="left")
        ttk.Label(start_frame, text="Start server at:").pack(side="left", padx=5)
        ttk.Entry(start_frame, width=8).pack(side="left")
        ttk.Label(start_frame, text="(HH:MM)").pack(side="left", padx=5)
        
        # Start options
        options_frame = ttk.Frame(section)
        options_frame.pack(fill="x", pady=2)
        ttk.Checkbutton(options_frame, text="Start with Windows").pack(side="left")
        ttk.Checkbutton(options_frame, text="Start minimized").pack(side="left", padx=20)
    
    def create_auto_shutdown_section(self, parent):
        section = ttk.LabelFrame(parent, text="Automatic Shutdown", padding="5")
        section.pack(fill="x", padx=5, pady=5)
        
        # Enable Auto-Shutdown
        shutdown_frame = ttk.Frame(section)
        shutdown_frame.pack(fill="x", pady=2)
        ttk.Checkbutton(shutdown_frame, text="Enable Auto-Shutdown").pack(side="left")
        ttk.Label(shutdown_frame, text="Shutdown at:").pack(side="left", padx=5)
        ttk.Entry(shutdown_frame, width=8).pack(side="left")
        ttk.Label(shutdown_frame, text="(HH:MM)").pack(side="left", padx=5)
        
        # Shutdown options
        options_frame = ttk.Frame(section)
        options_frame.pack(fill="x", pady=2)
        ttk.Checkbutton(options_frame, text="Warn players").pack(side="left")
        ttk.Label(options_frame, text="Warning time:").pack(side="left", padx=5)
        ttk.Entry(options_frame, width=5).pack(side="left")
        ttk.Label(options_frame, text="minutes").pack(side="left", padx=5)

def main():
    root = tk.Tk()
    app = AutomaticManagement(root)
    app.pack(fill="both", expand=True)
    root.mainloop()

if __name__ == "__main__":
    main()

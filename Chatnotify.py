import tkinter as tk
from tkinter import ttk
from scrollable_frame import ScrollableFrameMixin

class ChatNotificationsPanel(ttk.Frame, ScrollableFrameMixin):
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
        
        # Create the chat notifications section
        self.create_chat_notifications_section(scrollable_frame)
        
        # Pack the scrollable elements
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def create_chat_notifications_section(self, parent):
        section = ttk.LabelFrame(parent, text="Chat and Notifications", padding="5")
        section.pack(fill="x", padx=5, pady=5)
        
        # Create two-column layout
        columns_frame = ttk.Frame(section)
        columns_frame.pack(fill="x", pady=2)
        
        # Left column for chat options
        left_frame = ttk.Frame(columns_frame)
        left_frame.pack(side="left", fill="x", expand=True)
        
        left_options = [
            "Enable Global Voice Chat",
            "Enable Proximity Text Chat"
        ]
        
        for option in left_options:
            ttk.Checkbutton(left_frame, text=option).pack(anchor="w", pady=1)
        
        # Right column for notification options
        right_frame = ttk.Frame(columns_frame)
        right_frame.pack(side="left", fill="x", expand=True)
        
        right_options = [
            "Enable 'Player Left' Notifications",
            "Enable 'Player Joined' Notifications"
        ]
        
        for option in right_options:
            ttk.Checkbutton(right_frame, text=option).pack(anchor="w", pady=1)

def main():
    root = tk.Tk()
    root.title("ARK Server Configuration - Chat and Notifications")
    app = ChatNotificationsPanel(root)
    app.pack(fill="both", expand=True)
    root.mainloop()

if __name__ == "__main__":
    main()
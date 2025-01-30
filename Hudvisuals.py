import tkinter as tk
from tkinter import ttk
from scrollable_frame import ScrollableFrameMixin

class HUDVisualsPanel(ttk.Frame, ScrollableFrameMixin):
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
       
       # Create the HUD and visuals section
       self.create_hud_visuals_section(scrollable_frame)
       
       # Pack the scrollable elements
       self.canvas.pack(side="left", fill="both", expand=True)
       scrollbar.pack(side="right", fill="y")
   
   def create_hud_visuals_section(self, parent):
       section = ttk.LabelFrame(parent, text="HUD and Visuals", padding="5")
       section.pack(fill="x", padx=5, pady=5)
       
       # Create three-column layout
       columns_frame = ttk.Frame(section)
       columns_frame.pack(fill="x", pady=2)
       
       # Left column for basic HUD options
       left_frame = ttk.Frame(columns_frame)
       left_frame.pack(side="left", fill="x", expand=True)
       
       left_options = [
           "Allow Crosshair",
           "Allow HUD",
           "Allow Map Player Location"
       ]
       
       for option in left_options:
           ttk.Checkbutton(left_frame, text=option).pack(anchor="w", pady=1)
       
       # Middle column for view options
       middle_frame = ttk.Frame(columns_frame)
       middle_frame.pack(side="left", fill="x", expand=True)
       
       middle_options = [
           "Allow Third-Person View",
           "Show Floating Damage Text",
           "Allow Hit Markers"
       ]
       
       for option in middle_options:
           ttk.Checkbutton(middle_frame, text=option).pack(anchor="w", pady=1)
       
       # Right column for gamma settings
       right_frame = ttk.Frame(columns_frame)
       right_frame.pack(side="left", fill="x", expand=True)
       
       right_options = [
           "Allow Player Gamma Settings in PvP",
           "Allow Player Gamma Settings in PvE"
       ]
       
       for option in right_options:
           ttk.Checkbutton(right_frame, text=option).pack(anchor="w", pady=1)

def main():
   root = tk.Tk()
   root.title("ARK Server Configuration - HUD and Visuals")
   app = HUDVisualsPanel(root)
   app.pack(fill="both", expand=True)
   root.mainloop()

if __name__ == "__main__":
   main()
import tkinter as tk
from tkinter import ttk
from scrollable_frame import ScrollableFrameMixin

class PlayerSettingsPanel(ttk.Frame, ScrollableFrameMixin):
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
       self.create_player_settings_section(scrollable_frame)
       self.create_base_stats_section(scrollable_frame)
       self.create_per_level_stats_section(scrollable_frame)
       
       # Pack the scrollable elements
       self.canvas.pack(side="left", fill="both", expand=True)
       scrollbar.pack(side="right", fill="y")
   
   def create_slider_with_entry(self, parent, text, default_value=1.0, unit="x"):
       frame = ttk.Frame(parent)
       frame.pack(fill="x", pady=2)
       
       ttk.Label(frame, text=text).pack(side="left", padx=(5,0))
       
       slider = ttk.Scale(frame, from_=0, to=10, orient="horizontal")
       slider.set(default_value)
       slider.pack(side="left", fill="x", expand=True, padx=5)
       
       entry_var = tk.StringVar(value=str(default_value))
       entry = ttk.Entry(frame, textvariable=entry_var, width=8)
       entry.pack(side="left", padx=(0,5))
       
       if unit:
           ttk.Label(frame, text=unit).pack(side="left", padx=(0,5))
       
       return slider, entry_var
   
   def create_player_settings_section(self, parent):
       section = ttk.LabelFrame(parent, text="Player Settings", padding="5")
       section.pack(fill="x", padx=5, pady=5)
       
       # Flyer carry checkbox
       ttk.Checkbutton(section, text="Enable Flyer-Carry").pack(anchor="w", pady=2)
       
       # Player multipliers
       multipliers = [
           "XP Multiplier", "Damage", "Resistance", "Water Drain", 
           "Food Drain", "Stamina Drain", "Health Recovery",
           "Harvesting Damage", "Crafting Skill Bonus Multiplier",
           "Max Fall Speed Multiplier"
       ]
       
       for multiplier in multipliers:
           self.create_slider_with_entry(section, multiplier)
   
   def create_base_stats_section(self, parent):
       section = ttk.LabelFrame(parent, text="Base Stat Multipliers", padding="5")
       section.pack(fill="x", padx=5, pady=5)
       
       # Main checkbox
       ttk.Checkbutton(section, text="Base Stat Multipliers").pack(anchor="w", pady=2)
       
       # Create two-column layout
       columns_frame = ttk.Frame(section)
       columns_frame.pack(fill="x", pady=2)
       
       # Left column
       left_frame = ttk.Frame(columns_frame)
       left_frame.pack(side="left", fill="x", expand=True)
       
       left_stats = ["Health", "Stamina", "Torpidity", "Oxygen", "Food", "Water"]
       
       for stat in left_stats:
           self.create_slider_with_entry(left_frame, stat)
       
       # Right column
       right_frame = ttk.Frame(columns_frame)
       right_frame.pack(side="left", fill="x", expand=True)
       
       right_stats = ["Temperature", "Weight", "Damage", "Speed", "Fortitude", "Crafting"]
       
       for stat in right_stats:
           self.create_slider_with_entry(right_frame, stat)
   
   def create_per_level_stats_section(self, parent):
       section = ttk.LabelFrame(parent, text="Per-Level Stat Multipliers", padding="5")
       section.pack(fill="x", padx=5, pady=5)
       
       # Main checkbox
       ttk.Checkbutton(section, text="Per-Level Stat Multipliers").pack(anchor="w", pady=2)
       
       # Create two-column layout
       columns_frame = ttk.Frame(section)
       columns_frame.pack(fill="x", pady=2)
       
       # Left column
       left_frame = ttk.Frame(columns_frame)
       left_frame.pack(side="left", fill="x", expand=True)
       
       left_stats = ["Health", "Stamina", "Oxygen", "Food", "Water"]
       
       for stat in left_stats:
           self.create_slider_with_entry(left_frame, stat)
       
       # Right column
       right_frame = ttk.Frame(columns_frame)
       right_frame.pack(side="left", fill="x", expand=True)
       
       right_stats = ["Temperature", "Weight", "Damage", "Speed", "Fortitude", "Crafting"]
       
       for stat in right_stats:
           self.create_slider_with_entry(right_frame, stat)

def main():
   root = tk.Tk()
   root.title("ARK Server Configuration - Player Settings")
   app = PlayerSettingsPanel(root)
   app.pack(fill="both", expand=True)
   root.mainloop()

if __name__ == "__main__":
   main()
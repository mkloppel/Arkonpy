import tkinter as tk
from tkinter import ttk
from scrollable_frame import ScrollableFrameMixin

class EnvironmentPanel(ttk.Frame, ScrollableFrameMixin):
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
       self.create_resource_settings_section(scrollable_frame)
       self.create_harvest_options_section(scrollable_frame)
       self.create_custom_harvest_section(scrollable_frame)
       self.create_time_weather_section(scrollable_frame)
       self.create_decomposition_section(scrollable_frame)
       self.create_growth_intervals_section(scrollable_frame)
       self.create_xp_multipliers_section(scrollable_frame)
       
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

   def create_resource_settings_section(self, parent):
       section = ttk.LabelFrame(parent, text="Resource Settings", padding="5")
       section.pack(fill="x", padx=5, pady=5)
       
       settings = [
           ("Dino Spawns", 1),
           ("Taming Speed", 1),
           ("Harvest Amount", 1),
           ("Resource Respawn", 1),
           ("Suppress Replenish Radius (Player)", 1),
           ("Suppress Replenish Radius (Structure)", 1)
       ]
       
       for setting, default in settings:
           self.create_slider_with_entry(section, setting, default)

   def create_harvest_options_section(self, parent):
       section = ttk.LabelFrame(parent, text="Harvest Options", padding="5")
       section.pack(fill="x", padx=5, pady=5)
       
       ttk.Checkbutton(section, text="Clamp Resource Harvest Damage").pack(anchor="w", pady=2)
       ttk.Checkbutton(section, text="Use Optimized Harvesting Health").pack(anchor="w", pady=2)
       self.create_slider_with_entry(section, "Harvest Health", 1)

   def create_custom_harvest_section(self, parent):
       section = ttk.LabelFrame(parent, text="Custom Harvest Configuration", padding="5")
       section.pack(fill="x", padx=5, pady=5)
       
       # Top controls frame
       controls_frame = ttk.Frame(section)
       controls_frame.pack(fill="x", pady=2)
       
       ttk.Checkbutton(controls_frame, text="Custom Harvest Amount Multipliers").pack(side="left", padx=5)
       ttk.Label(controls_frame, text="Filter:").pack(side="left", padx=5)
       ttk.Combobox(controls_frame, values=["All"]).pack(side="left", padx=5)
       
       # Create resource table
       columns = ('name', 'source', 'amount_type', 'amount')
       tree = ttk.Treeview(section, columns=columns, show='headings', height=10)
       
       tree.heading('name', text='Name')
       tree.heading('source', text='Source')
       tree.heading('amount_type', text='Amount Type')
       tree.heading('amount', text='Amount')
       
       tree.pack(fill="both", expand=True, pady=5)

   def create_time_weather_section(self, parent):
       section = ttk.LabelFrame(parent, text="Time and Weather Settings", padding="5")
       section.pack(fill="x", padx=5, pady=5)
       
       settings = [
           ("Base Temperature", 1),
           ("Day Cycle Speed", 1),
           ("Day Time Speed", 1),
           ("Night Time Speed", 1)
       ]
       
       for setting, default in settings:
           self.create_slider_with_entry(section, setting, default)
           
       ttk.Checkbutton(section, text="Disable Weather - Fog").pack(anchor="w", pady=2)

   def create_decomposition_section(self, parent):
       section = ttk.LabelFrame(parent, text="Decomposition Settings", padding="5")
       section.pack(fill="x", padx=5, pady=5)
       
       self.create_slider_with_entry(section, "Global Spoiling Time", 1)
       ttk.Checkbutton(section, text="Clamp Item Spoiling Times").pack(anchor="w", pady=2)
       
       settings = [
           ("Global Item Decomp Time", 1),
           ("Global Corpse Decomp Time", 1)
       ]
       
       for setting, default in settings:
           self.create_slider_with_entry(section, setting, default)

   def create_growth_intervals_section(self, parent):
       section = ttk.LabelFrame(parent, text="Growth and Intervals", padding="5")
       section.pack(fill="x", padx=5, pady=5)
       
       settings = [
           ("Crop Decay Speed", 1),
           ("Crop Growth Speed", 1),
           ("Lay Egg Interval", 1),
           ("Poop Interval", 1),
           ("Hair Growth Speed", 1)
       ]
       
       for setting, default in settings:
           self.create_slider_with_entry(section, setting, default)

   def create_xp_multipliers_section(self, parent):
       section = ttk.LabelFrame(parent, text="Earned XP Multipliers", padding="5")
       section.pack(fill="x", padx=5, pady=5)
       
       settings = [
           ("Generic (over time)", 1),
           ("Crafting", 1),
           ("Harvesting", 1),
           ("Killing", 1),
           ("Special Events", 1)
       ]
       
       for setting, default in settings:
           self.create_slider_with_entry(section, setting, default)

def main():
   root = tk.Tk()
   root.title("ARK Server Configuration - Environment")
   app = EnvironmentPanel(root)
   app.pack(fill="both", expand=True)
   root.mainloop()

if __name__ == "__main__":
   main()
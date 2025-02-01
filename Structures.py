import tkinter as tk
from tkinter import ttk
from scrollable_frame import ScrollableFrameMixin

class StructuresPanel(ttk.Frame, ScrollableFrameMixin):
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
       self.create_basic_settings_section(scrollable_frame)
       self.create_pvp_settings_section(scrollable_frame)
       self.create_structure_limits_section(scrollable_frame)
       self.create_platform_options_section(scrollable_frame)
       self.create_decay_settings_section(scrollable_frame)
       self.create_auto_destroy_section(scrollable_frame)
       self.create_defense_settings_section(scrollable_frame)
       self.create_pickup_settings_section(scrollable_frame)
       self.create_genesis_section(scrollable_frame)
       
       # Pack the scrollable elements
       self.canvas.pack(side="left", fill="both", expand=True)
       scrollbar.pack(side="right", fill="y")

   def create_slider_with_entry(self, parent, text, default_value=1.0, unit="x", max_value=10):
       frame = ttk.Frame(parent)
       frame.pack(fill="x", pady=2)
       
       ttk.Label(frame, text=text).pack(side="left", padx=(5,0))
       
       slider = ttk.Scale(frame, from_=0, to=max_value, orient="horizontal")
       slider.set(default_value)
       slider.pack(side="left", fill="x", expand=True, padx=5)
       
       entry_var = tk.StringVar(value=str(default_value))
       entry = ttk.Entry(frame, textvariable=entry_var, width=8)
       entry.pack(side="left", padx=(0,5))
       
       if unit:
           ttk.Label(frame, text=unit).pack(side="left", padx=(0,5))
       
       return slider, entry_var

   def create_basic_settings_section(self, parent):
       section = ttk.LabelFrame(parent, text="Basic Structure Settings", padding="5")
       section.pack(fill="x", padx=5, pady=5)
       
       ttk.Checkbutton(section, text="Disable Structure Placement Collision").pack(anchor="w", pady=2)
       
       settings = [
           ("Structure Resistance", 1),
           ("Structure Damage", 1),
           ("Structure Damage Repair Cooldown", 180, "seconds", 300)
       ]
       
       for setting in settings:
           self.create_slider_with_entry(section, *setting)

   def create_pvp_settings_section(self, parent):
       section = ttk.LabelFrame(parent, text="PvP Structure Settings", padding="5")
       section.pack(fill="x", padx=5, pady=5)
       
       ttk.Checkbutton(section, text="Enable PvP Structure Decay").pack(anchor="w", pady=2)
       self.create_slider_with_entry(section, "PvP Zone Structure Damage", 6)

   def create_structure_limits_section(self, parent):
       section = ttk.LabelFrame(parent, text="Structure Limits", padding="5")
       section.pack(fill="x", padx=5, pady=5)
       
       settings = [
           ("Max Structures Visible", 10500, "items", 20000),
           ("Per-Platform Structures Multiplier", 1),
           ("Max Platform Saddle Structures", 0, "items", 1000)
       ]
       
       for setting in settings:
           self.create_slider_with_entry(section, *setting)

   def create_platform_options_section(self, parent):
       section = ttk.LabelFrame(parent, text="Platform Options", padding="5")
       section.pack(fill="x", padx=5, pady=5)
       
       options = [
           "Override Structure Platform Prevention",
           "Allow Unaligned Dinos on Flyer Platform",
           "Allow Structures at Supply Drops PvE"
       ]
       
       for option in options:
           ttk.Checkbutton(section, text=option).pack(anchor="w", pady=2)

   def create_decay_settings_section(self, parent):
       section = ttk.LabelFrame(parent, text="Decay Settings", padding="5")
       section.pack(fill="x", padx=5, pady=5)
       
       ttk.Checkbutton(section, text="Enable Structure Decay PvE").pack(anchor="w", pady=2)
       
       settings = [
           ("Structure Decay Period", 0, "seconds", 100000),
           ("Structure Decay Multiplier", 1)
       ]
       
       for setting in settings:
           self.create_slider_with_entry(section, *setting)

   def create_auto_destroy_section(self, parent):
       section = ttk.LabelFrame(parent, text="Auto Destroy Settings", padding="5")
       section.pack(fill="x", padx=5, pady=5)
       
       checkboxes = [
           "Auto Destroy Structures",
           "Only Auto Destroy Core Structures",
           "Only Decay Unsnapped Core Structures",
           "Fast Decay Unsnapped Core Structures",
           "Destroy Unconnected Water Pipes",
           "Enable Fast Decay"
       ]
       
       for option in checkboxes:
           ttk.Checkbutton(section, text=option).pack(anchor="w", pady=2)
           
       settings = [
           ("Auto Destroy Old Structures Multiplier", 0),
           ("Fast Decay Interval", 43200, "seconds", 100000)
       ]
       
       for setting in settings:
           self.create_slider_with_entry(section, *setting)

   def create_defense_settings_section(self, parent):
       section = ttk.LabelFrame(parent, text="Defense Settings", padding="5")
       section.pack(fill="x", padx=5, pady=5)
       
       checkboxes = [
           "Force All Structure Locking",
           "Passive Defenses Damage Riderless Dinos",
           "Hard Limit Turrets In Range",
           "Limit Turrets In Range"
       ]
       
       for option in checkboxes:
           ttk.Checkbutton(section, text=option).pack(anchor="w", pady=2)
           
       settings = [
           ("Limit Range", 10000, "units", 20000),
           ("Limit Number", 100, "", 1000)
       ]
       
       for setting in settings:
           self.create_slider_with_entry(section, *setting)

   def create_pickup_settings_section(self, parent):
       section = ttk.LabelFrame(parent, text="Structure Pickup", padding="5")
       section.pack(fill="x", padx=5, pady=5)
       
       ttk.Checkbutton(section, text="Always Allow Structure Pickup").pack(anchor="w", pady=2)
       
       settings = [
           ("Structure Pickup Time after Placement", 30, "seconds", 100),
           ("Structure Pickup Hold Duration", 0.5, "seconds", 10)
       ]
       
       for setting in settings:
           self.create_slider_with_entry(section, *setting)
           
       ttk.Checkbutton(section, text="Allow Integrated Structures Plus").pack(anchor="w", pady=2)

   def create_genesis_section(self, parent):
       section = ttk.LabelFrame(parent, text="Genesis: Part 1", padding="5")
       section.pack(fill="x", padx=5, pady=5)
       
       ttk.Checkbutton(section, text="Disable Building in Mission Areas").pack(anchor="w", pady=2)

def main():
   root = tk.Tk()
   root.title("ARK Server Configuration - Structures")
   app = StructuresPanel(root)
   app.pack(fill="both", expand=True)
   root.mainloop()

if __name__ == "__main__":
   main()
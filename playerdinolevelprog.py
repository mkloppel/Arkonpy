import tkinter as tk
from tkinter import ttk
from scrollable_frame import ScrollableFrameMixin

class LevelProgressionsPanel(ttk.Frame, ScrollableFrameMixin):
   def __init__(self, parent):
       super().__init__(parent)
       self.create_frames()
       
   def create_frames(self):
       # Create main container frame
       main_frame = ttk.Frame(self)
       main_frame.pack(fill="both", expand=True, padx=5, pady=5)
       
       # Create top controls
       self.create_top_controls(main_frame)
       
       # Create warning note
       self.create_warning_note(main_frame)
       
       # Create enable options
       self.create_enable_options(main_frame)
       
       # Create progression panels
       panels_frame = ttk.Frame(main_frame)
       panels_frame.pack(fill="both", expand=True, pady=5)
       
       # Configure column weights for 50/50 split
       panels_frame.grid_columnconfigure(0, weight=1)
       panels_frame.grid_columnconfigure(1, weight=1)
       
       # Create the two main panels
       self.create_player_levels_panel(panels_frame)
       self.create_dino_levels_panel(panels_frame)

   def create_top_controls(self, parent):
       frame = ttk.Frame(parent)
       frame.pack(fill="x", pady=5)
       
       # Player Max XP
       player_frame = ttk.Frame(frame)
       player_frame.pack(fill="x", pady=2)
       
       ttk.Label(player_frame, text="Player Max XP:").pack(side="left", padx=5)
       ttk.Checkbutton(player_frame).pack(side="left")
       ttk.Scale(player_frame, from_=0, to=100, orient="horizontal").pack(side="left", fill="x", expand=True, padx=5)
       entry = ttk.Entry(player_frame, width=8)
       entry.insert(0, "5")
       entry.pack(side="left")
       ttk.Label(player_frame, text="xp").pack(side="left", padx=5)
       ttk.Button(player_frame, text="↻", width=3).pack(side="left", padx=5)
       
       # Dino Max XP
       dino_frame = ttk.Frame(frame)
       dino_frame.pack(fill="x", pady=2)
       
       ttk.Label(dino_frame, text="Dino Max XP:").pack(side="left", padx=5)
       ttk.Checkbutton(dino_frame).pack(side="left")
       ttk.Scale(dino_frame, from_=0, to=100, orient="horizontal").pack(side="left", fill="x", expand=True, padx=5)
       entry = ttk.Entry(dino_frame, width=8)
       entry.insert(0, "10")
       entry.pack(side="left")
       ttk.Label(dino_frame, text="xp").pack(side="left", padx=5)
       ttk.Button(dino_frame, text="↻", width=3).pack(side="left", padx=5)

   def create_warning_note(self, parent):
       frame = ttk.Frame(parent)
       frame.pack(fill="x", pady=5)
       
       warning_text = "NOTE: The last 75 player levels are used for Ascension and Other leveling and are shown with a coloured background. If you customize your own player levels, make sure you add an additional 75 levels."
       ttk.Label(frame, text=warning_text, wraplength=800, justify="left").pack(anchor="w")

   def create_enable_options(self, parent):
       frame = ttk.Frame(parent)
       frame.pack(fill="x", pady=5)
       
       ttk.Checkbutton(frame, text="Enable Custom Level Progressions").pack(side="left", padx=5)
       ttk.Checkbutton(frame, text="Enable Dino Level Progressions").pack(side="right", padx=5)

   def create_level_grid(self, parent, includes_engram=False):
       columns = ['level', 'xp_required']
       if includes_engram:
           columns.extend(['engram_points', 'engram_total'])
           
       tree = ttk.Treeview(parent, columns=columns, show='headings', height=15)
       
       # Configure columns
       tree.heading('level', text='Level')
       tree.heading('xp_required', text='XP Required')
       if includes_engram:
           tree.heading('engram_points', text='Engram Points')
           tree.heading('engram_total', text='Engram Total')
       
       tree.column('level', width=50)
       tree.column('xp_required', width=100)
       if includes_engram:
           tree.column('engram_points', width=100)
           tree.column('engram_total', width=100)
       
       # Add sample data
       sample_data = []
       for i in range(1, 13):
           if includes_engram:
               sample_data.append((i, i*100, 8, i*8))
           else:
               sample_data.append((i, i*50))
               
       for item in sample_data:
           tree.insert('', 'end', values=item)
       
       return tree

   def create_player_levels_panel(self, parent):
       frame = ttk.LabelFrame(parent, text="Custom Player Levels", padding="5")
       frame.grid(row=0, column=0, sticky="nsew", padx=2)
       
       # Create button toolbar
       toolbar = ttk.Frame(frame)
       toolbar.pack(fill="x", pady=2)
       
       ttk.Button(toolbar, text="×", width=3).pack(side="left", padx=2)
       ttk.Button(toolbar, text="↻", width=3).pack(side="left", padx=2)
       ttk.Button(toolbar, text="📝", width=3).pack(side="left", padx=2)
       ttk.Button(toolbar, text="↓", width=3).pack(side="left", padx=2)
       ttk.Button(toolbar, text="↑", width=3).pack(side="left", padx=2)
       
       # Create tree view
       tree = self.create_level_grid(frame, includes_engram=True)
       scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
       tree.configure(yscrollcommand=scrollbar.set)
       
       tree.pack(side="left", fill="both", expand=True)
       scrollbar.pack(side="right", fill="y")

   def create_dino_levels_panel(self, parent):
       frame = ttk.LabelFrame(parent, text="Custom Dino Levels", padding="5")
       frame.grid(row=0, column=1, sticky="nsew", padx=2)
       
       # Create button toolbar
       toolbar = ttk.Frame(frame)
       toolbar.pack(fill="x", pady=2)
       
       ttk.Button(toolbar, text="×", width=3).pack(side="left", padx=2)
       ttk.Button(toolbar, text="↻", width=3).pack(side="left", padx=2)
       ttk.Button(toolbar, text="📝", width=3).pack(side="left", padx=2)
       ttk.Button(toolbar, text="↓", width=3).pack(side="left", padx=2)
       ttk.Button(toolbar, text="↑", width=3).pack(side="left", padx=2)
       
       # Create tree view
       tree = self.create_level_grid(frame, includes_engram=False)
       scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
       tree.configure(yscrollcommand=scrollbar.set)
       
       tree.pack(side="left", fill="both", expand=True)
       scrollbar.pack(side="right", fill="y")

def main():
   root = tk.Tk()
   root.title("ARK Server Configuration - Player and Dino Level Progressions")
   root.geometry("1200x800")  # Larger default size for this panel
   app = LevelProgressionsPanel(root)
   app.pack(fill="both", expand=True)
   root.mainloop()

if __name__ == "__main__":
   main()
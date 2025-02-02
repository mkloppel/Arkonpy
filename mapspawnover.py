import tkinter as tk
from tkinter import ttk
from scrollable_frame import ScrollableFrameMixin

class MapSpawnerOverridesPanel(ttk.Frame, ScrollableFrameMixin):
   def __init__(self, parent):
       super().__init__(parent)
       self.create_frames()
       
   def create_frames(self):
       # Create main container frame
       main_frame = ttk.Frame(self)
       main_frame.pack(fill="both", expand=True, padx=5, pady=5)
       
       # Create warning note
       self.create_warning_note(main_frame)
       
       # Create panels container
       panels_frame = ttk.Frame(main_frame)
       panels_frame.pack(fill="both", expand=True, pady=5)
       
       # Configure column weights for 40/60 split
       panels_frame.grid_columnconfigure(0, weight=2)  # Containers panel
       panels_frame.grid_columnconfigure(1, weight=3)  # Entries panel
       
       # Create the two main panels
       self.create_containers_panel(panels_frame)
       self.create_entries_panel(panels_frame)

   def create_warning_note(self, parent):
       note_frame = ttk.Frame(parent)
       note_frame.pack(fill="x", pady=5)
       
       note = ttk.Label(
           note_frame,
           text="NOTE: If you want to manage your overrides manually or with another application, "
                "you can disable the option that will prevent the server manager managing the "
                "overrides. See the 'Custom Override Options' in the global settings.",
           foreground='dark green',
           wraplength=800,
           justify="left"
       )
       note.pack(anchor="w")

   def create_containers_panel(self, parent):
       frame = ttk.LabelFrame(parent, text="Containers", padding="5")
       frame.grid(row=0, column=0, sticky="nsew", padx=(0,2))
       
       # Create button toolbar
       toolbar = ttk.Frame(frame)
       toolbar.pack(fill="x", pady=2)
       
       ttk.Button(toolbar, text="+", width=3).pack(side="left", padx=2)
       ttk.Button(toolbar, text="□", width=3).pack(side="left", padx=2)
       ttk.Button(toolbar, text="×", width=3).pack(side="left", padx=2)
       ttk.Button(toolbar, text="⎘", width=3).pack(side="left", padx=2)
       
       # Create treeview
       list_frame = ttk.Frame(frame)
       list_frame.pack(fill="both", expand=True)
       
       columns = ('type', 'spawner')
       tree = ttk.Treeview(list_frame, columns=columns, show='headings', height=15)
       
       tree.heading('type', text='Type')
       tree.heading('spawner', text='Spawner')
       
       tree.column('type', width=150)
       tree.column('spawner', width=150)
       
       # Add scrollbar
       scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=tree.yview)
       tree.configure(yscrollcommand=scrollbar.set)
       
       tree.pack(side="left", fill="both", expand=True)
       scrollbar.pack(side="right", fill="y")

   def create_entries_panel(self, parent):
       frame = ttk.LabelFrame(parent, text="Entries", padding="5")
       frame.grid(row=0, column=1, sticky="nsew", padx=(2,0))
       
       # Create button toolbar
       toolbar = ttk.Frame(frame)
       toolbar.pack(fill="x", pady=2)
       
       ttk.Button(toolbar, text="+", width=3).pack(side="left", padx=2)
       ttk.Button(toolbar, text="×", width=3).pack(side="left", padx=2)
       
       # Create treeview
       list_frame = ttk.Frame(frame)
       list_frame.pack(fill="both", expand=True)
       
       columns = ('name', 'dino', 'weight', 'max_percentage')
       tree = ttk.Treeview(list_frame, columns=columns, show='headings', height=15)
       
       tree.heading('name', text='Name')
       tree.heading('dino', text='Dino')
       tree.heading('weight', text='Weight')
       tree.heading('max_percentage', text='Max Percentage')
       
       tree.column('name', width=150)
       tree.column('dino', width=150)
       tree.column('weight', width=100)
       tree.column('max_percentage', width=100)
       
       # Add scrollbar
       scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=tree.yview)
       tree.configure(yscrollcommand=scrollbar.set)
       
       tree.pack(side="left", fill="both", expand=True)
       scrollbar.pack(side="right", fill="y")

def main():
   root = tk.Tk()
   root.title("ARK Server Configuration - Map Spawner Overrides")
   root.geometry("1000x600")
   app = MapSpawnerOverridesPanel(root)
   app.pack(fill="both", expand=True)
   root.mainloop()

if __name__ == "__main__":
   main()
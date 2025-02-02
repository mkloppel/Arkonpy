import tkinter as tk
from tkinter import ttk
from scrollable_frame import ScrollableFrameMixin

class CraftingOverridesPanel(ttk.Frame, ScrollableFrameMixin):
   def __init__(self, parent):
       super().__init__(parent)
       self.create_frames()
       
   def create_frames(self):
       # Create main container frame
       main_frame = ttk.Frame(self)
       main_frame.pack(fill="both", expand=True, padx=5, pady=5)
       
       # Create warning notes
       self.create_warning_notes(main_frame)
       
       # Create panels container
       panels_frame = ttk.Frame(main_frame)
       panels_frame.pack(fill="both", expand=True, pady=5)
       
       # Configure column weights for panels
       panels_frame.grid_columnconfigure(0, weight=1)
       panels_frame.grid_columnconfigure(1, weight=2)  # Resource panel slightly wider
       
       # Create the two main panels
       self.create_crafted_items_panel(panels_frame)
       self.create_resource_items_panel(panels_frame)

   def create_warning_notes(self, parent):
       notes_frame = ttk.Frame(parent)
       notes_frame.pack(fill="x", pady=5)
       
       # First note in green
       note1 = ttk.Label(
           notes_frame,
           text="NOTE: If you want to manage your overrides manually or with another application, "
                "you can disable the option that will prevent the server manager managing the "
                "overrides. See the 'Custom Override Options' in the global settings.",
           foreground='dark green',
           wraplength=800,
           justify="left"
       )
       note1.pack(anchor="w", pady=(0,5))
       
       # Second note
       note2 = ttk.Label(
           notes_frame,
           text="NOTE: Changing the resources of a crafted item will require the Engram to be "
                "re-learnt. If the Engram is already known, a mindwipe tonic must be used so "
                "that it can be re-learnt.",
           wraplength=800,
           justify="left"
       )
       note2.pack(anchor="w")

   def create_crafted_items_panel(self, parent):
       frame = ttk.LabelFrame(parent, text="Crafted Items", padding="5")
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
       
       columns = ('crafted_item',)
       tree = ttk.Treeview(list_frame, columns=columns, show='headings', height=15)
       
       tree.heading('crafted_item', text='Crafted Item')
       tree.column('crafted_item', width=200)
       
       # Add scrollbar
       scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=tree.yview)
       tree.configure(yscrollcommand=scrollbar.set)
       
       tree.pack(side="left", fill="both", expand=True)
       scrollbar.pack(side="right", fill="y")

   def create_resource_items_panel(self, parent):
       frame = ttk.LabelFrame(parent, text="Resource Items", padding="5")
       frame.grid(row=0, column=1, sticky="nsew", padx=(2,0))
       
       # Create button toolbar
       toolbar = ttk.Frame(frame)
       toolbar.pack(fill="x", pady=2)
       
       ttk.Button(toolbar, text="+", width=3).pack(side="left", padx=2)
       ttk.Button(toolbar, text="×", width=3).pack(side="left", padx=2)
       
       # Create treeview
       list_frame = ttk.Frame(frame)
       list_frame.pack(fill="both", expand=True)
       
       columns = ('resource_item', 'quantity', 'require_exact')
       tree = ttk.Treeview(list_frame, columns=columns, show='headings', height=15)
       
       tree.heading('resource_item', text='Resource Item')
       tree.heading('quantity', text='Quantity')
       tree.heading('require_exact', text='Require Exact Resource Type')
       
       tree.column('resource_item', width=200)
       tree.column('quantity', width=100)
       tree.column('require_exact', width=150)
       
       # Add scrollbar
       scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=tree.yview)
       tree.configure(yscrollcommand=scrollbar.set)
       
       tree.pack(side="left", fill="both", expand=True)
       scrollbar.pack(side="right", fill="y")

def main():
   root = tk.Tk()
   root.title("ARK Server Configuration - Crafting Overrides")
   root.geometry("1000x600")
   app = CraftingOverridesPanel(root)
   app.pack(fill="both", expand=True)
   root.mainloop()

if __name__ == "__main__":
   main()
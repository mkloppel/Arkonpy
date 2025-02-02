import tkinter as tk
from tkinter import ttk
from scrollable_frame import ScrollableFrameMixin

class StackSizeOverridesPanel(ttk.Frame, ScrollableFrameMixin):
   def __init__(self, parent):
       super().__init__(parent)
       self.create_frames()
       
   def create_frames(self):
       # Create main container frame
       main_frame = ttk.Frame(self)
       main_frame.pack(fill="both", expand=True, padx=5, pady=5)
       
       # Create warning note
       self.create_warning_note(main_frame)
       
       # Create global multiplier
       self.create_global_multiplier(main_frame)
       
       # Create stacked items panel
       self.create_stacked_items_panel(main_frame)

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

   def create_global_multiplier(self, parent):
       frame = ttk.Frame(parent)
       frame.pack(fill="x", pady=5)
       
       ttk.Label(frame, text="Item Stack Size Multiplier").pack(side="left", padx=5)
       
       slider = ttk.Scale(frame, from_=0, to=100, orient="horizontal")
       slider.set(1)
       slider.pack(side="left", fill="x", expand=True, padx=5)
       
       entry_var = tk.StringVar(value="1")
       entry = ttk.Entry(frame, textvariable=entry_var, width=8)
       entry.pack(side="left", padx=(0,5))
       
       ttk.Label(frame, text="x").pack(side="left")

   def create_stacked_items_panel(self, parent):
       frame = ttk.LabelFrame(parent, text="Stacked Items", padding="5")
       frame.pack(fill="both", expand=True)
       
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
       
       columns = ('item', 'max_quantity', 'ignore_multiplier')
       tree = ttk.Treeview(list_frame, columns=columns, show='headings', height=15)
       
       tree.heading('item', text='Item')
       tree.heading('max_quantity', text='Max Item Quantity')
       tree.heading('ignore_multiplier', text='Ignore Multiplier')
       
       # Configure column widths
       tree.column('item', width=300)
       tree.column('max_quantity', width=150)
       tree.column('ignore_multiplier', width=150)
       
       # Add scrollbar
       scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=tree.yview)
       tree.configure(yscrollcommand=scrollbar.set)
       
       # Pack elements
       tree.pack(side="left", fill="both", expand=True)
       scrollbar.pack(side="right", fill="y")

def main():
   root = tk.Tk()
   root.title("ARK Server Configuration - Stack Size Overrides")
   root.geometry("800x600")
   app = StackSizeOverridesPanel(root)
   app.pack(fill="both", expand=True)
   root.mainloop()

if __name__ == "__main__":
   main()
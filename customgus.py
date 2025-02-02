import tkinter as tk
from tkinter import ttk
from scrollable_frame import ScrollableFrameMixin

class CustomSettingsPanel(ttk.Frame, ScrollableFrameMixin):
   def __init__(self, parent):
       super().__init__(parent)
       self.create_frames()
       
   def create_frames(self):
       # Create main container frame
       main_frame = ttk.Frame(self)
       main_frame.pack(fill="both", expand=True, padx=5, pady=5)
       
       # Configure column weights for 50/50 split
       main_frame.grid_columnconfigure(0, weight=1)
       main_frame.grid_columnconfigure(1, weight=1)
       
       # Create the two main panels
       self.create_sections_panel(main_frame)
       self.create_items_panel(main_frame)
       
   def create_sections_panel(self, parent):
       frame = ttk.LabelFrame(parent, text="Custom Sections", padding="5")
       frame.grid(row=0, column=0, sticky="nsew", padx=2)
       
       # Create button toolbar
       toolbar = ttk.Frame(frame)
       toolbar.pack(fill="x", pady=2)
       
       # Create buttons
       ttk.Button(toolbar, text="↻", width=3).pack(side="left", padx=2)
       ttk.Button(toolbar, text="+", width=3).pack(side="left", padx=2)
       ttk.Button(toolbar, text="□", width=3).pack(side="left", padx=2)
       ttk.Button(toolbar, text="↓", width=3).pack(side="left", padx=2)
       ttk.Button(toolbar, text="×", width=3).pack(side="left", padx=2)
       
       # Create treeview
       list_frame = ttk.Frame(frame)
       list_frame.pack(fill="both", expand=True)
       
       columns = ('section_name',)
       tree = ttk.Treeview(list_frame, columns=columns, show='headings', height=15)
       
       tree.heading('section_name', text='Section Name')
       tree.column('section_name', width=200)
       
       # Add scrollbar
       scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=tree.yview)
       tree.configure(yscrollcommand=scrollbar.set)
       
       # Pack elements
       tree.pack(side="left", fill="both", expand=True)
       scrollbar.pack(side="right", fill="y")
       
   def create_items_panel(self, parent):
       frame = ttk.LabelFrame(parent, text="Custom Items", padding="5")
       frame.grid(row=0, column=1, sticky="nsew", padx=2)
       
       # Create button toolbar
       toolbar = ttk.Frame(frame)
       toolbar.pack(fill="x", pady=2)
       
       # Create buttons
       ttk.Button(toolbar, text="+", width=3).pack(side="left", padx=2)
       ttk.Button(toolbar, text="□", width=3).pack(side="left", padx=2)
       ttk.Button(toolbar, text="×", width=3).pack(side="left", padx=2)
       
       # Create treeview
       list_frame = ttk.Frame(frame)
       list_frame.pack(fill="both", expand=True)
       
       columns = ('key', 'value')
       tree = ttk.Treeview(list_frame, columns=columns, show='headings', height=15)
       
       tree.heading('key', text='Key')
       tree.heading('value', text='Value')
       
       tree.column('key', width=200)
       tree.column('value', width=200)
       
       # Add scrollbar
       scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=tree.yview)
       tree.configure(yscrollcommand=scrollbar.set)
       
       # Pack elements
       tree.pack(side="left", fill="both", expand=True)
       scrollbar.pack(side="right", fill="y")

def main():
   root = tk.Tk()
   root.title("ARK Server Configuration - Custom GameUserSettings.ini Settings")
   root.geometry("800x500")  # Default size for two panels
   app = CustomSettingsPanel(root)
   app.pack(fill="both", expand=True)
   root.mainloop()

if __name__ == "__main__":
   main()
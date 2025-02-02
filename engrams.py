import tkinter as tk
from tkinter import ttk
from scrollable_frame import ScrollableFrameMixin

class EngramsPanel(ttk.Frame, ScrollableFrameMixin):
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
       
       # Create sections
       self.create_top_controls(scrollable_frame)
       self.create_engrams_table(scrollable_frame)
       
       # Pack the scrollable elements
       self.canvas.pack(side="left", fill="both", expand=True)
       scrollbar.pack(side="right", fill="y")

   def create_top_controls(self, parent):
       control_frame = ttk.Frame(parent, padding="5")
       control_frame.pack(fill="x", padx=5, pady=5)
       
       # Top row of controls
       top_row = ttk.Frame(control_frame)
       top_row.pack(fill="x", pady=2)
       
       ttk.Checkbutton(top_row, text="Auto Unlock All Engrams").pack(side="left", padx=5)
       
       # Engram overrides frame with buttons
       override_frame = ttk.Frame(top_row)
       override_frame.pack(side="left", padx=5)
       ttk.Checkbutton(override_frame, text="Enable Engram Overrides").pack(side="left")
       ttk.Button(override_frame, text="↻").pack(side="left", padx=2)
       ttk.Button(override_frame, text="□").pack(side="left", padx=2)
       ttk.Button(override_frame, text="▤").pack(side="left", padx=2)
       ttk.Button(override_frame, text="↑").pack(side="left", padx=2)
       ttk.Button(override_frame, text="↓").pack(side="left", padx=2)
       
       # Second row with filter controls
       filter_row = ttk.Frame(control_frame)
       filter_row.pack(fill="x", pady=2)
       
       ttk.Checkbutton(filter_row, text="Only Allow Selected Engrams").pack(side="left", padx=5)
       
       ttk.Label(filter_row, text="Filter:").pack(side="left", padx=5)
       filter_combo = ttk.Combobox(filter_row, values=["All"])
       filter_combo.pack(side="left", padx=5)
       filter_combo.set("All")
       
       filter_entry = ttk.Entry(filter_row)
       filter_entry.pack(side="left", fill="x", expand=True, padx=5)
       
       ttk.Button(filter_row, text="🔍").pack(side="left", padx=5)

   def create_engrams_table(self, parent):
       # Create frame for table
       table_frame = ttk.Frame(parent, padding="5")
       table_frame.pack(fill="both", expand=True, padx=5, pady=5)
       
       # Create Treeview
       columns = ('name', 'mod', 'tekgram', 'level', 'cost', 'hidden', 'remove_prereq', 'auto_unlock', 'unlock_level')
       self.tree = ttk.Treeview(table_frame, columns=columns, show='headings', height=20)
       
       # Define column headings
       self.tree.heading('name', text='Name')
       self.tree.heading('mod', text='Mod')
       self.tree.heading('tekgram', text='Is Tekgram')
       self.tree.heading('level', text='Level')
       self.tree.heading('cost', text='Cost')
       self.tree.heading('hidden', text='Hidden')
       self.tree.heading('remove_prereq', text='Remove Prereqs')
       self.tree.heading('auto_unlock', text='Auto Unlock')
       self.tree.heading('unlock_level', text='Unlock Level')
       
       # Configure columns
       self.tree.column('name', width=150)
       self.tree.column('mod', width=100)
       self.tree.column('tekgram', width=80, anchor='center')
       self.tree.column('level', width=60, anchor='center')
       self.tree.column('cost', width=60, anchor='center')
       self.tree.column('hidden', width=60, anchor='center')
       self.tree.column('remove_prereq', width=100, anchor='center')
       self.tree.column('auto_unlock', width=80, anchor='center')
       self.tree.column('unlock_level', width=80, anchor='center')
       
       # Add scrollbar
       vsb = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
       hsb = ttk.Scrollbar(table_frame, orient="horizontal", command=self.tree.xview)
       self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
       
       # Grid layout for table and scrollbars
       self.tree.grid(column=0, row=0, sticky='nsew')
       vsb.grid(column=1, row=0, sticky='ns')
       hsb.grid(column=0, row=1, sticky='ew')
       
       table_frame.grid_columnconfigure(0, weight=1)
       table_frame.grid_rowconfigure(0, weight=1)
       
       # Add sample data
       sample_data = [
           ('Saddle - Basilisk', 'Aberration', False, 85, 28, False, False, False, 85),
           ('Charge Battery', 'Aberration', False, 71, 22, False, False, False, 71),
           ('Charge Lantern', 'Aberration', False, 80, 32, False, False, False, 80),
           ('Climbing Pick', 'Aberration', False, 34, 16, False, False, False, 34),
           # Add more sample data as needed
       ]
       
       # Insert sample data with alternating colors
       for i, item in enumerate(sample_data):
           tag = 'evenrow' if i % 2 == 0 else 'oddrow'
           self.tree.insert('', 'end', values=item, tags=(tag,))
       
       # Configure row colors
       self.tree.tag_configure('oddrow', background='#F0E6FF')  # Light pink
       self.tree.tag_configure('evenrow', background='white')

def main():
   root = tk.Tk()
   root.title("ARK Server Configuration - Engrams")
   app = EngramsPanel(root)
   app.pack(fill="both", expand=True)
   root.mainloop()

if __name__ == "__main__":
   main()
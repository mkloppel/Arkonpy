import tkinter as tk
from tkinter import ttk
from scrollable_frame import ScrollableFrameMixin

class ServerFileDetailsPanel(ttk.Frame, ScrollableFrameMixin):
   def __init__(self, parent):
       super().__init__(parent)
       self.create_frames()
       
   def create_frames(self):
       # Create main container frame
       main_frame = ttk.Frame(self)
       main_frame.pack(fill="both", expand=True)
       
       # Add warning banner
       warning_frame = ttk.Frame(main_frame)
       warning_frame.pack(fill="x", padx=5, pady=5)
       warning_label = ttk.Label(
           warning_frame, 
           text="NOTE: Any changes will require a server restart to take effect.",
           font=('TkDefaultFont', 9, 'bold')
       )
       warning_label.pack(anchor="w")
       
       # Create panel container
       panels_frame = ttk.Frame(main_frame)
       panels_frame.pack(fill="both", expand=True, padx=5, pady=5)
       
       # Configure equal column weights
       panels_frame.grid_columnconfigure(0, weight=1)
       panels_frame.grid_columnconfigure(1, weight=1)
       panels_frame.grid_columnconfigure(2, weight=1)
       
       # Create the three panels
       self.create_admin_panel(panels_frame, 0)
       self.create_whitelist_panel(panels_frame, 1)
       self.create_exclusive_panel(panels_frame, 2)
       
   def create_list_view(self, parent):
       # Create Treeview for player list
       columns = ('player_id', 'player_name')
       tree = ttk.Treeview(parent, columns=columns, show='headings', height=15)
       
       # Configure columns
       tree.heading('player_id', text='Player Id')
       tree.heading('player_name', text='Player Name')
       
       tree.column('player_id', width=120)
       tree.column('player_name', width=120)
       
       # Add scrollbar
       scrollbar = ttk.Scrollbar(parent, orient="vertical", command=tree.yview)
       tree.configure(yscrollcommand=scrollbar.set)
       
       # Pack elements
       tree.pack(side="left", fill="both", expand=True)
       scrollbar.pack(side="right", fill="y")
       
       return tree
       
   def create_control_buttons(self, parent):
       button_frame = ttk.Frame(parent)
       button_frame.pack(fill="x", padx=2, pady=2)
       
       add_btn = ttk.Button(button_frame, text="+", width=3)
       add_btn.pack(side="left", padx=2)
       
       remove_btn = ttk.Button(button_frame, text="×", width=3)
       remove_btn.pack(side="left", padx=2)
       
       refresh_btn = ttk.Button(button_frame, text="↻", width=3)
       refresh_btn.pack(side="left", padx=2)
       
   def create_admin_panel(self, parent, column):
       frame = ttk.LabelFrame(parent, text="Administrators", padding="5")
       frame.grid(row=0, column=column, sticky="nsew", padx=2)
       
       # Add control buttons
       self.create_control_buttons(frame)
       
       # Add list view
       list_frame = ttk.Frame(frame)
       list_frame.pack(fill="both", expand=True)
       self.create_list_view(list_frame)
       
   def create_whitelist_panel(self, parent, column):
       frame = ttk.LabelFrame(parent, text="Whitelisted", padding="5")
       frame.grid(row=0, column=column, sticky="nsew", padx=2)
       
       # Add control buttons
       self.create_control_buttons(frame)
       
       # Add list view
       list_frame = ttk.Frame(frame)
       list_frame.pack(fill="both", expand=True)
       self.create_list_view(list_frame)
       
   def create_exclusive_panel(self, parent, column):
       frame = ttk.LabelFrame(parent, text="Exclusive Join", padding="5")
       frame.grid(row=0, column=column, sticky="nsew", padx=2)
       
       # Add enable checkbox
       ttk.Checkbutton(frame, text="Enable Exclusive Join").pack(anchor="w", pady=2)
       
       # Add control buttons
       self.create_control_buttons(frame)
       
       # Add list view
       list_frame = ttk.Frame(frame)
       list_frame.pack(fill="both", expand=True)
       self.create_list_view(list_frame)

def main():
   root = tk.Tk()
   root.title("ARK Server Configuration - Server File Details")
   root.geometry("1200x500")  # Wider default size for three panels
   app = ServerFileDetailsPanel(root)
   app.pack(fill="both", expand=True)
   root.mainloop()

if __name__ == "__main__":
   main()
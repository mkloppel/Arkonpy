import tkinter as tk
from tkinter import ttk
from scrollable_frame import ScrollableFrameMixin  # Assumes this module is available

class SupplyCrateOverridesPanel(ttk.Frame, ScrollableFrameMixin):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_frames()

    def create_frames(self):
        # Create main container frame with a label
        container = ttk.LabelFrame(self, text="Supply Crate Overrides", padding=5)
        container.pack(fill="both", expand=True, padx=5, pady=5)

        # Create warning notes frame at the top
        warning_frame = ttk.Frame(container)
        warning_frame.pack(fill="x", pady=5)

        # Create green note (Note 1)
        green_note = ttk.Label(
            warning_frame,
            text="NOTE: If you want to manage your overrides manually or with another application, you can disable the option that will prevent the server manager managing the overrides. See the 'Custom Override Options' in the global settings.",
            foreground='dark green',
            wraplength=800,
            justify="left"
        )
        green_note.pack(anchor="w")

        # Create red warning note (Note 2)
        red_note = ttk.Label(
            warning_frame,
            text="WARNING: If you do not populate each grid properly, it could result in the Supply Crate not spawning into the world. Please ensure ALL sections are populated.",
            foreground='red',
            wraplength=800,
            justify="left"
        )
        red_note.pack(anchor="w", pady=(5, 0))

        # Create vertical stack layout for the four panels
        panels_container = ttk.Frame(container)
        panels_container.pack(fill="both", expand=True)

        # Create the Supply Crates Panel (Top)
        self.create_supply_crates_panel(panels_container)
        # Create the Item Sets Panel (Second)
        self.create_item_sets_panel(panels_container)
        # Create the Item Set Entries Panel (Third)
        self.create_item_set_entries_panel(panels_container)
        # Create the Items Panel (Bottom)
        self.create_items_panel(panels_container)

    def create_supply_crates_panel(self, parent):
        # Supply Crates Panel: Contains toolbar and multi-column list view for supply crates
        panel = ttk.LabelFrame(parent, text="Supply Crates", padding="5")
        panel.pack(fill="x", pady=5)

        # Create toolbar with control buttons: Add, Edit, Remove, Copy
        toolbar = ttk.Frame(panel)
        toolbar.pack(fill="x", pady=2)
        ttk.Button(toolbar, text="+", width=3).pack(side="left", padx=2)
        ttk.Button(toolbar, text="□", width=3).pack(side="left", padx=2)
        ttk.Button(toolbar, text="×", width=3).pack(side="left", padx=2)
        ttk.Button(toolbar, text="⎘", width=3).pack(side="left", padx=2)

        # Create list view using Treeview widget
        list_frame = ttk.Frame(panel)
        list_frame.pack(fill="both", expand=True)
        columns = (
            'supply_crate', 'min_itemsets', 'max_itemsets',
            'quality_multiplier', 'prevent_duplicates',
            'append_itemsets', 'prevent_increasing'
        )
        tree = ttk.Treeview(list_frame, columns=columns, show='headings', height=10)
        # Define column headings
        tree.heading('supply_crate', text='Supply Crate')
        tree.heading('min_itemsets', text='Min ItemSets')
        tree.heading('max_itemsets', text='Max ItemSets')
        tree.heading('quality_multiplier', text='Quality Multiplier')
        tree.heading('prevent_duplicates', text='Prevent Duplicates')
        tree.heading('append_itemsets', text='Append Item Sets')
        tree.heading('prevent_increasing', text='Prevent Increasing')
        # Set default column widths
        tree.column('supply_crate', width=120)
        tree.column('min_itemsets', width=100)
        tree.column('max_itemsets', width=100)
        tree.column('quality_multiplier', width=120)
        tree.column('prevent_duplicates', width=120)
        tree.column('append_itemsets', width=120)
        tree.column('prevent_increasing', width=120)
        # Add vertical scrollbar to the treeview
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def create_item_sets_panel(self, parent):
        # Item Sets Panel: Contains toolbar and list view for item sets
        panel = ttk.LabelFrame(parent, text="Item Sets", padding="5")
        panel.pack(fill="x", pady=5)

        # Create toolbar with control buttons: Add, Remove
        toolbar = ttk.Frame(panel)
        toolbar.pack(fill="x", pady=2)
        ttk.Button(toolbar, text="+", width=3).pack(side="left", padx=2)
        ttk.Button(toolbar, text="×", width=3).pack(side="left", padx=2)

        # Create list view using Treeview widget
        list_frame = ttk.Frame(panel)
        list_frame.pack(fill="both", expand=True)
        columns = ('description', 'min_items', 'max_items', 'quality_multiplier', 'weight', 'prevent_duplicates')
        tree = ttk.Treeview(list_frame, columns=columns, show='headings', height=10)
        # Define column headings
        tree.heading('description', text='Description')
        tree.heading('min_items', text='Min Items')
        tree.heading('max_items', text='Max Items')
        tree.heading('quality_multiplier', text='Quality Multiplier')
        tree.heading('weight', text='Weight')
        tree.heading('prevent_duplicates', text='Prevent Duplicates')
        # Set default column widths
        tree.column('description', width=150)
        tree.column('min_items', width=100)
        tree.column('max_items', width=100)
        tree.column('quality_multiplier', width=120)
        tree.column('weight', width=100)
        tree.column('prevent_duplicates', width=120)
        # Add vertical scrollbar to the treeview
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def create_item_set_entries_panel(self, parent):
        # Item Set Entries Panel: Contains toolbar and list view for item set entries
        panel = ttk.LabelFrame(parent, text="Item Set Entries", padding="5")
        panel.pack(fill="x", pady=5)

        # Create toolbar with control buttons: Add, Remove
        toolbar = ttk.Frame(panel)
        toolbar.pack(fill="x", pady=2)
        ttk.Button(toolbar, text="+", width=3).pack(side="left", padx=2)
        ttk.Button(toolbar, text="×", width=3).pack(side="left", padx=2)

        # Create list view using Treeview widget
        list_frame = ttk.Frame(panel)
        list_frame.pack(fill="both", expand=True)
        columns = (
            'description', 'min_quantity', 'max_quantity', 'min_quality',
            'max_quality', 'weight', 'force_blueprint', 'blueprint_chance'
        )
        tree = ttk.Treeview(list_frame, columns=columns, show='headings', height=10)
        # Define column headings
        tree.heading('description', text='Description')
        tree.heading('min_quantity', text='Min Quantity')
        tree.heading('max_quantity', text='Max Quantity')
        tree.heading('min_quality', text='Min Quality')
        tree.heading('max_quality', text='Max Quality')
        tree.heading('weight', text='Weight')
        tree.heading('force_blueprint', text='Force Blueprint')
        tree.heading('blueprint_chance', text='Blueprint Chance')
        # Set default column widths
        tree.column('description', width=150)
        tree.column('min_quantity', width=100)
        tree.column('max_quantity', width=100)
        tree.column('min_quality', width=100)
        tree.column('max_quality', width=100)
        tree.column('weight', width=100)
        tree.column('force_blueprint', width=120)
        tree.column('blueprint_chance', width=120)
        # Add vertical scrollbar to the treeview
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def create_items_panel(self, parent):
        # Items Panel: Contains toolbar and two-column list view for items
        panel = ttk.LabelFrame(parent, text="Items", padding="5")
        panel.pack(fill="x", pady=5)

        # Create toolbar with control buttons: Add, Remove
        toolbar = ttk.Frame(panel)
        toolbar.pack(fill="x", pady=2)
        ttk.Button(toolbar, text="+", width=3).pack(side="left", padx=2)
        ttk.Button(toolbar, text="×", width=3).pack(side="left", padx=2)

        # Create list view using Treeview widget
        list_frame = ttk.Frame(panel)
        list_frame.pack(fill="both", expand=True)
        columns = ('item', 'weight')
        tree = ttk.Treeview(list_frame, columns=columns, show='headings', height=10)
        # Define column headings
        tree.heading('item', text='Item')
        tree.heading('weight', text='Weight')
        # Set default column widths
        tree.column('item', width=150)
        tree.column('weight', width=100)
        # Add vertical scrollbar to the treeview
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

def main():
    # Main application window
    root = tk.Tk()
    root.title("Server Configuration - Supply Crate Overrides")
    root.geometry("1000x800")
    app = SupplyCrateOverridesPanel(root)
    app.pack(fill="both", expand=True)
    root.mainloop()

if __name__ == "__main__":
    main()
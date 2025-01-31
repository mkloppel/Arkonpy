import tkinter as tk
from tkinter import ttk
from scrollable_frame import ScrollableFrameMixin

class DinoSettingsPanel(ttk.Frame, ScrollableFrameMixin):
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
        self.create_dino_counts_section(scrollable_frame)
        self.create_dino_stats_section(scrollable_frame)
        self.create_tame_settings_section(scrollable_frame)
        self.create_additional_stats_section(scrollable_frame)
        self.create_raid_settings_section(scrollable_frame)
        self.create_flyer_settings_section(scrollable_frame)
        self.create_riding_settings_section(scrollable_frame)
        self.create_customization_section(scrollable_frame)
        self.create_dino_configuration_table(scrollable_frame)
        self.create_wild_multipliers_section(scrollable_frame)
        self.create_tamed_multipliers_section(scrollable_frame)
        self.create_tamed_add_multipliers_section(scrollable_frame)
        self.create_affinity_multipliers_section(scrollable_frame)  # New
        self.create_breeding_multipliers_section(scrollable_frame)  # New
        self.create_imprinting_section(scrollable_frame)  # New

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
    
    def create_dino_counts_section(self, parent):
        section = ttk.LabelFrame(parent, text="Dino Counts", padding="5")
        section.pack(fill="x", padx=5, pady=5)

        self.create_slider_with_entry(section, "Max Tamed Dinos (server)", 4000, "", 5000)
        self.create_slider_with_entry(section, "Max Tamed Dinos (tribe)", 40, "", 100)
       
    def create_dino_stats_section(self, parent):
        section = ttk.LabelFrame(parent, text="Base Dino Stats", padding="5")
        section.pack(fill="x", padx=5, pady=5)

        stats = [
            ("Damage", 1), ("Tamed Damage", 1),
            ("Resistance", 1), ("Tamed Resistance", 1),
            ("Food Drain", 1), ("Tamed Food Drain", 1),
            ("Torpor Drain", 1), ("Tamed Torpor Drain", 1)
        ]

        for stat, default in stats:
            self.create_slider_with_entry(section, stat, default)
   
    def create_tame_settings_section(self, parent):
        section = ttk.LabelFrame(parent, text="Tame Settings", padding="5")
        section.pack(fill="x", padx=5, pady=5)

        self.create_slider_with_entry(section, "Passive Tame Interval", 1)
        self.create_slider_with_entry(section, "Tamed Dinos Saddle Structure Cost", 19, "", 50)
        ttk.Checkbutton(section, text="Use Tame Limit for Structures Only").pack(anchor="w", pady=2)
   
    def create_additional_stats_section(self, parent):
        section = ttk.LabelFrame(parent, text="Additional Stats", padding="5")
        section.pack(fill="x", padx=5, pady=5)

        stats = [
            ("Food Drain", 1), ("Stamina Drain", 1),
            ("Health Recovery", 1), ("Harvesting Damage", 3),
            ("Turret Damage", 1)
        ]

        for stat, default in stats:
            self.create_slider_with_entry(section, stat, default)

    def create_raid_settings_section(self, parent):
        section = ttk.LabelFrame(parent, text="Raid Settings", padding="5")
        section.pack(fill="x", padx=5, pady=5)

        ttk.Checkbutton(section, text="Allow Raid Dino Feeding").pack(anchor="w", pady=2)
        self.create_slider_with_entry(section, "Food Drain Multiplier", 1)

    def create_flyer_settings_section(self, parent):
        section = ttk.LabelFrame(parent, text="Flyer Settings", padding="5")
        section.pack(fill="x", padx=5, pady=5)

        # Create three-column layout
        columns_frame = ttk.Frame(section)
        columns_frame.pack(fill="x", pady=2)

        # Define checkboxes for each column
        left_options = [
            "Allow Flyers in Caves",
            "Prevent Dino Mate Boost",
            "Disable Dino Decay PvE"
        ]

        middle_options = [
            "Allow Flying Stamina Recovery",
            "Disable Force Ground Flyer with Explosives",
            "Disable Dino Decay PvP"
        ]

        right_options = [
            "Allow Flyer Speed Leveling",
            "Allow Multiple Attached C4",
            "Auto Destroy Decayed Dinos"
        ]

        # Create columns
        for i, options in enumerate([left_options, middle_options, right_options]):
            column = ttk.Frame(columns_frame)
            column.pack(side="left", fill="x", expand=True)
            
            for option in options:
                ttk.Checkbutton(column, text=option).pack(anchor="w", pady=1)

        self.create_slider_with_entry(section, "PvE Dino Decay Period", 1)

    def create_riding_settings_section(self, parent):
        section = ttk.LabelFrame(parent, text="Riding Settings", padding="5")
        section.pack(fill="x", padx=5, pady=5)

        options = [
            "Disable Dino Riding",
            "Change Flyer Riding",
            "Enable Flyer Riding"
        ]

        for option in options:
            ttk.Checkbutton(section, text=option).pack(anchor="w", pady=1)
   
    def create_customization_section(self, parent):
        section = ttk.LabelFrame(parent, text="Dino Customization", padding="5")
        section.pack(fill="x", padx=5, pady=5)

        # Top row with checkboxes
        checkbox_frame = ttk.Frame(section)
        checkbox_frame.pack(fill="x", pady=2)

        options = [
            "Spawn Multipliers", "Tamed Damage", "Tamed Resistance",
            "Wild Damage", "Wild Resistance"
        ]

        for option in options:
            ttk.Checkbutton(checkbox_frame, text=option).pack(side="left", padx=5)

        # Bottom row with filter
        filter_frame = ttk.Frame(section)
        filter_frame.pack(fill="x", pady=2)

        ttk.Label(filter_frame, text="Filter:").pack(side="left", padx=(5,0))
        ttk.Combobox(filter_frame, values=["All"]).pack(side="left", padx=5)
       
    def create_dino_configuration_table(self, parent):
        section = ttk.LabelFrame(parent, text="Dino Configuration", padding="5")
        section.pack(fill="x", padx=5, pady=5)

        # Create Treeview
        columns = ('name', 'mod', 'spawnable', 'tameable', 'replace_with')
        tree = ttk.Treeview(section, columns=columns, show='headings', height=10)

        # Define column headings
        tree.heading('name', text='Name')
        tree.heading('mod', text='Mod')
        tree.heading('spawnable', text='Spawnable')
        tree.heading('tameable', text='Tameable')
        tree.heading('replace_with', text='Replace With')

        # Configure columns
        tree.column('name', width=150)
        tree.column('mod', width=100)
        tree.column('spawnable', width=80, anchor='center')
        tree.column('tameable', width=80, anchor='center')
        tree.column('replace_with', width=200)

        # Add scrollbar
        scrollbar = ttk.Scrollbar(section, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)

        # Pack elements
        tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Add sample data
        sample_data = [
        ('Aberrant Beelzebufo', 'Aberration', True, True, '(Aberration) Aberrant Beelzebufo'),
        ('Aberrant Carbonemys', 'Aberration', True, True, '(Aberration) Aberrant Carbonemys'),
        # Add more sample data as needed
        ]

        for item in sample_data:
            tree.insert('', 'end', values=item)

    def create_wild_multipliers_section(self, parent):
        section = ttk.LabelFrame(parent, text="Per-Level Stat Multipliers (Wild)", padding="5")
        section.pack(fill="x", padx=5, pady=5)

        self.create_stat_columns(section, {
            'left': [
                ('Health', 1), ('Stamina', 1),
                ('Oxygen', 1), ('Food', 1)
            ],
            'right': [
                ('Temperature', 1), ('Weight', 1),
                ('Damage', 1), ('Speed', 1),
                ('Crafting', 1)
            ]
        })

    def create_tamed_multipliers_section(self, parent):
        section = ttk.LabelFrame(parent, text="Per-Level Stat Multipliers (Tamed)", padding="5")
        section.pack(fill="x", padx=5, pady=5)

        self.create_stat_columns(section, {
            'left': [
                ('Health', 0.2), ('Stamina', 1),
                ('Oxygen', 1), ('Food', 1)
            ],
            'right': [
                ('Temperature', 1), ('Weight', 1),
                ('Damage', 0.17), ('Speed', 1),
                ('Crafting', 1)
            ]
        })

    def create_tamed_add_multipliers_section(self, parent):
        section = ttk.LabelFrame(parent, text="Per-Level Stat Multipliers (Tamed) - Add", padding="5")
        section.pack(fill="x", padx=5, pady=5)

        self.create_stat_columns(section, {
            'left': [
                ('Health', 0.14), ('Stamina', 1),
                ('Torpidity', 1), ('Oxygen', 1),
                ('Food', 1), ('Water', 1)
            ],
            'right': [
                ('Temperature', 1), ('Weight', 1),
                ('Damage', 0.14), ('Speed', 1),
                ('Fortitude', 1), ('Crafting', 1)
            ]
        })

    def create_stat_columns(self, parent, stats):
        columns_frame = ttk.Frame(parent)
        columns_frame.pack(fill="x", pady=2)

        # Left column
        left_frame = ttk.Frame(columns_frame)
        left_frame.pack(side="left", fill="x", expand=True)

        for stat, value in stats['left']:
            self.create_slider_with_entry(left_frame, stat, value)

        # Right column
        right_frame = ttk.Frame(columns_frame)
        right_frame.pack(side="left", fill="x", expand=True)

        for stat, value in stats['right']:
            self.create_slider_with_entry(right_frame, stat, value)

    def create_affinity_multipliers_section(self, parent):
        section = ttk.LabelFrame(parent, text="Per-Level Stat Multipliers (Tamed) - Affinity", padding="5")
        section.pack(fill="x", padx=5, pady=5)

        self.create_stat_columns(section, {
            'left': [
                ('Health', 0.44), ('Stamina', 1),
                ('Torpidity', 1), ('Oxygen', 1),
                ('Food', 1), ('Water', 1)
            ],
            'right': [
                ('Temperature', 1), ('Weight', 1),
                ('Damage', 0.44), ('Speed', 1),
                ('Fortitude', 1), ('Crafting', 1)
            ]
        })

    def create_breeding_multipliers_section(self, parent):
        section = ttk.LabelFrame(parent, text="Dino Breeding Multipliers", padding="5")
        section.pack(fill="x", padx=5, pady=5)

        breeding_settings = [
            ('Mating Interval', 1),
            ('Mating Speed', 1),
            ('Egg Hatch Speed', 1),
            ('Baby Mature Speed', 1),
            ('Baby Food Consumption Speed', 1)
        ]

        for setting, default in breeding_settings:
            self.create_slider_with_entry(section, setting, default)

    def create_imprinting_section(self, parent):
        section = ttk.LabelFrame(parent, text="Dino Imprinting", padding="5")
        section.pack(fill="x", padx=5, pady=5)

        # Checkbox options
        checkbox_frame = ttk.Frame(section)
        checkbox_frame.pack(fill="x", pady=2)

        checkboxes = [
            "Disable Baby Dino Imprint Buff",
            "Allow Baby Dino Imprint Cuddle by Anyone"
        ]

        for option in checkboxes:
            ttk.Checkbutton(checkbox_frame, text=option).pack(anchor="w", pady=1)

        # Slider settings
        imprint_settings = [
            ('Imprinting Stat Scale', 1),
            ('Imprint Amount Scale', 1),
            ('Cuddle Interval', 1),
            ('Cuddle Grace Period', 1),
            ('Cuddle Lose Imprint Quality Speed', 1)
        ]

        for setting, default in imprint_settings:
            self.create_slider_with_entry(section, setting, default)

def main():
    root = tk.Tk()
    root.title("ARK Server Configuration - Dino Settings")
    app = DinoSettingsPanel(root)
    app.pack(fill="both", expand=True)
    root.mainloop()

if __name__ == "__main__":
    main()

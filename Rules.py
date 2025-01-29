import tkinter as tk
from tkinter import ttk
import re
from scrollable_frame import ScrollableFrameMixin

class RulesContent(ttk.Frame, ScrollableFrameMixin):
    def __init__(self, parent):
        super().__init__(parent)
        # Initialize variables
        self.variables = {}
        self.slider_values = {}
        self.create_frames()

    def create_frames(self):
        # Create main scrollable container
        self.canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        # Add scroll functionality
        self.add_scroll_functionality(self.canvas)
        
        # Create all sections
        self.create_general_rules()
        self.create_tribute_section()
        self.create_cluster_options_section()
        self.create_pve_schedule_section()
        self.create_tribe_settings_section()
        self.create_tribe_warfare_section()
        self.create_disease_network_section()
        self.create_game_mechanics_section()
        self.create_cryopod_section()
        self.create_genesis_sections()
        self.create_hexagons_section()
        
        # Pack the scrollable elements
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def create_labeled_checkbox(self, parent, text, row, column, columnspan=1):
        var = tk.BooleanVar()
        self.variables[text] = var
        cb = ttk.Checkbutton(parent, text=text, variable=var)
        cb.grid(row=row, column=column, columnspan=columnspan, sticky='w', padx=5, pady=2)
        return cb

    def create_slider_with_entry(self, parent, text, default_value, unit="", float_type=True):
        frame = ttk.Frame(parent)
        frame.pack(fill="x", pady=2)
        
        label = ttk.Label(frame, text=text)
        label.pack(side="left", padx=5)
        
        slider_var = tk.DoubleVar(value=float(default_value))
        slider = ttk.Scale(frame, from_=0, to=100 if float_type else 1000,
                         variable=slider_var, orient='horizontal')
        slider.pack(side="left", fill="x", expand=True, padx=5)
        
        entry_var = tk.StringVar(value=str(default_value))
        entry = ttk.Entry(frame, textvariable=entry_var, width=10)
        entry.pack(side="left", padx=5)
        
        if unit:
            unit_label = ttk.Label(frame, text=unit)
            unit_label.pack(side="left", padx=5)
        
        self.slider_values[text] = (slider_var, entry_var)
        return frame, slider, entry

    def create_time_input(self, parent, text, row, column):
        def validate_time(P):
            if P == "":
                return True
            return bool(re.match(r'^([01]?[0-9]|2[0-3]):[0-5][0-9]$', P))
        
        label = ttk.Label(parent, text=text)
        label.grid(row=row, column=column, padx=5, pady=2)
        
        vcmd = (self.register(validate_time), '%P')
        entry = ttk.Entry(parent, width=10, validate='key', validatecommand=vcmd)
        entry.insert(0, "00:00")
        entry.grid(row=row, column=column + 1, padx=5, pady=2)
        return entry
    
    def create_general_rules(self):
        frame = ttk.LabelFrame(self.scrollable_frame, text="General Rules")
        frame.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
        frame.grid_columnconfigure(1, weight=1)
        
        # Left column checkboxes
        left_checkboxes = [
            "Enable Hardcore Mode",
            "Enable PvP",
            "Disable PvE Friendly Fire",
            "Enable PvE Cave Building",
            "Prevent Building in Resource Rich Areas",
            "Enable PvE Cryo Sickness",
            "Disable PvP Friendly Fire",
            "Disable Supply Crates",
            "Random Supply Crate Points"
        ]
        
        # Right column checkboxes
        right_checkboxes = [
            "Use Corpse Locator",
            "Allow Platform Saddle Multi Floors",
            "Enable Difficulty Override",
            "Disable Non-Meat Fish Loot"
        ]
        
        # Create left column
        for i, text in enumerate(left_checkboxes):
            self.create_labeled_checkbox(frame, text, i, 0)
            
        # Create right column
        for i, text in enumerate(right_checkboxes):
            self.create_labeled_checkbox(frame, text, i, 2)
            
        # Create sliders
        slider_configs = [
            ("Supply Crate Loot Quality Multiplier", 1.0, "x", True),
            ("Fishing Loot Quality Multiplier", 1.0, "x", True),
            ("Platform Saddle Build Area Bounds Multiplier", 1.0, "x", True),
            ("Max Gateways on Saddles", 2, "", False),
            ("Max Dino Level", 120, "levels", False),
            ("Difficulty Offset", 1.0, "", True)
        ]
        
        for i, (text, default, unit, is_float) in enumerate(slider_configs):
            slider_frame = ttk.Frame(frame)
            slider_frame.grid(row=i + len(left_checkboxes), column=0, columnspan=3, sticky='ew', padx=5, pady=2)
            self.create_slider_with_entry(slider_frame, text, default, unit, is_float)

    def create_downloads_section(self):
        frame = ttk.LabelFrame(self.scrollable_frame, text="Downloads")
        frame.grid(row=1, column=0, sticky='nsew', padx=5, pady=5)
        frame.grid_columnconfigure(1, weight=1)
        
        # Left column checkboxes
        left_checkboxes = [
            "Allow Foreign Dino Downloads",
            "Allow Item Downloads",
            "Allow Survivor Downloads",
            "Allow Foreign Item Downloads"
        ]
        
        # Right column checkboxes  
        right_checkboxes = [
            "Allow Foreign Survivor Downloads",
            "Prevent Download Dino Classes",
            "Prevent Download Item Classes",
            "Prevent Upload Dino Classes"
        ]
        
        # Create left column
        for i, text in enumerate(left_checkboxes):
            self.create_labeled_checkbox(frame, text, i, 0)
            
        # Create right column
        for i, text in enumerate(right_checkboxes):
            self.create_labeled_checkbox(frame, text, i, 2)
            
    def create_tribute_section(self):
        frame = ttk.LabelFrame(self.scrollable_frame, text="Tribute Options")
        frame.grid(row=2, column=0, sticky='nsew', padx=5, pady=5)
        frame.grid_columnconfigure(1, weight=1)
        
        # Upload restriction checkboxes
        checkboxes = [
            "No Survivor Uploads",
            "No Item Uploads",
            "No Dino Uploads"
        ]
        
        for i, text in enumerate(checkboxes):
            self.create_labeled_checkbox(frame, text, i, 0)
        
        # Max Tribute settings
        slider_frame = ttk.Frame(frame)
        slider_frame.grid(row=3, column=0, columnspan=3, sticky='ew', padx=5, pady=2)
        self.create_slider_with_entry(slider_frame, "Max Tribute Dinos", 50, "dinos", False)
        
        slider_frame2 = ttk.Frame(frame)
        slider_frame2.grid(row=4, column=0, columnspan=3, sticky='ew', padx=5, pady=2)
        self.create_slider_with_entry(slider_frame2, "Max Tribute Items", 50, "items", False)
        
    def create_cluster_options_section(self):
        frame = ttk.LabelFrame(self.scrollable_frame, text="Cluster Tribute Options")
        frame.grid(row=3, column=0, sticky='nsew', padx=5, pady=5)
        frame.grid_columnconfigure(1, weight=1)
        
        # Checkboxes
        checkboxes = [
            "No Transfer from Filtering",
            "Increase PvP Respawn Interval",
            "Prevent Offline PvP",
            "PvE Schedule"
        ]
        
        for i, text in enumerate(checkboxes):
            self.create_labeled_checkbox(frame, text, i, 0)
        
        # Sliders
        slider_configs = [
            ("Override Survivor Upload Expiration", 1440, "minutes", False),
            ("Override Item Upload Expiration", 1440, "minutes", False),
            ("Override Dino Upload Expiration", 1440, "minutes", False),
            ("Override Minimum Dino Re-upload Interval", 720, "minutes", False),
            ("Interval Check Period", 300, "seconds", False),
            ("Interval Multiplier", 1.0, "", True),
            ("Interval Base Amount", 60, "seconds", False),
            ("Logout Interval", 900, "seconds", False),
            ("Connection Invincible Interval", 5, "seconds", False)
        ]
        
        for i, (text, default, unit, is_float) in enumerate(slider_configs):
            slider_frame = ttk.Frame(frame)
            slider_frame.grid(row=i + len(checkboxes), column=0, columnspan=3, sticky='ew', padx=5, pady=2)
            self.create_slider_with_entry(slider_frame, text, default, unit, is_float)
        

    def create_pve_schedule_section(self):
        frame = ttk.LabelFrame(self.scrollable_frame, text="PvE Schedule")
        frame.grid(row=4, column=0, sticky='nsew', padx=5, pady=5)
        frame.grid_columnconfigure(1, weight=1)
        
        self.create_labeled_checkbox(frame, "PvE Schedule", 0, 0)
        self.create_labeled_checkbox(frame, "Use Server Time", 1, 0)
        
        self.create_time_input(frame, "Start Time:", 2, 0)
        self.create_time_input(frame, "Stop Time:", 2, 2)

    def create_tribe_settings_section(self):
        frame = ttk.LabelFrame(self.scrollable_frame, text="Tribe Settings")
        frame.grid(row=5, column=0, sticky='nsew', padx=5, pady=5)
        frame.grid_columnconfigure(1, weight=1)
        
        sliders_config = [
            ("Max Players in Tribe", 70, "players", False),
            ("Tribe Name Change Cooldown", 15, "minutes", False),
            ("Tribe Slot Reuse Cooldown", 0, "minutes", False),
            ("Max Alliances Per Tribe", 10, "", False),
            ("Max Tribes Per Alliance", 10, "", False)
        ]
        
        self.create_labeled_checkbox(frame, "Allow Tribe Alliances", 0, 0)
        
        for i, (text, default, unit, is_float) in enumerate(sliders_config):
            slider_frame = ttk.Frame(frame)
            slider_frame.grid(row=i + 1, column=0, columnspan=3, sticky='ew', padx=5, pady=2)
            self.create_slider_with_entry(slider_frame, text, default, unit, is_float)

    def create_tribe_warfare_section(self):
        frame = ttk.LabelFrame(self.scrollable_frame, text='PvE "Tribe Warfare" Options')
        frame.grid(row=6, column=0, sticky='nsew', padx=5, pady=5)
        frame.grid_columnconfigure(1, weight=1)
        
        checkboxes = [
            "Allow Tribe Warfare",
            "Allow Cancelling Tribe Warfare",
            "Allow Custom Recipes"
        ]
        
        for i, text in enumerate(checkboxes):
            self.create_labeled_checkbox(frame, text, i, 0)
            
        slider_frame = ttk.Frame(frame)
        slider_frame.grid(row=3, column=0, columnspan=3, sticky='ew', padx=5, pady=2)
        self.create_slider_with_entry(slider_frame, "Effectiveness Multiplier", 1, "x", True)
        
        slider_frame2 = ttk.Frame(frame)
        slider_frame2.grid(row=4, column=0, columnspan=3, sticky='ew', padx=5, pady=2)
        self.create_slider_with_entry(slider_frame2, "Skill Multiplier", 1, "x", True)

    def create_disease_network_section(self):
        frame = ttk.LabelFrame(self.scrollable_frame, text="Disease and Network Settings")
        frame.grid(row=7, column=0, sticky='nsew', padx=5, pady=5)
        frame.grid_columnconfigure(1, weight=1)
        
        checkboxes = [
            "Enable Diseases",
            "Non Permanent Diseases",
            "Override NPC Network Stasis Range Scale"
        ]
        
        for i, text in enumerate(checkboxes):
            self.create_labeled_checkbox(frame, text, i, 0)
            
        sliders_config = [
            ("Online Player Count Start", 70, "players", False),
            ("Online Player Count End", 120, "players", False),
            ("Scale Maximum", 0.5, "%", True)
        ]
        
        for i, (text, default, unit, is_float) in enumerate(sliders_config):
            self.create_slider_with_entry(frame, text, default, i + len(checkboxes), unit, is_float)

    def create_game_mechanics_section(self):
        frame = ttk.LabelFrame(self.scrollable_frame, text="Game Mechanics Multipliers")
        frame.grid(row=8, column=0, sticky='nsew', padx=5, pady=5)
        frame.grid_columnconfigure(1, weight=1)
        
        sliders_config = [
            ("Oxygen Swim Speed Stat Multiplier", 1, "x", True),
            ("Use Corpse Life Span Multiplier", 1, "x", True),
            ("Global Powered Battery Durability", 4, "x", True),
            ("Fuel Consumption Interval Multiplier", 1, "x", True),
            ("Limit Non Player Dropped Items Range", 0, "items", False),
            ("Limit Non Player Dropped Items Count", 0, "items", False)
        ]
        
        for i, (text, default, unit, is_float) in enumerate(sliders_config):
            self.create_slider_with_entry(frame, text, default, i, unit, is_float)

    def create_cryopod_section(self):
        frame = ttk.LabelFrame(self.scrollable_frame, text="Cryopod Settings")
        frame.grid(row=9, column=0, sticky='nsew', padx=5, pady=5)
        frame.grid_columnconfigure(1, weight=1)
        
        self.create_labeled_checkbox(frame, "Enable Cryopod Nerf", 0, 0)
        
        sliders_config = [
            ("Duration", 10, "seconds", False),
            ("Outgoing Damage Multiplier", 1, "x", True),
            ("Incoming Damage Multiplier Percent", 0, "%", True)
        ]
        
        for i, (text, default, unit, is_float) in enumerate(sliders_config):
            self.create_slider_with_entry(frame, text, default, i + 1, unit, is_float)

    def create_genesis_sections(self):
        # Genesis Part 1
        frame1 = ttk.LabelFrame(self.scrollable_frame, text="Genesis: Part 1")
        frame1.grid(row=10, column=0, sticky='nsew', padx=5, pady=5)
        
        self.create_labeled_checkbox(frame1, "Disable Missions", 0, 0)
        self.create_labeled_checkbox(frame1, "Allow TEK Suit Powers", 0, 1)
        
        # Genesis Part 2
        frame2 = ttk.LabelFrame(self.scrollable_frame, text="Genesis: Part 2")
        frame2.grid(row=11, column=0, sticky='nsew', padx=5, pady=5)
        frame2.grid_columnconfigure(1, weight=1)
        
        checkboxes = [
            "Disable TEK Suit on Spawn",
            "Disable World Buffs",
            "Enable World Buff Scaling"
        ]
        
        for i, text in enumerate(checkboxes):
            self.create_labeled_checkbox(frame2, text, i, 0)
            
        self.create_slider_with_entry(frame2, "World Buff Scaling Efficacy", 1, 3, "x", True)

    def create_hexagons_section(self):
        frame = ttk.LabelFrame(self.scrollable_frame, text="Hexagons")
        frame.grid(row=12, column=0, sticky='nsew', padx=5, pady=5)
        frame.grid_columnconfigure(1, weight=1)
        
        self.create_labeled_checkbox(frame, "Disable Hexagon Store", 0, 0)
        self.create_labeled_checkbox(frame, "Allow Only Engram Points Trade", 1, 0)
        
        sliders_config = [
            ("Max Hexagons per Character", 2500000, "", False),
            ("Hexagon Reward Multiplier", 1, "x", True),
            ("Hexagon Cost Multiplier", 1, "x", True)
        ]
        
        for i, (text, default, unit, is_float) in enumerate(sliders_config):
            self.create_slider_with_entry(frame, text, default, i + 2, unit, is_float)

    def create_item_stat_clamps_section(self):
        frame = ttk.LabelFrame(self.scrollable_frame, text="Item Stat Clamps")
        frame.grid(row=13, column=0, sticky='nsew', padx=5, pady=5)
        frame.grid_columnconfigure(1, weight=1)
        frame.grid_columnconfigure(3, weight=1)
        
        # Warning message with distinctive styling
        warning_frame = ttk.Frame(frame)
        warning_frame.grid(row=0, column=0, columnspan=4, sticky='ew', padx=5, pady=5)
        
        warning_label = tk.Label(
            warning_frame,
            text="WARNING: This will permanently change the stats of any existing items so make sure to "
                 "backup your current save before modifying and playing with the clamping values.",
            wraplength=700,
            fg='red',
            justify='left',
            font=('TkDefaultFont', 10, 'bold')
        )
        warning_label.pack(fill='x', padx=5, pady=5)
        
        # Left column stat clamps
        left_stats = [
            "Generic Quality",
            "Armor",
            "Weapon Damage Percent",
            "Hypo Insulation"
        ]
        
        # Right column stat clamps
        right_stats = [
            "Weight",
            "Max Durability",
            "Weapon Clip Ammo",
            "Hyper Insulation"
        ]
        
        def create_stat_clamp(parent, text, row, base_column):
            # Checkbox
            var = tk.BooleanVar()
            self.variables[f"{text}_enabled"] = var
            cb = ttk.Checkbutton(parent, variable=var)
            cb.grid(row=row, column=base_column, padx=(5, 0), pady=2)
            
            # Slider and Entry combination
            frame = ttk.Frame(parent)
            frame.grid(row=row, column=base_column + 1, sticky='ew', padx=5, pady=2)
            frame.grid_columnconfigure(0, weight=1)
            
            # Label
            label = ttk.Label(frame, text=text)
            label.grid(row=0, column=0, sticky='w', padx=(0, 5))
            
            # Slider
            slider_var = tk.DoubleVar(value=0)
            slider = ttk.Scale(frame, from_=0, to=100, variable=slider_var, orient='horizontal')
            slider.grid(row=0, column=1, sticky='ew', padx=5)
            
            # Entry
            entry_var = tk.StringVar(value="0")
            entry = ttk.Entry(frame, textvariable=entry_var, width=10)
            entry.grid(row=0, column=2, padx=(5, 0))
            
            self.slider_values[text] = (slider_var, entry_var)
        
        # Create left column stats
        for i, stat in enumerate(left_stats):
            create_stat_clamp(frame, stat, i + 1, 0)
        
        # Create right column stats
        for i, stat in enumerate(right_stats):
            create_stat_clamp(frame, stat, i + 1, 2)

        if __name__ == "__main__":
            root = tk.Tk()
            root.geometry("800x600")
            app = RulesContent(root)
            app.pack(fill="both", expand=True)
            root.mainloop()

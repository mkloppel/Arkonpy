import tkinter as tk
from tkinter import ttk, BooleanVar, DoubleVar, StringVar, IntVar
import re
from scrollable_frame import ScrollableFrameMixin

# Simple Tooltip class
class Tooltip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event=None):
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25

        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")

        label = tk.Label(self.tooltip, text=self.text, background="#ffffe0", relief="solid", borderwidth=1,
                         wraplength=300, justify="left")
        label.pack(ipadx=1)

    def hide_tooltip(self, event=None):
        if self.tooltip:
            self.tooltip.destroy()
        self.tooltip = None

class RulesContent(ttk.Frame, ScrollableFrameMixin):
    # Map UI Labels/Keys to INI Setting Names and Sections
    # Format: "UI Key": ("INI Setting Name", "Section", "Type", DefaultValue, InvertLogic)
    # Section is usually 'GameUserSettings' -> '[ServerSettings]' or 'Game' -> '[/Script/ShooterGame.ShooterGameMode]'
    # Type: bool, float, int, str
    # InvertLogic: True if UI checkbox checked means INI setting is False
    # Defaults are based on jsons/ServerSettings.json where available
    SETTING_MAP = {
        # General Rules - Checkboxes
        "Enable Hardcore Mode": ("ServerHardcore", "GameUserSettings", "bool", False, False),
        "Enable PvP": ("serverPVE", "GameUserSettings", "bool", False, True), # Checked = PvP = serverPVE=False
        "Disable PvE Friendly Fire": ("bDisableFriendlyFire", "GameUserSettings", "bool", False, False), # Not in JSON
        "Enable PvE Cave Building": ("AllowCaveBuildingPvE", "GameUserSettings", "bool", False, False),
        "Prevent Building in Resource Rich Areas": ("EnableExtraStructurePreventionVolumes", "GameUserSettings", "bool", False, False), # Checked = Prevent = Enable=True
        "Enable PvE Cryo Sickness": ("EnableCryoSicknessPVE", "GameUserSettings", "bool", False, False),
        "Disable PvP Friendly Fire": ("bDisableFriendlyFire", "GameUserSettings", "bool", False, False), # Not in JSON (Assuming same as PvE)
        "Disable Supply Crates": ("bDisableLootCrates", "GameUserSettings", "bool", False, False), # Not in JSON
        "Random Supply Crate Points": ("RandomSupplyCratePoints", "GameUserSettings", "bool", False, False),
        "Use Corpse Locator": ("bUseCorpseLocator", "GameUserSettings", "bool", True, False), # Not in JSON
        "Allow Platform Saddle Multi Floors": ("bAllowPlatformSaddleMultiFloors", "GameUserSettings", "bool", True, False), # Not in JSON
        # "Enable Difficulty Override": - Handled by DifficultyOffset slider
        "Disable Non-Meat Fish Loot": ("bDisableFishLoot", "GameUserSettings", "bool", False, False), # Not in JSON

        # General Rules - Sliders
        "Supply Crate Loot Quality Multiplier": ("SupplyCrateLootQualityMultiplier", "GameUserSettings", "float", 1.0, False), # Not in JSON
        "Fishing Loot Quality Multiplier": ("FishingLootQualityMultiplier", "GameUserSettings", "float", 1.0, False), # Not in JSON
        "Platform Saddle Build Area Bounds Multiplier": ("PlatformSaddleBuildAreaBoundsMultiplier", "GameUserSettings", "float", 1.0, False),
        "Max Gateways on Saddles": ("MaxGateFrameOnSaddles", "GameUserSettings", "int", 0, False),
        # "Max Dino Level": - Determined by DifficultyOffset
        "Difficulty Offset": ("DifficultyOffset", "GameUserSettings", "float", 1.0, False),

        # Downloads - Checkboxes (Many need inverted logic)
        "Allow Foreign Dino Downloads": ("PreventDownloadDinos", "GameUserSettings", "bool", False, True), # Checked = Allow = Prevent=False
        "Allow Item Downloads": ("PreventDownloadItems", "GameUserSettings", "bool", False, True), # Checked = Allow = Prevent=False
        "Allow Survivor Downloads": ("PreventDownloadSurvivors", "GameUserSettings", "bool", False, True), # Checked = Allow = Prevent=False
        "Allow Foreign Item Downloads": ("PreventUploadItems", "GameUserSettings", "bool", False, True), # Checked = Allow = Prevent=False (Uses PreventUploadItems)
        "Allow Foreign Survivor Downloads": ("PreventUploadSurvivors", "GameUserSettings", "bool", False, True), # Checked = Allow = Prevent=False (Uses PreventUploadSurvivors)
        "Prevent Download Dino Classes": ("PreventDownloadDinos", "GameUserSettings", "bool", False, False), # Direct mapping
        "Prevent Download Item Classes": ("PreventDownloadItems", "GameUserSettings", "bool", False, False), # Direct mapping
        "Prevent Upload Dino Classes": ("PreventUploadDinos", "GameUserSettings", "bool", False, False), # Direct mapping

        # Tribute Options - Checkboxes
        "No Survivor Uploads": ("PreventUploadSurvivors", "GameUserSettings", "bool", False, False),
        "No Item Uploads": ("PreventUploadItems", "GameUserSettings", "bool", False, False),
        "No Dino Uploads": ("PreventUploadDinos", "GameUserSettings", "bool", False, False),

        # Tribute Options - Sliders
        "Max Tribute Dinos": ("MaxTributeDinos", "GameUserSettings", "int", 20, False),
        "Max Tribute Items": ("MaxTributeItems", "GameUserSettings", "int", 50, False),

        # Cluster Tribute Options - Checkboxes
        "No Transfer from Filtering": ("noTributeDownloads", "GameUserSettings", "bool", False, False),
        "Increase PvP Respawn Interval": ("bIncreasePvPRespawnInterval", "GameUserSettings", "bool", False, False), # Not in JSON
        "Prevent Offline PvP": ("PreventOfflinePvP", "GameUserSettings", "bool", False, False),
        # "PvE Schedule": - Handled separately below

        # Cluster Tribute Options - Sliders (Unit conversion deferred)
        "Override Survivor Upload Expiration": ("TributeCharacterExpirationSeconds", "GameUserSettings", "int", 0, False), # Seconds
        "Override Item Upload Expiration": ("TributeItemExpirationSeconds", "GameUserSettings", "int", 86400, False), # Seconds
        "Override Dino Upload Expiration": ("TributeDinoExpirationSeconds", "GameUserSettings", "int", 86400, False), # Seconds
        "Override Minimum Dino Re-upload Interval": ("MinimumDinoReuploadInterval", "GameUserSettings", "float", 0.0, False), # Seconds
        "Interval Check Period": ("PreventOfflinePvPInterval", "GameUserSettings", "float", 0.0, False), # seconds
        "Interval Multiplier": ("PvPRespawnIntervalMultiplier", "GameUserSettings", "float", 1.0, False), # Not in JSON
        "Interval Base Amount": ("PvPRespawnIntervalBaseAmount", "GameUserSettings", "float", 60.0, False), # Not in JSON
        "Logout Interval": ("KickIdlePlayersPeriod", "GameUserSettings", "float", 3600.0, False), # seconds
        "Connection Invincible Interval": ("PlayerDefaultSpawnInvincibleTime", "GameUserSettings", "float", 5.0, False), # Not in JSON

        # PvE Schedule
        "PvE Schedule": ("UsePvESchedule", "Internal", "bool", False, False), # Internal flag to enable/disable times
        "Use Server Time": ("UseServerTimeForPvE", "Internal", "bool", False, False), # Internal flag
        "Start Time:": ("PvEStartTime", "GameUserSettings", "str", "00:00", False), # Not in JSON
        "Stop Time:": ("PvEStopTime", "GameUserSettings", "str", "00:00", False), # Not in JSON

        # Tribe Settings - Checkboxes
        "Allow Tribe Alliances": ("PreventTribeAlliances", "GameUserSettings", "bool", False, True), # Checked = Allow = Prevent=False

        # Tribe Settings - Sliders
        "Max Players in Tribe": ("MaxPlayersInTribe", "GameUserSettings", "int", 70, False), # Not in JSON
        "Tribe Name Change Cooldown": ("TribeNameChangeCooldown", "GameUserSettings", "float", 15.0, False), # minutes
        "Tribe Slot Reuse Cooldown": ("TribeSlotReuseCooldown", "GameUserSettings", "float", 0.0, False), # Not in JSON
        "Max Alliances Per Tribe": ("MaxAlliancesPerTribe", "GameUserSettings", "int", 10, False), # Not in JSON
        "Max Tribes Per Alliance": ("MaxTribesPerAlliance", "GameUserSettings", "int", 10, False), # Not in JSON

        # PvE "Tribe Warfare" Options - Checkboxes
        "Allow Tribe Warfare": ("bAllowTribeWarfare", "GameUserSettings", "bool", False, False), # Not in JSON
        "Allow Cancelling Tribe Warfare": ("bAllowCancelTribeWarfare", "GameUserSettings", "bool", False, False), # Not in JSON
        "Allow Custom Recipes": ("bAllowCustomRecipes", "GameUserSettings", "bool", True, False), # Not in JSON

        # PvE "Tribe Warfare" Options - Sliders
        "Effectiveness Multiplier": ("CraftingSkillBonusMultiplier", "GameUserSettings", "float", 1.0, False), # Not in JSON
        "Skill Multiplier": ("CustomRecipeSkillMultiplier", "GameUserSettings", "float", 1.0, False), # Not in JSON

        # Disease and Network Settings - Checkboxes
        "Enable Diseases": ("PreventDiseases", "GameUserSettings", "bool", False, True), # Checked = Enable = Prevent=False
        "Non Permanent Diseases": ("NonPermanentDiseases", "GameUserSettings", "bool", False, False),
        "Override NPC Network Stasis Range Scale": ("UseNPCNetworkStasisScaling", "Internal", "bool", False, False), # Internal flag

        # Disease and Network Settings - Sliders
        "Online Player Count Start": ("NPCNetworkStasisRangeScalePlayerCountStart", "GameUserSettings", "int", 0, False),
        "Online Player Count End": ("NPCNetworkStasisRangeScalePlayerCountEnd", "GameUserSettings", "int", 0, False),
        "Scale Maximum": ("NPCNetworkStasisRangeScalePercentEnd", "GameUserSettings", "float", 0.55, False), # 0.0-1.0

        # Game Mechanics Multipliers - Sliders
        "Oxygen Swim Speed Stat Multiplier": ("OxygenSwimSpeedStatMultiplier", "GameUserSettings", "float", 1.0, False),
        "Use Corpse Life Span Multiplier": ("GlobalCorpseDecompositionTimeMultiplier", "GameUserSettings", "float", 1.0, False), # Not in JSON
        "Global Powered Battery Durability": ("GlobalPoweredBatteryDurabilityDecreaseMultiplier", "GameUserSettings", "float", 4.0, False), # Not in JSON
        "Fuel Consumption Interval Multiplier": ("FuelConsumptionIntervalMultiplier", "GameUserSettings", "float", 1.0, False), # Not in JSON
        "Limit Non Player Dropped Items Range": ("MaxNonPlayerDroppedItemsRange", "GameUserSettings", "int", 0, False), # Not in JSON
        "Limit Non Player Dropped Items Count": ("MaxNonPlayerDroppedItemsCount", "GameUserSettings", "int", 0, False), # Not in JSON

        # Cryopod Settings - Checkboxes
        "Enable Cryopod Nerf": ("EnableCryopodNerf", "GameUserSettings", "bool", False, False),

        # Cryopod Settings - Sliders
        "Duration": ("CryopodNerfDuration", "GameUserSettings", "float", 0.0, False), # seconds
        "Outgoing Damage Multiplier": ("CryopodNerfDamageMult", "GameUserSettings", "float", 0.01, False), # Default ~0.01
        "Incoming Damage Multiplier Percent": ("CryopodNerfIncomingDamageMultPercent", "GameUserSettings", "float", 0.0, False), # 0.0-1.0?

        # Genesis: Part 1 - Checkboxes
        "Disable Missions": ("bDisableGenesisMissions", "GameUserSettings", "bool", False, False), # Not in JSON
        "Allow TEK Suit Powers": ("AllowTekSuitPowersInGenesis", "GameUserSettings", "bool", False, False),

        # Genesis: Part 2 - Checkboxes
        "Disable TEK Suit on Spawn": ("DisableGenesis2TekSuitOnSpawn", "GameUserSettings", "bool", False, False), # Not in JSON
        "Disable World Buffs": ("DisableWorldBuffs", "GameUserSettings", "bool", False, False), # Not in JSON
        "Enable World Buff Scaling": ("EnableWorldBuffScaling", "GameUserSettings", "bool", False, False), # Not in JSON

        # Genesis: Part 2 - Sliders
        "World Buff Scaling Efficacy": ("WorldBuffScalingEfficacy", "GameUserSettings", "float", 1.0, False), # Not in JSON

        # Hexagons - Checkboxes
        "Disable Hexagon Store": ("bDisableHexagonStore", "GameUserSettings", "bool", False, False), # Not in JSON
        "Allow Only Engram Points Trade": ("bAllowOnlyEngramPointTrade", "GameUserSettings", "bool", False, False), # Not in JSON

        # Hexagons - Sliders
        "Max Hexagons per Character": ("MaxHexagonsPerCharacter", "GameUserSettings", "int", 2000000000, False),
        "Hexagon Reward Multiplier": ("HexagonRewardMultiplier", "GameUserSettings", "float", 1.0, False), # Not in JSON
        "Hexagon Cost Multiplier": ("HexagonCostMultiplier", "GameUserSettings", "float", 1.0, False), # Not in JSON

        # Item Stat Clamps - Deferred for now due to complexity (Game.ini)
    }

    def __init__(self, parent, profile, config_manager):
        super().__init__(parent)
        self.profile = profile
        self.config_manager = config_manager

        # Store tk variables for widgets
        self.widget_vars = {} # Maps UI Key -> tk.Variable
        self.widget_map = {} # Maps UI Key -> widget instance

        self.create_frames()
        self._load_settings()
        self._setup_bindings_and_tooltips()

    def create_frames(self):
        # Create main scrollable container
        self.canvas = tk.Canvas(self, borderwidth=0, background="#ffffff")
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

        # Create all sections within the scrollable_frame
        self.create_general_rules(self.scrollable_frame)
        self.create_downloads_section(self.scrollable_frame) # Added this line back
        self.create_tribute_section(self.scrollable_frame)
        self.create_cluster_options_section(self.scrollable_frame)
        self.create_pve_schedule_section(self.scrollable_frame)
        self.create_tribe_settings_section(self.scrollable_frame)
        self.create_tribe_warfare_section(self.scrollable_frame)
        self.create_disease_network_section(self.scrollable_frame)
        self.create_game_mechanics_section(self.scrollable_frame)
        self.create_cryopod_section(self.scrollable_frame)
        self.create_genesis_sections(self.scrollable_frame)
        self.create_hexagons_section(self.scrollable_frame)
        # self.create_item_stat_clamps_section(self.scrollable_frame) # Deferred

        # Grid layout for canvas and scrollbar
        self.canvas.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    # --- Helper Methods for Creating Widgets ---

    def _create_widget_var(self, ui_key):
        """Creates the appropriate tk.Variable based on SETTING_MAP"""
        if ui_key not in self.SETTING_MAP:
            print(f"Warning: UI Key '{ui_key}' not found in SETTING_MAP.")
            return None
        _, _, var_type, default, _ = self.SETTING_MAP[ui_key]
        if var_type == "bool":
            var = BooleanVar(value=default)
        elif var_type == "float":
            var = DoubleVar(value=float(default))
        elif var_type == "int":
            var = IntVar(value=int(default))
        elif var_type == "str":
            var = StringVar(value=str(default))
        else:
            print(f"Warning: Unknown var_type '{var_type}' for UI Key '{ui_key}'.")
            return None
        self.widget_vars[ui_key] = var
        return var

    def create_labeled_checkbox(self, parent, ui_key, row, column, columnspan=1):
        """Creates a checkbox linked to a tk.BooleanVar"""
        var = self._create_widget_var(ui_key)
        if var is None: return None # Handle missing mapping

        cb = ttk.Checkbutton(parent, text=ui_key, variable=var)
        cb.grid(row=row, column=column, columnspan=columnspan, sticky='w', padx=5, pady=2)
        self.widget_map[ui_key] = cb # Store widget instance
        return cb

    def create_slider_with_entry(self, parent, ui_key, unit=""):
        """Creates a slider/entry combo linked to a tk.DoubleVar or tk.IntVar"""
        if ui_key not in self.SETTING_MAP:
             print(f"Warning: UI Key '{ui_key}' not found in SETTING_MAP.")
             return None, None, None
        _, _, var_type, default, _ = self.SETTING_MAP[ui_key]
        is_float = (var_type == "float")

        var = self._create_widget_var(ui_key)
        if var is None: return None, None, None # Handle missing mapping

        frame = ttk.Frame(parent)
        # Removed frame.grid here, should be handled by caller

        label = ttk.Label(frame, text=ui_key)
        label.grid(row=0, column=0, padx=5, sticky='w')

        # Determine slider range - needs refinement based on setting
        min_val = 0
        max_val = 10.0 if is_float else 1000 # Default ranges, adjust as needed per setting
        if ui_key == "Difficulty Offset": max_val = 10.0 # Example specific range
        if ui_key == "Max Gateways on Saddles": max_val = 10
        if ui_key == "Max Players in Tribe": max_val = 100
        if ui_key == "Max Tribute Dinos": max_val = 200
        if ui_key == "Max Tribute Items": max_val = 200
        # ... add more specific ranges ...

        slider = ttk.Scale(frame, from_=min_val, to=max_val, variable=var, orient='horizontal',
                           command=lambda v, k=ui_key: self._update_entry_from_slider(k))
        slider.grid(row=0, column=1, padx=5, sticky='ew')

        entry = ttk.Entry(frame, textvariable=var, width=10)
        entry.grid(row=0, column=2, padx=5)
        # Add validation/binding to update slider from entry later if needed

        if unit:
            unit_label = ttk.Label(frame, text=unit)
            unit_label.grid(row=0, column=3, padx=5, sticky='w')

        self.widget_map[ui_key] = frame # Store frame containing slider/entry
        # Store individual components if needed for fine-grained control
        self.widget_map[f"{ui_key}_slider"] = slider
        self.widget_map[f"{ui_key}_entry"] = entry

        return frame, slider, entry

    def _update_entry_from_slider(self, ui_key):
        """Callback to update entry when slider moves."""
        if ui_key in self.widget_vars:
            # Formatting might be needed, especially for floats
            # self.widget_vars[ui_key].set(round(self.widget_vars[ui_key].get(), 2)) # Example rounding
            pass # Tkinter variable linking handles this automatically

    def create_time_input(self, parent, ui_key, row, column):
        """Creates a validated time entry field"""
        var = self._create_widget_var(ui_key)
        if var is None: return None # Handle missing mapping

        def validate_time(P):
            if P == "": return True
            return bool(re.match(r'^([01]?[0-9]|2[0-3]):[0-5][0-9]$', P))

        label = ttk.Label(parent, text=ui_key)
        label.grid(row=row, column=column, padx=5, pady=2, sticky='w')

        vcmd = (parent.register(validate_time), '%P')
        entry = ttk.Entry(parent, textvariable=var, width=10, validate='key', validatecommand=vcmd)
        entry.grid(row=row, column=column + 1, padx=5, pady=2, sticky='w')
        self.widget_map[ui_key] = entry # Store widget instance
        return entry

    # --- Section Creation Methods (Pass parent frame) ---

    def create_general_rules(self, parent):
        frame = ttk.LabelFrame(parent, text="General Rules")
        frame.grid(row=0, column=0, sticky='nsew', padx=10, pady=5, ipady=5)
        frame.grid_columnconfigure(1, weight=1)

        label = ttk.Label(frame, text=text)
        label.grid(row=0, column=0, padx=5, sticky='w')

        slider_var = tk.DoubleVar(value=float(default_value))
        slider = ttk.Scale(frame, from_=0, to=100 if float_type else 1000,
                         variable=slider_var, orient='horizontal')
        slider.grid(row=0, column=1, padx=5, sticky='ew')

        entry_var = tk.StringVar(value=str(default_value))
        entry = ttk.Entry(frame, textvariable=entry_var, width=10)
        entry.grid(row=0, column=2, padx=5)

        if unit:
            unit_label = ttk.Label(frame, text=unit)
            unit_label.grid(row=0, column=3, padx=5, sticky='w')

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
            "Enable PvE Cryo Sickness",
            "Disable PvP Friendly Fire", # Duplicates PvE?
            "Disable Supply Crates",
            "Random Supply Crate Points",
        ]
        right_checkboxes = [
            "Use Corpse Locator",
            "Allow Platform Saddle Multi Floors",
            # "Enable Difficulty Override", # Handled by slider
            "Disable Non-Meat Fish Loot",
        ]

        row_offset = 0
        for i, key in enumerate(left_checkboxes):
            self.create_labeled_checkbox(frame, key, i + row_offset, 0)
        for i, key in enumerate(right_checkboxes):
            self.create_labeled_checkbox(frame, key, i + row_offset, 2)

        # Sliders
        slider_keys = [
            "Supply Crate Loot Quality Multiplier",
            "Fishing Loot Quality Multiplier",
            "Platform Saddle Build Area Bounds Multiplier",
            "Max Gateways on Saddles",
            # "Max Dino Level", # Handled by Difficulty Offset
            "Difficulty Offset",
        ]
        slider_units = ["x", "x", "x", "", "", ""] # Match slider_keys

        row_offset = max(len(left_checkboxes), len(right_checkboxes))
        for i, key in enumerate(slider_keys):
            slider_frame, _, _ = self.create_slider_with_entry(frame, key, unit=slider_units[i])
            if slider_frame:
                slider_frame.grid(row=i + row_offset, column=0, columnspan=4, sticky='ew', padx=5, pady=2)
                slider_frame.grid_columnconfigure(1, weight=1) # Make slider expand

    def create_downloads_section(self, parent):
        frame = ttk.LabelFrame(parent, text="Downloads")
        frame.grid(row=1, column=0, sticky='nsew', padx=10, pady=5, ipady=5)
        frame.grid_columnconfigure(1, weight=1) # Allow space between columns
        left_checkboxes = [
            "Allow Foreign Dino Downloads",
            "Allow Item Downloads",
            "Allow Survivor Downloads",
            "Allow Item Downloads",
            "Allow Survivor Downloads",
            "Allow Foreign Item Downloads",
        ]
        right_checkboxes = [
            "Allow Foreign Survivor Downloads",
            # --- Direct Prevention --- (Maybe group these?)
            "Prevent Download Dino Classes",
            "Prevent Download Item Classes",
            "Prevent Upload Dino Classes", # Should be PreventUploadDinos? Check SETTING_MAP
        ]

        for i, key in enumerate(left_checkboxes):
            self.create_labeled_checkbox(frame, key, i, 0)
        for i, key in enumerate(right_checkboxes):
            self.create_labeled_checkbox(frame, key, i, 2)

    def create_tribute_section(self, parent):
        frame = ttk.LabelFrame(parent, text="Tribute Options")
        frame.grid(row=2, column=0, sticky='nsew', padx=10, pady=5, ipady=5)
        frame.grid_columnconfigure(1, weight=1)
        checkboxes = [
            "No Survivor Uploads",
            "No Item Uploads",
            "No Item Uploads",
            "No Dino Uploads",
        ]
        for i, key in enumerate(checkboxes):
            self.create_labeled_checkbox(frame, key, i, 0)

        # Sliders
        slider_keys = ["Max Tribute Dinos", "Max Tribute Items"]
        slider_units = ["dinos", "items"]
        row_offset = len(checkboxes)
        for i, key in enumerate(slider_keys):
            slider_frame, _, _ = self.create_slider_with_entry(frame, key, unit=slider_units[i])
            if slider_frame:
                slider_frame.grid(row=i + row_offset, column=0, columnspan=3, sticky='ew', padx=5, pady=2)
                slider_frame.grid_columnconfigure(1, weight=1)

    def create_cluster_options_section(self, parent):
        frame = ttk.LabelFrame(parent, text="Cluster Tribute Options")
        frame.grid(row=3, column=0, sticky='nsew', padx=10, pady=5, ipady=5)
        frame.grid_columnconfigure(1, weight=1)
        checkboxes = [
            "No Transfer from Filtering",
            "Increase PvP Respawn Interval",
            "Prevent Offline PvP",
            # "PvE Schedule" # Handled in its own section
        ]
        for i, key in enumerate(checkboxes):
            self.create_labeled_checkbox(frame, key, i, 0)

        # Sliders
        slider_keys = [
            "Override Survivor Upload Expiration", "Override Item Upload Expiration",
            "Override Dino Upload Expiration", "Override Minimum Dino Re-upload Interval",
            "Interval Check Period", "Interval Multiplier", "Interval Base Amount",
            "Logout Interval", "Connection Invincible Interval"
        ]
        slider_units = ["seconds", "seconds", "seconds", "seconds", "seconds", "x", "seconds", "seconds", "seconds"] # Adjusted units

        row_offset = len(checkboxes)
        for i, key in enumerate(slider_keys):
            slider_frame, _, _ = self.create_slider_with_entry(frame, key, unit=slider_units[i])
            if slider_frame:
                slider_frame.grid(row=i + row_offset, column=0, columnspan=3, sticky='ew', padx=5, pady=2)
                slider_frame.grid_columnconfigure(1, weight=1)

    def create_pve_schedule_section(self, parent):
        frame = ttk.LabelFrame(parent, text="PvE Schedule")
        frame.grid(row=4, column=0, sticky='nsew', padx=10, pady=5, ipady=5)
        frame.grid_columnconfigure(1, weight=1) # Space for time entries

        self.create_labeled_checkbox(frame, "PvE Schedule", 0, 0)
        self.create_labeled_checkbox(frame, "Use Server Time", 1, 0) # UI Only?

        self.create_time_input(frame, "Start Time:", 2, 0)
        self.create_time_input(frame, "Stop Time:", 3, 0) # Separate rows for clarity

    def create_tribe_settings_section(self, parent):
        frame = ttk.LabelFrame(parent, text="Tribe Settings")
        frame.grid(row=5, column=0, sticky='nsew', padx=10, pady=5, ipady=5)
        frame.grid_columnconfigure(1, weight=1)

        self.create_labeled_checkbox(frame, "Allow Tribe Alliances", 0, 0)

        # Sliders
        slider_keys = [
            "Max Players in Tribe", "Tribe Name Change Cooldown", "Tribe Slot Reuse Cooldown",
            "Max Alliances Per Tribe", "Max Tribes Per Alliance"
        ]
        slider_units = ["players", "minutes", "minutes", "", ""]

        row_offset = 1 # After checkbox
        for i, key in enumerate(slider_keys):
            slider_frame, _, _ = self.create_slider_with_entry(frame, key, unit=slider_units[i])
            if slider_frame:
                slider_frame.grid(row=i + row_offset, column=0, columnspan=3, sticky='ew', padx=5, pady=2)
                slider_frame.grid_columnconfigure(1, weight=1)

    def create_tribe_warfare_section(self, parent):
        frame = ttk.LabelFrame(parent, text='PvE "Tribe Warfare" Options')
        frame.grid(row=6, column=0, sticky='nsew', padx=10, pady=5, ipady=5)
        frame.grid_columnconfigure(1, weight=1)

        checkboxes = [
            "Allow Tribe Warfare", "Allow Cancelling Tribe Warfare", "Allow Custom Recipes"
        ]
        for i, key in enumerate(checkboxes):
            self.create_labeled_checkbox(frame, key, i, 0)

        # Sliders
        slider_keys = ["Effectiveness Multiplier", "Skill Multiplier"]
        slider_units = ["x", "x"]
        row_offset = len(checkboxes)
        for i, key in enumerate(slider_keys):
            slider_frame, _, _ = self.create_slider_with_entry(frame, key, unit=slider_units[i])
            if slider_frame:
                slider_frame.grid(row=i + row_offset, column=0, columnspan=3, sticky='ew', padx=5, pady=2)
                slider_frame.grid_columnconfigure(1, weight=1)

    def create_disease_network_section(self, parent):
        frame = ttk.LabelFrame(parent, text="Disease and Network Settings")
        frame.grid(row=7, column=0, sticky='nsew', padx=10, pady=5, ipady=5)
        frame.grid_columnconfigure(1, weight=1)

        checkboxes = [
            "Enable Diseases", "Non Permanent Diseases", "Override NPC Network Stasis Range Scale"
        ]
        for i, key in enumerate(checkboxes):
            self.create_labeled_checkbox(frame, key, i, 0)

        # Sliders
        slider_keys = ["Online Player Count Start", "Online Player Count End", "Scale Maximum"]
        slider_units = ["players", "players", "%"]
        row_offset = len(checkboxes)
        for i, key in enumerate(slider_keys):
            slider_frame, _, _ = self.create_slider_with_entry(frame, key, unit=slider_units[i])
            if slider_frame:
                slider_frame.grid(row=i + row_offset, column=0, columnspan=3, sticky='ew', padx=5, pady=2)
                slider_frame.grid_columnconfigure(1, weight=1)

    def create_game_mechanics_section(self, parent):
        frame = ttk.LabelFrame(parent, text="Game Mechanics Multipliers")
        frame.grid(row=8, column=0, sticky='nsew', padx=10, pady=5, ipady=5)
        frame.grid_columnconfigure(1, weight=1)

        # Sliders Only
        slider_keys = [
            "Oxygen Swim Speed Stat Multiplier", "Use Corpse Life Span Multiplier",
            "Global Powered Battery Durability", "Fuel Consumption Interval Multiplier",
            "Limit Non Player Dropped Items Range", "Limit Non Player Dropped Items Count"
        ]
        slider_units = ["x", "x", "x", "x", "items", "items"]
        for i, key in enumerate(slider_keys):
            slider_frame, _, _ = self.create_slider_with_entry(frame, key, unit=slider_units[i])
            if slider_frame:
                slider_frame.grid(row=i, column=0, columnspan=3, sticky='ew', padx=5, pady=2)
                slider_frame.grid_columnconfigure(1, weight=1)

    def create_cryopod_section(self, parent):
        frame = ttk.LabelFrame(parent, text="Cryopod Settings")
        frame.grid(row=9, column=0, sticky='nsew', padx=10, pady=5, ipady=5)
        frame.grid_columnconfigure(1, weight=1)

        self.create_labeled_checkbox(frame, "Enable Cryopod Nerf", 0, 0)

        # Sliders
        slider_keys = ["Duration", "Outgoing Damage Multiplier", "Incoming Damage Multiplier Percent"]
        slider_units = ["seconds", "x", "%"]
        row_offset = 1 # After checkbox
        for i, key in enumerate(slider_keys):
            slider_frame, _, _ = self.create_slider_with_entry(frame, key, unit=slider_units[i])
            if slider_frame:
                slider_frame.grid(row=i + row_offset, column=0, columnspan=3, sticky='ew', padx=5, pady=2)
                slider_frame.grid_columnconfigure(1, weight=1)

    def create_genesis_sections(self, parent):
        # Genesis Part 1
        frame1 = ttk.LabelFrame(parent, text="Genesis: Part 1")
        frame1.grid(row=10, column=0, sticky='nsew', padx=10, pady=5, ipady=5)
        frame1.grid_columnconfigure(1, weight=1) # Allow spacing

        self.create_labeled_checkbox(frame1, "Disable Missions", 0, 0)
        self.create_labeled_checkbox(frame1, "Allow TEK Suit Powers", 0, 1)

        # Genesis Part 2
        frame2 = ttk.LabelFrame(parent, text="Genesis: Part 2")
        frame2.grid(row=11, column=0, sticky='nsew', padx=10, pady=5, ipady=5)
        frame2.grid_columnconfigure(1, weight=1)

        checkboxes = [
            "Disable TEK Suit on Spawn", "Disable World Buffs", "Enable World Buff Scaling"
        ]
        for i, key in enumerate(checkboxes):
            self.create_labeled_checkbox(frame2, key, i, 0)

        # Slider
        slider_key = "World Buff Scaling Efficacy"
        slider_unit = "x"
        row_offset = len(checkboxes)
        slider_frame, _, _ = self.create_slider_with_entry(frame2, slider_key, unit=slider_unit)
        if slider_frame:
            slider_frame.grid(row=row_offset, column=0, columnspan=3, sticky='ew', padx=5, pady=2)
            slider_frame.grid_columnconfigure(1, weight=1)

    def create_hexagons_section(self, parent):
        frame = ttk.LabelFrame(parent, text="Hexagons")
        frame.grid(row=12, column=0, sticky='nsew', padx=10, pady=5, ipady=5)
        frame.grid_columnconfigure(1, weight=1)

        self.create_labeled_checkbox(frame, "Disable Hexagon Store", 0, 0)
        self.create_labeled_checkbox(frame, "Allow Only Engram Points Trade", 1, 0)

        # Sliders
        slider_keys = ["Max Hexagons per Character", "Hexagon Reward Multiplier", "Hexagon Cost Multiplier"]
        slider_units = ["", "x", "x"]
        row_offset = 2 # After checkboxes
        for i, key in enumerate(slider_keys):
            slider_frame, _, _ = self.create_slider_with_entry(frame, key, unit=slider_units[i])
            if slider_frame:
                slider_frame.grid(row=i + row_offset, column=0, columnspan=3, sticky='ew', padx=5, pady=2)
                slider_frame.grid_columnconfigure(1, weight=1)

    def create_item_stat_clamps_section(self, parent):
        # Deferred implementation
        frame = ttk.LabelFrame(parent, text="Item Stat Clamps (Deferred)")
        frame.grid(row=13, column=0, sticky='nsew', padx=10, pady=5, ipady=5)
        # frame.grid_columnconfigure(1, weight=1) # Example if needed later
        # frame.grid_columnconfigure(3, weight=1)

        # Warning message
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
        warning_label.grid(row=0, column=0, sticky='w', padx=5, pady=5)
        
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
            clamp_frame = ttk.Frame(parent)
            clamp_frame.grid(row=row, column=base_column + 1, sticky='ew', padx=5, pady=2)
            clamp_frame.grid_columnconfigure(1, weight=1)
            
            # Label
            label = ttk.Label(clamp_frame, text=text)
            label.grid(row=0, column=0, sticky='w', padx=(0, 5))
            
            # Slider
            slider_var = tk.DoubleVar(value=0)
            slider = ttk.Scale(clamp_frame, from_=0, to=100, variable=slider_var, orient='horizontal')
            slider.grid(row=0, column=1, sticky='ew', padx=5)
            
            # Entry
            entry_var = tk.StringVar(value="0")
            entry = ttk.Entry(clamp_frame, textvariable=entry_var, width=10)
            entry.grid(row=0, column=2, padx=(5, 0))
            
            self.slider_values[text] = (slider_var, entry_var)
        
        # Create left column stats
        for i, stat in enumerate(left_stats):
            # create_stat_clamp(frame, stat, i + 1, 0) # Example if needed later

        # Create right column stats
        # for i, stat in enumerate(right_stats):
            # create_stat_clamp(frame, stat, i + 1, 2) # Example if needed later
        ttk.Label(frame, text="Integration for Item Stat Clamps (Game.ini) is deferred.").grid(row=1, column=0, columnspan=4, pady=10)


    # --- Load, Save, Bindings ---

    def _load_settings(self):
        """Load settings from profile into UI widgets."""
        if not self.profile: return

        for ui_key, var in self.widget_vars.items():
            if ui_key not in self.SETTING_MAP: continue
            setting_name, section, var_type, default, invert = self.SETTING_MAP[ui_key]

            if section == "Internal": continue # Skip internal flags

            # Determine which dictionary to use
            settings_dict = self.profile.game_user_settings if section == "GameUserSettings" else self.profile.game_settings

            # Get value from profile, using default if not found
            raw_value = settings_dict.get(setting_name, default)

            # Convert raw value (usually string from INI/JSON) to tk variable type
            try:
                if var_type == "bool":
                    # Handle potential string representations of bool
                    if isinstance(raw_value, str):
                        value = raw_value.lower() == 'true'
                    else:
                        value = bool(raw_value)
                    if invert: value = not value # Apply inversion for UI
                elif var_type == "float":
                    value = float(raw_value)
                elif var_type == "int":
                    value = int(raw_value)
                elif var_type == "str":
                    value = str(raw_value)
                else:
                    value = default # Fallback for unknown types

                var.set(value)
            except (ValueError, TypeError) as e:
                print(f"Error loading setting '{setting_name}' for UI '{ui_key}': {e}. Using default: {default}")
                # Attempt to set default, converting it first if needed
                try:
                    if var_type == "bool": default_val = bool(default)
                    elif var_type == "float": default_val = float(default)
                    elif var_type == "int": default_val = int(default)
                    else: default_val = str(default)
                    var.set(default_val)
                except Exception:
                    print(f"Error setting default for {ui_key}") # Fallback if default is bad

    def _save_setting(self, ui_key, *args):
        """Callback to save a setting when its UI widget changes."""
        if not self.profile: return
        if ui_key not in self.SETTING_MAP or ui_key not in self.widget_vars: return

        setting_name, section, var_type, _, invert = self.SETTING_MAP[ui_key]
        var = self.widget_vars[ui_key]

        if section == "Internal": return # Don't save internal flags directly

        # Get value from tk variable
        value = var.get()

        # Apply inversion if necessary before saving
        if var_type == "bool" and invert:
            value = not value

        # Convert Python type to INI-compatible string/type if needed
        # Booleans are often True/False, numbers are strings
        if var_type == "bool":
            save_value = str(value) # "True" or "False"
        elif var_type == "float":
             # Format float to avoid excessive precision?
             save_value = f"{value:.6f}".rstrip('0').rstrip('.') # Clean float string
             if save_value == "" or save_value == "-": save_value = "0.0" # Handle case where value is 0 or negative 0
        elif var_type == "int":
             save_value = str(value)
        else: # String or other
             save_value = str(value)

        # Update the profile
        # print(f"Saving: {section}.{setting_name} = {save_value} (from UI: {ui_key}={var.get()})") # Debug print
        self.profile.update_setting(section, setting_name, save_value)

    def _setup_bindings_and_tooltips(self):
        """Attach save callbacks and tooltips to widgets."""
        if not self.config_manager: return # Need config manager for tooltips

        for ui_key, widget in self.widget_map.items():
            if ui_key not in self.SETTING_MAP: continue
            setting_name, section, var_type, _, _ = self.SETTING_MAP[ui_key]

            if section == "Internal": continue # No saving/tooltips for internal flags

            # --- Bind Save Callback ---
            var = self.widget_vars.get(ui_key)
            if var:
                # Use trace for variable changes
                var.trace_add("write", lambda name, index, mode, k=ui_key: self._save_setting(k))

            # --- Add Tooltip ---
            description = self.config_manager.get_setting_description(setting_name)
            if description:
                # Need to attach tooltip to the correct element (label, checkbox, frame)
                tooltip_widget = widget
                # For sliders/entries, attach to the containing frame or label if possible
                if isinstance(widget, ttk.Frame):
                     # Try finding the label within the frame
                     # Check children, find the Label
                     found_label = False
                     for child in widget.winfo_children():
                         if isinstance(child, ttk.Label) and child.cget("text") == ui_key:
                             tooltip_widget = child
                             found_label = True
                             break
                     if not found_label: # Fallback to frame if label not found
                         tooltip_widget = widget

                elif isinstance(widget, ttk.Entry) and not isinstance(widget.master, ttk.Frame):
                     # If entry is directly placed, find its label sibling? Complex. Attach to entry for now.
                     pass # Attach to entry itself

                if tooltip_widget:
                    Tooltip(tooltip_widget, f"{setting_name}\n\n{description}")


# Example main for testing (if needed)
# if __name__ == "__main__":
#     root = tk.Tk()
#     root.geometry("800x600")
#
#     # --- Mock Profile and Config Manager for testing ---
#     class MockProfile:
#         def __init__(self):
#             self.game_user_settings = {"ServerHardcore": "True", "DifficultyOffset": "2.5"}
#             self.game_settings = {}
#         def update_setting(self, section, key, value):
#             print(f"Mock Save: {section}.{key} = {value}")
#             if section == "GameUserSettings": self.game_user_settings[key] = value
#             else: self.game_settings[key] = value
#         def add_observer(self, obs): pass
#         def remove_observer(self, obs): pass
#
#     class MockConfigManager:
#         def get_setting_description(self, setting_name):
#             # Simulate finding some descriptions
#             desc_map = {
#                 "ServerHardcore": "Enables Hardcore mode.",
#                 "DifficultyOffset": "Adjusts server difficulty.",
#                 "serverPVE": "Enables Player vs Environment mode.",
#                 "AllowCaveBuildingPvE": "Allows building in caves in PvE.",
#                 "PreventDownloadDinos": "Prevents downloading dinos.",
#                 "MaxTributeDinos": "Max dinos allowed in tribute.",
#                 "PreventOfflinePvP": "Enables Offline Raid Protection.",
#                 "KickIdlePlayersPeriod": "Kicks players after idle time (seconds)."
#             }
#             return desc_map.get(setting_name, f"Missing description for {setting_name}")
#     # --- End Mock ---
#
#     mock_profile = MockProfile()
#     mock_config_manager = MockConfigManager()
#
#     app = RulesContent(root, mock_profile, mock_config_manager)
#     app.pack(fill="both", expand=True)
#     root.mainloop()

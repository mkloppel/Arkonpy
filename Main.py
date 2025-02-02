import tkinter as tk
from tkinter import ttk
from Administration_section import AdminContent
from Auto_managment import AutomaticManagement
from Rules import RulesContent
from Chatnotify import ChatNotificationsPanel
from Hudvisuals import HUDVisualsPanel
from Playersettings import PlayerSettingsPanel
from dinosetting import DinoSettingsPanel
from enviromentsection import EnvironmentPanel
from Structures import StructuresPanel
from engrams import EngramsPanel
from serverplayerlists import ServerFileDetailsPanel
from customgus import CustomSettingsPanel
from customgameini import CustomGameINIPanel
from playerdinolevelprog import LevelProgressionsPanel
from craftingoverrides import CraftingOverridesPanel

class AdminPanel:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Panel")
        
        # Set minimum window size
        self.root.minsize(800, 1200)
        
        # Configure grid weight to allow dynamic resizing
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
        # Sections list
        self.sections = [
            'Administration',
            'Automatic Management',
            'Server Details',
            'Rules',
            'Chat and Notifications',
            'HUD and Visuals',
            'Player Settings',
            'Dino Settings',
            'Environment',
            'Structures',
            'Engrams',
            'Server File Details',
            'Custom GameUserSettings.ini Settings',
            'Custom Game.ini Settings',
            'Player and Dino Level Progressions',
            'Crafting Overrides',
            'Stack Size Overrides',
            'Map Spawner Overrides'
        ]
        
        # Create enhanced header section 1
        self.header1 = ttk.Frame(root, padding="5")
        self.header1.grid(row=0, column=0, sticky="ew")
        self.header1.columnconfigure(1, weight=1)  # Make IP section expand
        
        # Left section - Version
        version_frame = ttk.Frame(self.header1)
        version_frame.grid(row=0, column=0, padx=5)
        ttk.Label(version_frame, text="Version:").pack(side=tk.LEFT)
        ttk.Button(version_frame, text="☰", width=3).pack(side=tk.LEFT, padx=5)
        
        # Center section - IP and Monitor
        ip_frame = ttk.Frame(self.header1)
        ip_frame.grid(row=0, column=1, padx=5)
        ttk.Label(ip_frame, text="My Public IP:").pack(side=tk.LEFT)
        ip_entry = ttk.Entry(ip_frame, width=15)
        ip_entry.pack(side=tk.LEFT, padx=5)
        ttk.Button(ip_frame, text="Server Monitor").pack(side=tk.LEFT, padx=5)
        
        # Right section - Task Status
        status_frame = ttk.Frame(self.header1)
        status_frame.grid(row=0, column=2, padx=5)
        
        # Auto-Backup
        backup_frame = ttk.Frame(status_frame)
        backup_frame.pack(side=tk.LEFT, padx=10)
        ttk.Label(backup_frame, text="Auto-Backup:").pack(side=tk.LEFT)
        ttk.Label(backup_frame, text="Ready", foreground="green").pack(side=tk.LEFT, padx=5)
        ttk.Button(backup_frame, text="Run", style="Green.TButton").pack(side=tk.LEFT, padx=2)
        ttk.Button(backup_frame, text="Disable").pack(side=tk.LEFT, padx=2)
        
        # Auto-Update
        update_frame = ttk.Frame(status_frame)
        update_frame.pack(side=tk.LEFT, padx=10)
        ttk.Label(update_frame, text="Auto-Update:").pack(side=tk.LEFT)
        ttk.Label(update_frame, text="Disabled", foreground="orange").pack(side=tk.LEFT, padx=5)
        ttk.Button(update_frame, text="Enable", style="Orange.TButton").pack(side=tk.LEFT, padx=2)
        
        # Discord Bot
        bot_frame = ttk.Frame(status_frame)
        bot_frame.pack(side=tk.LEFT, padx=10)
        ttk.Label(bot_frame, text="Discord Bot:").pack(side=tk.LEFT)
        ttk.Label(bot_frame, text="Disabled", foreground="orange").pack(side=tk.LEFT, padx=5)
        
        # Far right - Utility buttons
        utils_frame = ttk.Frame(self.header1)
        utils_frame.grid(row=0, column=3, padx=5)
        ttk.Button(utils_frame, text="📄").pack(side=tk.LEFT, padx=2)
        ttk.Button(utils_frame, text="🔄").pack(side=tk.LEFT, padx=2)
        ttk.Button(utils_frame, text="📊").pack(side=tk.LEFT, padx=2)
        ttk.Button(utils_frame, text="❓").pack(side=tk.LEFT, padx=2)
        
        # Configure styles for colored buttons
        style = ttk.Style()
        style.configure("Green.TButton", background="green")
        style.configure("Orange.TButton", background="orange")
        
        # Create additional header section
        self.additional_header = ttk.Frame(root, padding="10")
        self.additional_header.grid(row=1, column=0, sticky="ew")
        ttk.Label(self.additional_header, text="Additional Header Section").pack(anchor="w")
        
        # Integrate TabSystem into additional header
        self.tab_system = TabSystem(self.additional_header)
        self.tab_system.pack(fill="x")
        
        # Add ProfileSection below tabs
        self.profile_section = ProfileSection(self.additional_header)
        self.profile_section.pack(fill="x", pady=5)
        
        # Create header sections
        self.header2 = ttk.Frame(root, padding="10")
        self.header2.grid(row=2, column=0, sticky="ew")
        ttk.Label(self.header2, text="Header Section 2").pack(anchor="w")
        
        # Create paned window for adjustable sections
        self.paned = ttk.PanedWindow(root, orient="horizontal")
        self.paned.grid(row=3, column=0, sticky="nsew")
        
        # Create left sidebar frame
        self.sidebar = ttk.Frame(self.paned, padding="5")
        
        # Create sidebar listbox with scrollbar
        self.listbox_frame = ttk.Frame(self.sidebar)
        self.listbox_frame.pack(fill=tk.BOTH, expand=True)
        
        self.listbox = tk.Listbox(self.listbox_frame, width=30)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.scrollbar = ttk.Scrollbar(self.listbox_frame, orient="vertical", command=self.listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.configure(yscrollcommand=self.scrollbar.set)
        
        # Populate listbox with sections
        for section in self.sections:
            self.listbox.insert(tk.END, section)
            
        # Create main content area
        self.content = ttk.Frame(self.paned, padding="10")
        
        # Content header
        self.content_header = ttk.Label(self.content, text="Select a section", font=("", 12, "bold"))
        self.content_header.pack(anchor="w", pady=(0, 10))
        
        # Content area
        self.content_area = ttk.Frame(self.content, relief="solid", borderwidth=1)
        self.content_area.pack(fill=tk.BOTH, expand=True)
        
        # Add frames to paned window
        self.paned.add(self.sidebar, weight=0)  # weight=0 means it won't auto-expand
        self.paned.add(self.content, weight=1)  # weight=1 means it will take up extra space
        
        # Set initial sash position (adjust the 200 value to change initial sidebar width)
        self.root.update()
        self.paned.sashpos(0, 200)
        
        # Bind selection event
        self.listbox.bind('<<ListboxSelect>>', self.on_select)
        
        # Apply custom styling
        style.configure("TFrame", background="white")
        style.configure("TLabel", background="white")
        
    def on_select(self, event):
        if self.listbox.curselection():
            selection = self.listbox.get(self.listbox.curselection())
            self.content_header.configure(text=selection)
            
            # Clear previous content and unbind any scroll events
            self.root.unbind_all("<MouseWheel>")
            for widget in self.content_area.winfo_children():
                widget.destroy()
            
            # Load specific content for each section
            if selection == "Administration":
                admin_content = AdminContent(self.content_area)
                admin_content.pack(fill="both", expand=True)
            elif selection == "Automatic Management":
                auto_content = AutomaticManagement(self.content_area)
                auto_content.pack(fill="both", expand=True)
            elif selection == "Rules":
                rules_content = RulesContent(self.content_area)
                rules_content.pack(fill="both", expand=True)
            elif selection == "Chat and Notifications":
                chat_content = ChatNotificationsPanel(self.content_area)
                chat_content.pack(fill="both", expand=True)
            elif selection == "HUD and Visuals":
                hud_content = HUDVisualsPanel(self.content_area)
                hud_content.pack(fill="both", expand=True)
            elif selection == "Player Settings":
                player_content = PlayerSettingsPanel(self.content_area)
                player_content.pack(fill="both", expand=True)
            elif selection == "Dino Settings":
                dino_content = DinoSettingsPanel(self.content_area)
                dino_content.pack(fill="both", expand=True)
            elif selection == "Environment":
                env_content = EnvironmentPanel(self.content_area)
                env_content.pack(fill="both", expand=True)
            elif selection == "Structures":
                structures_content = StructuresPanel(self.content_area)
                structures_content.pack(fill="both", expand=True)
            elif selection == "Engrams":
                engrams_content = EngramsPanel(self.content_area)
                engrams_content.pack(fill="both", expand=True)
            elif selection == "Server File Details":
                server_files_content = ServerFileDetailsPanel(self.content_area)
                server_files_content.pack(fill="both", expand=True)
            elif selection == "Custom GameUserSettings.ini Settings":
                custom_gus_content = CustomSettingsPanel(self.content_area)
                custom_gus_content.pack(fill="both", expand=True)
            elif selection == "Custom Game.ini Settings":
                custom_gameini_content = CustomGameINIPanel(self.content_area)
                custom_gameini_content.pack(fill="both", expand=True)
            elif selection == "Player and Dino Level Progressions":
                level_prog_content = LevelProgressionsPanel(self.content_area)
                level_prog_content.pack(fill="both", expand=True)
            elif selection == "Crafting Overrides":
                crafting_content = CraftingOverridesPanel(self.content_area)
                crafting_content.pack(fill="both", expand=True)

class TabSystem(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        # Create notebook for tabs
        self.notebook_frame = ttk.Frame(self)
        self.notebook_frame.pack(fill="x")

        self.add_tab_button = ttk.Button(self.notebook_frame, text="+", width=3, command=self.add_new_tab)
        self.add_tab_button.pack(side="left", padx=5)

        self.notebook = ttk.Notebook(self.notebook_frame)
        self.notebook.pack(side="left", fill="x", expand=True)
        
        # Add default tab
        self.add_default_tab()
        
        self.tab_counter = 1
        
    def add_default_tab(self):
        default_tab = ttk.Frame(self.notebook)
        self.notebook.add(default_tab, text="Default Tab")
        
        # Add close button to tab
        close_button = ttk.Button(default_tab, text="×", width=2, 
                                command=lambda: self.close_tab(default_tab))
        close_button.pack(side='left', padx=2)

    def add_new_tab(self):
        self.tab_counter += 1
        new_tab = ttk.Frame(self.notebook)
        self.notebook.add(new_tab, text=f"Tab {self.tab_counter}")

        # Add close button to tab
        close_button = ttk.Button(new_tab, text="×", width=2,
                                command=lambda: self.close_tab(new_tab))
        close_button.pack(side='left', padx=2)
        
        # Select the new tab
        self.notebook.select(new_tab)
        
    def close_tab(self, tab):
        # Don't close if it's the last tab
        if self.notebook.index('end') > 1:
            self.notebook.forget(tab)

class ProfileSection(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.setup_grid()
        self.create_profile_row()
        self.create_version_row()
        self.create_location_row()
        self.create_status_row()
        
    def setup_grid(self):
        for i in range(4):
            self.grid_rowconfigure(i, weight=1)
        self.grid_columnconfigure(1, weight=1)  # Make middle column expandable
        
    def create_profile_row(self):
        # Profile label and entry
        ttk.Label(self, text="Profile:").grid(row=0, column=0, padx=5, sticky='w')
        profile_entry = ttk.Entry(self)
        profile_entry.insert(0, "Unnamed Profile")
        profile_entry.grid(row=0, column=1, sticky='ew', padx=5)
        
        # Right-side buttons
        buttons_frame = ttk.Frame(self)
        buttons_frame.grid(row=0, column=2, sticky='e')
        
        ttk.Button(buttons_frame, text="Create Support Zip").pack(side='left', padx=2)
        ttk.Button(buttons_frame, text="Sync").pack(side='left', padx=2)
        ttk.Button(buttons_frame, text="Import").pack(side='left', padx=2)
        ttk.Button(buttons_frame, text="Save").pack(side='left', padx=2)
        
    def create_version_row(self):
        # Version info
        version_frame = ttk.Frame(self)
        version_frame.grid(row=1, column=0, columnspan=2, sticky='w', padx=5)
        
        ttk.Label(version_frame, text="Installed Version:").pack(side='left')
        ttk.Label(version_frame, text="0.0").pack(side='left', padx=5)
        ttk.Button(version_frame, text="ℹ", width=2).pack(side='left')
        
        # Right-side controls
        controls_frame = ttk.Frame(self)
        controls_frame.grid(row=1, column=2, sticky='e')
        
        ttk.Label(controls_frame, text="✓").pack(side='left', padx=2)
        ttk.Label(controls_frame, text="□").pack(side='left', padx=2)
        ttk.Button(controls_frame, text="Install").pack(side='left', padx=2)
        
    def create_location_row(self):
        ttk.Label(self, text="Installation Location:").grid(row=2, column=0, columnspan=2, sticky='w', padx=5)
        
        location_frame = ttk.Frame(self)
        location_frame.grid(row=2, column=2, sticky='e')
        
        ttk.Button(location_frame, text="📁", width=2).pack(side='left', padx=2)
        ttk.Button(location_frame, text="Set Location...").pack(side='left', padx=2)
        
    def create_status_row(self):
        # Status
        ttk.Label(self, text="Status: Uninstalled").grid(row=3, column=0, sticky='w', padx=5)
        
        # Availability
        ttk.Label(self, text="Availability: Unavailable").grid(row=3, column=1, sticky='w', padx=5)
        
        # Players section
        players_frame = ttk.Frame(self)
        players_frame.grid(row=3, column=2, sticky='e')
        
        ttk.Label(players_frame, text="Players: 0 / 70").pack(side='left', padx=5)
        ttk.Button(players_frame, text="Start").pack(side='left', padx=2)
        ttk.Button(players_frame, text="Players").pack(side='left', padx=2)

def main():
    root = tk.Tk()
    app = AdminPanel(root)
    root.mainloop()

if __name__ == "__main__":
    main()

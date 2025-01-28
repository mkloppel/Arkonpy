import tkinter as tk
from tkinter import ttk
from Main import ScrollableFrameMixin

class AdminContent(ttk.Frame, ScrollableFrameMixin):
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
        self.create_name_passwords_section(scrollable_frame)
        self.create_networking_section(scrollable_frame)
        self.create_maps_mods_section(scrollable_frame)
        self.create_saves_section(scrollable_frame)
        self.create_motd_section(scrollable_frame)
        self.create_server_options_section(scrollable_frame)
        self.create_server_log_section(scrollable_frame)
        self.create_branch_details_section(scrollable_frame)
        self.create_command_line_section(scrollable_frame)
        
        # Pack the scrollable elements
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
            
    def create_name_passwords_section(self, parent):
        section = ttk.LabelFrame(parent, text="Name and Passwords", padding="5")
        section.pack(fill="x", padx=5, pady=5)
        
        # Server Name row
        name_frame = ttk.Frame(section)
        name_frame.pack(fill="x")
        ttk.Label(name_frame, text="Server Name:").pack(side="left")
        ttk.Entry(name_frame).pack(side="left", fill="x", expand=True, padx=5)
        ttk.Label(name_frame, text="Length: 0").pack(side="left")
        
        # Passwords row
        pass_frame = ttk.Frame(section)
        pass_frame.pack(fill="x", pady=5)
        
        # Server Password
        ttk.Label(pass_frame, text="Server Password:").pack(side="left")
        ttk.Entry(pass_frame, show="*").pack(side="left", padx=5)
        
        # Admin Password
        ttk.Label(pass_frame, text="Admin Password:").pack(side="left")
        ttk.Entry(pass_frame, show="*").pack(side="left", padx=5)
        
        # Spectator Password
        ttk.Label(pass_frame, text="Spectator Password:").pack(side="left")
        ttk.Entry(pass_frame, show="*").pack(side="left", padx=5)
    
    def create_networking_section(self, parent):
        section = ttk.LabelFrame(parent, text="Networking", padding="5")
        section.pack(fill="x", padx=5, pady=5)
        
        # Local IP row
        ip_frame = ttk.Frame(section)
        ip_frame.pack(fill="x", pady=2)
        ttk.Label(ip_frame, text="Local IP:").pack(side="left")
        ttk.Combobox(ip_frame, values=["Let the server choose"]).pack(side="left", padx=5)
        ttk.Button(ip_frame, text="↻").pack(side="left")
        
        # Ports row
        ports_frame = ttk.Frame(section)
        ports_frame.pack(fill="x", pady=2)
        
        # Server Port
        ttk.Label(ports_frame, text="Server Port:").pack(side="left")
        ttk.Entry(ports_frame).pack(side="left", padx=5)
        
        # Peer Port
        ttk.Label(ports_frame, text="Peer Port:").pack(side="left")
        ttk.Entry(ports_frame).pack(side="left", padx=5)
        
        # Query Port
        ttk.Label(ports_frame, text="Query Port:").pack(side="left")
        ttk.Entry(ports_frame).pack(side="left", padx=5)
        
        # RCON row
        rcon_frame = ttk.Frame(section)
        rcon_frame.pack(fill="x", pady=2)
        ttk.Checkbutton(rcon_frame, text="Enable RCON").pack(side="left")
        ttk.Label(rcon_frame, text="RCON Port:").pack(side="left")
        ttk.Entry(rcon_frame).pack(side="left", padx=5)
        ttk.Label(rcon_frame, text="RCON Server Log Buffer:").pack(side="left")
        ttk.Entry(rcon_frame).pack(side="left", padx=5)
        ttk.Button(rcon_frame, text="RCON").pack(side="left")

    def create_maps_mods_section(self, parent):
        section = ttk.LabelFrame(parent, text="Maps and Mods", padding="5")
        section.pack(fill="x", padx=5, pady=5)
        
        # Map Name row
        map_frame = ttk.Frame(section)
        map_frame.pack(fill="x", pady=2)
        ttk.Label(map_frame, text="Map Name or Map Mod Path:").pack(side="left")
        ttk.Combobox(map_frame).pack(side="left", fill="x", expand=True, padx=5)
        ttk.Button(map_frame, text="📁").pack(side="left")
        
        # Total Conversion ID row
        conversion_frame = ttk.Frame(section)
        conversion_frame.pack(fill="x", pady=2)
        ttk.Label(conversion_frame, text="Total Conversion ID:").pack(side="left")
        ttk.Combobox(conversion_frame).pack(side="left", fill="x", expand=True, padx=5)
        ttk.Button(conversion_frame, text="📁").pack(side="left")
        
        # Mod IDs row
        mod_frame = ttk.Frame(section)
        mod_frame.pack(fill="x", pady=2)
        ttk.Label(mod_frame, text="Mod IDs:").pack(side="left")
        ttk.Entry(mod_frame).pack(side="left", fill="x", expand=True, padx=5)
        ttk.Button(mod_frame, text="Browse").pack(side="left", padx=2)
        ttk.Button(mod_frame, text="Download").pack(side="left")

    def create_saves_section(self, parent):
        section = ttk.LabelFrame(parent, text="Saves", padding="5")
        section.pack(fill="x", padx=5, pady=5)
        
        save_frame = ttk.Frame(section)
        save_frame.pack(fill="x")
        ttk.Label(save_frame, text="Auto Save Period:").pack(side="left")
        ttk.Scale(save_frame, from_=0, to=60, orient="horizontal").pack(side="left", fill="x", expand=True, padx=5)
        ttk.Entry(save_frame, width=5).pack(side="left")
        ttk.Label(save_frame, text="minutes").pack(side="left", padx=5)
        ttk.Button(save_frame, text="Backup Now").pack(side="left", padx=2)
        ttk.Button(save_frame, text="Restore...").pack(side="left")
        
    def create_motd_section(self, parent):
        section = ttk.LabelFrame(parent, text="Message of the Day", padding="5")
        section.pack(fill="x", padx=5, pady=5)
        
        motd_frame = ttk.Frame(section)
        motd_frame.pack(fill="x")
        ttk.Label(motd_frame, text="Lines: 0").pack(side="left")
        ttk.Label(motd_frame, text="Length: 0").pack(side="left", padx=20)
        
        # Add text box
        text_frame = ttk.Frame(section)
        text_frame.pack(fill="both", expand=True, pady=5)
        
        self.motd_text = tk.Text(text_frame, height=4, wrap="word")
        self.motd_text.pack(fill="both", expand=True)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(text_frame, orient="vertical", command=self.motd_text.yview)
        scrollbar.pack(side="right", fill="y")
        self.motd_text.configure(yscrollcommand=scrollbar.set)

    def create_server_options_section(self, parent):
        section = ttk.LabelFrame(parent, text="Server Options", padding="5")
        section.pack(fill="x", padx=5, pady=5)
        
        # Top row with max players and idle timeout
        top_frame = ttk.Frame(section)
        top_frame.pack(fill="x", pady=2)
        
        # Max Players
        ttk.Label(top_frame, text="Max Players:").pack(side="left")
        ttk.Scale(top_frame, from_=0, to=100, orient="horizontal").pack(side="left", padx=5)
        ttk.Entry(top_frame, width=5).pack(side="left")
        
        # Idle Timeout
        ttk.Checkbutton(top_frame, text="Enable Idle Timeout").pack(side="left", padx=20)
        ttk.Entry(top_frame, width=8).pack(side="left", padx=5)
        ttk.Label(top_frame, text="seconds").pack(side="left")
        
        # Create two columns for checkboxes
        checkbox_frame = ttk.Frame(section)
        checkbox_frame.pack(fill="x", pady=5)
        
        left_frame = ttk.Frame(checkbox_frame)
        left_frame.pack(side="left", fill="x", expand=True)
        
        right_frame = ttk.Frame(checkbox_frame)
        right_frame.pack(side="left", fill="x", expand=True)
        
        # Left column checkboxes
        left_options = [
            "Use Ban List URL", "Disable VAC", "Enable BattlEye",
            "Disable Player-Move-Physics", "Use All Available Cores",
            "Use Cache", "No Hang Detection", "No Dinos",
            "No Under Mesh Checking", "No Under Mesh Killing",
            "Enable Vivox", "Allow Shared Connections",
            "Force Respawn Dinos", "Enable Auto Force Respawn"
        ]
        
        for option in left_options:
            ttk.Checkbutton(left_frame, text=option).pack(anchor="w", pady=1)
        
        # Right column checkboxes
        right_options = [
            "Disable Anti-Speed", "Force DirectX 10",
            "Force Shader Model 4", "Force Low Memory",
            "Force No Man Sky", "Use No Memory Bias",
            "Stasis Keep Controllers", "Server Allow Arise",
            "Structure Memory Optimizations", "Enable Crossplay",
            "Enable Public IP for Epic", "Epic Store Players Only"
        ]
        
        for option in right_options:
            ttk.Checkbutton(right_frame, text=option).pack(anchor="w", pady=1)
        
        # Bottom rows
        bottom_frame = ttk.Frame(section)
        bottom_frame.pack(fill="x", pady=5)
        
        # Respawn interval
        respawn_frame = ttk.Frame(bottom_frame)
        respawn_frame.pack(fill="x", pady=2)
        ttk.Label(respawn_frame, text="Auto Force Respawn Interval:").pack(side="left")
        ttk.Scale(respawn_frame, from_=0, to=48, orient="horizontal").pack(side="left", fill="x", expand=True, padx=5)
        ttk.Entry(respawn_frame, width=5).pack(side="left")
        ttk.Label(respawn_frame, text="hours").pack(side="left")
        
        # Save directory
        save_frame = ttk.Frame(bottom_frame)
        save_frame.pack(fill="x", pady=2)
        ttk.Label(save_frame, text="Alternate Save Directory:").pack(side="left")
        ttk.Entry(save_frame).pack(side="left", fill="x", expand=True, padx=5)
        ttk.Label(save_frame, text="(Optional)").pack(side="left")
        
        # Cluster ID
        cluster_frame = ttk.Frame(bottom_frame)
        cluster_frame.pack(fill="x", pady=2)
        ttk.Label(cluster_frame, text="Cross-ARK Data Transfer ClusterId:").pack(side="left")
        ttk.Entry(cluster_frame).pack(side="left", fill="x", expand=True, padx=5)
        ttk.Checkbutton(cluster_frame, text="Cluster Directory Override").pack(side="left")

    def create_server_log_section(self, parent):
        section = ttk.LabelFrame(parent, text="Server Log Options", padding="5")
        section.pack(fill="x", padx=5, pady=5)
        
        # Create two columns
        columns_frame = ttk.Frame(section)
        columns_frame.pack(fill="x", pady=2)
        
        # Left column
        left_frame = ttk.Frame(columns_frame)
        left_frame.pack(side="left", fill="x", expand=True)
        
        left_options = [
            "Enable Server Admin Logs",
            "Server Admin Logs Include Tribe",
            "Server RCON Output Tribe Logs",
            "Allow Hide Damage Source",
            "Enable Web Alarms"
        ]
        
        for option in left_options:
            ttk.Checkbutton(left_frame, text=option).pack(anchor="w", pady=1)
        
        # Right column
        right_frame = ttk.Frame(columns_frame)
        right_frame.pack(side="left", fill="x", expand=True)
        
        # Max tribe logs
        tribe_frame = ttk.Frame(right_frame)
        tribe_frame.pack(fill="x", pady=1)
        ttk.Label(tribe_frame, text="Maximum Tribe Logs:").pack(side="left")
        ttk.Entry(tribe_frame, width=8).pack(side="left", padx=5)
        
        right_options = [
            "Log Admin Commands to Chat (public)",
            "Log Admin Commands to Chat (admins only)",
            "Tribe Log Destroyed Enemy Structures"
        ]
        
        for option in right_options:
            ttk.Checkbutton(right_frame, text=option).pack(anchor="w", pady=1)
        
        # Web section
        web_frame = ttk.Frame(section)
        web_frame.pack(fill="x", pady=5)
        
        ttk.Label(web_frame, text="Web Key:").pack(side="left")
        ttk.Entry(web_frame, show="*").pack(side="left", padx=5)
        ttk.Label(web_frame, text="Web URL:").pack(side="left")
        ttk.Entry(web_frame, show="*").pack(side="left", padx=5)
        
        # Warning note
        ttk.Label(section, text="NOTE: The server manager does not provide the Web Alarms functionality,\nit just allows you to enable/disable the Web Alarms and create the necessary file.",
                 wraplength=500).pack(pady=5)

    def create_branch_details_section(self, parent):
        section = ttk.LabelFrame(parent, text="Branch Details", padding="5")
        section.pack(fill="x", padx=5, pady=5)
        
        branch_frame = ttk.Frame(section)
        branch_frame.pack(fill="x")
        
        ttk.Label(branch_frame, text="Branch Name:").pack(side="left")
        ttk.Combobox(branch_frame, values=["Live"]).pack(side="left", padx=5)
        ttk.Label(branch_frame, text="Branch Password:").pack(side="left")
        ttk.Entry(branch_frame, show="*").pack(side="left", padx=5)

    def create_command_line_section(self, parent):
        section = ttk.LabelFrame(parent, text="Command Line", padding="5")
        section.pack(fill="x", padx=5, pady=5)
        
        # Priority and CPU
        priority_frame = ttk.Frame(section)
        priority_frame.pack(fill="x", pady=2)
        
        ttk.Label(priority_frame, text="Priority:").pack(side="left")
        ttk.Combobox(priority_frame, values=["Normal"]).pack(side="left", padx=5)
        ttk.Label(priority_frame, text="Affinity - CPU:").pack(side="left")
        ttk.Entry(priority_frame).pack(side="left", padx=5)
        ttk.Button(priority_frame, text="...").pack(side="left")
        
        # Launcher Args
        launcher_frame = ttk.Frame(section)
        launcher_frame.pack(fill="x", pady=2)
        ttk.Label(launcher_frame, text="Launcher Args:").pack(side="left")
        ttk.Entry(launcher_frame).pack(side="left", fill="x", expand=True, padx=5)
        ttk.Checkbutton(launcher_frame, text="Override Launcher").pack(side="left")
        
        # Server Args
        server_frame = ttk.Frame(section)
        server_frame.pack(fill="x", pady=2)
        ttk.Label(server_frame, text="Server Args:").pack(side="left")
        ttk.Entry(server_frame).pack(side="left", fill="x", expand=True, padx=5)
        ttk.Button(server_frame, text="Show Command...").pack(side="left")
        
    def main():
        root = tk.Tk()
        app = AdminContent(root)  # Note: AdminContent, not AdminPanel
        app.pack(fill="both", expand=True)
        root.mainloop()

    if __name__ == "__main__":
        main()

import tkinter as tk
from tkinter import ttk, messagebox
from server_config_manager import ServerConfigManager

class NamePasswordsManager:
    """
    Manages the Name and Passwords section of the admin panel.
    Connects UI elements to the server configuration.
    """
    def __init__(self, parent_frame, config_manager):
        """
        Initialize the manager with a parent frame and config manager.
        
        Args:
            parent_frame: The parent frame where UI elements will be placed
            config_manager: Instance of ServerConfigManager to handle config values
        """
        self.parent = parent_frame
        self.config_manager = config_manager
        
        # UI variables
        self.server_name_var = tk.StringVar()
        self.server_password_var = tk.StringVar()
        self.admin_password_var = tk.StringVar()
        self.spectator_password_var = tk.StringVar()
        
        # Character count for server name
        self.name_length_var = tk.StringVar(value="Length: 0")
        
        # Initialize UI elements
        self.create_ui_elements()
        
        # Connect variables to config manager
        self.load_values_from_config()
        
        # Set up event handlers
        self.setup_event_handlers()
    
    def create_ui_elements(self):
        """Create and place UI elements in the parent frame."""
        # Server Name row
        name_frame = ttk.Frame(self.parent)
        name_frame.pack(fill="x")
        ttk.Label(name_frame, text="Server Name:").pack(side="left")
        
        self.server_name_entry = ttk.Entry(name_frame, textvariable=self.server_name_var)
        self.server_name_entry.pack(side="left", fill="x", expand=True, padx=5)
        
        self.name_length_label = ttk.Label(name_frame, textvariable=self.name_length_var)
        self.name_length_label.pack(side="left")
        
        # Passwords row
        pass_frame = ttk.Frame(self.parent)
        pass_frame.pack(fill="x", pady=5)
        
        # Server Password
        ttk.Label(pass_frame, text="Server Password:").pack(side="left")
        self.server_password_entry = ttk.Entry(pass_frame, show="*", textvariable=self.server_password_var)
        self.server_password_entry.pack(side="left", padx=5)
        
        # Admin Password
        ttk.Label(pass_frame, text="Admin Password:").pack(side="left")
        self.admin_password_entry = ttk.Entry(pass_frame, show="*", textvariable=self.admin_password_var)
        self.admin_password_entry.pack(side="left", padx=5)
        
        # Spectator Password
        ttk.Label(pass_frame, text="Spectator Password:").pack(side="left")
        self.spectator_password_entry = ttk.Entry(pass_frame, show="*", textvariable=self.spectator_password_var)
        self.spectator_password_entry.pack(side="left", padx=5)
        
        # Add tooltips with descriptions from the JSON
        self.create_tooltips()
    
    def create_tooltips(self):
        """Create tooltips for the UI elements with descriptions from the JSON."""
        # This is a simple implementation - in a real app, you might want a more sophisticated tooltip
        self.server_name_entry.bind("<Enter>", lambda e: self.show_tooltip(e, "ServerName"))
        self.server_name_entry.bind("<Leave>", self.hide_tooltip)
        
        self.server_password_entry.bind("<Enter>", lambda e: self.show_tooltip(e, "ServerPassword"))
        self.server_password_entry.bind("<Leave>", self.hide_tooltip)
        
        self.admin_password_entry.bind("<Enter>", lambda e: self.show_tooltip(e, "ServerAdminPassword"))
        self.admin_password_entry.bind("<Leave>", self.hide_tooltip)
        
        self.spectator_password_entry.bind("<Enter>", lambda e: self.show_tooltip(e, "SpectatorPassword"))
        self.spectator_password_entry.bind("<Leave>", self.hide_tooltip)
    
    def show_tooltip(self, event, setting_name):
        """Show a tooltip with the description of a setting."""
        description = self.config_manager.get_setting_description(setting_name)
        if not description:
            return
        
        # Create a toplevel window for the tooltip
        self.tooltip = tk.Toplevel(self.parent)
        self.tooltip.wm_overrideredirect(True)  # Remove window decorations
        
        # Position near the mouse
        x, y = event.widget.winfo_rootx(), event.widget.winfo_rooty() + event.widget.winfo_height() + 10
        self.tooltip.wm_geometry(f"+{x}+{y}")
        
        # Add the description text
        label = ttk.Label(self.tooltip, text=description, wraplength=400, 
                          background="#FFFFDD", relief="solid", borderwidth=1)
        label.pack(padx=5, pady=5)
    
    def hide_tooltip(self, event):
        """Hide the tooltip."""
        if hasattr(self, "tooltip"):
            self.tooltip.destroy()
    
    def setup_event_handlers(self):
        """Set up event handlers for UI elements."""
        # Update character count when server name changes
        self.server_name_var.trace_add("write", self.update_name_length)
        
        # Save values to config when they change
        self.server_name_var.trace_add("write", lambda *args: self.save_value_to_config("ServerName", self.server_name_var.get()))
        self.server_password_var.trace_add("write", lambda *args: self.save_value_to_config("ServerPassword", self.server_password_var.get()))
        self.admin_password_var.trace_add("write", lambda *args: self.save_value_to_config("AdminPassword", self.admin_password_var.get()))
        self.spectator_password_var.trace_add("write", lambda *args: self.save_value_to_config("SpectatorPassword", self.spectator_password_var.get()))
    
    def update_name_length(self, *args):
        """Update the server name length label."""
        length = len(self.server_name_var.get())
        self.name_length_var.set(f"Length: {length}")
        
        # Warn if name is too long (ARK has a limit, typically around 50 characters)
        if length > 50:
            self.name_length_label.configure(foreground="red")
        else:
            self.name_length_label.configure(foreground="black")
    
    def save_value_to_config(self, setting_name, value):
        """Save a value to the config manager."""
        self.config_manager.set_setting(setting_name, value)
    
    def load_values_from_config(self):
        """Load values from the config manager to the UI variables."""
        self.server_name_var.set(self.config_manager.get_setting("ServerName"))
        self.server_password_var.set(self.config_manager.get_setting("ServerPassword"))
        self.admin_password_var.set(self.config_manager.get_setting("AdminPassword"))
        self.spectator_password_var.set(self.config_manager.get_setting("SpectatorPassword"))
        
        # Update the name length
        self.update_name_length()
    
    def save_all(self):
        """Save all values to the config manager and trigger a save."""
        # Values are already saved to the config manager when they change
        # This method is for explicit save actions
        return self.config_manager.save_config()

# Example usage:
def main():
    root = tk.Tk()
    root.title("ARK Server Configuration")
    
    # Create a frame for the Name and Passwords section
    section = ttk.LabelFrame(root, text="Name and Passwords", padding="5")
    section.pack(fill="x", padx=5, pady=5)
    
    # Create a config manager
    config_manager = ServerConfigManager()
    
    # Create the Name and Passwords manager
    name_passwords_manager = NamePasswordsManager(section, config_manager)
    
    # Add a save button
    save_button = ttk.Button(root, text="Save Configuration", 
                            command=lambda: messagebox.showinfo("Save", 
                                    "Configuration saved!" if name_passwords_manager.save_all() 
                                    else "Failed to save configuration"))
    save_button.pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    main()

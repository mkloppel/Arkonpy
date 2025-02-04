import os
from pathlib import Path
import json
from string import Template

# -------------------------------
# Class representing a single server profile
# -------------------------------
class ServerProfile:
    """
    Represents a configuration profile for a dedicated server.
    Contains settings for INI files and generates batch files for server startup.
    """
    def __init__(self, name, config_dir):
        self.name = name  # Unique identifier for the server (e.g., "ArkServer1")
        self.config_dir = Path(config_dir)  # Directory to store profile files
        # Dictionaries to hold configuration settings for different files
        self.game_user_settings = {}  # Settings to be written to GameUserSettings.ini
        self.game_settings = {}       # Settings to be written to Game.ini
        self.observers = []  # List of GUI panels observing this profile

    def load_profile(self):
        """
        Loads the server configuration from a JSON file into in-memory dictionaries.
        """
        profile_file = self.config_dir / f"{self.name}.json"
        if profile_file.exists():
            with open(profile_file, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.game_user_settings = data.get("game_user_settings", {})
                self.game_settings = data.get("game_settings", {})
        # If the file does not exist, the profile remains with default empty settings.

    def save_profile(self):
        """
        Saves the current server configuration (settings in memory) to a JSON file.
        """
        profile_file = self.config_dir / f"{self.name}.json"
        data = {
            "game_user_settings": self.game_user_settings,
            "game_settings": self.game_settings
        }
        with open(profile_file, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        # Notify observers that settings have been saved
        self.notify_observers("save")

    def add_observer(self, observer):
        """Add a GUI panel as an observer"""
        if observer not in self.observers:
            self.observers.append(observer)
    
    def remove_observer(self, observer):
        """Remove a GUI panel observer"""
        if observer in self.observers:
            self.observers.remove(observer)
            
    def notify_observers(self, event_type):
        """Notify all observers of changes"""
        for observer in self.observers:
            if hasattr(observer, 'on_profile_changed'):
                observer.on_profile_changed(event_type)
                
    def update_setting(self, section, key, value):
        """Update a specific setting and notify observers"""
        if section == "GameUserSettings":
            self.game_user_settings[key] = value
        elif section == "Game":
            self.game_settings[key] = value
        self.notify_observers("update")

    def generate_ini_file(self, template_path, output_path):
        """
        Generates an INI configuration file from a template by substituting settings.
        
        Args:
            template_path (str or Path): Path to the INI template file.
            output_path (str or Path): Path where the generated INI file will be saved.
        """
        template_path = Path(template_path)
        output_path = Path(output_path)
        # Read the template file content
        with open(template_path, "r", encoding="utf-8") as file:
            template_content = file.read()
        # Create a Template instance using Python's built-in templating
        ini_template = Template(template_content)
        # Combine settings from both dictionaries for substitution
        combined_settings = {}
        combined_settings.update(self.game_user_settings)
        combined_settings.update(self.game_settings)
        # Substitute placeholders in the template with actual settings
        generated_content = ini_template.safe_substitute(combined_settings)
        # Write the generated content to the output file
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(generated_content)

    def generate_start_bat(self, template_path, output_path):
        """
        Generates a .bat file to start the server from a template with substituted settings.
        
        Args:
            template_path (str or Path): Path to the .bat template file.
            output_path (str or Path): Path where the generated .bat file will be saved.
        """
        template_path = Path(template_path)
        output_path = Path(output_path)
        # Read the batch file template
        with open(template_path, "r", encoding="utf-8") as file:
            template_content = file.read()
        bat_template = Template(template_content)
        # Create a dictionary with command-line parameters; values below are example defaults.
        bat_settings = {
            "SERVER_PORT": self.game_user_settings.get("server_port", "7777"),   # Example: default server port
            "MAX_PLAYERS": self.game_user_settings.get("max_players", "70")       # Example: default maximum players
        }
        # Substitute placeholders in the batch template with the server settings
        generated_content = bat_template.safe_substitute(bat_settings)
        # Write the generated batch file content to disk
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(generated_content)

# -------------------------------
# Manager class for multiple server profiles
# -------------------------------
class ServerManager:
    """
    Manages multiple server profiles by handling their creation, loading, saving, and configuration generation.
    """
    def __init__(self, profiles_dir):
        self.profiles_dir = Path(profiles_dir)
        self.server_profiles = {}  # Dictionary mapping profile names to ServerProfile instances

    def add_server_profile(self, name):
        """
        Creates and registers a new server profile.
        
        Args:
            name (str): Unique name for the new server profile.
        Returns:
            ServerProfile: The newly created server profile instance.
        """
        profile = ServerProfile(name, self.profiles_dir)
        self.server_profiles[name] = profile
        return profile

    def load_all_profiles(self):
        """
        Loads all server profile JSON files from the profiles directory into memory.
        """
        for file in self.profiles_dir.glob("*.json"):
            server_name = file.stem
            profile = ServerProfile(server_name, self.profiles_dir)
            profile.load_profile()
            self.server_profiles[server_name] = profile

    def save_all_profiles(self):
        """
        Saves all in-memory server profiles back to their respective JSON files.
        """
        for profile in self.server_profiles.values():
            profile.save_profile()

    def generate_all_configurations(self, ini_template, bat_template):
        """
        Generates configuration files for all managed server profiles using the specified templates.
        
        Args:
            ini_template (str or Path): Path to the INI file template.
            bat_template (str or Path): Path to the .bat file template.
        """
        for profile in self.server_profiles.values():
            ini_output_path = self.profiles_dir / f"{profile.name}_GameUserSettings.ini"
            bat_output_path = self.profiles_dir / f"{profile.name}_StartServer.bat"
            profile.generate_ini_file(ini_template, ini_output_path)
            profile.generate_start_bat(bat_template, bat_output_path)

# -------------------------------
# Main function demonstrating usage
# -------------------------------
def main():
    """
    Main function that demonstrates creating a server profile, updating settings,
    saving the profile, and generating configuration files.
    """
    # Define the directory for storing profiles; adjust to a valid local path.
    profiles_directory = "C:/ServerProfiles"  # Example directory path.
    # Ensure the directory exists
    os.makedirs(profiles_directory, exist_ok=True)
    
    # Instantiate the server manager with the profiles directory.
    manager = ServerManager(profiles_directory)
    
    # Add a new server profile with a unique name.
    profile = manager.add_server_profile("ArkServer1")
    
    # Update configuration settings for this profile.
    profile.game_user_settings = {
        "server_port": "7777",    # Example server port setting.
        "max_players": "70"       # Example maximum players setting.
    }
    profile.game_settings = {
        "setting1": "value1",     # Replace with actual game setting.
        "setting2": "value2"      # Replace with actual game setting.
    }
    
    # Save the updated profile to disk.
    profile.save_profile()
    
    # Define paths to the template files; adjust to valid template file locations.
    ini_template_file = "C:/Templates/GameUserSettings.ini.template"  # Template for INI file.
    bat_template_file = "C:/Templates/StartServer.bat.template"         # Template for batch start file.
    
    # Generate the INI and BAT files for the profile.
    profile.generate_ini_file(
        ini_template=ini_template_file,
        output_path=f"C:/ServerProfiles/{profile.name}_GameUserSettings.ini"
    )
    profile.generate_start_bat(
        template_path=bat_template_file,
        output_path=f"C:/ServerProfiles/{profile.name}_StartServer.bat"
    )
    
    # Optionally, load all profiles and generate configurations in bulk.
    manager.load_all_profiles()
    manager.generate_all_configurations(ini_template_file, bat_template_file)

if __name__ == "__main__":
    main()

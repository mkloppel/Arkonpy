import json
import os
from pathlib import Path

class ServerConfigManager:
    """
    Manages server configuration by reading from and writing to configuration files.
    Provides methods to get and set server settings.
    """
    def __init__(self, config_dir="server_profiles"):
        self.config_dir = Path(config_dir)
        self.config_dir.mkdir(exist_ok=True)
        
        # Load settings from JSON files
        self.server_settings = self._load_json_file("jsons/ServerSettings.json")
        self.command_line_args = self._load_json_file("jsons/commandlinearguements.json")
        
        # Current configuration values
        self.current_config = {
            # Server identification
            "ServerName": "",
            "ServerPassword": "",
            "AdminPassword": "",
            "SpectatorPassword": "",
            
            # Other settings will be added as needed
        }
        
        # Default GameUserSettings.ini template
        self.game_user_settings_template = """[ServerSettings]
ServerName={ServerName}
ServerPassword={ServerPassword}
ServerAdminPassword={AdminPassword}
SpectatorPassword={SpectatorPassword}
"""
    
    def _load_json_file(self, file_path):
        """Load a JSON file and return its contents."""
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading {file_path}: {e}")
            return {}
    
    def get_setting(self, setting_name):
        """Get the current value of a setting."""
        return self.current_config.get(setting_name, "")
    
    def set_setting(self, setting_name, value):
        """Set a configuration value."""
        self.current_config[setting_name] = value
        # In a real implementation, you might want to validate the value here
        return True
    
    def save_config(self, profile_name="default"):
        """Save the current configuration to the appropriate files."""
        profile_dir = self.config_dir / profile_name
        profile_dir.mkdir(exist_ok=True)
        
        # Save GameUserSettings.ini
        self._save_game_user_settings(profile_dir)
        
        # Save profile metadata
        self._save_profile_metadata(profile_dir, profile_name)
        
        return True
    
    def _save_game_user_settings(self, profile_dir):
        """Save the GameUserSettings.ini file."""
        game_user_settings_path = profile_dir / "GameUserSettings.ini"
        
        # Format the template with current values
        content = self.game_user_settings_template.format(**self.current_config)
        
        with open(game_user_settings_path, 'w') as f:
            f.write(content)
    
    def _save_profile_metadata(self, profile_dir, profile_name):
        """Save profile metadata."""
        metadata_path = profile_dir / "profile.json"
        
        metadata = {
            "name": profile_name,
            "last_updated": self._get_timestamp(),
            "settings": self.current_config
        }
        
        with open(metadata_path, 'w') as f:
            json.dump(metadata, f, indent=2)
    
    def _get_timestamp(self):
        """Get current timestamp in ISO format."""
        from datetime import datetime
        return datetime.now().isoformat()
    
    def load_profile(self, profile_name="default"):
        """Load a profile's configuration."""
        profile_dir = self.config_dir / profile_name
        metadata_path = profile_dir / "profile.json"
        
        if not metadata_path.exists():
            return False
        
        try:
            with open(metadata_path, 'r') as f:
                metadata = json.load(f)
                self.current_config = metadata.get("settings", {})
            return True
        except (FileNotFoundError, json.JSONDecodeError):
            return False
    
    def get_setting_description(self, setting_name):
        """Get the description of a setting from the server settings JSON."""
        if not self.server_settings or "ServerSettings" not in self.server_settings:
            return ""
        
        for setting in self.server_settings["ServerSettings"]:
            if setting["setting"] == setting_name:
                return setting["description"]
        
        return ""

    def get_setting_default(self, setting_name):
        """Get the default value of a setting from the server settings JSON."""
        # This requires the JSON to have a 'default' field.
        # Adjust based on actual JSON structure.
        if not self.server_settings or "ServerSettings" not in self.server_settings:
            return None # Or a sensible default like "" or 0

        for setting in self.server_settings["ServerSettings"]:
            if setting.get("setting") == setting_name: # Use .get() for safety
                return setting.get("default") # Assumes 'default' key exists

        return None # Setting not found

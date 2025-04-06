import socket
import tkinter as tk
from tkinter import ttk
from scrollable_frame import ScrollableFrameMixin

class DisplayIPPanel(ttk.Frame, ScrollableFrameMixin):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_frames()
        
    def create_frames(self):
        """Create the main frame structure"""
        main_frame = ttk.Frame(self)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.create_ip_display_section(main_frame)
        
    def create_ip_display_section(self, parent):
        """Create the IP display section"""
        frame = ttk.LabelFrame(parent, text="Server IP Information")
        frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Get IP addresses
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        
        try:
            # Try to get external IP (this requires internet connection)
            external_ip = self.get_external_ip()
        except:
            external_ip = "Could not determine (check internet connection)"
        
        # Hostname display
        ttk.Label(frame, text="Hostname:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        ttk.Label(frame, text=hostname).grid(row=0, column=1, sticky="w", padx=5, pady=5)
        
        # Local IP display
        ttk.Label(frame, text="Local IP:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        ttk.Label(frame, text=local_ip).grid(row=1, column=1, sticky="w", padx=5, pady=5)
        
        # External IP display
        ttk.Label(frame, text="External IP:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        ttk.Label(frame, text=external_ip).grid(row=2, column=1, sticky="w", padx=5, pady=5)
        
        # Refresh button
        refresh_btn = ttk.Button(frame, text="Refresh", command=self.refresh_ip_info)
        refresh_btn.grid(row=3, column=0, columnspan=2, pady=10)
        
        # Store references for updating
        self.hostname_label = hostname
        self.local_ip_label = local_ip
        self.external_ip_label = external_ip
        self.frame = frame
    
    def get_external_ip(self):
        """Get the external IP address"""
        try:
            import urllib.request
            external_ip = urllib.request.urlopen('https://api.ipify.org').read().decode('utf8')
            return external_ip
        except:
            return "Could not determine (check internet connection)"
    
    def refresh_ip_info(self):
        """Refresh the IP information"""
        # This would be implemented to update the display with current IP info
        # For now, just show a message that it would refresh
        refresh_label = ttk.Label(self.frame, text="IP information would refresh here")
        refresh_label.grid(row=4, column=0, columnspan=2, pady=5)
        # Schedule label to disappear after 2 seconds
        self.after(2000, refresh_label.destroy)

def main():
    """Test function to run this panel standalone"""
    root = tk.Tk()
    root.title("Display IP Panel")
    root.geometry("600x400")
    
    panel = DisplayIPPanel(root)
    panel.pack(fill="both", expand=True)
    
    root.mainloop()

if __name__ == "__main__":
    main()

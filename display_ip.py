import urllib.request

def get_external_ip():
    """
    Get the external IP address as would be seen by services like Steam or Epic.
    
    Returns:
        str: The external IP address or "UNKNOWN" if it couldn't be determined
    """
    try:
        # Using ipify.org API to get the external IP address
        external_ip = urllib.request.urlopen('https://api.ipify.org').read().decode('utf8')
        return external_ip if external_ip else "UNKNOWN"
    except Exception as e:
        return "UNKNOWN"

# This can be called at application start to refresh the IP
def refresh_external_ip():
    """
    Refresh and return the current external IP address
    
    Returns:
        str: The current external IP address
    """
    return get_external_ip()

if __name__ == "__main__":
    # Simple test when run directly
    print(f"External IP: {get_external_ip()}")

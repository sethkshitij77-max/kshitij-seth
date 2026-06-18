import os
import platform
import subprocess

def ping_ip(ip_address):
    """
    Pings a target IP address or domain and returns True if reachable.
    """
    # Determine the operating system
    current_os = platform.system().lower()
    
    # Configure parameter based on OS (-n for Windows, -c for Mac/Linux)
    if current_os == "windows":
        parameter = "-n"
    else:
        parameter = "-c"
        
    # Build the command (sending 1 packet with a 2-second timeout)
    command = ["ping", parameter, "1", "-w", "2000" if current_os == "windows" else "2", ip_address]
    
    try:
        # Run command without popping up shell windows or displaying console output
        response = subprocess.run(
            command, 
            stdout=subprocess.DEVNULL, 
            stderr=subprocess.DEVNULL, 
            timeout=3
        )
        # A return code of 0 means the host responded successfully
        return response.returncode == 0
    except (subprocess.SubprocessError, subprocess.TimeoutExpired):
        return False

# Example Usage
if __name__ == "__main__":
    target = input("Enter an IP address or Domain to ping: ").strip()
    print(f"Pinging {target}...")
    
    if ping_ip(target):
        print(f"[SUCCESS] {target} is active and reachable.")
    else:
        print(f"[FAILED] {target} is down or blocking ICMP packets.")

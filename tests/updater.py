import urllib.request
import os

# Set the URL of the update file and the current version number
update_url = "http://example.com/update.txt"
current_version = "1.0"

# Fetch the contents of the update file from the remote server
with urllib.request.urlopen(update_url) as response:
    update_data = response.read().decode("utf-8")

# Extract the version number from the update data
new_version = update_data.splitlines()[0]

# Check if a new version is available
if new_version != current_version:
    print(f"New version {new_version} available! Downloading...")
    
    # Download the updated script from the remote server
    updated_script_url = "http://example.com/my_script.py"
    urllib.request.urlretrieve(updated_script_url, "my_script.py.new")
    
    # Rename the current script to a backup file
    os.rename("my_script.py", "my_script.py.bak")
    
    # Rename the updated script to the original script name
    os.rename("my_script.py.new", "my_script.py")
    
    print("Update complete. Please restart the script.")
else:
    print("No updates available.")

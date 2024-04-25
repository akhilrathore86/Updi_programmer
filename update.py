import requests
import os
import sys
import hashlib

def get_current_code():
    with open(sys.argv[0], 'r') as file:
        return file.read()

def get_code_hash(code):
    return hashlib.sha256(code.encode()).hexdigest()

def check_for_update():
    # URL of the raw Python script on GitHub
    url = 'https://raw.githubusercontent.com/akhilrathore86/Updi_programmer/main/update.py'
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.text
    except requests.exceptions.RequestException as e:
        print("Error checking for updates:", e)
        return None

def update_script(new_code):
    # Write the new code to a temporary file
    temp_file = 'temp_update_script.py'
    with open(temp_file, 'w') as file:
        file.write(new_code)
    
    # Replace the current script with the updated version
    os.replace(temp_file, sys.argv[0])

if __name__ == "__main__":
    print("Checking for updates...")
    current_code = get_current_code()
    current_hash = get_code_hash(current_code)
    
    new_code = check_for_update()
    if new_code:
        new_hash = get_code_hash(new_code)
        if new_hash != current_hash:
            print("Update available. Updating...")
            update_script(new_code)
            print("Update successful. Restarting...")
            os.execv(sys.executable, [sys.executable] + sys.argv)
        else:
            print("No updates available.")
    else:
        print("Failed to check for updates. Please check your internet connection.")
    print("hello")

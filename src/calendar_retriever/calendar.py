import requests
import hashlib
import os
import configparser
from pathlib import Path
from plyer import notification

def load_config():
    config = configparser.ConfigParser()
    config_path = Path(__file__).parent.parent.parent / 'config.ini'
    
    if not config_path.exists():
        print("Error: config.ini file not found!")
        print("Please create a config.ini file in the project root directory.")
        print("You can copy the example from config.ini.example")
        exit(1)
        
    config.read(config_path)
    return config['Calendar']

def get_file_hash(content):
    return hashlib.md5(content).hexdigest()

def download_calendar():
    try:
        config = load_config()
        ics_url = config['ics_url']
        local_file = config['local_file']
        hash_file = config['hash_file']

        response = requests.get(ics_url)
        response.raise_for_status()
        new_content = response.content

        new_hash = get_file_hash(new_content)

        try:
            with open(hash_file, "r") as f:
                old_hash = f.read().strip()
        except FileNotFoundError:
            old_hash = None

        if os.path.exists(hash_file):
            with open(hash_file, "r") as file:
                old_hash = file.read().strip()

        if new_hash != old_hash:
            with open(local_file, "wb") as file:
                file.write(new_content)
            with open(hash_file, "w") as file:
                file.write(new_hash)
            self.send_notification()
        else:
            print("No updates to the calendar.")
    except Exception as e:
        print(f"An error occurred: {e}")


def send_notification():
    notification.notify(
        title="Calendar Updated",
        message="The calendar has been updated.",
        app_name="Calendar Retriever",
        timeout=10
    )


if __name__ == "__main__":
    download_calendar()

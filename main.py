# main.py

# Imports
import os, json, time
from scripts import display, utility
from scripts.display import clear_screen

# Global Variables
base_url_location_eia = ''
file_type_search_fvb = []
standard_mode_3nc = True
asynchronous_mode_4fn = False
working_directory_vem = ''
TOR_PORT = 9050

# Initialization
def set_working_directory():
    global working_directory_vem
    working_directory_vem = os.path.dirname(os.path.realpath(__file__))
clear_screen()
print("\nScript Initialized...")
time.sleep(2)

# Load Settings
def load_settings():
    global base_url_location_eia, file_type_search_fvb, standard_mode_3nc, asynchronous_mode_4fn
    try:
        with open('settings.json', 'r') as f:
            settings = json.load(f)
            base_url_location_eia = settings.get("base_url_location_eia", "")
            file_type_search_fvb = settings.get("file_type_search_fvb", [])
            standard_mode_3nc = settings.get("standard_mode_3nc", True)
            asynchronous_mode_4fn = settings.get("asynchronous_mode_4fn", False)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No Settings!")

# Save Settings
def save_settings():
    global base_url_location_eia, file_type_search_fvb, standard_mode_3nc, asynchronous_mode_4fn
    settings = {
        "base_url_location_eia": base_url_location_eia,
        "file_type_search_fvb": file_type_search_fvb,
        "standard_mode_3nc": standard_mode_3nc,
        "asynchronous_mode_4fn": asynchronous_mode_4fn
    }
    with open('settings.json', 'w') as f:
        json.dump(settings, f, indent=4)

# Main
def main():
    global base_url_location_eia, file_type_search_fvb, standard_mode_3nc, asynchronous_mode_4fn, working_directory_vem, TOR_PORT
    set_working_directory()
    load_settings()
    clear_screen()

    display.handle_menu(
        base_url_location_eia,
        file_type_search_fvb,
        standard_mode_3nc,
        asynchronous_mode_4fn,
        save_settings,
        display.begin_rip_message,
        lambda *args: utility.scrape_and_download(*args, working_directory_vem, TOR_PORT, display.update_progress),  # Pass the update_progress callback from display.py
        display.exit_message
    )

# Entry Point
if __name__ == "__main__":
    main()

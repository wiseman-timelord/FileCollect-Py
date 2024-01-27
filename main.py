# main.py

# Imports
import json, time
from scripts import display, utility
from scripts.display import clear_screen

# Variables
base_url_location_eia = ''
file_type_search_fvb = []
standard_mode_3nc = True

# Initialization
clear_screen()
print("\nScript Initialized...")
time.sleep(2)

# Load Settings
def load_settings():
    global base_url_location_eia, file_type_search_fvb, standard_mode_3nc
    try:
        with open('settings.json', 'r') as f:
            settings = json.load(f)
            base_url_location_eia = settings.get("base_url_location_eia", "")
            file_type_search_fvb = settings.get("file_type_search_fvb", [])
            standard_mode_3nc = settings.get("standard_mode_3nc", True)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No Settings!")

# Save Settings
def save_settings():
    global base_url_location_eia, file_type_search_fvb, standard_mode_3nc
    settings = {
        "base_url_location_eia": base_url_location_eia,
        "file_type_search_fvb": file_type_search_fvb,
        "standard_mode_3nc": standard_mode_3nc
    }
    with open('settings.json', 'w') as f:
        json.dump(settings, f, indent=4)

# Main
def main():
    global base_url_location_eia, file_type_search_fvb, standard_mode_3nc
    load_settings()
    clear_screen() 
    display.handle_menu(
        base_url_location_eia, 
        file_type_search_fvb, 
        standard_mode_3nc, 
        save_settings,
        display.begin_rip_message,
        utility.scrape_and_download,
        display.exit_message
    )
   
# Entry Point
if __name__ == "__main__":
    main()

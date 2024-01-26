# main.py

import json
from scripts import display, utility

# Global variables
base_url_location_eia = ''
file_type_search_fvb = []
standard_mode_3nc = True  # Default mode set to Standard

def load_settings():
    global base_url_location_eia, file_type_search_fvb, standard_mode_3nc
    try:
        with open('settings.json', 'r') as f:
            settings = json.load(f)
            base_url_location_eia = settings.get("base_url_location_eia", "")
            file_type_search_fvb = settings.get("file_type_search_fvb", [])
            standard_mode_3nc = settings.get("standard_mode_3nc", True)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No existing settings found or file is corrupt. Starting with blank settings.")

def save_settings():
    global base_url_location_eia, file_type_search_fvb, standard_mode_3nc
    settings = {
        "base_url_location_eia": base_url_location_eia,
        "file_type_search_fvb": file_type_search_fvb,
        "standard_mode_3nc": standard_mode_3nc
    }
    with open('settings.json', 'w') as f:
        json.dump(settings, f, indent=4)

def main():
    global base_url_location_eia, file_type_search_fvb, standard_mode_3nc
    load_settings()

    while True:
        choice, base_url_location_eia, file_type_search_fvb, standard_mode_3nc = display.handle_menu(base_url_location_eia, file_type_search_fvb, standard_mode_3nc)
        
        if choice == 'B':
            save_settings()
            display.begin_rip_message(base_url_location_eia)
            utility.scrape_and_download(base_url_location_eia, file_type_search_fvb, not standard_mode_3nc)
        elif choice == 'X':
            save_settings()
            display.exit_message()
            break
            
            
# entry point            
if __name__ == "__main__":
    main()

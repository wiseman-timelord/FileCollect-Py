import json
from scripts import display, utility

# Global variables
base_url_location_eia = ''
file_type_search_fvb = []

def load_settings():
    global base_url_location_eia, file_type_search_fvb
    try:
        with open('settings.json', 'r') as f:
            settings = json.load(f)
            base_url_location_eia = settings.get("base_url", "")
            file_type_search_fvb = settings.get("file_type_search_fvb", [])
    except (FileNotFoundError, json.JSONDecodeError):
        print("No existing settings found or file is corrupt. Starting with blank settings.")

def save_settings():
    global base_url_location_eia, file_type_search_fvb
    settings = {
        "base_url_location_eia": base_url_location_eia,
        "file_type_search_fvb": file_type_search_fvb
    }
    with open('settings.json', 'w') as f:
        json.dump(settings, f, indent=4)

def main():
    global base_url_location_eia, file_type_search_fvb
    load_settings()

    while True:
        display.display_menu()
        choice = input().strip().upper()

        if choice == '1':
            base_url_location_eia = display.get_page_location()
        elif choice == '2':
            file_extension = display.get_file_extension()
            if file_extension and file_extension not in file_type_search_fvb:
                file_type_search_fvb.append(file_extension)
        elif choice in ['B', 'X']:
            save_settings()
            if choice == 'B':
                display.begin_rip_message(base_url_location_eia)
                utility.begin_rip(base_url_location_eia, file_type_search_fvb)
            else:  # 'X' is selected
                display.exit_message()
                break
        else:
            display.invalid_option_message()

if __name__ == "__main__":
    main()

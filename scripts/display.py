# display.py

import os

def display_menu(base_url_location_eia, file_type_search_fvb, standard_mode_3nc):
    mode_text = "Standard Mode" if standard_mode_3nc else "Tor/Onion Mode"
    file_ext_text = ", ".join(file_type_search_fvb) if file_type_search_fvb else "None"

    # Handle empty base_url_location_eia by displaying "None"
    display_url = base_url_location_eia[-62:] if len(base_url_location_eia) > 62 else base_url_location_eia
    url_display_text = f"({display_url if display_url else 'None'})"  # This line is modified

    # Calculate dynamic padding for center alignment
    total_length = 64
    left_padding = (total_length - len(url_display_text)) // 2
    right_padding = total_length - left_padding - len(url_display_text)
    formatted_url = f"{' ' * left_padding}{url_display_text}{' ' * right_padding}"

    print("")
    print("=======================( FileCollector )======================")
    print("\n\n\n")
    print("                      1. Page Location.")
    print(f"{formatted_url}")
    print("")
    print("                       2. File Extension.")
    print(f"                              ({file_ext_text})")
    print("")
    print("                       3. Toggle Privacy")
    print(f"                         ({mode_text})")
    print("\n\n\n")
    print("Select :- Menu Options = 1-3, Begin Rip = B, Exit Menu = X: ", end='')

# In display.py

def handle_menu(base_url_location_eia, file_type_search_fvb, standard_mode_3nc, save_settings_func, begin_rip_message_func, scrape_and_download_func, exit_message_func):
    while True:
        display_menu(base_url_location_eia, file_type_search_fvb, standard_mode_3nc)
        choice = input().strip().upper()

        if choice == '1':
            base_url_location_eia = get_page_location()
        elif choice == '2':
            file_extension = get_file_extension()
            if file_extension and file_extension not in file_type_search_fvb:
                file_type_search_fvb.append(file_extension)
        elif choice == '3':
            standard_mode_3nc = not standard_mode_3nc
        elif choice == 'B':
            save_settings_func()
            begin_rip_message_func(base_url_location_eia)
            scrape_and_download_func(base_url_location_eia, file_type_search_fvb, not standard_mode_3nc)
        elif choice == 'X':
            save_settings_func()
            exit_message_func()
            break
        else:
            invalid_option_message()


def get_page_location():
    print("Enter the URL of the page to scrape: ", end='')
    return input()

def get_file_extension():
    print("Enter the file extension to download (e.g., .pdf, .jpg): ", end='')
    return input()

def begin_rip_message(base_url_location_eia):
    print(f"Starting to scrape and download files from {base_url_location_eia}")

def exit_message():
    print("Exiting FileCollector.")

def invalid_option_message():
    print("Invalid option, please try again.")

def clear_screen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For MacOS and Linux (os.name: 'posix')
    else:
        _ = os.system('clear')
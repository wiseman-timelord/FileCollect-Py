# display.py

# Imports
import os, time

# Tor Errors
error_message_map_sls = {
    FileNotFoundError: "File Not Found",
    json.JSONDecodeError: "Invalid JSON",
    requests.exceptions.HTTPError: "HTTP Error",
    requests.exceptions.RequestException: "Request Failed",
    requests.exceptions.ConnectionError: "Connection Failed",
    aiohttp.ClientError: "Client Error",
    aiohttp.ServerDisconnectedError: "Server Disconnected",
    Exception: "Unexpected Error",
    "tor_not_running": "Tor Unavailable",
    "tor_checking": "Tor Checking",
    "tor_starting": "Tor Starting",
    "tor_retry": "Tor Retry",
    "tor_failed": "Tor Failed",
    "ip_checking": "Checking IP",
    "ip_hidden": "IP Hidden",
    "tor_active": "Tor Active",
    "secure_mode": "Secure Mode",
}

# Functions Begin
def update_progress(filename, downloaded, total, start_time):
    elapsed_time = time.time() - start_time if start_time else 0
    download_speed = downloaded / elapsed_time if elapsed_time > 0 else 0
    remaining_data = total - downloaded
    estimated_total_time = remaining_data / download_speed if download_speed > 0 else 0
    display_progress_bar(filename, downloaded, total, elapsed_time, estimated_total_time)

def format_file_size(size_in_bytes):
    units = ['B', 'KB', 'MB', 'GB', 'TB']
    size = max(size_in_bytes, 0)
    power = min((len(units) - 1), (size.bit_length() - 1) // 10)
    size /= (1024 ** power)
    return "{:.2f}/{}{}".format(size, int(size), units[power])

def format_time(seconds):
    hours, remainder = divmod(int(seconds), 3600)
    minutes, seconds = divmod(remainder, 60)
    return '{:02}:{:02}:{:02}'.format(min(hours, 99), minutes, seconds)

def display_progress_bar(filename, current, total, elapsed_time, estimated_total_time):
    truncated_filename = (filename[:12] + '...') if len(filename) > 15 else filename
    bar_length = 20
    progress = current / total if total > 0 else 0
    filled_length = int(round(bar_length * progress))
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    size_info = format_file_size(current) + '/' + format_file_size(total)
    time_info = format_time(elapsed_time) + '/' + format_time(estimated_total_time)
    sys.stdout.write(f'\r{truncated_filename} [{bar}] {size_info} {time_info}')
    sys.stdout.flush()

def display_inactive_progress_bar(filename, total):
    truncated_filename = (filename[:12] + '...') if len(filename) > 15 else filename
    bar = '?' * 20
    size_info = '???/{}'.format(format_file_size(total))
    time_info = '??/??'
    
    sys.stdout.write(f'\r{truncated_filename} [{bar}] {size_info} {time_info}')
    sys.stdout.flush()

def display_menu(base_url_location_eia, file_type_search_fvb, standard_mode_3nc, asynchronous_mode_4fn):
    mode_text = "Standard Mode" if standard_mode_3nc else "Tor/Onion Mode"
    file_ext_text = ", ".join(file_type_search_fvb) if file_type_search_fvb else "None"
    privacy_mode_text = mode_text
    asynchronous_mode_4fn_text = "Enabled" if asynchronous_mode_4fn else "Disabled"
    display_url = base_url_location_eia[-62:] if len(base_url_location_eia) > 62 else base_url_location_eia
    url_display_text = f"({display_url if display_url else 'None'})"  # This line is modified
    total_length = 64
    left_padding = (total_length - len(url_display_text)) // 2
    right_padding = total_length - left_padding - len(url_display_text)
    formatted_url = f"{' ' * left_padding}{url_display_text}{' ' * right_padding}"

    print("")
    print("=======================( FilesCollect )=======================")
    print("\n\n\n")
    print("                   1. Content Page Location")
    print(f"{formatted_url}")
    print("")
    print("                    2. File Extension Type")
    print(f"                              ({file_ext_text})")
    print("")
    print("                    3. Network Privacy Modes")
    print(f"                      ({privacy_mode_text})")
    print("")
    print("                      4. Multi-Thread Modes")
    print(f"                      ({asynchronous_mode_4fn_text})")
    print("") 
    print("                      5. Random Timer Delay")
    print(f"                          ({random_delay_r5y})")
    print("")
    print("                      6. Set Tor Port Number")
    print(f"                            ({TOR_PORT})")
    print("\n\n\n")
    print("Select :- Menu Options = 1-6, Begin Scrape = B, Exit Menu = X: ", end='')

def handle_menu(base_url_location_eia, file_type_search_fvb, standard_mode_3nc, asynchronous_mode_4fn, random_delay_r5y, TOR_PORT, save_settings_func, begin_rip_message_func, scrape_and_download_func, exit_message_func):
    while True:
        display_menu(base_url_location_eia, file_type_search_fvb, standard_mode_3nc, asynchronous_mode_4fn, random_delay_r5y, TOR_PORT) 
        choice = input().strip().upper()
        if choice == '1':
            base_url_location_eia = get_page_location()
        elif choice == '2':
            file_extension = get_file_extension()
            if file_extension and file_extension not in file_type_search_fvb:
                file_type_search_fvb.append(file_extension)
        elif choice == '3':
            standard_mode_3nc = not standard_mode_3nc
        elif choice == '4':
            asynchronous_mode_4fn = not asynchronous_mode_4fn
        elif choice == '5':
            print("Set Random Delay (Options: Off/15/30/60/120/240/480): ", end='')
            new_delay = input().strip()
            if new_delay in ['Off', '15', '30', '60', '120', '240', '480']:
                random_delay_r5y = new_delay
                print(f"Random delay set to {random_delay_r5y}")
            else:
                print("Invalid option, please choose from Off/15/30/60/120/240/480.")    
        elif choice == '6':
            print("Enter Port Number: ", end='')
            new_port = input()
            if new_port.isdigit():
                TOR_PORT = int(new_port)
                print(f"Tor port number set to {TOR_PORT}")
            else:
                print("Invalid Port, Enter Port.")
        elif choice == 'B':
            save_settings_func()
            begin_rip_message_func(base_url_location_eia)
            scrape_and_download_func(base_url_location_eia, file_type_search_fvb, not standard_mode_3nc, asynchronous_mode_4fn, TOR_PORT)
        elif choice == 'X':
            save_settings_func()
            exit_message_func()
            break
        else:
            invalid_option_message()

def get_page_location():
    print("Enter the page URL: ", end='')
    return input()

def get_file_extension():
    print("Enter file extension (e.g. .pdf, .jpg): ", end='')
    return input()

def begin_rip_message(base_url_location_eia):
    print(f"Starting to scrape and download files from {base_url_location_eia}")

def exit_message():
    print("Exiting FileCollector.")

def invalid_option_message():
    print("Invalid option, please try again.")

def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

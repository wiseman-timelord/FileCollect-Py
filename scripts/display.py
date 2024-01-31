# display.py

# Imports
import os, time, json, sys, requests, aiohttp, psutil

# clear screen
def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

# initialization complete
def script_initialization():
    clear_screen()
    print("\nScript Initialized...")
    time.sleep(2)

# Tor Errors
error_msgs = {
    FileNotFoundError: "File Not Found",
    json.JSONDecodeError: "Invalid JSON",
    requests.exceptions.HTTPError: "HTTP Error",
    requests.exceptions.RequestException: "Request Failed",
    requests.exceptions.ConnectionError: "Connection Failed",
    aiohttp.ClientError: "Client Error",
    aiohttp.ServerDisconnectedError: "Server Disconnected",
    Exception: "Unexpected Error",
    "tor_not_running": "Tor Unavailable",
    "tor_failed": "Tor Failed",
    "ip_checking": "Checking IP",
    "ip_hidden": "IP Hidden",
    "tor_active": "Tor Active",
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

def display_progress_bar(filename, current, total, elapsed_time, estimated_total_time, update_interval=1):
    global last_update_time
    if not 'last_update_time' in globals():
        last_update_time = 0
    if time.time() - last_update_time > update_interval:
        truncated_filename = (filename[:12] + '...') if len(filename) > 15 else filename
        bar_length = 20
        progress = current / total if total > 0 else 0
        filled_length = int(round(bar_length * progress))
        bar = '█' * filled_length + '-' * (bar_length - filled_length)
        size_info = format_file_size(current) + '/' + format_file_size(total)
        time_info = format_time(elapsed_time) + '/' + format_time(estimated_total_time)
        sys.stdout.write(f'\r{truncated_filename} [{bar}] {size_info} {time_info}')
        sys.stdout.flush()
        last_update_time = time.time()

def display_inactive_progress_bar(filename, total):
    truncated_filename = (filename[:12] + '...') if len(filename) > 15 else filename
    bar = '?' * 20
    size_info = '???/{}'.format(format_file_size(total))
    time_info = '??/??'
    sys.stdout.write(f'\r{truncated_filename} [{bar}] {size_info} {time_info}')
    sys.stdout.flush()

def display_menu(config):
    mode_text = "Standard Mode" if config.standard_mode else "Tor/Onion Mode"
    file_ext_text = ", ".join(config.file_type_search_fvb) if config.file_type_search_fvb else "None"
    privacy_mode_text = mode_text
    asynchronous_mode_text = "Enabled" if config.asynchronous_mode else "Disabled"
    display_url = config.base_url_location_eia[-62:] if len(config.base_url_location_eia) > 62 else config.base_url_location_eia
    url_display_text = f"({display_url if display_url else 'None'})"
    total_length = 62
    left_padding = (total_length - len(url_display_text)) // 2
    right_padding = total_length - left_padding - len(url_display_text)
    formatted_url = f"{' ' * left_padding}{url_display_text}{' ' * right_padding}"

    clear_screen()
    print("")
    print("=======================( FilesCollect )=======================")
    print("\n\n\n")
    print("                   1. Content Page Location")
    print(f"{formatted_url}")
    print("")
    print("                   2. File Extension Type")
    print(f"                            ({file_ext_text})")
    print("")
    print("                   3. Network Privacy Modes")
    print(f"                        ({privacy_mode_text})")
    print("")
    print("                    4. Multi-Thread Modes")
    print(f"                          ({asynchronous_mode_text})")
    print("") 
    print("                    5. Random Timer Delay")
    print(f"                             ({config.random_delay_r5y})")
    print("")
    print("                    6. Set Tor Port Number")
    print(f"                            ({config.tor_port})")
    print("\n\n\n")
    print("Select:- Options = 1-6, Begin = B, Exit = X: ", end='')

def handle_menu(config, save_settings_func, scrape_and_download_func):
    while True:
        display_menu(config)
        choice = input().strip().upper()
        if choice == '1':
            config.base_url_location_eia = get_page_location()
        elif choice == '2':
            file_extension = get_file_extension()
            if file_extension and file_extension not in config.file_type_search_fvb:
                config.file_type_search_fvb.append(file_extension)
        elif choice == '3':
            config.standard_mode = not config.standard_mode
        elif choice == '4':
            config.asynchronous_mode = not config.asynchronous_mode
        elif choice == '5':
            update_random_delay(config)
        elif choice == '6':
            print("Enter Port Number: ", end='')
            new_port = input().strip()
            time.sleep(1)
            if new_port.isdigit() and 1024 <= int(new_port) <= 65535:
                config.tor_port = int(new_port)
                print(f"...Tor port number set to {config.tor_port}")
            else:
                print("Invalid Port. Please enter a number between 1024 and 65535.")
                time.sleep(2)
        elif choice == 'B':
            clear_screen()
            print("\nBeginning Processes..")
            time.sleep(2)
            save_settings_func(config)  # Save settings before beginning the scrape
            print("..Saving Settings..")
            time.sleep(1)
            print("..Begin Scrape..")
            time.sleep(2)
            begin_rip_message_func(config.base_url_location_eia)
            time.sleep(1)
            scrape_and_download_func(
                config
            )
            print("..Scrape Finished.")
            time.sleep(2)
        elif choice == 'X':
            save_settings_func(config)
            exit_message()
            time.sleep(1)
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

def update_random_delay(config):
    config.current_delay_index_3vs = (config.current_delay_index_3vs + 1) % len(config.delay_options_7fu)
    config.random_delay_r5y = config.delay_options_7fu[config.current_delay_index_3vs]
    print(f"...Random delay set to {config.random_delay_r5y} seconds.")
    time.sleep(1)

def display_final_summary(config):
    if config.total_time_elapsed_4vd > 0:
        config.current_score_9fr = (config.total_files_downloaded_vr5 / config.total_time_elapsed_4vd) * 100
    first_time = False
    if config.low_score_3hf == 0 and config.high_score_6hd == 0:
        config.low_score_3hf, config.high_score_6hd = config.current_score_9fr, config.current_score_9fr
        first_time = True
    new_high_score = False
    if config.current_score_9fr > config.high_score_6hd:
        config.high_score_6hd = config.current_score_9fr
        new_high_score = True
    new_low_score = False
    if config.current_score_9fr < config.low_score_3hf:
        config.low_score_3hf = config.current_score_9fr
        new_low_score = True
    save_settings(config)
    print("\n==================== Final Summary Stats ====================")
    if first_time:
        print(f"First Score: {current_score:.2f}")
    else:
        if new_high_score:
            print(f"New High Score: {current_score:.2f}")
        elif new_low_score:
            print(f"New Low Score: {current_score:.2f}")
        else:
            print(f"Average Score: {current_score:.2f}")
    print(f"Total Files Downloaded: {total_files_downloaded_vr5}")
    print(f"Total Time Elapsed: {total_time_elapsed_4vd} seconds")
    print("=============================================================")
    input("Press any key to return to the menu...")
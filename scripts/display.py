# display.py

def display_menu():
    print("")
    print("=======================( FileCollector )======================")
    print("\n\n\n")
    print("                    1. Enter Page Location.")
    print("")
    print("                    2. Enter File Extension.")
    print("\n\n\n")
    print("Select :- Menu Options = 1-2, Begin Rip = B, Exit Menu = X: ", end='')

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

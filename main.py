# main.py

# Imports
import os, json, time
from scripts import display, utility
from scripts.display import clear_screen

# Global Variables
working_directory_vem = ''
base_url_location_eia = ''
file_type_search_fvb = []
standard_mode_3nc = True
asynchronous_mode_4fn = False
random_delay_r5y = "15"
low_score_3hf = 0
high_score_6hd = 0
total_files_downloaded_vr5 = 0
total_time_elapsed_4vd = 0
delay_options_7fu = ['15', '30', '60', '120', '240', '480']
current_delay_index_3vs = 0
current_score_9fr = 0.0
TOR_PORT = 9050

# Initialization
def set_working_directory():
    global working_directory_vem
    working_directory_vem = os.path.dirname(os.path.realpath(__file__))
clear_screen()
print("\nScript Initialized...")
time.sleep(2)

class Config:
    def __init__(self):
        self.working_directory = os.path.dirname(os.path.realpath(__file__))
        self.base_url_location = ''
        self.file_type_search = []
        self.standard_mode = True
        self.asynchronous_mode = False
        self.random_delay = "15"
        self.low_score = float('inf')
        self.high_score = 0.0
        self.total_files_downloaded_vr5 = 0
        self.total_time_elapsed_4vd = 0
        self.delay_options_7fu = ['15', '30', '60', '120', '240', '480']
        self.current_delay_index_3vs = 0
        self.current_score_9fr = 0.0
        self.tor_port = 9050
config = Config()


# Main
def main():
    global base_url_location_eia, file_type_search_fvb, standard_mode_3nc, asynchronous_mode_4fn, working_directory_vem, TOR_PORT, low_score_3hf, high_score_6hd, total_files_downloaded_vr5, total_time_elapsed_4vd, current_score_9fr
    set_working_directory()
    load_settings(config)
    clear_screen()
    display.handle_menu(config, save_settings, utility.scrape_and_download)
    current_score_9fr = (total_files_downloaded_vr5 / total_time_elapsed_4vd) * 100 if total_time_elapsed_4vd > 0 else 0
    display.display_final_summary(low_score_3hf, high_score_6hd, total_files_downloaded_vr5, total_time_elapsed_4vd, current_score_9fr)
    
# Entry Point
if __name__ == "__main__":
    main()

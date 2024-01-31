# main.py

# Imports
import os, json, time, asyncio
from scripts import display, utility, manage
from scripts.display import clear_screen
from scripts.utility import load_settings, save_settings
from scripts.manage import scrape_and_download

# Global Variables
working_directory_vem = ''
total_files_downloaded_vr5 = 0
total_time_elapsed_4vd = 0
delay_options_7fu = ['15', '30', '60', '120', '240', '480']
current_delay_index_3vs = 0
current_score_9fr = 0.0
progress_lock_6hg = asyncio.Lock()

# Config Class
class Config:
    def __init__(self):
        self.working_directory = os.path.dirname(os.path.realpath(__file__))
        self.base_url_location = ''
        self.file_type_search = []
        self.standard_mode = True
        self.max_concurrent_downloads_6d3 = 1
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

# Initialization
def set_working_directory(config):
    config.working_directory_vem = os.path.dirname(os.path.realpath(__file__))

# Main
def main():
    config = Config()
    set_working_directory(config)
    load_settings(config)
    display.script_initialization()
    clear_screen()
    display.handle_menu(config, save_settings, scrape_and_download)
    config.current_score_9fr = (config.total_files_downloaded_vr5 / config.total_time_elapsed_4vd) * 100 if config.total_time_elapsed_4vd > 0 else 0
    display.display_final_summary(config)
    
# Entry Point
if __name__ == "__main__":
    main()

# utility.py

# Imports
import os, asyncio, aiohttp, requests, psutil, subprocess, time, random, json, random
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from torpy.http.adapter import TorHttpAdapter
from torpy import TorClient
from scripts.display import display_progress_bar, error_msgs



# Handle Errors
def handle_error(e):
    return error_msgs.get(type(e), "Error Occurred")

# Simplified Directory Creation
def create_dir_from_url(url):
    try:
        path = urlparse(url).path.lstrip('/').rsplit('.', 1)[0]
        return os.path.join(*path.split('/'))
    except Exception as e:
        print(f"Error parsing URL: {e}")
        return None

# Load Settings
def load_settings(config):
    try:
        with open('settings.json', 'r') as f:
            settings = json.load(f)
            config.base_url_location_eia = settings.get("base_url_location_eia", "")
            config.file_type_search_fvb = settings.get("file_type_search_fvb", [])
            config.standard_mode_3nc = settings.get("standard_mode_3nc", True)
            config.asynchronous_mode_4fn = settings.get("asynchronous_mode_4fn", False)
            config.random_delay_r5y = settings.get("random_delay_r5y", "Off")
            config.low_score_3hf = settings.get("low_score_3hf", 0.0)
            config.high_score_6hd = settings.get("high_score_6hd", 0.0)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Settings Corrupted! Using Default.")
        config.base_url_location_eia = ""
        config.file_type_search_fvb = []
        config.standard_mode_3nc = True
        config.asynchronous_mode_4fn = False
        config.random_delay_r5y = "Off"
        config.low_score_3hf = 0
        config.high_score_6hd = 0

# Save Settings
def save_settings(config):
    settings = {
        "base_url_location_eia": config.base_url_location,
        "file_type_search_fvb": config.file_type_search,
        "standard_mode_3nc": config.standard_mode,
        "asynchronous_mode_4fn": config.asynchronous_mode,
        "random_delay_r5y": config.random_delay,
        "low_score_3hf": config.low_score,
        "high_score_6hd": config.high_score,
        "TOR_PORT": config.tor_port
    }
    with open('settings.json', 'w') as f:
        json.dump(settings, f, indent=4)

def get_random_delay(random_delay_r5y):
    base_delay = 15
    max_additional_time = int(random_delay_r5y)
    total_delay = base_delay + random.randint(0, max_additional_time)
    return total_delay


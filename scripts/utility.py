# utility.py

# Imports
import os, asyncio, aiohttp, requests, psutil, subprocess, time, random
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from torpy.http.adapter import TorHttpAdapter
from torpy import TorClient
from scripts.display import display_progress_bar, error_message_map_sls

# Functions
def format_error_message(exception):
    return error_message_map_sls.get(type(exception), "Error Occurred")

def create_directory_from_url(url):
    try:
        parsed_url = urlparse(url)
        path = parsed_url.path
        clean_path = path.lstrip('/').rsplit('.', 1)[0]
        return os.path.join(*clean_path.split('/'))
    except Exception as e:
        print(f"Error in parsing URL '{url}': {e}")
        return None


async def download_file(session, url, directory, semaphore, progress_callback):
    async with semaphore:
        local_filename = url.split('/')[-1]
        path = os.path.join(directory, local_filename)
        try:
            async with session.get(url) as response:
                response.raise_for_status()
                total_size = int(response.headers.get('content-length', 0))
                downloaded = 0
                with open(path, 'wb') as f:
                    while True:
                        chunk = await response.content.read(8192)
                        if not chunk:
                            break
                        f.write(chunk)
                        downloaded += len(chunk)
                        progress_callback(local_filename, downloaded, total_size)
            print(f"Downloaded {local_filename}")
        except Exception as e:
            print(format_error_message(e))

def is_tor_running(port):
    try:
        for conn in psutil.net_connections(kind='tcp'):
            if conn.laddr.port == port and conn.status == psutil.CONN_LISTEN:
                return True
        return False
    except Exception as e:
        print(format_error_message(e))
        return False

def is_tor_ready(port):
    for i in range(30):
        for conn in psutil.net_connections(kind='tcp'):
            if conn.laddr.port == port and conn.status == psutil.CONN_LISTEN:
                return True
        time.sleep(1)
    return False

def start_tor_service(working_directory_vem, port):
    original_ip = get_current_ip()
    print(error_message_map_sls["ip_checking"])
    tor_executable = 'tor.exe' if os.name == 'nt' else 'tor'
    tor_path = os.path.join(working_directory_vem, 'libraries', 'tor-expert-bundle', 'tor', tor_executable)
    try:
        print(error_message_map_sls["tor_starting"])
        subprocess.Popen(tor_path)
        if is_tor_ready(port):
            print(error_message_map_sls["tor_active"])
            check_ip_change(original_ip)
        else:
            print(error_message_map_sls["tor_failed"])
    except Exception as e:
        print(format_error_message(e))


async def download_file(session, url, directory, semaphore, progress_callback, start_time=None):
    async with semaphore:
        local_filename = url.split('/')[-1]
        path = os.path.join(directory, local_filename)
        try:
            async with session.get(url) as response:
                response.raise_for_status()
                total_size = int(response.headers.get('content-length', 0))
                downloaded = 0
                with open(path, 'wb') as f:
                    while True:
                        chunk = await response.content.read(8192)
                        if not chunk:
                            break
                        f.write(chunk)
                        downloaded += len(chunk)
                        progress_callback(local_filename, downloaded, total_size, start_time)
            print(f"Downloaded {local_filename}")
        except Exception as e:
            print(format_error_message(e))

async def scrape_and_download(base_url_location_eia, file_types, use_tor, asynchronous_mode_4fn, working_directory_vem, TOR_PORT, progress_callback, random_delay_r5y):
    try:
        directory = create_directory_from_url(base_url_location_eia)
        if directory is None:
            return

        full_path = os.path.join(working_directory_vem, 'downloads', directory)
        if not os.path.exists(full_path):
            os.makedirs(full_path)

        session = aiohttp.ClientSession() if asynchronous_mode_4fn else requests.Session()
        if use_tor:
            if not is_tor_running(TOR_PORT):
                start_tor_service(working_directory_vem, TOR_PORT)

            session.proxies = {
                'http': f'socks5h://localhost:{TOR_PORT}',
                'https': f'socks5h://localhost:{TOR_PORT}'
            }
        start_time = time.time()
        if asynchronous_mode_4fn:
            download_semaphore = asyncio.Semaphore(2)
            try:
                async with session.get(base_url_location_eia) as response:
                    response.raise_for_status()
                    text = await response.text()
                soup = BeautifulSoup(text, 'html.parser')
                tasks = []
                for href in soup.find_all('a', href=True):
                    if any(href.endswith(file_type) for file_type in file_types):
                        await asyncio.sleep(get_random_delay(random_delay_r5y))  # Apply random delay here
                        task = download_file(
                            session,
                            urljoin(base_url_location_eia, href),
                            full_path,
                            download_semaphore,
                            progress_callback,
                            start_time
                        )
                        tasks.append(task)
                await asyncio.gather(*tasks)
            except Exception as e:
                print(format_error_message(e))
        else:
            try:
                response = session.get(base_url_location_eia)
                response.raise_for_status()
                soup = BeautifulSoup(response.text, 'html.parser')
                for link in soup.find_all('a', href=True):
                    href = link['href']
                    if any(href.endswith(file_type) for file_type in file_types):
                        time.sleep(get_random_delay(random_delay_r5y))  # Apply random delay here
                        download_file_sync(
                            session,
                            urljoin(base_url_location_eia, href),
                            full_path,
                            progress_callback,
                            start_time
                        )
            except Exception as e:
                print(format_error_message(e))
            finally:
                session.close()
    except Exception as e:
        print(format_error_message(e))
    finally:
        if asynchronous_mode_4fn and session:
            await session.close()


def download_file_sync(session, url, directory, progress_callback, start_time=None):
    local_filename = url.split('/')[-1]
    path = os.path.join(directory, local_filename)
    try:
        response = session.get(url, stream=True)
        response.raise_for_status()
        total_size = int(response.headers.get('content-length', 0))
        downloaded = 0
        with open(path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    progress_callback(local_filename, downloaded, total_size, start_time)
        print(f"Downloaded {local_filename}")
    except Exception as e:
        print(format_error_message(e))

def get_current_ip():
    try:
        response = requests.get('https://api.ipify.org')  # Using ipify API for example
        if response.status_code == 200:
            return response.text
    except Exception as e:
        print(format_error_message(e))
    return None

def check_ip_change(original_ip):
    new_ip = get_current_ip()
    if new_ip and new_ip != original_ip:
        print(error_message_map_sls["ip_hidden"])  # IP Hidden
    else:
        print(error_message_map_sls["ip_unchanged"])  # IP Unchanged

def get_random_delay(random_delay_r5y):
    if random_delay_r5y == 'Off':
        return 0
    else:
        max_additional_time = int(random_delay_r5y)
        return random.randint(1, max_additional_time)
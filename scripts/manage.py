# manage.py

from urllib.parse import urljoin
from .tor_utility import is_tor_running, start_tor_service

# Unified download function
async def download_file(session, url, directory, config, semaphore, progress_callback, start_time=None):
    local_filename, path = url.split('/')[-1], os.path.join(directory, url.split('/')[-1])
    try:
        if async_mode:
            async with semaphore, session.get(url) as response:
                await handle_response(response, path, progress_callback, local_filename, start_time)
        else:
            with session.get(url, stream=True) as response:
                handle_response(response, path, progress_callback, local_filename, start_time)
        print(f"Downloaded {local_filename}")
    except aiohttp.ClientError as e:
        print(f"AIOHttp Client Error: {str(e)}")
        time.sleep(2)
    except requests.exceptions.RequestException as e:
        print(f"Requests Error: {str(e)}")
        time.sleep(2)

async def handle_response(response, path, progress_callback, local_filename, start_time=None):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    response.raise_for_status()
    total_size = int(response.headers.get('content-length', 0))
    downloaded = 0
    if os.path.exists(path):
        downloaded = os.path.getsize(path)
        if downloaded == total_size:
            print(f"File {local_filename} already downloaded. Skipping...")
            return
    with open(path, 'wb') as f:
        if downloaded > 0:
            f.seek(downloaded)
        while True:
            chunk = await response.content.read(8192) if start_time else await response.content.read(8192)
            if not chunk:
                break
            f.write(chunk)
            downloaded += len(chunk)
            progress_callback(local_filename, downloaded, total_size, start_time)

# Tor handling and IP checking
def handle_tor(working_directory_vem, port):
    original_ip, tor_executable = get_current_ip(), 'tor.exe' if os.name == 'nt' else 'tor'
    tor_path = os.path.join(working_directory_vem, 'libraries', 'tor-expert-bundle', 'tor', tor_executable)
    if not is_tor_ready(port):
        try:
            subprocess.Popen(tor_path)
            print("Starting Tor...")
            time.sleep(10)  # Wait for Tor to initialize
            if is_tor_ready(port):
                print("Tor Active")
                check_ip_change(original_ip)
            else:
                print("Failed to start Tor.")
        except OSError as e:
            print(f"Tor startup failed: {str(e)}")
            print("Please ensure the Tor executable is correctly installed and the path is specified.")
        
    else:
        print("Tor is already running.")
    time.sleep(2)



async def scrape_and_download(config):
    try:
        directory, full_path = setup_download_directory(config.base_url_location_eia, config.working_directory_vem)
        if not directory:
            print("Check URL and Dir rights.")
            return
        if config.max_concurrent_downloads_6d3 > 1:
            async with aiohttp.ClientSession() as session:
                setup_session_proxies(session, not config.standard_mode_3nc,     config.TOR_PORT, config.working_directory_vem)
                await handle_async_downloads(session, config, full_path)
        else:
            with requests.Session() as session:
                setup_session_proxies(session, not config.standard_mode_3nc, config.TOR_PORT, config.working_directory_vem)
                handle_sync_downloads(session, config, full_path)
    except Exception as e:
        print(format_error_message(e))





async def update_progress_with_lock(filename, downloaded, total, start_time):
    async with progress_lock_6hg:
        update_progress(filename, downloaded, total, start_time)

def handle_sync_downloads(session, config, full_path):
    try:
        response = session.get(config.base_url_location_eia)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        for link in soup.find_all('a', href=True):
            href = link['href']
            if should_download(href, config.file_type_search_fvb):
                time.sleep(get_random_delay(config.random_delay_r5y))  # Apply random delay before starting each download
                download_file_sync(session, urljoin(config.base_url_location_eia, href), full_path, update_progress)
    except Exception as e:
        print(format_error_message(e))

async def handle_async_downloads(session, config, full_path):
    download_semaphore = asyncio.Semaphore(config.max_concurrent_downloads_6d3)
    try:
        async with session.get(config.base_url_location_eia) as response:
            response.raise_for_status()
            text = await response.text()
        soup = BeautifulSoup(text, 'html.parser')
        tasks = []
        for href in soup.find_all('a', href=True):
            if should_download(href['href'], config.file_type_search_fvb):
                url = urljoin(config.base_url_location_eia, href['href'])
                delay = get_random_delay(config.random_delay_r5y)
                task = asyncio.create_task(
                    download_with_delay(
                        session,
                        url,
                        full_path,
                        download_semaphore,
                        update_progress_with_lock,
                        delay
                    )
                )
                tasks.append(task)
        await asyncio.gather(*tasks)
    except Exception as e:
        print(format_error_message(e))


async def download_with_delay(session, url, directory, semaphore, progress_callback, delay):
    await asyncio.sleep(delay)
    await download_file(session, url, directory, config, semaphore, progress_callback)

def setup_download_directory(base_url_location_eia, working_directory_vem):
    directory = create_dir_from_url(base_url_location_eia)
    if directory is None:
        return None, None
    full_path = os.path.join(working_directory_vem, 'downloads', directory)
    if not os.path.exists(full_path):
        os.makedirs(full_path)
    return directory, full_path

def setup_session_proxies(session, use_tor, TOR_PORT, working_directory_vem):
    if use_tor:
        if not is_tor_running(TOR_PORT):
            start_tor_service(working_directory_vem, TOR_PORT)
        session.proxies = {'http': f'socks5h://localhost:{TOR_PORT}', 'https': f'socks5h://localhost:{TOR_PORT}'}

def should_download(href, file_types):
    return any(href.endswith(file_type) for file_type in file_types)

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
        print("Sync Download Error")
        time.sleep(2)

def get_current_ip():
    try:
        response = requests.get('https://api.ipify.org')
        if response.status_code == 200:
            return response.text
    except Exception as e:
        print("IP Error")
        time.sleep(2)
    return None

def check_ip_change(original_ip):
    new_ip = get_current_ip()
    if new_ip and new_ip != original_ip:
        print("IP Hidden")
        time.sleep(2)
    else:
        print("IP Unchanged")
        time.sleep(2)
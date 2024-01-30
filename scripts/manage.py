# manage.py

# Unified download function
async def download_file(session, url, config, semaphore, progress_callback, async_mode=True, start_time=None):
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

def handle_response(response, path, progress_callback, local_filename, start_time=None):
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
            chunk = await response.content.read(8192) if start_time else response.content.read(8192)
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
    else:
        print("Tor is already running.")
    time.sleep(2)



async def scrape_and_download(base_url_location_eia, file_types, use_tor, asynchronous_mode_4fn, working_directory_vem, TOR_PORT, progress_callback, random_delay_r5y):
    try:
        directory, full_path = setup_download_directory(base_url_location_eia, working_directory_vem)
        if not directory:
            return

        async with aiohttp.ClientSession() as session if asynchronous_mode_4fn else requests.Session() as session:
            setup_session_proxies(session, use_tor, TOR_PORT, working_directory_vem)

            if asynchronous_mode_4fn:
                await handle_async_downloads(session, base_url_location_eia, file_types, full_path, progress_callback, random_delay_r5y)
            else:
                handle_sync_downloads(session, base_url_location_eia, file_types, full_path, progress_callback, random_delay_r5y)

    except Exception as e:
        print(format_error_message(e))

async def handle_async_downloads(session, base_url_location_eia, file_types, full_path, progress_callback, random_delay_r5y):
    download_semaphore = asyncio.Semaphore(2)
    try:
        async with session.get(base_url_location_eia) as response:
            response.raise_for_status()
            text = await response.text()
        soup = BeautifulSoup(text, 'html.parser')
        tasks = [
            asyncio.create_task(
                handle_download(
                    session, 
                    urljoin(base_url_location_eia, href['href']), 
                    full_path, 
                    download_semaphore, 
                    progress_callback, 
                    await get_random_delay(random_delay_r5y)  # Apply random delay before starting each download
                )
            ) for href in soup.find_all('a', href=True) if should_download(href['href'], file_types)
        ]
        await asyncio.gather(*tasks)
    except Exception as e:
        print(format_error_message(e))


def handle_sync_downloads(session, base_url_location_eia, file_types, full_path, progress_callback, random_delay_r5y):
    try {
        response = session.get(base_url_location_eia)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        for link in soup.find_all('a', href=True):
            href = link['href']
            if should_download(href, file_types):
                time.sleep(get_random_delay(random_delay_r5y))  # Apply random delay before starting each download
                download_file_sync(session, urljoin(base_url_location_eia, href), full_path, progress_callback)
    except Exception as e:
        print(format_error_message(e))


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
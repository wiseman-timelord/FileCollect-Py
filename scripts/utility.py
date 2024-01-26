import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from torpy.http.adapter import TorHttpAdapter
from torpy import TorClient

def create_directory_from_url(url):
    try:
        parsed_url = urlparse(url)
        path = parsed_url.path
        clean_path = path.lstrip('/').rsplit('.', 1)[0]
        return clean_path.replace('/', '_')
    except Exception as e:
        print(f"Error in parsing URL '{url}': {e}")
        return None

def get_standard_session():
    return requests.Session()

def get_tor_session():
    session = requests.Session()
    session.mount('http://', TorHttpAdapter())
    session.mount('https://', TorHttpAdapter())
    return session

def scrape_and_download(base_url_location_eia, file_types, use_tor):
    session = get_tor_session() if use_tor else get_standard_session()
    directory = create_directory_from_url(base_url_location_eia)
    if directory is None:
        return

    full_path = os.path.join('./downloads', directory)
    if not os.path.exists(full_path):
        os.makedirs(full_path)

    try:
        response = session.get(base_url_location_eia)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred while scraping {base_url_location_eia}: {e}")
        return
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while scraping {base_url_location_eia}: {e}")
        return

    try:
        soup = BeautifulSoup(response.text, 'html.parser')
    except Exception as e:
        print(f"Error parsing HTML from {base_url_location_eia}: {e}")
        return

    for link in soup.find_all('a', href=True):
        href = link['href']
        if any(href.endswith(file_type) for file_type in file_types):
            download_file(urljoin(base_url_location_eia, href), full_path, use_tor)

def download_file(url, directory, use_tor):
    session = get_tor_session() if use_tor else get_standard_session()
    try:
        local_filename = url.split('/')[-1]
        path = os.path.join(directory, local_filename)

        response = session.get(url, stream=True)
        response.raise_for_status()

        try:
            with open(path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            print(f"Downloaded {local_filename}")
        except IOError as e:
            print(f"Error writing file {local_filename}: {e}")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred while downloading {url}: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while downloading {url}: {e}")

# utility.py

import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin, urlparse

def create_directory_from_url(url):
    parsed_url = urlparse(url)
    path = parsed_url.path
    clean_path = path.lstrip('/').rsplit('.', 1)[0]
    directory_name = clean_path.replace('/', '_')
    return directory_name

def scrape_and_download(base_url_location_eia, file_types):
    try:
        directory = create_directory_from_url(base_url_location_eia)
        full_path = os.path.join('./downloads', directory)
        if not os.path.exists(full_path):
            os.makedirs(full_path)
        response = requests.get(base_url_location_eia)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        for link in soup.find_all('a', href=True):
            href = link['href']
            if any(href.endswith(file_type) for file_type in file_types):
                download_file(urljoin(base_url_location_eia, href), full_path)
    except Exception as e:
        print(f"Error scraping {base_url_location_eia}: {e}")

def download_file(url, directory):
    try:
        local_filename = url.split('/')[-1]
        path = os.path.join(directory, local_filename)
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192): 
                    f.write(chunk)
        print(f"Downloaded {local_filename}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

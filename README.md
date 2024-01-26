# FileCollect-Py

### STATUS
NOT WORKING!
- Under development, early stages, description coming, may be done later today, depends on the difficulty of onion/tor configuration...

## DESCRIPTION
FileCollect-Py is a robust and user-friendly application designed to streamline the process of collecting files from the web. Through an intuitive menu-driven interface, users can specify the target webpage and desired file types. The program intelligently manages user settings, persisting them across sessions for convenience. With sophisticated web scraping capabilities, FileCollect-Py efficiently downloads specified file types, organizing them in a custom directory structure that mirrors the webpage's URL. Enhanced with comprehensive error handling, FileCollect-Py ensures reliability and ease of use, making it an indispensable tool for automated file collection tasks.

### FEATURES
- **Interactive Menu**: FileCollect-Py employs an interactive menu system, allowing users to enter the URL of the page they want to scrape and specify file extensions of interest.
- **Persistent Settings**: The program uses a `settings.json` file to persistently store and retrieve user preferences like the base URL and desired file types, providing a seamless user experience across sessions.
- **Scraping and Downloading**: FileCollect-Py is capable of scraping web pages for specified file types and downloading them efficiently, organizing the downloads in directories named after the structure of the provided URL.
- **Container Extration**: The utility module generates a unique directory structure for downloaded files based on the webpage's URL, ensuring organized storage and easy retrieval of collected files.

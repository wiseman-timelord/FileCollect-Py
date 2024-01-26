# FilesCollect-Py

### STATUS
Development. Remaining tasks are...
- Error "No existing settings found or file is corrupt. Starting with blank settings.
", solution replace with "None" for blank values from json for "1. Page Location.".
- develop tor/onion features to completion: 1) is everything present that needs to be. 2) possibly requires login period after pressing b to begin start, with progress display, ie "Connecting To Onion.."? 
- progress during download of file: 1) list all filtered files, 2) one by one display "Downloading: examplefilename.pdf", "Completed: examplefilename". 3) final summary stats, completed, failed. 
- format menu 100% correctly. 
- check everything over.
- run live tests & bugfix.
- Finish documentation.

## DESCRIPTION
FilesCollect-Py is a robust and user-friendly application designed to streamline the process of collecting files from the web. Through an intuitive menu-driven interface, users can specify the target webpage and desired file types. The program intelligently manages user settings, persisting them across sessions for convenience. With sophisticated web scraping capabilities, FilesCollect-Py efficiently downloads specified file types, organizing them in a custom directory structure that mirrors the webpage's URL. Enhanced with comprehensive error handling, FilesCollect-Py ensures reliability and ease of use, making it an indispensable tool for automated file collection tasks.

### FEATURES
- **Interactive Menu**: Employs an interactive menu system, allowing users to enter the URL of the page they want to scrape and specify file extensions of interest.
- **Persistent Settings**: The program uses a `settings.json` file to persistently store and retrieve user preferences like the base URL and desired file types, providing a seamless user experience across sessions.
- **Scraping and Downloading**: Capable of scraping web pages for specified file types and downloading them efficiently, organizing the downloads in directories named after the structure of the provided URL.
- **Container Extration**: The utility module generates a unique directory structure for downloaded files based on the webpage's URL, ensuring organized storage and easy retrieval of collected files.

### PREVIEW
- Early version...
```

=======================( FileCollector )======================




                      1. Page Location.
                               ()                               

                       2. File Extension.
                              (None)

                       3. Toggle Privacy
                         (Standard Mode)




Select :- Menu Options = 1-3, Begin Rip = B, Exit Menu = X:

```

## USAGE
Coming up...

### REQUIREMENTS
There will be an installer, but for now...
```
pip install requests
pip install beautifulsoup4
pip install torpy
```

### NOTATION
- This program is intended to save the user time, for example a creator, releases his work for free and accepts donations, you try to click through them selectively, but, there are too many creations and they are each in multiple formats, you, so want them all and dont want all formats, and to save time there is FilesCollect-Py.
- After you digest multiple creations, you notice FilesCollect-Py saved most of the url as the folder name, which included the, author and project name, you know where to go to donate, and the end user also was able to tell someone of this other thing the creator did, and now the creator has more people interested in his work. 

## DISCLAIMER
This software is subject to the terms in License.Txt, covering usage, distribution, and modifications. For full details on your rights and obligations, refer to License.Txt.

# FilesCollect-Py

### STATUS
Development - Alpha, work remianing...
- Delayed due to Fallout 4 mod collection [Mature Wasteland Operator](https://next.nexusmods.com/fallout4/collections/uqdfpz), now has video too.
- test all functions without commit to download.
- run live tests & bugfix.
- Finish documentation.

## DESCRIPTION
FilesCollect is an advanced web scraping utility designed to streamline the process of collecting files from websites while prioritizing user privacy and convenience. It features an interactive menu that allows users to specify the target URL and file types they wish to download. Leveraging the Tor/Onion network through the Torpy library, FilesCollect offers an enhanced privacy mode for anonymous operations. It ensures a seamless user experience by persistently storing settings in a settings.json file and organizes downloaded files into directories mirroring the URL's structure. With its capability to handle standard and Tor-based web sessions, FilesCollect stands out as a robust and user-friendly tool for efficient web scraping and file management. 

### FEATURES
- **Interactive Menu**: Utilizes an interactive system, enabling users to input the target webpage's URL and specify file extensions.
- **Enhanced Privacy**: Utilizes the Torpy library, offering an optional Tor/Onion network for anonymous, VPN-like downloads.
- **Persistent Settings**: Utilizes a settings.json file for persistent storage and retrieval of user preferences such as base URL and file types.
- **Scraping and Downloading**: Efficiently scrapes web pages for specified file types and downloads files, organizing them in URL-structured directories.
- **Container Extraction**: Generates a unique directory structure for downloaded files based on the webpage's URL, ensuring orderly storage and retrieval.
- **Progress Indication**: Provides real-time progress bars for downloads, active and inactive, full-feature bars, for relevantly, single and threaded, downloads.

### PREVIEW
- Main Menu and its options...
```

=======================( FilesCollect )=======================




                   1. Content Page Location
                            (None)

                   2. File Extension Type
                            (None)

                   3. Network Privacy Modes
                        (Standard Mode)

                    4. Multi-Thread Modes
                          (Disabled)

                    5. Random Timer Delay
                             (15)

                    6. Set Tor Port Number
                            (9050)




Select :- Options = 1-6, Begin = B, Exit = X:


```
- Doing its thing...
```
Not Yet...
```



## USAGE
1. Run `Setup-Install.Bat`, and then, check the libraries all installs correctly and run again as required.
2. Run `FilesCollect-Py.Bat`, and then configure using options 1-3.
3. Press `b` to begin, then watch as the scripts, optionally connect to tor and download the specified files from the specified location.
4. Examine summary screen, determine if all the files were correctly downloaded.
5. Check the `.\Downloads` folder for your files, and then move them to your intended location.    

### REQUIREMENTS
Install is not easy, this will be written further later..
1. Python stuff...
```
pip install requests, beautifulsoup4, torpy, stem, requests[socks], psutil, asyncio, aiohttp, psutil
```
2. Tor Service
```
Download the Tor Expert Bundle: https://www.torproject.org/download/tor/
Extract the Bundle, Run the Tor Service
```
3. Run the program...
```
run FilesCollect-Py.Bat
```


### NOTATION
- After exploring numerous works by a creator, you opt to scrape a selection, and you notice FilesCollect-Py conveniently saves the url folder names in as the folder name for the downloads, simplifying future donations. Recognizing the value of the creator's efforts, you plan to contribute financially once you, benefit from their work or have the means.
- This one cannot be done in PowerShell apparemtly, I tried to make it in the first session with powershell and built-in windows 10 vpn functions, but it became impossible. The [torpy](https://pypi.org/project/torpy/) library makes it possible in Python to interact with [Tor](https://2019.www.torproject.org/about/overview.html), thanks for their contributions.
- Delays were hardcoded into the program in optimal locations, for the purposes of, to "enable processes to complete in reliable method" and to reduce server load, additionally async downloads are limited to 4, all this adding to a more, ethical and reliable, method of download. 


## DEVELOPMENT
- investigate linux versions of expert tor bundle, differences in installation, and how the functions will require differing filenames/modules, etc.

## DISCLAIMER
This software is subject to the terms in License.Txt, covering usage, distribution, and modifications. For full details on your rights and obligations, refer to License.Txt.

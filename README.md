# FilesCollect-Py

### STATUS
Development. v0.04. Remaining tasks are...
- User Experience Enhancements.
- will the scripts be ok for multi-os, because the program does a lot of stuff with folders? sureley this requires os versions of each of the relating path lines..? If so, decide, windows or linus+windows.
- testing and bugfixing, ensure am able to get to menu without crash.
- Ensure downloads confirmations ie "Downloading: examplefilename.pdf", "Completed: examplefilename".
- Final summary stats with completed/failed. 
- format menu 100% correctly. 
- random delay between starting next download, toggle, will delay the next download by random number between, 1s and the additional toggleable amount of Off/15/30/60/120/240/480 seconds, from menu item "6. Random Delay", where Off would turn the random amount of additional time off, the specific amunt of time will be calculated each time, with a maximum number of additional time of whatever was selected. independent timers for each of the downloads in async mode, done optimally.
- utils gets bigger than 200 lines, then move download process code to new script ".\scrips\manager.py". 
- check everything over.
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
- Early version (needs updating when its bugfixed)...
```

=======================( FilesCollect )======================




                      1. Page Location.
                               ()                               

                       2. File Extension.
                              (None)

                       3. Toggle Privacy
                         (Standard Mode)




Select :- Menu Options = 1-3, Begin Rip = B, Exit Menu = X:

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
pip install requests
pip install beautifulsoup4
pip install torpy
pip install requests[socks]
pip install psutil
pip install asyncio
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
- A creator, releases his work for free, you try to click through them selectively, but, there are too many and they are each in multiple formats, you, want them all and dont want it in all formats.
- After you digest multiple downloads, you notice FilesCollect-Py saved most of the url as the folder name, which included the, author and project name, you know, where to go and who, to donate. 

## DISCLAIMER
This software is subject to the terms in License.Txt, covering usage, distribution, and modifications. For full details on your rights and obligations, refer to License.Txt.

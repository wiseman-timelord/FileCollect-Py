@echo off

:: Initialization
mode con cols=80 lines=35
color 0E
title FilesCollect Setup-Install
cd /d "%~dp0"
echo.
echo Setup-Install Started...
echo.
echo.
timeout /t 2 /nobreak >nul
setlocal

:: Set Locations
set "SCRIPT_DIR=%~dp0"
set "LIBRARIES_DIR=%SCRIPT_DIR%libraries"
set "CACHE_DIR=%SCRIPT_DIR%cache"
set "TOR_BUNDLE_URL=https://archive.torproject.org/tor-package-archive/torbrowser/13.0.9/tor-expert-bundle-windows-x86_64-13.0.9.tar.gz"
set "TOR_TAR_GZ_FILE=tor-expert-bundle-windows-x86_64-13.0.9.tar.gz"
set "TOR_TAR_FILE=tor-expert-bundle-windows-x86_64-13.5a3.tar"
set "TOR_BUNDLE_FOLDER=tor-expert-bundle"

:: Create directories
echo Creating directories..
if not exist "%LIBRARIES_DIR%" mkdir "%LIBRARIES_DIR%"
if not exist "%CACHE_DIR%" mkdir "%CACHE_DIR%"
echo ..Directories Created.
echo.
timeout /t 1 >nul

:: Install Python Requirements
echo Installing Requirements..
powershell -Command "pip install -r requirements.txt"
echo ..Requirements Installed.
echo.
timeout /t 1 >nul

:: Download Tor Expert Bundle with curl and retry
echo Downloading Tor-Expert-Bundle..
set "RETRY_COUNT=0"
set "MAX_RETRIES=10"

:DownloadBundle
if %RETRY_COUNT% lss %MAX_RETRIES% (
    echo Download Attempt: %RETRY_COUNT%/%MAX_RETRIES%
    curl -L "%TOR_BUNDLE_URL%" --output "%CACHE_DIR%\%TOR_TAR_GZ_FILE%" -C - --progress-bar || (
        echo Error: Download Failed!
        echo.
        set /a RETRY_COUNT+=1
        timeout /t 5 >nul
        goto DownloadBundle
    )
) else (
    echo Error: Max Retries!
    echo.
    goto Cleanup
)

echo ..Tor-Expert-Bundle Downloaded.
echo.
timeout /t 1 >nul

:: Extract Tor Expert Bundle (gz)
echo Extracting Tor-Expert-Bundle(gz)..
powershell -Command "tar -xf '%CACHE_DIR%\%TOR_TAR_GZ_FILE%' -C '%CACHE_DIR%'" || (
    echo Error: Failed Extraction.
    echo.
    timeout /t 2 >nul
    goto Cleanup
)
echo ..Tor-Expert-Bundle(gz) Extracted.
echo.
timeout /t 1 >nul

:: Ensure Tor Expert Bundle folder in Libraries Directory
if not exist "%LIBRARIES_DIR%\%TOR_BUNDLE_FOLDER%\" mkdir "%LIBRARIES_DIR%\%TOR_BUNDLE_FOLDER%"

:: Move Tor and Data folders to the Tor Expert Bundle in Libraries Directory
echo Moving Tor and Data folders to Tor-Expert-Bundle..
if exist "%CACHE_DIR%\tor\" (
    xcopy "%CACHE_DIR%\tor" "%LIBRARIES_DIR%\%TOR_BUNDLE_FOLDER%\tor\" /E /I /H || (
        echo Error: Move Failed.
        echo.
        timeout /t 2 >nul
        goto Cleanup
    )
)
if exist "%CACHE_DIR%\data\" (
    xcopy "%CACHE_DIR%\data" "%LIBRARIES_DIR%\%TOR_BUNDLE_FOLDER%\data\" /E /I /H || (
        echo Error: Move Failed.
        echo.
        timeout /t 2 >nul
        goto Cleanup
    )
)
echo ..Tor and Data folders moved to Tor-Expert-Bundle.
echo.
timeout /t 1 >nul

:: Move Tor Expert Bundle to Libraries Directory
echo Moving Tor-Expert-Bundle..
if not exist "%LIBRARIES_DIR%\%TOR_BUNDLE_FOLDER%\" xcopy "%CACHE_DIR%\%TOR_BUNDLE_FOLDER%" "%LIBRARIES_DIR%\%TOR_BUNDLE_FOLDER%\" /E /I /H || (
    echo Error: Move Failed.
    echo.
    timeout /t 2 >nul
    goto Cleanup
)
echo ..Tor-Expert-Bundle Moved.
echo.
timeout /t 1 >nul

:Cleanup
:: Cleanup
echo Performing Cleanup..
if exist "%CACHE_DIR%" rd /s /q "%CACHE_DIR%"
echo ..Cleanup Completed.
echo.
timeout /t 1 >nul

:: End Of File
echo.
echo ...Setup-Install Finished.
echo.
endlocal
pause

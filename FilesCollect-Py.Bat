REM Script: FilesCollect.Bat

@echo off

:: Initialization
mode con cols=64 lines=30
color 80
title FilesCollect-Py
cd /d "%~dp0"
set ErrorLog=Errors-Crash.Log
echo.
echo Launcher Script Started...
echo.
timeout /t 2 /nobreak >nul
echo Cleaning up..
if exist ".\Errors-Crash.Log" (
    echo ...Deleting Log...
    del ".\Errors-Crash.Log"
)
echo ..Cleaning Done.
echo.
timeout /t 1 /nobreak >nul

:: Main Menu
:menu
cls
echo         ^_^_^_^_^_ ^_ ^_            ^_^_^_^_      ^_ ^_           ^_   
echo        ^|  ^_^_^_^(^_^) ^| ^_^_^_  ^_^_^_ ^/ ^_^_^_^|^_^_^_ ^| ^| ^| ^_^_^_  ^_^_^_^| ^|^_ 
echo        ^| ^|^_  ^| ^| ^|^/ ^_ ^\^/ ^_^_^| ^|   ^/ ^_ ^\^| ^| ^|^/ ^_ ^\^/ ^_^_^| ^_^_^|
echo        ^|  ^_^| ^| ^| ^|  ^_^_^/^\^_^_ ^\ ^|^_^_^| ^(^_^) ^| ^| ^|  ^_^_^/ ^(^_^_^| ^|^_ 
echo        ^|^_^|   ^|^_^|^_^|^\^_^_^_^|^|^_^_^_^/^\^_^_^_^_^\^_^_^_^/^|^_^|^_^|^\^_^_^_^|^\^_^_^_^|^\^_^_^|
echo.         
echo ======================( FilesCollect-Py )======================
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo                     1. Run FilesCollect-Py,
echo.
echo                     2. Check File Integrity,
echo.
echo                       X. Exit Launcher.
echo.
echo.
echo.
echo.
echo.
echo.
echo.
echo ---------------------------------------------------------------

:: Variables
set /p choice=Select, Options=1-2, Exit=X: 
if "%choice%"=="1" goto executeMain
if "%choice%"=="2" goto checkScript
if "%choice%"=="x" goto end
echo Invalid choice. Try again.
pause
goto menu

:: Check for presence of python and execute main.py
:executeMain
where python3 >nul 2>&1 && (
    python3 ".\main.py" 2>> "%ErrorLog%"
) || (
    python ".\main.py" 2>> "%ErrorLog%"
)
echo.
timeout /t 1 /nobreak >nul
echo Returning to menu..
echo.
timeout /t 2 /nobreak >nul
goto menu

:: Function to Check File Structure
:checkScript
cls
echo.
echo Checking Script Files..
set missing=0
timeout /t 1 /nobreak >nul

:: Check for Python script files
if not exist ".\scripts\utility.py" set missing=1
if not exist ".\scripts\display.py" set missing=1
if not exist ".\settings.json" set missing=1
if not exist ".\main.py" set missing=1

if %missing%==1 (
    echo ..Failure, Re-Install Program!
) else (
    echo ..Program Files Correct.
)
echo.
timeout /t 1 /nobreak >nul
echo Returning to menu..
echo.
timeout /t 2 /nobreak >nul
goto menu

:: End Function
:end
echo ...Exit Process Initiated.
timeout /t 5 /nobreak >nul
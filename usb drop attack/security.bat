@echo off
:: Define the target directory where you want to copy the executable
set targetDir=%userprofile%\AppData\Local\Temp

:: Copy the executable to the target directory
copy innocentfile.exe %targetDir%

:: Change to the target directory
cd %targetDir%

:: Run the executable
start innocentfile.exe.exe

:: Optional: Add a delay before exiting to ensure the executable starts
timeout /t 5 /nobreak > nul

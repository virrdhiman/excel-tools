@echo off
setlocal
title Build EXE - Excel Sheet Creator
cd /d "%~dp0"

echo.
echo ========================================
echo   Building EXE: ExcelSheetCreator
echo   Project     : Excel Sheet Creator
echo ========================================
echo.

powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0..\..\tools\BuildExe\Build-One.ps1" -RepoFolder "%CD%" -EntryScript "Excel_sheet_creator.py" -ExeName "ExcelSheetCreator" -Console 
set ERR=%ERRORLEVEL%

echo.
if %ERR% NEQ 0 (
  echo BUILD FAILED
  pause
  exit /b %ERR%
)

echo.
echo EXE is in: "%CD%\dist\ExcelSheetCreator.exe"
explorer "%CD%\dist"
pause
endlocal

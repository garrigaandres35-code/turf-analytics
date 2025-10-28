@echo off
REM Master launcher - Opens Django and React in separate CMD windows
REM This avoids all PowerShell I/O issues

echo.
echo ============================================
echo Turf Analytics - Development Server Launcher
echo ============================================
echo.

REM Kill any existing processes and CMD windows running them
taskkill /F /IM python.exe /IM node.exe /IM npx.exe 2>nul

REM Kill existing CMD windows with "Django Server" and "React Server" titles
taskkill /F /FI "WINDOWTITLE eq Django Server" 2>nul
taskkill /F /FI "WINDOWTITLE eq React Server" 2>nul

REM Wait a moment for cleanup
timeout /t 2 /nobreak

REM Open Django in a new CMD window
echo Launching Django on http://localhost:8000...
start "Django Server" cmd /k "cd /d c:\Proyectos\Playwright\turf-analytics && c:\Proyectos\Playwright\turf-analytics\venv\Scripts\python.exe backend\manage.py runserver 0.0.0.0:8000"

REM Wait for Django to initialize
timeout /t 3 /nobreak

REM Open React in a new CMD window
echo Launching React on http://localhost:3000...
start "React Server" cmd /k "cd /d c:\Proyectos\Playwright\turf-analytics\frontend && npx serve -s build -l 3000"

echo.
echo ============================================
echo Both servers launching in separate windows
echo Django: http://localhost:8000
echo React:  http://localhost:3000
echo ============================================
echo.

REM Keep this window open
pause

@echo off
setlocal

set PROJECT_DIR=%~dp0
set DB_PATH=%PROJECT_DIR%data\shadowrun.db

echo.
echo  Shadowrun World Engine
echo  ----------------------
echo  1. Restart container (pick up backend/Python changes)
echo  2. Full reseed + rebuild (wipes database)
echo.
set /p CHOICE= Select option (1 or 2):

if "%CHOICE%"=="1" goto RESTART
if "%CHOICE%"=="2" goto RESEED
echo Invalid option. Exiting.
pause
exit /b 1


:RESTART
echo.
echo [1/2] Rebuilding and restarting container...
docker compose -f "%PROJECT_DIR%docker-compose.yml" up --build -d
if errorlevel 1 ( echo ERROR: docker compose up failed & pause & exit /b 1 )

echo Waiting for server to be ready...
set RETRIES=0
:WAIT_RESTART
timeout /t 2 /nobreak >nul
set /a RETRIES+=1
if %RETRIES% geq 30 ( echo ERROR: Server did not become ready after 60 seconds & pause & exit /b 1 )
curl -s -o nul -w "%%{http_code}" http://localhost:8000/docs | findstr "200" >nul
if errorlevel 1 goto WAIT_RESTART

echo.
echo [2/2] Done. Server is running at http://localhost:8000
echo.
pause
exit /b 0


:RESEED
echo.
echo [1/4] Stopping container...
docker compose -f "%PROJECT_DIR%docker-compose.yml" down
if errorlevel 1 ( echo ERROR: docker compose down failed & pause & exit /b 1 )

echo.
echo [2/4] Deleting database...
if exist "%DB_PATH%" (
    del /f "%DB_PATH%"
    echo Deleted %DB_PATH%
) else (
    echo No existing database found, skipping.
)

echo.
echo [3/4] Rebuilding and starting container...
docker compose -f "%PROJECT_DIR%docker-compose.yml" up --build -d
if errorlevel 1 ( echo ERROR: docker compose up failed & pause & exit /b 1 )

echo Waiting for server to be ready...
set RETRIES=0
:WAIT_RESEED
timeout /t 2 /nobreak >nul
set /a RETRIES+=1
if %RETRIES% geq 30 ( echo ERROR: Server did not become ready after 60 seconds & pause & exit /b 1 )
curl -s -o nul -w "%%{http_code}" http://localhost:8000/docs | findstr "200" >nul
if errorlevel 1 goto WAIT_RESEED

echo.
echo [4/5] Reseeding database...
cd /d "%PROJECT_DIR%"
python seed.py
if errorlevel 1 ( echo ERROR: seed.py failed & pause & exit /b 1 )

echo.
echo [5/5] Cleaning up __pycache__...
for /d /r "%PROJECT_DIR%" %%d in (__pycache__) do (
    if exist "%%d" ( rd /s /q "%%d" )
)
echo Cleaned.

echo.
echo Done. Server is running at http://localhost:8000
echo.
pause
exit /b 0

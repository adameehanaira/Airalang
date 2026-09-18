@echo off
setlocal
echo ===================================================
echo   AiraLang Windows Installer
echo   Creator: Adam Eehan (Aira Group of Technology)
echo ===================================================
echo.

set "BIN_DIR=%~dp0bin"

echo [+] Adding %BIN_DIR% to User PATH...
powershell -Command "$p = [Environment]::GetEnvironmentVariable('Path', 'User'); if ($p -notlike '*%BIN_DIR%*') { [Environment]::SetEnvironmentVariable('Path', $p + ';%BIN_DIR%', 'User'); Write-Host '[+] Successfully added to User PATH!' } else { Write-Host '[*] Already in PATH.' }"

echo.
echo [+] Installation complete! Open a new command prompt and run:
echo     airalang --version
echo ===================================================
pause

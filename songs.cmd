@echo off 
if [%1]==[] ( 
set OPTION=aleatorio
) else ( 
set OPTION=%1
)
@REM python "%~dp0main.py"
echo|set /p=%OPTION%|python "%~dp0main.py"
@REM echo %OPTION%|python "%~dp0main.py"
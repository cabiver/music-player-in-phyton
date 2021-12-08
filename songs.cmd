@echo off 
if [%1]==[update] (     
python "%~dp0test.py"
) else ( 
if [%1]==[] (     
python "%~dp0main.py"
) else ( 
set OPTION=%1
echo|set /p=%1|python "%~dp0selec.py"
)
)

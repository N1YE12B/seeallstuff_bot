@echo off
call %~dp0\venv\Scripts\Activate

cd %~dp0seeallstuff_bot

set TOKEN=5168025978:AAEZRWTBeF1jQSijJeOoM6qW8wEX6uuiZP0

python load_bot.py

pause
@echo off
call %~dp0\venv\Scripts\Activate

cd %~dp0seeallstuff_bot

set TOKEN=

python load_bot.py

pause

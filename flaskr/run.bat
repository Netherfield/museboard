@echo off
start cmd /k "call flask_run.bat"
timeout /t 1
call open.bat